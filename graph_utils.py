import random
from tkinter import filedialog
def generate_random_graph(n, density=0.1):
    graph = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            if random.random() < density:
                graph[i][j] = graph[j][i] = 1
    return graph

def save_graph_to_file(graph):
    """Save the graph as an adjacency matrix to a file."""
    file_path = filedialog.asksaveasfilename(
        title="Save Graph to File",
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt")]
    )
    if file_path:
        with open(file_path, 'w') as f:
            for row in graph:
                f.write(' '.join(map(str, row)) + '\n')
        print(f"Graph saved to {file_path}")


def load_graph_from_file():
    """Load a graph from a file containing an adjacency matrix."""
    global graph
    file_path = filedialog.askopenfilename(
        title="Load Graph from File",
        filetypes=[("Text files", "*.txt")]
    )
    if file_path:
        with open(file_path, 'r') as f:
            graph = [list(map(int, line.split())) for line in f.readlines()]
        print(f"Graph loaded from {file_path}")
        return graph
