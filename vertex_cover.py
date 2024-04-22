# Find an approximation of the maximal clique in a graph
# First find the complement of the graph
# Then find the vertex cover of the complement
# The maximal clique is the set of all nodes not in the complement vertex cover
from utils import load_file, parse_args
import numpy as np

def complement_graph(graph):
    # create a matrix of ones the same size as the graph
    # then subtract the graph from it to get the complement
    complement = np.ones_like(graph) - graph
    # set the diagonal to zero
    np.fill_diagonal(complement, 0)
    return complement

def vertex_cover(graph):
    # greedy algorithm to find a vertex cover
    n = len(graph)
    cover = set()
    # for each start node
    for i in range(n):
        # for each end node
        for j in range(i + 1, n):
            # if there is an edge between the two nodes 
            # and neither node is in the cover
            # add both nodes to the cover
            if graph[i][j] and i not in cover and j not in cover:
                cover.add(i)
                cover.add(j)
    return cover

def maximal_clique(graph):
    complement = complement_graph(graph)
    cover = vertex_cover(complement)
    clique = set(range(len(graph))) - cover
    return clique

# Example usage
graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
]

if __name__ == "__main__":
    # python comp.py graph.adjmat
    file_path = parse_args()
    graph = load_file(file_path)
    clique = maximal_clique(graph)
    print("Maximal Clique:", clique)
    print("Size:", len(clique))