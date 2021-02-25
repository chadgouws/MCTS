# Manage Monte Carlo Tree Search

# @ Author: Chad Gouws
# Date: 09/12/2019

import pickle
import numpy as np


class MonteCarloTreeSearchNode:

    def __init__(self, c_param, tree):
        self.c_param = c_param
        self.tree = tree
        self.rollout_actions = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.binary_actions = [0, 1]
        self.states = {1: [0, 0, 0, 0, 0, 0]}
        self.initial_parameters = [0, 0]
        self.parameters = {}
        self.children = []

    def is_terminal_node(self, node_key):

        if node_key not in self.tree:
            return True
        else:
            return False

    def expand_tree(self, state):

        keys = []
        for i in range(len(state)):
            for j in self.binary_actions:
                state[i] = j

                max_node_key = max(self.states)
                parent_node_key = max_node_key
                new_node_key = max_node_key + 1

                self._create_dictionaries(new_node_key, state)
                keys.append(new_node_key)

        self._create_children(parent_node_key, keys)

    def rollout(self, current_node):

        roll = np.random.randint(0, 20, 25)
        rollout_actions = self.rollout_actions

        for r in roll:
            rollout_actions = self._perform_rollout(r, rollout_actions)                    # Select move
            reward = self._is_win_loss(rollout_actions, current_node)                      # Check for win/loss

            if reward == 1:
                pass
            else:
                break

        return reward

    def best_child(self, node_key):

        children = self.tree[node_key]

        n = []
        w = []
        for child in children:
            p = self.parameters[child]
            n.append(p[0])
            w.append(p[1])

        N = self.parameters[node_key][0]

        uct = self._upper_confidence_bound(N, n, w)

        max_uct = np.where(uct == np.amax(uct))

        return children[max_uct[0][0]]

    def backpropagate(self, reward, branch):

        for node in branch:
            parameters = self.parameters[node]
            self.parameters[node] = [parameters[0] + 1, parameters[1] + reward]

    def _perform_rollout(self, action, rollout_actions):

        a = rollout_actions[0]
        b = rollout_actions[1]
        c = rollout_actions[2]
        d = rollout_actions[3]
        e = rollout_actions[4]
        f = rollout_actions[5]
        g = rollout_actions[6]
        start_day = rollout_actions[7]
        end_day = rollout_actions[8]
        salary_perc = rollout_actions[9]

        if action == 0:
            a -= 1
        elif action == 1:
            b -= 1
        elif action == 2:
            c -= 1
        elif action == 3:
            d -= 1
        elif action == 4:
            e -= 1
        elif action == 5:
            f -= 1
        elif action == 6:
            g -= 1
        elif action == 7:
            start_day -= 1
        elif action == 8:
            end_day -= 1
        elif action == 9:
            a += 1
        elif action == 10:
            b += 1
        elif action == 11:
            c += 1
        elif action == 12:
            d += 1
        elif action == 13:
            e += 1
        elif action == 14:
            f += 1
        elif action == 15:
            g += 1
        elif action == 16:
            start_day += 1
        elif action == 17:
            end_day += 1
        elif action == 18:
            salary_perc -= 1
        elif action == 19:
            salary_perc += 1
        else:
            pass

        return np.array([a, b, c, d, e, f, g, start_day, end_day, salary_perc])

    def _is_win_loss(self, current_node, previous_node, rollout_actions=None,):

        current_state = np.array(self.states[current_node])
        previous_state = np.array(self.states[previous_node])

        if rollout_actions is None:
            pass
        else:
            next_state = current_state + rollout_actions

        start_day = next_state[7]
        end_day = next_state[8]
        days = list(range(start_day, end_day))

        if start_day < 1:
            return 0
        elif end_day < start_day or end_day > 365:
            return 0
        elif self._is_state_valid(days, next_state):
            return 1
        else:
            return 0

    def _is_state_valid(self, days, next_state):

        coefficients = next_state[:7] / 1000

        for x in days:
            y = np.sum(coefficients * np.array([x**3, x**2, x, 1, 1/x, 1/x**2, 1/x**3]))

            if 0 < y < 0.9:
                flag = True
            else:
                flag = False
                break

        return flag

    def _upper_confidence_bound(self, N, n, w):
        return w / n + self.c_param * np.sqrt(np.log(N) / n)

    def _create_dictionaries(self, node_key, state):
        self.states[node_key] = state
        self.parameters[node_key] = self.initial_parameters

    def _create_children(self, parent_key, children_keys):
        self.tree[parent_key] = children_keys


if __name__ == '__main__':

    a = 1
