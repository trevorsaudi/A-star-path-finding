# A* Path Finding Algorithm

This project implements the A* path-finding algorithm using Python and Pygame. The goal of the algorithm is to find the shortest path between a start point (A) and an end point (B) in a grid of nodes and edges. The algorithm uses informed search with heuristics to efficiently explore the search space.

## Dependencies

To run this project, you need to have the following dependencies installed:

- Python 3.x
- Pygame

## Installation

1. Install Python: Visit the official Python website (`https://www.python.org`) and download the latest version of Python for your operating system. Follow the installation instructions to complete the installation.

2. Install Pygame: Open a terminal or command prompt and run the following command to install Pygame using pip:

   ```
   pip install pygame
   ```

## Running the Code

To run the A* path-finding algorithm, follow these steps:

1. Open a terminal or command prompt and navigate to the directory where you have saved the Python script.

2. Run the following command to execute the script:

   ```
   python script_name.py
   ```

   Replace `script_name.py` with the actual name of the Python script file.

3. Once the Pygame window opens, you will see a grid displayed. You can click on the grid to define the start point (left-click), end point (left-click after setting the start point), and barriers (left-click and drag). Right-clicking on a node will remove any existing markers.

4. Press the SPACE key to start the algorithm once you have set the start and end points. The algorithm will search for the shortest path between the two points and visualize the process on the grid.

5. Press the C key to clear the grid and start again with new points.

6. To exit the program, close the Pygame window or press the ESC key.

Note: You can modify the `ROWS` and `WIDTH` variables in the code to adjust the size of the grid and the window dimensions.

## Demo 
Run the application on the terminal 

![alt text](https://github.com/trevorsaudi/A-star-path-finding/blob/main/demo.gif "Demo")

