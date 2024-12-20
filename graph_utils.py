import random
from tkinter import filedialog
import json
import numpy as np
import random

def generate_random_graph(n, density=0.1):
    adj_list = {i: [] for i in range(n)}
    
    for i in range(n):
        for j in range(i + 1, n):
            if random.random() < density:
                adj_list[i].append(j)
                adj_list[j].append(i) 
    
    return adj_list



def save_graph_to_file(adj_list):
    file_path = filedialog.asksaveasfilename(
        title="Save Graph to File",
        defaultextension=".json",
        filetypes=[("JSON files", "*.json"), ("Text files", "*.txt")]
    )
    if file_path:
        with open(file_path, 'w') as f:
            json.dump(adj_list, f, indent=4)  
        print(f"Graph saved to {file_path}")



def load_graph_from_file():
    global graph
    file_path = filedialog.askopenfilename(
        title="Load Graph from File",
        filetypes=[("JSON files", "*.json"), ("Text files", "*.txt")]
    )
    if file_path:
        with open(file_path, 'r') as f:
            graph = json.load(f)
        
        # Convert keys to integers
        graph = {int(node): neighbors for node, neighbors in graph.items()}
        
        print(f"Graph loaded from {file_path}")
        return graph

def adj_list_to_matrix(adj_list):
    # Get the number of nodes 
    nodes = list(adj_list.keys())
    n = len(nodes)
    
    # Empty adjacency matrix of size n x n
    adj_matrix = np.zeros((n, n), dtype=int)

    for node, neighbors in adj_list.items():
        for neighbor in neighbors:
            adj_matrix[node][neighbor] = 1
            adj_matrix[neighbor][node] = 1  

    return adj_matrix


def matrix_to_adj_list(matrix):
    adj_list = {}
    for i in range(len(matrix)):
        adj_list[i] = []
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                adj_list[i].append(j)
    print("adj_list", adj_list)
    return adj_list
