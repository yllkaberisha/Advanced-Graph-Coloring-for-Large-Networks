import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy as np
from itertools import cycle

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

def greedy_coloring_by_degree(graph):
    G = matrix_to_adj_list(graph)
    nodes_sorted_by_degree = sorted(G, key=lambda node: len(G[node]), reverse=True)
    
    n = len(G)
    coloring = [-1] * n  # Initialize all nodes as uncolored

    for node in nodes_sorted_by_degree:
        neighbor_colors = set()
        for neighbor in G[node]:
            if coloring[neighbor] != -1:
                neighbor_colors.add(coloring[neighbor])

        # Find the first available color that is not used by the neighbors
        for color in range(n):
            if color not in neighbor_colors:
                coloring[node] = color
                break

    # Create the node order based coloring result
    ordered_colors = [coloring[node] for node in nodes_sorted_by_degree]
    
    return ordered_colors, nodes_sorted_by_degree



def matrix_to_adj_list(matrix):
    adj_list = {}
    for i in range(len(matrix)):
        adj_list[i] = []
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                adj_list[i].append(j)
    return adj_list



# Backtracking coloring algorithm
def backtracking_coloring(graph, m, node=0, result=None):
    if result is None:
        result = [-1] * len(graph)  # Store the color assigned to each node
    
    n = len(graph)
    
    if node == n:
        return result  # All nodes are colored
    
    for color in range(m):
        if is_safe(graph, node, color, result):
            result[node] = color
            result = backtracking_coloring(graph, m, node + 1, result)
            if -1 not in result:
                return result  # Solution found
    
    result[node] = -1  # Backtrack
    return result

def is_safe(graph, node, color, result):
    for neighbor in range(len(graph)):
        if graph[node][neighbor] == 1 and result[neighbor] == color:
            return False
    return True
