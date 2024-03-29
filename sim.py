from numpy.random import choice
import time

start_time = time.time()
sims = 100000

bias_count = {'H': 0, 'T': 0}

for i in range(sims):
    # Choose what side the coin should be biased for.
    bias = choice(['H', 'T'], 1, p=[.4, .6])[0]
    not_bias = 'H' if bias == 'T' else 'T'

    draws = list(choice([bias, not_bias], 4, p=[.7, .3]))

    if draws.count('H') == 3:
        bias_count[bias] += 1


h_bias = bias_count['H']/(bias_count['H']+bias_count['T'])

time_running = time.time() - start_time
print(f'Bias H: {h_bias}')
print(f'Bias T: {1-h_bias}')
print(f'Time: {time_running}')
