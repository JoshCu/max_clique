import numpy as np
import argparse
from pathlib import Path
from functools import lru_cache

@lru_cache()
def load_file(filename: Path) -> np.ndarray:
    # check that the file is a .adjmat file
    if str(filename).endswith(".adjmat"):
        return load_mat_file(filename)
    else:
        filename = filename.with_suffix(".adjmat")
        if not filename.is_file():
            raise FileNotFoundError(f"Expected an .adjmat file, could not find an existing called {filename}")
        return load_mat_file(filename)

def load_mat_file(filename: Path) -> np.ndarray:
    # read the file and parse the weights (connections)
    with open(filename, "r") as file:
        file_content = [[int(weight) for weight in line.strip().split()[1:]] for line in file]

    matrix = np.zeros((len(file_content), len(file_content)), dtype=int)
    for i, row in enumerate(file_content):
        for j, weight in enumerate(row[:-1]):
            matrix[i, j] = weight
    # mirror over the diagonal
    matrix = np.maximum(matrix, matrix.T)
    return matrix

def parse_args():
    # parse the filename from the command line
    parser = argparse.ArgumentParser(description="Maximal Clique Finder")
    parser.add_argument("filename", type=str, help="Path to the file")
    args = parser.parse_args()
    return Path(args.filename)