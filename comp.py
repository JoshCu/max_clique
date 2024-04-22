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
    remaining_edges = np.sum(graph) // 2
    max_edges = remaining_edges
    while remaining_edges > 0:
        max_degree = -1
        max_degree_vertex = -1

        for i in range(n):
            if i not in cover:
                degree = np.sum(graph[i])
                if degree > max_degree:
                    max_degree = degree
                    max_degree_vertex = i

        cover.add(max_degree_vertex)
        graph[max_degree_vertex] = np.zeros(n)
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