from numpy.random import choice
import numpy as np
import time

start_time = time.time()
nr_sims = 100000

# H will be encoded as 0
# T will be encoded as 1
# This is done to make the computations easier

# List of biases. 60% of the data 1 40% 0
biases = choice([0, 1], nr_sims, p=[.4, .6])


# We will first make 4 lists. Each simulating the coin flips when the coin is biased for 0.
# Then we will sum these lists together to find the sum of 4 flips. (H=0, T=1)
# Then we will do the same with a coin biased for 1.

# sum a list of 4 np arrays together. It looks like this:
# sum ([
#     [1, 0, 1, 1, ...],
#     [1, 0, 0, 1, ...],
#     [0, 0, 1, 0, ...],
#     [1, 1, 1, 0, ...]
# ])
#   = [3, 1, 3, 2, ...]

sim_all_0 = sum([choice([0, 1], nr_sims, p=[.7, .3]) for i in range(4)])
sim_all_1 = sum([choice([1, 0], nr_sims, p=[.7, .3]) for i in range(4)])

# Multiply all coin flip sums in sim_all_0 with 0 when the coin is biased for 1 and vice versa.
# This effectively ignores them.
# Count how many elements are 1, that is, only one T.
bias_count_0 = np.count_nonzero(sim_all_0 * (1 - biases) == 1)
bias_count_1 = np.count_nonzero(sim_all_1 * biases == 1)

# The probability of bias for head.
h_bias = bias_count_0 / (bias_count_0 + bias_count_1)

time_running = time.time() - start_time

print(f'Bias H: {h_bias}')
print(f'Bias T: {1-h_bias}')
print(f'Time: {time_running}')
