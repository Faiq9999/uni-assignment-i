from timeit import timeit
from floyd import floyd
from floyd_recursive import floyd as floyd_recursive

NO_PATH = 2048
graph = [[0, 7, NO_PATH, 8], [NO_PATH, 0, 5, NO_PATH], [NO_PATH, NO_PATH, 0, 2], [NO_PATH, NO_PATH, NO_PATH, 0]]
MAX_LENGTH = len(graph[0])


TEST_RUNS=600

time_taken = timeit("floyd(graph)",number=TEST_RUNS,globals=globals())
print("time taken for floyd without recursion: ", end="\n")
print((time_taken*1000000000) / TEST_RUNS, "ns")


time_taken = timeit("floyd_recursive(graph)",number=TEST_RUNS,globals=globals())

print("time taken for floyd with recursion: ", end="\n")

print((time_taken*1000000000) / TEST_RUNS, "ns")

