# Monte Carlo Tree Search

# @ Author: Chad Gouws
# Date: 07/01/2020

from AlgorithmManagement import MonteCarloTreeSearchNode


n = MonteCarloTreeSearchNode()


class MonteCarloTreeSearch:

    def __init__(self):
        self.root = 1

    def best_action(self, no_of_simulations):

        for sim in no_of_simulations:

            branch = self._tree_policy()
            previous_node = branch[-2]
            current_node = branch[-1]
            reward = n.rollout(current_node)
            n.backpropagate(reward, branch)

        # Save all information

        return print('Simulations Complete')

    def _tree_policy(self):

        current_node = self.root
        branch = []
        while not n.is_terminal_node(current_node):
            branch.append(current_node)
            current_node = n.best_child(current_node)

        return branch
