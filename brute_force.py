# This is a very simple brute force algorithm.
# It is extremely slow and inefficient, but it is simple and guaranteed to work.
# For a given graph, genereate every possible combination of nodes.
# Check one by one if the combination is a clique.

from utils import load_file, parse_args
from tqdm import tqdm
from itertools import combinations

def find_largest_clique(graph):
    n = len(graph)
    max_clique = []
    # iterate over all possible clique sizes
    for k in range(n, 0, -1):
        # iterate over all possible combinations of nodes
        for combo in tqdm(combinations(range(n), k)):
            is_clique = True
            # check if the combination is a clique
            for i in range(k):
                for j in range(i + 1, k):
                    if not graph[combo[i]][combo[j]]:
                        is_clique = False
                        break
                if not is_clique:
                    break
            if is_clique:
                return list(combo)

    return max_clique

# Example graph
graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
]

if __name__ == "__main__":
    # python brute_force.py graph.adjmat
    file_path = parse_args()
    adj_mat = load_file(file_path)
    clique = find_largest_clique(adj_mat)
    print("Maximal Clique:", clique)
    print("Size:", len(clique))

    