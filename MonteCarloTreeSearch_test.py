# Test MonteCarloTreeSearch.py

# @ Author: Chad Gouws
# Date: 03/02/2020

from AlgorithmManagement import MonteCarloTreeSearchNode
import numpy as np


class TestMonteCarloTreeSearch:

    def __init__(self):
        self.tree = {1: [0, 1, 0, 2, 3, 5],
                     2: [0, 1, 0, 2, 3, 5],
                     3: [0, 1, 0, 2, 3, 5],
                     4: [0, 1, 0, 2, 3, 5],
                     5: [0, 1, 0, 2, 3, 5]}
        self.c_param = np.sqrt(2)
        self.mcn = MonteCarloTreeSearchNode(self.c_param, self.tree)

    def test_is_terminal_node(self):
        node_keys = [124, 10, 30, 41, 1000, 357, 10893]

        for node_key in node_keys:
            flag = self.mcn.is_terminal_node(node_key)

            if not flag:
                return False
            else:
                pass

        return True


if __name__ == '__main__':
    t = TestMonteCarloTreeSearch()

    t.test_is_terminal_node()
