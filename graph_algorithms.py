import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy as np
from itertools import cycle

def greedy_coloring(graph, nodeOrder=None):
    G = matrix_to_adj_list(graph)
    n = len(G)
    coloring = [-1] * n  # Initialize all nodes as uncolored

    if nodeOrder is not None:
        nodes = nodeOrder
    else:
        nodes = range(n);
    for node in nodes:
        # Collect colors used by neighbors
        neighbor_colors = set()
        for neighbor in G[node]:
            if coloring[neighbor] != -1:
                neighbor_colors.add(coloring[neighbor])

       # Assign the smallest available color
        for color in range(n):
            if color not in neighbor_colors:
                coloring[node] = color
                break
    
    return coloring

def greedy_coloring_by_degree(graph):
    G = matrix_to_adj_list(graph)
    nodes_sorted_by_degree = sorted(G, key=lambda node: len(G[node]), reverse=True)
    
    n = len(G)
    coloring = greedy_coloring(graph, nodes_sorted_by_degree)

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
    print("adj_list", adj_list)
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