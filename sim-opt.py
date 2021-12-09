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


# sum a list of 4 np arrays together. It looks like this:
# sum ([
#     [1, 0, 1, 1, ...],
#     [1, 0, 0, 1, ...],
#     [0, 0, 1, 0, ...],
#     [1, 1, 1, 0, ...]
# ])
#   = [3, 1, 3, 2, ...]

# Here 70% of the arrays are 0
draws_all_0 = sum([choice([0, 1], nr_sims, p=[.7, .3]) for i in range(4)])
# Here 70% of the arrays are 1
draws_all_1 = sum([choice([1, 0], nr_sims, p=[.7, .3]) for i in range(4)])

# Set all draws_all_0/1 to 0 when the bias are not for them. Effectively ignoring them.
# So, count how many have sum 1, that is, only one T.
bias_count_0 = np.count_nonzero(draws_all_0 * (1 - biases) == 1)
bias_count_1 = np.count_nonzero(draws_all_1 * biases == 1)

# The probability of bias for head.
h_bias = bias_count_0 / (bias_count_0 + bias_count_1)

time_running = time.time() - start_time

print(f'Bias H: {h_bias}')
print(f'Bias T: {1-h_bias}')
print(f'Time: {time_running}')
