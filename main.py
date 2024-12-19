import tkinter as tk
from tkinter import ttk, filedialog
from graph_utils import generate_random_graph, load_graph_from_file, save_graph_to_file
from graph_algorithms import greedy_coloring, greedy_coloring_by_degree, backtracking_coloring
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import networkx as nx  


step = 0                    # Track which node we are coloring
colors = []                 # Colors of nodes
graph = []                  # Graph structure
fig, ax = None, None        # Figure and axis for plotting
pos = None                  # Fixed node positions
nodes_order = []            # Order of which nodes to be colored first


def start_coloring(algorithm):
    global step, graph, colors, pos, nodes_order 
    print("Graph ", graph)
    step = 0 
    if algorithm == 'order':
        colors = greedy_coloring(graph) 
        nodes_order = list(range(len(graph))) 
    elif algorithm == 'degree':
        colors, nodes_order = greedy_coloring_by_degree(graph)
    elif algorithm == 'backtracking':
        m = 3
        colors, nodes_order  = backtracking_coloring(graph, m) 
    print("Node order" , nodes_order)
    print("Colors", colors)
    visualize_next_node()


def generate_graph(type):
    global graph, colors, step, nodes_entry, pos
    
    try:
        n = int(nodes_entry.get())  # Get the number of nodes from the input
        if n <= 0:
            raise ValueError("Number of nodes must be a positive integer.")
    except ValueError:
        print("Invalid input for the number of nodes. Using default value (10).")
        n = 10
   
    print("Generating graph with", n, "nodes.")
    if type == 'load':
        graph = load_graph_from_file()
    else:
        graph = generate_random_graph(n, density=0.3)  
    step = 0  
    pos = None
    visualize_graph(graph, colors, step) 


def visualize_next_node():
    global step
    if step < len(graph):                         # Coloring until all nodes are colored
        visualize_graph(graph, colors, step + 1)  
        step += 1 
        root.after(500, visualize_next_node)      # Delay of 500ms for animation

def visualize_graph(graph, colors, step):
    global pos, nodes_order
    n = len(graph)
    G = nx.Graph()

    # Add nodes and edges to the graph
    for i in range(n):
        G.add_node(i)
    for i in range(n):
        for j in range(i + 1, n):
            if graph[i][j] == 1:
                G.add_edge(i, j)

    # Calculate positions and degrees
    if pos is None:
        degrees = [deg for _, deg in G.degree()] 
        pos = {node: position for node, position in sorted(nx.spring_layout(G).items(), key=lambda item: degrees[item[0]], reverse=True)}

    # Set node colors based on the greedy algorithm result
    node_colors = ['lightgrey'] * n
    for i in range(step):
        if i < len(nodes_order) and i < len(colors):
            node_colors[nodes_order[i]] = plt.cm.rainbow(colors[i] / (max(colors) + 1)) 


    # Clear previous plot and redraw the updated graph 
    ax.clear()
    nx.draw(G, pos, with_labels=True, node_size=500, font_size=12,
            node_color=node_colors, ax=ax)

    ax.set_title(f"Graph Coloring - Step {step}")
    canvas.draw()

def create_gui():
    global step, colors, graph, canvas, ax, root, nodes_entry
    step = 0  
    
    # Create the main window
    root = tk.Tk()
    root.title("Graph Coloring")
    root.geometry("1000x800")

    style = ttk.Style()
    style.configure(
       "Large.TButton",
        font=("Arial", 14),  
        padding=(10, 10)    
    )

    input_frame = ttk.Frame(root)
    input_frame.pack(side=tk.TOP, fill=tk.X, pady=10)

    nodes_label = ttk.Label(input_frame, text="Number of Nodes:", font=("Arial", 14))
    nodes_label.pack(side=tk.LEFT, padx=5)

    nodes_entry = ttk.Entry(input_frame, font=("Arial", 14), width=10)
    nodes_entry.pack(side=tk.LEFT, padx=5)
    nodes_entry.insert(0, "10") 

    button_frame_top = ttk.Frame(root)
    button_frame_top.pack(side=tk.TOP, fill=tk.X, pady=10)
    
    load_button = ttk.Button(button_frame_top, text="Load from File", command=lambda: generate_graph('load'), style="Large.TButton")
    load_button.pack(side=tk.LEFT, padx=5)
    
    generate_button = ttk.Button(button_frame_top, text="Generate Graph",command=lambda: generate_graph('random'), style="Large.TButton")
    generate_button.pack(side=tk.LEFT, padx=5)

    save_button = ttk.Button(button_frame_top, text="Save Graph", command=lambda: save_graph_to_file(graph), style="Large.TButton")
    save_button.pack(side=tk.LEFT, padx=5)

    button_frame_bottom = ttk.Frame(root)
    button_frame_bottom.pack(side=tk.TOP, fill=tk.X, pady=10)

    greedy_by_order_button = ttk.Button(button_frame_bottom, text="Greedy by Node Order", command=lambda: start_coloring('order'), style="Large.TButton")
    greedy_by_order_button.pack(side=tk.LEFT, padx=5)

    greedy_by_degree_button = ttk.Button(button_frame_bottom, text="Greedy by Highest Degree", command=lambda: start_coloring('degree'), style="Large.TButton")
    greedy_by_degree_button.pack(side=tk.LEFT, padx=5)

    backtracking_button = ttk.Button(button_frame_bottom, text="Backtracking", command=lambda: start_coloring('backtracking'), style="Large.TButton")
    backtracking_button.pack(side=tk.LEFT, padx=5)

    # Create a figure and axis for the graph plot
    global fig, ax
    fig, ax = plt.subplots(figsize=(10, 8))

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().pack()


    root.mainloop()

# Start the program
if __name__ == "__main__":
    create_gui()




