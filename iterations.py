# File Name

# @ Author: 
# Date:

class MonteCarloTreeSearch:

    def __init__(self):
        self.iteration = 0
        self.step_size = 1

    def get_number_of_iterations(self):

        while True:
            try:
                max_iterations = int(input('\nSet maximum number of iterations (default = 1000):'))
                break

            except:
                print('Number must be an integer.')

        print('Max iterations: ' + str(max_iterations))

        return max_iterations

    def iterate_algorithm(self, max_iteration):

        iteration = self.iteration

        while iteration < max_iteration:
            print('\nIteration: ' + str(iteration))
            iteration += self.step_size

        else:
            print('\n\nComplete (Iterations: ' + str(iteration) + ')')

        return iteration


if __name__ == '__main__':

    MCTS = MonteCarlo()

    max_iterations = MCTS.get_number_of_iterations()
    MCTS.iterate_algorithm(max_iterations)