
 import random
import networkx as nx
import matplotlib.pyplot as plt

# Global variables
step = 0  # To track which node we are coloring
colors = []  # Store the colors of nodes
graph = []  # Store the graph structure
fig, ax = None, None  # To store the figure and axis for plotting
pos = None  # Store the fixed node positions

# Greedy coloring algorithm
def greedy_coloring(graph):
    n = len(graph)
    result = [-1] * n  # Store the color assigned to each node
    result[0] = 0  # Assign the first color to the first node
    
    # A temporary array to mark the availability of colors
    available = [False] * n

    # Assign colors to all the vertices one by one
    for u in range(1, n):
        # Mark the colors of adjacent nodes as unavailable
        for v in range(n):
            if graph[u][v] == 1 and result[v] != -1:  # If there's an edge and v is colored
                available[result[v]] = True

        # Find the first available color
        color = 0
        while color < n and available[color]:
            color += 1

        result[u] = color  # Assign the first available color
        available = [False] * n  # Reset the availability array for the next node
    
    return result
# Generate a random sparse graph
def generate_random_graph(n, density=0.1):
    graph = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            if random.random() < density:
                graph[i][j] = graph[j][i] = 1
    return graph

# Visualize the graph with assigned colors
def visualize_graph(graph, colors, step):
    global pos
    n = len(graph)
    G = nx.Graph()

    # Add nodes and edges to the graph
    for i in range(n):
        G.add_node(i)
    for i in range(n):
        for j in range(i+1, n):
            if graph[i][j] == 1:
                G.add_edge(i, j)

    # If the positions are not yet calculated, calculate them now
    if pos is None:
        pos = nx.spring_layout(G)  # Spring layout for better spacing (only once)

    # Set node colors based on the greedy algorithm result up to 'step' nodes
    node_colors = ['lightgrey'] * n
    for i in range(step):
        node_colors[i] = plt.cm.rainbow(colors[i] / (max(colors) + 1))  # Normalize color index for colormap

    # Clear previous plot and redraw the updated graph (but keep the layout fixed)
    ax.clear()
    nx.draw(G, pos, with_labels=True, node_size=500, font_size=12,
            node_color=node_colors, ax=ax)

    ax.set_title(f"Graph Coloring - Step {step}")
