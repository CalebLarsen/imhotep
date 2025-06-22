from imhotep_game import game_core, State, InputVec, StateVec  # noqa: F401
import numpy as np
import random

STATE_VEC_LEN = 6 # Couldn't get this to be automatic :(
INPUT_VEC_LEN = 4

class HyperParams:
    def __init__(self):
        self.runs = 100
        self.big_mutation = 0.01
        self.small_mutation = 0.1

def random_matrix():
    # m = np.zeros((INPUT_VEC_LEN, STATE_VEC_LEN))
    # for y in range(INPUT_VEC_LEN):
    #     for x in range(STATE_VEC_LEN):
    #         m[y][x] = random.random() * 3000000
    m = np.array([[2.99978805e-01, 2.49982338e-03, 3.29976686e-04, 0.00000000e+00,
  0.00000000e+00, 0.00000000e+00],
 [2.99978805e-04, 2.49982338e-06, 3.29976686e-07, 0.00000000e+00,
  0.00000000e+00, 0.00000000e+00],
 [6.99950545e-04, 5.83292121e-06, 7.69945600e-07, 0.00000000e+00,
  0.00000000e+00, 0.00000000e+00],
 [8.33274459e-03, 6.94395382e-05, 9.16601905e-06, 0.00000000e+00,
  0.00000000e+00, 0.00000000e+00]])
    return m

def np_to_input(input) -> InputVec:
    return input[0], input[1], input[2], input[3]

def fitness(state: State) -> float:
    fitness = 0
    fitness += state.people
    fitness += state.tels_flooded * 100
    fitness += state.storage * 1000
    fitness += state.years * 1000000
    fitness -= state.errors * 10000000
    fitness += state.levels * 10000000
    if state.years == 0:
        fitness -= 1000000000
    return fitness

def test_matrix(m) -> float:
    total_fitness = 0
    hp = HyperParams()
    for _ in range(hp.runs):
        state = State()
        while not state.finished:
            input = np_to_input(m @ state.vector())
            state = game_core(state, input)
        total_fitness += fitness(state)
    return total_fitness / hp.runs

def mutate_matrix(m):
    m_copy = m.copy()
    hp = HyperParams()
    for y in range(INPUT_VEC_LEN):
        for x in range(STATE_VEC_LEN):
            r = random.random()
            if r < hp.big_mutation:
                mut = random.random() / 2 - 0.5
                m_copy[y][x] = mut
                pass
            elif r < hp.small_mutation:
                # mut = random.random() / 1e-5 - 5e-6
                # m_copy[y][x] += mut
                pass
    return m_copy
            

def main():
    prev_m = random_matrix()
    best_f = float('-inf')
    bestest_m = random_matrix()
    for _ in range(100):
        best_m = np.eye(2)
        best_fit = float('-inf')
        for _ in range(HyperParams().runs):
            m = mutate_matrix(prev_m)
            f = test_matrix(m)
            if f > best_fit:
                best_fit = f
                best_m = m
        prev_m = best_m
        print("Fitness:", best_fit)
        if best_fit > best_f:
            best_f = best_fit
            bestest_m = best_m
    print("Best:", best_f)
    print("Best Matrix:", bestest_m)


if __name__ == "__main__":
    main()
