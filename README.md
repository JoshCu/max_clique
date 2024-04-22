# Maximal Clique Finder

This project includes Python scripts to find the maximal clique in a graph using different algorithms. The graphs are represented as adjacency matrices stored in `.adjmat` files.

## Runtime / Performance warnings
1. [`brute_force.py`](brute_force.py): Will run effectively forever on any graph larger than ~10
2. [`vertex_cover.py`](vertex_cover.py): Performs so poorly it finds no max clique on any example files

## Python Files

1. [`brute_force.py`](brute_force.py): This script uses a simple brute force algorithm to find the maximal clique. It is slow and inefficient, but guaranteed to work.

2. [`vertex_cover.py`](vertex_cover.py): This script will find the vertex cover of the compliment graph, then use that to give an approximation of the max clique

3. [`comp.py`](comp.py): This script uses a more efficient algorithm to find the maximal clique. It's similar to the vertex_cover implementation except it uses a better vertex cover algorithm. It uses the `numba` library for just-in-time compilation to speed up the computation.

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
