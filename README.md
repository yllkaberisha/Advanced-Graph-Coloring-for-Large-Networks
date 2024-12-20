# Advanced-Graph-Coloring-for-Large-Networks
This project is a Python-based tool for visualizing graph coloring algorithms. It provides an interactive GUI to generate graphs, load graphs from files, save graphs, and visualize graph coloring using different algorithms. The tool supports greedy coloring by node order, greedy coloring by highest degree, and backtracking algorithms.

## Features
- **Graph Generation:** Generate random graphs with customizable nodes.
- **Load/Save Graphs:** Load graphs from JSON files or save generated graphs.
- **Visualization:** Visualize the graph coloring process step-by-step.
- **Algorithms:**
  - Greedy Coloring by Node Order
  - Greedy Coloring by Highest Degree
  - Backtracking Coloring

## User Guide
### Graph Operations
1. **Generate Graph:** Enter the number of nodes in the input box and click "Generate Graph" to create a random graph.
2. **Load Graph:** Load a graph from a JSON file.
3. **Save Graph:** Save the current graph to a JSON file.

### Graph Coloring
1. Select an algorithm from the buttons:
   - **Greedy by Node Order:** Colors nodes in the order of their indices.
   - **Greedy by Highest Degree:** Colors nodes in descending order of their degrees.
   - **Backtracking:** Uses backtracking to find an optimal coloring with minimal colors.
2. The graph visualization updates step-by-step to show the coloring process.

<table>
  <tr>
     <td>Greedy by Node Order</td>
     <td>Greedy by Highest Degree</td>
     <td>Backtracking</td>
  </tr>
  <tr>
    <td><img src="https://github.com/user-attachments/assets/94c3ae7c-0bfc-402c-a3aa-38839b213aaf" ></td>
    <td><img src="https://github.com/user-attachments/assets/d09d84cb-3af5-4a38-88c9-fee6b5f18537" ></td>
    <td><img src="https://github.com/user-attachments/assets/12f4f10c-aa64-4ab3-8f52-5e686cd76a27" ></td>
  </tr>
<tr>
    <td>Time complexity: O(n^2)</td>
    <td>Time complexity: O(n^2)</td>
    <td>Time complexity: O(m^n) (m - max colors, n - nodes)</td>
  </tr>
  <tr>
    <td>Space complexity: O(n)</td>
    <td>Space complexity: O(n)</td>
    <td>Space complexity: O(n)</td>
  </tr>
</table>

### Visualization
- Nodes are initially gray and are assigned colors as they are processed.
- The number of colors used is displayed at the end of the process.

## Code Structure
- **Graph Algorithms (`graph_algorithms.py`):** Contains implementations of graph coloring algorithms.
- **Graph Utilities (`graph_utils.py`):** Handles graph generation, loading, saving.
- **Main Script:** Combines algorithms and utilities to provide an interactive GUI.

## Example Graphs
Sample graphs in JSON format are included in the repository. These can be used to test the tool by loading them through the GUI.


  ## Installation
1. Clone the repository or download the source code.
2. Install Python and the required libraries:
   ```bash
   pip install networkx matplotlib
   ```

## How to Run
1. Open a terminal and navigate to the project directory.
2. Run the script:
   ```bash
   python main.py
   ```
3. The GUI will launch, allowing you to interact with the tool.

