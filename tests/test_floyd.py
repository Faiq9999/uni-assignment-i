from unittest import TestCase
from floyd import floyd

NO_PATH = 2048
graph = [[0, 7, NO_PATH, 8], [NO_PATH, 0, 5, NO_PATH], [NO_PATH, NO_PATH, 0, 2], [NO_PATH, NO_PATH, NO_PATH, 0]]
MAX_LENGTH = len(graph[0])


class TestFloyd(TestCase):
    def test_floyd(self):
        expected_result = [[0, 7, 12, 8], [2048, 0, 5, 7], [2048, 2048, 0, 2], [2048, 2048, 2048, 0]]
        actual_result = floyd(graph)
        assert actual_result == expected_result
