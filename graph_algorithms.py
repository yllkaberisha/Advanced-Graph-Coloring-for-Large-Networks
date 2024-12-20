import networkx as nx
import matplotlib.pyplot as plt
from tkinter import messagebox
import numpy as np
from itertools import cycle

def greedy_coloring(graph, nodeOrder=None):
    n = len(graph)
    coloring = [-1] * n  # Initialize all nodes as uncolored

    if nodeOrder is not None:
        nodes = nodeOrder
    else:
        nodes = range(n);
    for node in nodes:
        # Collect colors used by neighbors
        neighbor_colors = set()
        for neighbor in graph[node]:
            if coloring[neighbor] != -1:
                neighbor_colors.add(coloring[neighbor])

       # Assign the smallest available color
        for color in range(n):
            if color not in neighbor_colors:
                coloring[node] = color
                break
    
    return coloring

def greedy_coloring_by_degree(graph):
    nodes_sorted_by_degree = sorted(graph, key=lambda node: len(graph[node]), reverse=True)

    coloring = greedy_coloring(graph, nodes_sorted_by_degree)

    # Create the node order based coloring result
    ordered_colors = [coloring[node] for node in nodes_sorted_by_degree]
    
    return ordered_colors, nodes_sorted_by_degree


def backtracking_coloring(graph, maxColorAllowed=None, gui_mode=False):
    n = len(graph)
    nodes_order_backtracking =[]
    color_order_backtracking = []
    if maxColorAllowed is None:
        maxColorAllowed = max(len(set(sum(graph, []))) for _ in range(n))  # Estimate maxColorAllowed if not provided

    print("Max Color Allowed:", maxColorAllowed)
    colors = [-1] * n  # Initialize all nodes as uncolored

    def is_valid_color(node, color, colors, G):
        """Check if no conflicts with neighbors"""
        for neighbor in G[node]:
            if colors[neighbor] == color:
                return False
        return True

    def backtrack(node, G, maxColorAllowed, colors):
        if node == len(G):
            return True  # All nodes have been successfully colored
        
        for color in range(maxColorAllowed):
            if is_valid_color(node, color, colors, G):
                colors[node] = color

                # For better visualization
                nodes_order_backtracking.append(node)
                color_order_backtracking.append(color)

                if backtrack(node + 1, G, maxColorAllowed, colors): # Go to next node
                    return True
                colors[node] = -1  # Backtrack
                # For better visualization
                nodes_order_backtracking.append(node)
                color_order_backtracking.append(-1)

        return False

    if backtrack(0, graph, maxColorAllowed, colors):
        return color_order_backtracking, nodes_order_backtracking
    else:
        if gui_mode:
            messagebox.showinfo("No Solution", f"Solution does not exist for the given number {maxColorAllowed} of colors.")
        else:
            print(f"Solution does not exist for the given number of {maxColorAllowed} colors.")
        return [-1] * n, range(n)  # If coloring fails
