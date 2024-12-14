
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