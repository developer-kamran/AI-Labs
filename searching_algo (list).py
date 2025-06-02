import tkinter as tk
from tkinter import messagebox, ttk
import random
import math
import heapq
from collections import deque
from typing import Dict, List, Tuple, Set, Optional

# Global variables
graph: Dict[str, List[Tuple[str, int]]] = {}  # Adjacency list with weights
node_positions: Dict[str, Tuple[float, float]] = {}  # Node positions on canvas
start: Optional[str] = None
goal: Optional[str] = None
directed_graph: bool = True  # Default to directed graph
weighted_graph: bool = False  # Default to unweighted graph

# Graph visualization settings
NODE_RADIUS = 20
CANVAS_SIZE = 600
BACKGROUND_COLOR = "#f0f0f0"
NODE_COLOR = "white"
START_COLOR = "#4CAF50"  # Green
GOAL_COLOR = "#F44336"   # Red
PATH_COLOR = "#FFEB3B"   # Yellow
EDGE_COLOR = "#333333"
VISITED_COLOR = "#BBDEFB"  # Light blue
CURRENT_COLOR = "#7E57C2"  # Purple
EDGE_LABEL_COLOR = "#333333"
EDGE_LABEL_BG = "#FFFFFF"  # White background for cost circles

def get_neighbors(node: str) -> List[Tuple[str, int]]:
    """Get neighbors from the adjacency list with their weights."""
    return graph.get(node, [])

def random_search(start: str, goal: str) -> Tuple[List[str], List[str]]:
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
            return reconstruct_path(parent, start, goal), visited

        for neighbor, _ in get_neighbors(current):
            if neighbor not in closed_list and neighbor not in open_list:
                open_list.append(neighbor)
                parent[neighbor] = current

    return [], visited

def uniform_cost_search(start: str, goal: str) -> Tuple[List[str], List[str], float]:
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

        for neighbor, weight in get_neighbors(current):
            new_cost = cost_so_far[current] + weight
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                heapq.heappush(open_list, (new_cost, neighbor))
                parent[neighbor] = current

    return [], visited, 0

def bfs(start: str, goal: str) -> Tuple[List[str], List[str]]:
    queue = deque([start])
    visited = set()
    parent = {}
    visited_order = []

    while queue:
        current = queue.popleft()
        if current in visited:
            continue
        visited.add(current)
        visited_order.append(current)

        if current == goal:
            return reconstruct_path(parent, start, goal), visited_order

        for neighbor, _ in get_neighbors(current):
            if neighbor not in visited and neighbor not in queue:
                queue.append(neighbor)
                parent[neighbor] = current

    return [], visited_order

def dfs(start: str, goal: str) -> Tuple[List[str], List[str]]:
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
            return reconstruct_path(parent, start, goal), visited_order

        for neighbor, _ in reversed(get_neighbors(current)):  # Reverse for DFS order
            if neighbor not in visited:
                stack.append(neighbor)
                parent[neighbor] = current

    return [], visited_order

def reconstruct_path(parent: Dict[str, str], start: str, goal: str) -> List[str]:
    if goal not in parent:
        return []
    path = [goal]
    while path[-1] != start:
        path.append(parent[path[-1]])
    path.reverse()
    return path

