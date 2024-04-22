# Similar to vertex_cover.py
# This script finds an approximation of the maximal clique in a graph
# First find the complement of the graph
# Then find the vertex cover of the complement
######### adding the node with the highest degree first! #########
# The maximal clique is the set of all nodes not in the complement vertex cover

from utils import load_file, parse_args
import numpy as np
from numba import njit

def complement_graph(graph):
    complement = np.ones_like(graph) - graph
    np.fill_diagonal(complement, 0)
    return complement

@njit
def greedy_vertex_cover(graph):
    n = len(graph)
    cover = set()
    # the number of edges in the graph
    # is the sum of the upper triangle of the adjacency matrix
    remaining_edges = np.sum(graph) // 2
    max_edges = remaining_edges
    # while there are still edges in the graph
    while remaining_edges > 0:
        max_degree = -1
        max_degree_vertex = -1
        # find the node with the highest degree
        for i in range(n):
            # if the node is not already in the cover
            if i not in cover:
                degree = np.sum(graph[i])
                # check if the degree is higher than the current max
                # and if it is, update the max
                if degree > max_degree:
                    max_degree = degree
                    max_degree_vertex = i

        # add the node with the highest degree to the cover
        cover.add(max_degree_vertex)
        # remove the edges connected to the node
        # this sets the row to all zeros
        graph[max_degree_vertex] = np.zeros(n)
        # this magic numpy slice sets the column to all zeros
        graph[:, max_degree_vertex] = 0
        remaining_edges -= max_degree

    return cover

def maximal_clique(graph):
    complement = complement_graph(graph)
    cover = greedy_vertex_cover(complement)
    clique = set(range(len(graph))) - cover
    return clique

# Example graph
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
