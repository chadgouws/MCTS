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

        false_keys = [124, 10, 30, 41, 1000, 357, 10893]
        true_keys = [1, 2, 3, 4, 5]

        for node_key in false_keys:
            flag = self.mcn.is_terminal_node(node_key)

            if not flag:
                return print('TEST: is_terminal_node: ', str(False), '\tFault: false_keys')
            else:
                pass

        for node_key in true_keys:
            flag = self.mcn.is_terminal_node(node_key)

            if flag:
                return print('TEST: is_terminal_node: ', str(False), '\t| Fault: true_keys')
            else:
                pass

        return print('TEST: is_terminal_node:\t\t', str(True))

    def test_expand_tree(self):

        state = [1, 0, 0, 0, 0, 0]
        s = len(self.mcn.states)
        self.mcn.expand_tree(state)

        if len(self.mcn.states) == s+2*len(state):
            return print('TEST: expand_tree: \t\t\t True')
        else:
            return print('TEST: expand_tree: \t\t\t False \t| Fault')


if __name__ == '__main__':
    t = TestMonteCarloTreeSearch()

    t.test_is_terminal_node()
    t.test_expand_tree()
