import tkinter as tk
from tkinter import messagebox
import random
import heapq
from collections import deque

cell_size = 50
start = (0, 0)
goal = None
grid = []
weights = []
is_weighted = False

def get_neighbors(node):
    x, y = node
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    neighbors = []
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
            if grid[nx][ny] != 0:
                neighbors.append((nx, ny))
    return neighbors

def random_search(start, goal):
    open_list = [start]
    closed_list = set()
    parent = {}
    visited = []

    while open_list:
        current = random.choice(open_list)
        open_list.remove(current)
        closed_list.add(current)
        visited.append(current)

        if current == goal:
            return reconstruct_path(parent, start, goal), visited, calculate_path_cost(parent, start, goal)

        for neighbor in get_neighbors(current):
            if neighbor not in closed_list and neighbor not in open_list:
                open_list.append(neighbor)
                parent[neighbor] = current

    return [], visited, 0

def uniform_cost_search(start, goal):
    open_list = [(0, start)]
    heapq.heapify(open_list)
    closed_list = set()
    parent = {}
    cost_so_far = {start: 0}
    visited = []

    while open_list:
        cost, current = heapq.heappop(open_list)
        visited.append(current)

        if current == goal:
            return reconstruct_path(parent, start, goal), visited, cost_so_far[current]

        closed_list.add(current)

        for neighbor in get_neighbors(current):
            x, y = neighbor
            weight = weights[x][y] if is_weighted else 1
            new_cost = cost_so_far[current] + weight
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                heapq.heappush(open_list, (new_cost, neighbor))
                parent[neighbor] = current

    return [], visited, 0

def bfs(start, goal):
    queue = deque([start])
    visited = set()
    parent = {}
    visited_order = []

    while queue:
        current = queue.popleft()
        visited.add(current)
        visited_order.append(current)

        if current == goal:
            return reconstruct_path(parent, start, goal), visited_order, calculate_path_cost(parent, start, goal)

        for neighbor in get_neighbors(current):
            if neighbor not in visited and neighbor not in queue:
                queue.append(neighbor)
                parent[neighbor] = current

    return [], visited_order, 0

def dfs(start, goal):
    stack = [start]
    visited = set()
    parent = {}
    visited_order = []

    while stack:
        current = stack.pop()
        if current in visited:
            continue
        visited.add(current)
        visited_order.append(current)

        if current == goal:
            return reconstruct_path(parent, start, goal), visited_order, calculate_path_cost(parent, start, goal)

        for neighbor in reversed(get_neighbors(current)):  # Reverse for DFS order
            if neighbor not in visited:
                stack.append(neighbor)
                parent[neighbor] = current

    return [], visited_order, 0

def reconstruct_path(parent, start, goal):
    if goal not in parent:
        return []
    path = [goal]
    while path[-1] != start:
        path.append(parent[path[-1]])
    path.reverse()
    return path

def calculate_path_cost(parent, start, goal):
    path = reconstruct_path(parent, start, goal)
    if not path:
        return 0
    if not is_weighted:
        return len(path) - 1  # Steps count for unweighted
    # Sum weights excluding start node for weighted
    return sum(weights[x][y] for x, y in path[1:])

def draw_grid(canvas, grid, path=[]):
    canvas.delete("all")
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            x1, y1 = j * cell_size, i * cell_size
            x2, y2 = x1 + cell_size, y1 + cell_size

            color = "white"
            if (i, j) == start:
                color = "green"
            elif (i, j) == goal:
                color = "red"
            elif grid[i][j] == 0:
                color = "black"
            elif (i, j) in path:
                color = "yellow"

            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="gray")

            if is_weighted and grid[i][j] != 0:
                canvas.create_text((x1 + x2)//2, (y1 + y2)//2, 
                                 text=str(weights[i][j]), 
                                 font=("Arial", 12, "bold"))

def open_visualizer():
    visual = tk.Toplevel()
    visual.title("Pathfinding Visualizer")
    visual.geometry("+500+200")

    rows = len(grid)
    cols = len(grid[0])
    canvas = tk.Canvas(visual, width=cols * cell_size, height=rows * cell_size)
    canvas.pack()

    button_frame = tk.Frame(visual)
    button_frame.pack(pady=5)

    coord_display = tk.Text(visual, height=8, width=cols * 2)
    coord_display.pack()

    def run_search(algorithm):
        if algorithm == "random":
            path, visited, cost = random_search(start, goal)
        elif algorithm == "ucs":
            path, visited, cost = uniform_cost_search(start, goal)
        elif algorithm == "bfs":
            path, visited, cost = bfs(start, goal)
        elif algorithm == "dfs":
            path, visited, cost = dfs(start, goal)
        else:
            return

        draw_grid(canvas, grid, path)

        coord_display.delete("1.0", tk.END)
        coord_display.insert(tk.END, "Visited Coordinates:\n")
        for coord in visited:
            coord_display.insert(tk.END, f"{coord}\n")
        if is_weighted:
            coord_display.insert(tk.END, f"\nTotal Cost: {cost}\n")
    

    draw_grid(canvas, grid)

    algorithms = [
        ("random", "Random Search"),
        ("ucs", "Uniform Cost Search"),
        ("bfs", "Breadth-First Search"),
        ("dfs", "Depth-First Search")
    ]

    for algo, label in algorithms:
        tk.Button(button_frame, text=label, 
                command=lambda a=algo: run_search(a), 
                width=20).pack(side=tk.LEFT, padx=5)

def parse_input_matrix():
    global grid, weights, goal, is_weighted
    try:
        is_weighted = weight_var.get()
        input_str = matrix_input.get("1.0", tk.END).strip()
        rows = input_str.splitlines()
        grid.clear()
        weights.clear()

        for row in rows:
            line = [int(val) for val in row.split()]
            
            if not is_weighted and any(val > 1 for val in line):
                raise ValueError("In unweighted mode, values must be 0 or 1")
                
            grid.append([1 if val > 0 else 0 for val in line])
            weights.append([val if (is_weighted and val > 0) else 0 for val in line])

        # Validate start and goal positions
        goal = (len(grid)-1, len(grid[0])-1)
        if grid[start[0]][start[1]] == 0 or grid[goal[0]][goal[1]] == 0:
            raise ValueError("Start or Goal position cannot be a wall")

        open_visualizer()
    except Exception as e:
        messagebox.showerror("Input Error", str(e))

root = tk.Tk()
root.title("Pathfinding Input")

weight_var = tk.BooleanVar()

# GUI Layout
tk.Checkbutton(root, text="Weighted Graph", variable=weight_var).pack(pady=5)

instruction = tk.Label(root, text="Enter grid matrix (space-separated values):")
instruction.pack()

example_label = tk.Label(root, text="", fg="gray")
example_label.pack()

matrix_input = tk.Text(root, height=10, width=40)
matrix_input.pack(pady=5)

tk.Button(root, text="Visualize Search Algorithms", 
        command=parse_input_matrix).pack(pady=10)

def update_example():
    if weight_var.get():
        example = "Weighted example:\n3 2 5 0\n1 4 0 2\n0 8 1 3\n2 5 6 1"
        instruction.config(text="Enter grid matrix (0 = wall, >0 = movement cost):")
    else:
        example = "Unweighted example:\n1 1 1 0\n1 0 1 1\n0 1 1 0\n1 1 1 1"
        instruction.config(text="Enter grid matrix (0 = wall, 1 = path):")
    example_label.config(text=example)

weight_var.trace_add("write", lambda *args: update_example())
update_example()

root.mainloop()