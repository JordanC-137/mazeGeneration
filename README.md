# Algorithmically Generated Maze

This Python code uses Prim's Algorithm to reduce a graph to a Minimum Spanning Tree. Then uses this tree as a maze.
This maze is outputted using escape codes for colour, to the terminal.

**Perfect Maze**: A maze where any two cells can be joined by a unique path.


## How do we achieve a Perfect Maze
The algorithm, documented in this baeldung article, connects each cell of the graph. The algorithm iteratively picks the lowest-weight connection that links a new-node to the set of visited nodes.

If we provide a lattice structure with edges of random weights, the product will be a random maze. An important feature is that every node is connected to every node. This allows us to choose any 2 random nodes, and use them as our maze's start and end points. 

We can easily add a minimum Euclidean distance between the start and end points, as a method of giving the maze a minimum difficulty.

## Explanation of the code
The code consists of 2 files. The maze.py file and the Matrix.py file.

The matrix.py file is concerned with the maintenance of an *adjacency matrix*. An Adjacency Matrix is a useful way to represent the Graph data structure and the relationships between nodes. The Matrix class consists of a constructor, and methods related to creating/removing connections between nodes, as well as displaying the adjacency matrix.

## Intentions of this project
I carried out this project as a challenge to my Pythonic and algorithmic ability. Additionally, I wanted a project that involved Data Structures, while still being fun and accessible. There were multiple left turns and major changes in approach, but this was a fun project that I would definitely recommend