def draw_graph(canvas: tk.Canvas, path: List[str] = [], visited: List[str] = [], current: str = None):
    """Draw the graph on the canvas with optional path highlighting."""
    canvas.delete("all")
    
    # Get all nodes that are either in the graph or have incoming edges
    nodes = set(graph.keys())
    for neighbors in graph.values():
        for neighbor, _ in neighbors:
            nodes.add(neighbor)
    nodes = list(nodes)
    
    num_nodes = len(nodes)
    center = (CANVAS_SIZE // 2, CANVAS_SIZE // 2)
    radius = min(250, CANVAS_SIZE // 2 - 50)
    
    # Circular layout
    for i, node in enumerate(nodes):
        angle = 2 * math.pi * i / num_nodes if num_nodes > 0 else 0
        x = center[0] + radius * math.cos(angle)
        y = center[1] + radius * math.sin(angle)
        node_positions[node] = (x, y)

    # Draw edges first (so nodes appear on top)
    for node, neighbors in graph.items():
        if node not in node_positions:
            continue
        x1, y1 = node_positions[node]
        for neighbor, weight in neighbors:
            if neighbor in node_positions:
                x2, y2 = node_positions[neighbor]
                # Calculate direction vector
                dx = x2 - x1
                dy = y2 - y1
                # Normalize the direction vector
                length = math.sqrt(dx*dx + dy*dy)
                if length > 0:
                    dx = dx / length * NODE_RADIUS
                    dy = dy / length * NODE_RADIUS
                # Adjust start and end points to be on the node's circumference
                x1_adj = x1 + dx
                y1_adj = y1 + dy
                x2_adj = x2 - dx
                y2_adj = y2 - dy
                
                # Calculate midpoint for weight label
                mid_x = (x1_adj + x2_adj) / 2
                mid_y = (y1_adj + y2_adj) / 2
                
                # Draw the edge with arrow for directed graphs
                if directed_graph:
                    canvas.create_line(x1_adj, y1_adj, x2_adj, y2_adj, 
                                    fill=EDGE_COLOR, width=2, arrow=tk.LAST, arrowshape=(8, 10, 5))
                else:
                    canvas.create_line(x1_adj, y1_adj, x2_adj, y2_adj, 
                                    fill=EDGE_COLOR, width=2)
                
                # Draw weight label in a circle if graph is weighted
                if weighted_graph:
                    label_radius = 12
                    canvas.create_oval(mid_x - label_radius, mid_y - label_radius,
                                     mid_x + label_radius, mid_y + label_radius,
                                     fill=EDGE_LABEL_BG, outline=EDGE_COLOR)
                    canvas.create_text(mid_x, mid_y, text=str(weight), 
                                     fill=EDGE_LABEL_COLOR, font=("Arial", 8, "bold"))

    # Draw nodes
    for node, (x, y) in node_positions.items():
        # Determine node color
        if node == current:
            color = CURRENT_COLOR
        elif node == start:
            color = START_COLOR
        elif node == goal:
            color = GOAL_COLOR
        elif node in path:
            color = PATH_COLOR
        elif node in visited:
            color = VISITED_COLOR
        else:
            color = NODE_COLOR
        
        # Draw node
        canvas.create_oval(x - NODE_RADIUS, y - NODE_RADIUS,
                         x + NODE_RADIUS, y + NODE_RADIUS,
                         fill=color, outline="black", width=2)
        
        # Draw node label
        canvas.create_text(x, y, text=node, fill="black", font=("Arial", 10, "bold"))

def visualize_search_step_by_step(canvas: tk.Canvas, coord_display: tk.Text, algorithm: str):
    """Visualize the search algorithm step by step with animation."""
    if algorithm == "random":
        path, visited = random_search(start, goal)
        total_cost = 0
    elif algorithm == "ucs":
        path, visited, total_cost = uniform_cost_search(start, goal)
    elif algorithm == "bfs":
        path, visited = bfs(start, goal)
        total_cost = len(path) - 1 if path else 0  # Path length for unweighted
    elif algorithm == "dfs":
        path, visited = dfs(start, goal)
        total_cost = len(path) - 1 if path else 0  # Path length for unweighted
    else:
        return

    coord_display.delete("1.0", tk.END)
    coord_display.insert(tk.END, f"Running {algorithm.upper()}...\n")
    coord_display.insert(tk.END, f"Start: {start}, Goal: {goal}\n\n")
    
    # Animate the search process
    for i, node in enumerate(visited):
        canvas.after(500 * i, lambda n=node: draw_graph(canvas, [], visited[:visited.index(n)+1], n))
        canvas.after(500 * i, lambda n=node: coord_display.insert(tk.END, f"Visiting: {n}\n"))
    
    canvas.after(500 * len(visited), lambda: draw_graph(canvas, path, visited))
    if path:
        path_str = " → ".join(path)
        if weighted_graph:
            canvas.after(500 * len(visited), 
                        lambda: coord_display.insert(tk.END, f"\nPath found: {path_str}\nTotal cost: {total_cost}"))
        else:
            canvas.after(500 * len(visited), 
                        lambda: coord_display.insert(tk.END, f"\nPath found: {path_str}\nPath length: {len(path)-1}"))
    else:
        canvas.after(500 * len(visited), 
                    lambda: coord_display.insert(tk.END, "\nNo path found!"))

def open_visualizer():
    visual = tk.Toplevel()
    visual.title("Graph Pathfinding Visualizer")
    visual.geometry(f"{CANVAS_SIZE+100}x{CANVAS_SIZE+200}")
    
    # Create canvas with border
    canvas_frame = tk.Frame(visual, bd=2, relief=tk.SUNKEN)
    canvas_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
    canvas = tk.Canvas(canvas_frame, width=CANVAS_SIZE, height=CANVAS_SIZE, bg=BACKGROUND_COLOR)
    canvas.pack(expand=True)

    # Control panel
    control_frame = tk.Frame(visual)
    control_frame.pack(fill=tk.X, padx=10, pady=5)

    # Algorithm selection
    algo_var = tk.StringVar(value="bfs")
    ttk.Label(control_frame, text="Algorithm:").pack(side=tk.LEFT)
    
    # Only show UCS if graph is weighted, otherwise show all options
    if weighted_graph:
        algorithms = [("Uniform Cost Search", "ucs")]
    else:
        algorithms = [("BFS", "bfs"), ("DFS", "dfs"), ("Random", "random")]
    
    for text, value in algorithms:
        ttk.Radiobutton(control_frame, text=text, variable=algo_var, value=value).pack(side=tk.LEFT, padx=5)

    # Visualization options
    options_frame = tk.Frame(visual)
    options_frame.pack(fill=tk.X, padx=10, pady=5)
    
    ttk.Button(options_frame, text="Run Search", 
              command=lambda: visualize_search_step_by_step(canvas, coord_display, algo_var.get())).pack(side=tk.LEFT)
    
    ttk.Button(options_frame, text="Reset View", 
              command=lambda: draw_graph(canvas)).pack(side=tk.LEFT, padx=10)

    # Results display
    coord_display = tk.Text(visual, height=10, width=60, wrap=tk.WORD)
    coord_display.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

    # Initial draw
    draw_graph(canvas)
    visual.mainloop()

def parse_input_adj_list():
    """Parse the adjacency list input and validate it."""
    global graph, start, goal, directed_graph, weighted_graph
    
    try:
        input_str = adj_list_input.get("1.0", tk.END).strip()
        if not input_str:
            raise ValueError("Please enter adjacency list")
        
        lines = [line.strip() for line in input_str.splitlines() if line.strip()]
        graph.clear()
        
        # Check if graph is weighted by looking for parentheses in any line
        weighted_graph = any("(" in line and ")" in line for line in lines)
        
        for line in lines:
            if ":" not in line:
                raise ValueError(f"Invalid format in line: '{line}'. Expected 'node: neighbor1(weight), neighbor2(weight)'")
            
            node, neighbors = line.split(":", 1)
            node = node.strip()
            
            if not node:
                raise ValueError(f"Empty node name in line: '{line}'")
            
            # Parse neighbors with weights
            neighbor_list = []
            for neighbor_str in neighbors.split(","):
                neighbor_str = neighbor_str.strip()
                if not neighbor_str:
                    continue
                
                # Check if weight is specified
                if "(" in neighbor_str and ")" in neighbor_str:
                    neighbor_part = neighbor_str.split("(")
                    neighbor_name = neighbor_part[0].strip()
                    weight_str = neighbor_part[1].split(")")[0].strip()
                    try:
                        weight = int(weight_str)
                    except ValueError:
                        raise ValueError(f"Invalid weight in '{neighbor_str}'. Weight must be an integer")
                else:
                    neighbor_name = neighbor_str
                    weight = 1  # Default weight if not specified
                
                neighbor_list.append((neighbor_name, weight))
            
            graph[node] = neighbor_list
        
        # Get start and goal nodes
        start = start_input.get().strip()
        goal = goal_input.get().strip()
        
        if not start or not goal:
            raise ValueError("Both start and goal nodes must be specified")
        
        if start not in graph or goal not in graph:
            raise ValueError("Start or Goal node not found in graph")
        
        # Set graph type
        directed_graph = graph_type_var.get() == "directed"
        
        open_visualizer()
    except Exception as e:
        messagebox.showerror("Input Error", str(e))

def create_main_window():
    """Create and configure the main input window."""
    root = tk.Tk()
    root.title("Graph Pathfinding Visualizer")
    root.geometry("600x600")
    
    # Main container
    main_frame = ttk.Frame(root, padding="10")
    main_frame.pack(fill=tk.BOTH, expand=True)
    
    # Input section
    input_frame = ttk.LabelFrame(main_frame, text="Graph Input", padding="10")
    input_frame.pack(fill=tk.BOTH, expand=True, pady=5)
    
    ttk.Label(input_frame, text="Enter adjacency list (one node per line):").pack(anchor=tk.W)
    
    adj_list_input = tk.Text(input_frame, height=10, width=50)
    adj_list_input.pack(fill=tk.BOTH, expand=True, pady=5)
    adj_list_input.insert(tk.END, "A: B(2), C(5)\nB: A(2), D(1)\nC: A(5), D(3)\nD: B(1), C(3), E(4)\nE: D(4)")
    
    # Graph type selection
    graph_type_frame = ttk.Frame(input_frame)
    graph_type_frame.pack(fill=tk.X, pady=5)
    
    ttk.Label(graph_type_frame, text="Graph type:").pack(side=tk.LEFT)
    graph_type_var = tk.StringVar(value="directed")
    ttk.Radiobutton(graph_type_frame, text="Directed", variable=graph_type_var, value="directed").pack(side=tk.LEFT, padx=5)
    ttk.Radiobutton(graph_type_frame, text="Undirected", variable=graph_type_var, value="undirected").pack(side=tk.LEFT)
    
    # Start and goal inputs
    node_input_frame = ttk.Frame(input_frame)
    node_input_frame.pack(fill=tk.X, pady=5)
    
    ttk.Label(node_input_frame, text="Start node:").pack(side=tk.LEFT)
    start_input = ttk.Entry(node_input_frame, width=10)
    start_input.pack(side=tk.LEFT, padx=5)
    start_input.insert(0, "A")
    
    ttk.Label(node_input_frame, text="Goal node:").pack(side=tk.LEFT, padx=(10,0))
    goal_input = ttk.Entry(node_input_frame, width=10)
    goal_input.pack(side=tk.LEFT, padx=5)
    goal_input.insert(0, "E")
    
    # Visualize button
    ttk.Button(main_frame, text="Visualize Graph", command=parse_input_adj_list).pack(pady=10)
    
    # Example section
    example_frame = ttk.LabelFrame(main_frame, text="Example Input", padding="10")
    example_frame.pack(fill=tk.BOTH, expand=True, pady=5)
    
    example_text = """Example 1 (Weighted):
A: B(2), C(5)
B: A(2), D(1)
C: A(5), D(3)
D: B(1), C(3), E(4)
E: D(4)

Example 2 (Unweighted):
A: B, C
B: A, D
C: A, D
D: B, C, E
E: D"""
    
    example_label = ttk.Label(example_frame, text=example_text, justify=tk.LEFT)
    example_label.pack(anchor=tk.W)
    
    return root, adj_list_input, start_input, goal_input, graph_type_var

if __name__ == "__main__":
    root, adj_list_input, start_input, goal_input, graph_type_var = create_main_window()
    root.mainloop()