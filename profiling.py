"""
This code compares the performance of floyd warshall algorithms written recursively and non-recursively.
Created on 28th February 2024.
"""

from timeit import timeit
from floyd import floyd
from floyd_recursive import floyd2

NO_PATH = 2048
graph = [[0, 7, NO_PATH, 8], [NO_PATH, 0, 5, NO_PATH], [NO_PATH, NO_PATH, 0, 2], [NO_PATH, NO_PATH, NO_PATH, 0]]
MAX_LENGTH = len(graph[0])

TEST_RUNS = 600

if __name__ == '__main__':
    time_taken = timeit("floyd(graph)", number=TEST_RUNS, globals=globals())
    print("time taken for floyd without recursion: ", end="\n")
    print((time_taken * 1000000000) / TEST_RUNS, "ns")

    time_taken = timeit("floyd2(graph)", number=TEST_RUNS, globals=globals())

    print("time taken for floyd with recursion: ", end="\n")

    print((time_taken * 1000000000) / TEST_RUNS, "ns")
