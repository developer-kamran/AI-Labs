import tkinter as tk
import random
import heapq

# Grid setup
grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 1, 0, 0, 1],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0]
]

start = (0, 0)
goal = (4, 4)
cell_size = 60

def get_neighbors(node):
    x, y = node
    directions = [(0,1),(1,0),(0,-1),(-1,0)]
    neighbors = []
    for dx, dy in directions:
        nx, ny = x+dx, y+dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
            if grid[nx][ny] == 0:
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
            print("Goal reached with Random Search!")
            return reconstruct_path(parent, start, goal), visited

        for neighbor in get_neighbors(current):
            if neighbor not in closed_list and neighbor not in open_list:
                open_list.append(neighbor)
                parent[neighbor] = current

    print("No path found with Random Search.")
    return [], visited

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
            print("Goal reached with Uniform Cost Search!")
            return reconstruct_path(parent, start, goal), visited

        closed_list.add(current)

        for neighbor in get_neighbors(current):
            new_cost = cost_so_far[current] + 1
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                heapq.heappush(open_list, (new_cost, neighbor))
                parent[neighbor] = current

    print("No path found with Uniform Cost Search.")
    return [], visited

def reconstruct_path(parent, start, goal):
    path = [goal]
    while path[-1] != start:
        path.append(parent[path[-1]])
    path.reverse()
    return path

def draw_grid(canvas, path=[]):
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
            elif grid[i][j] == 1:
                color = "black"
            elif (i, j) in path:
                color = "yellow"

            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="gray")

def show_visited_nodes(visited):
    popup = tk.Toplevel(root)
    popup.title("Visited Nodes")
    popup.geometry("+480+100") 

    label = tk.Label(popup, text="Visited Coordinates:")
    label.pack()

    text = tk.Text(popup, height=20, width=30)
    text.pack()

    for coord in visited:
        text.insert(tk.END, f"{coord}\n")

def run_search(algorithm):
    if algorithm == "random":
        path, visited = random_search(start, goal)
    else:
        path, visited = uniform_cost_search(start, goal)

    draw_grid(canvas, path)
    show_visited_nodes(visited)

# --- Tkinter GUI Setup ---
root = tk.Tk()
root.title("Pathfinding Visualizer")

canvas = tk.Canvas(root, width=len(grid[0]) * cell_size, height=len(grid) * cell_size)
canvas.pack()

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Random Search", command=lambda: run_search("random")).pack(side=tk.LEFT, padx=10)
tk.Button(button_frame, text="Uniform Cost Search", command=lambda: run_search("ucs")).pack(side=tk.LEFT, padx=10)

draw_grid(canvas)
root.mainloop()
