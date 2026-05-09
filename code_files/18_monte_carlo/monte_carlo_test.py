import numpy as np
from Gridworld_test import standard_grid, negative_grid
from iterative_policy_evaluation_deterministic_test import print_policy, print_values

GAMMA = 0.9



def play_game(grid, policy, max_steps = 20):
    start_state = list(grid.actions.keys())
    start_idx = np.random.choice(len(start_state))
    grid.set_state(start_state[start_idx])

    s = grid.current_state()

    states = [s]
    rewards = [0]

    steps = 0

    while not grid.game_over():
        a = policy[s]
        r = grid.move(a)
        next_s = grid.current_state()

        states.append(next_s)
        rewards.append(r)

        steps += 1
        if steps >= max_steps:
            break

        s = next_s
    return states, rewards


if __name__ == '__main__':
    grid = standard_grid()

    print('Rewards:')
    print_values(grid.rewards,grid)

    policy = {
        (2, 0): 'U',
        (1, 0): 'U',
        (0, 0): 'R',
        (0, 1): 'R',
        (0, 2): 'R',
        (1, 2): 'R',
        (2, 1): 'R',
        (2, 2): 'R',
        (2, 3): 'U',
    }

    V = {}
    returns = {}
    states = grid.all_states()

    for s in states :
        if s in grid.actions :
            returns[s] = []
        else :
            V[s] = 0

    for t in range(100) :
        states, rewards = play_game(grid, policy)
        G = 0
        T = len(states)

        for t in range(T-2,-1,-1):
            s = states[t]
            r = rewards[t+1]
            G = r + GAMMA * G

            if s not in states[:t] :
                returns[s].append(G)
                V[s] = np.mean(returns[s])

    print('Values:')
    print_values(V,grid)
    
    print('policy:')
    print_policy(policy,grid) 