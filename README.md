# Advanced-Graph-Coloring-for-Large-Networks
Grupi 30


# Graph Coloring Visualization Tool

## Overview
This project is a Python-based tool for visualizing graph coloring algorithms. It provides an interactive GUI to generate graphs, load graphs from files, save graphs, and visualize graph coloring using different algorithms. The tool supports greedy coloring by node order, greedy coloring by highest degree, and backtracking algorithms.

## Features
- **Graph Generation:** Generate random graphs with customizable density.
- **Load/Save Graphs:** Load graphs from JSON files or save generated graphs.
- **Visualization:** Visualize the graph coloring process step-by-step.
- **Algorithms:**
  - Greedy Coloring by Node Order
  - Greedy Coloring by Highest Degree
  - Backtracking Coloring

## Requirements
- Python 
- Libraries:
  - `networkx`
  - `matplotlib`
  - `tkinter`
  - `numpy`


  ## Installation
1. Clone the repository or download the source code.
2. Install the required Python libraries:
   ```bash
   pip install networkx matplotlib numpy
   ```

## How to Run
1. Open a terminal and navigate to the project directory.
2. Run the script:
   ```bash
   python graph_coloring_tool.py
   ```
3. The GUI will launch, allowing you to interact with the tool.

## User Guide
### Graph Operations
1. **Generate Graph:** Enter the number of nodes in the input box and click "Generate Graph" to create a random graph.
2. **Load Graph:** Load a graph from a JSON file using the "Load from File" button.
3. **Save Graph:** Save the current graph to a JSON file using the "Save Graph" button.

### Graph Coloring
1. Select an algorithm from the buttons:
   - **Greedy by Node Order:** Colors nodes in the order of their indices.
   - **Greedy by Highest Degree:** Colors nodes in descending order of their degrees.
   - **Backtracking:** Uses backtracking to find an optimal coloring with minimal colors.
2. The graph visualization updates step-by-step to show the coloring process.

### Visualization
- Nodes are initially gray and are assigned colors as they are processed.
- The number of colors used is displayed at the end of the process.

