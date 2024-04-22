# Maximal Clique Finder

This project includes Python scripts to find the maximal clique in a graph using different algorithms. The graphs are represented as adjacency matrices stored in `.adjmat` files.

## Runtime / Performance warnings
1. [`brute_force.py`](brute_force.py): Will run effectively forever on any graph larger than ~10
2. [`vertex_cover.py`](vertex_cover.py): Performs so poorly it finds no max clique on any example files

## Python Files

1. [`brute_force.py`](brute_force.py): This script uses a simple brute force algorithm to find the maximal clique. It is slow and inefficient, but guaranteed to work.

2. [`vertex_cover.py`](vertex_cover.py): This script will find the vertex cover of the complement graph, then use that to give an approximation of the max clique

3. [`comp.py`](comp.py): This script uses a more efficient algorithm to find the maximal clique. It still works by subtracting the vertex cover of the complement from the nodes, but it calculates the vertex cover by adding the highest degree nodes first. It uses the `numba` library for just-in-time compilation to speed up the computation.

4. [`utils.py`](utils.py): This script includes utility functions to load the adjacency matrix from a file and parse command line arguments.

## Installation

To install the necessary packages, run the following command:

```bash
# install numba numpy tqdm
pip install -r requirements.txt
```

## Usage
To run any of the Python scripts with a specific .adjmat file, use the following command:

```bash
python comp.py graphs/Q60V1000.adjmat
```
