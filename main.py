import tkinter as tk
from tkinter import ttk, filedialog
from graph_utils import generate_random_graph
from graph_algorithms import greedy_coloring, greedy_coloring_by_degree, backtracking_coloring
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import pickle
import networkx as nx  # Importing networkx

# Global variables
step = 0  # To track which node we are coloring
colors = []  # Store the colors of nodes
graph = []  # Store the graph structure
fig, ax = None, None  # To store the figure and axis for plotting
pos = None  # Store the fixed node positions
nodes_order = [] 

# Function to visualize the graph with assigned colors
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

    # If the positions are not yet calculated, calculate them now
    if pos is None:
        degrees = [deg for _, deg in G.degree()]  # Calculate degrees
        pos = {node: position for node, position in sorted(nx.spring_layout(G).items(), key=lambda item: degrees[item[0]], reverse=True)}

    # Set node colors based on the greedy algorithm result up to 'step' nodes
    node_colors = ['lightgrey'] * n
    for i in range(step):
        node_colors[nodes_order[i]] = plt.cm.rainbow(colors[i] / (max(colors) + 1))  # Normalize color index for colormap

    # Clear previous plot and redraw the updated graph (but keep the layout fixed)
    ax.clear()
    nx.draw(G, pos, with_labels=True, node_size=500, font_size=12,
            node_color=node_colors, ax=ax)

    ax.set_title(f"Graph Coloring - Step {step}")
    canvas.draw()

# Function to be called when the button is clicked
def start_coloring(algorithm):
    global step, graph, colors, pos, nodes_order  # Add nodes_order global variable
    print("Graph ", graph)
    step = 0  # Reset step to start coloring from the first node
    if algorithm == 'order':
        colors = greedy_coloring(graph)  # Use original greedy coloring with node order
        nodes_order = list(range(len(graph))) 
    elif algorithm == 'degree':
        colors, nodes_order = greedy_coloring_by_degree(graph)  # Use greedy by highest degree
    elif algorithm == 'backtracking':
        m = max(len(set(sum(graph, []))) for _ in range(len(graph)))  # Estimating the number of colors needed
        colors = backtracking_coloring(graph, m)  # Use backtracking coloring
    print("Node order" , nodes_order)
    print("Colors", colors)
    visualize_next_node()  # Start the coloring process

# Function to visualize the next node in the graph
def visualize_next_node():
    global step
    if step < len(graph):  # Continue coloring until all nodes are colored
        visualize_graph(graph, colors, step + 1)  # Visualize the graph with the next color
        step += 1  # Increment step to color the next node
        root.after(500, visualize_next_node)  # Call this function after 500ms to color the next node

# Function to generate a new random graph
def generate_graph():
    global graph, colors, step
    n = 10  # Default number of nodes
    graph = generate_random_graph(n, density=0.3)  # Generate random sparse graph
    step = 0  # Reset step count
    visualize_graph(graph, colors, step)  # Visualize the new graph
    # save_graph_to_file(graph)

# Function to load graph from file
def load_graph_from_file():
    global graph, colors, step
    file_path = filedialog.askopenfilename(title="Load Graph from File", filetypes=[("Pickle files", "*.pkl")])
    if file_path:
        with open(file_path, 'rb') as f:
            graph = pickle.load(f)
        colors = greedy_coloring(graph)  # Apply greedy coloring algorithm
        step = 0  # Reset step count
        visualize_graph(graph, colors, step)  # Visualize the loaded graph
# Function to save graph to file
def save_graph_to_file(graph):
    file_path = filedialog.asksaveasfilename(title="Save Graph to File", defaultextension=".pkl", filetypes=[("Pickle files", "*.pkl")])
    if file_path:
        with open(file_path, 'wb') as f:
            pickle.dump(graph, f)

# Set up the GUI using Tkinter
def create_gui():
    global step, colors, graph, canvas, ax, root
    step = 0  # Initialize step count to 0
    graph = generate_random_graph(10, density=0.3)  # Generate random sparse graph
    colors = greedy_coloring(graph)  # Apply greedy coloring algorithm
    
    # Create the main window
    root = tk.Tk()
    root.title("Graph Coloring")

    # Set window size
    root.geometry("800x600")



    # Create buttons - first row: load and generate
    button_frame_top = ttk.Frame(root)
    button_frame_top.pack(side=tk.TOP, fill=tk.X, pady=10)
    
    load_button = ttk.Button(button_frame_top, text="Load from File", command=load_graph_from_file)
    load_button.pack(side=tk.LEFT, padx=5)
    
    generate_button = ttk.Button(button_frame_top, text="Generate Graph", command=generate_graph)
    generate_button.pack(side=tk.LEFT, padx=5)

    # Create buttons - second row: algorithm options
    button_frame_bottom = ttk.Frame(root)
    button_frame_bottom.pack(side=tk.TOP, fill=tk.X, pady=10)

    greedy_by_order_button = ttk.Button(button_frame_bottom, text="Greedy by Node Order", command=lambda: start_coloring('order'))
    greedy_by_order_button.pack(side=tk.LEFT, padx=5)

    greedy_by_degree_button = ttk.Button(button_frame_bottom, text="Greedy by Highest Degree", command=lambda: start_coloring('degree'))
    greedy_by_degree_button.pack(side=tk.LEFT, padx=5)

    backtracking_button = ttk.Button(button_frame_bottom, text="Backtracking", command=lambda: start_coloring('backtracking'))
    backtracking_button.pack(side=tk.LEFT, padx=5)

    # Create a figure and axis for the graph plot
    global fig, ax
    fig, ax = plt.subplots(figsize=(8, 6))

    # Create a canvas to embed the matplotlib figure in the Tkinter window
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().pack()

    # Run the Tkinter event loop
    root.mainloop()

# Main function to start the program
if __name__ == "__main__":
    create_gui()




