# Python Speedup Example

Example of how a python script can be made faster using Numpy.

This example is a simulation of a problem which can be solved by Bayes formula:

A Coin is biased 70% for head OR tail. It comes from a factory where 60% of coins are biased for tail. Observed sequence: H, H, T, H. What is the probability that the coin is biased for head?

When running 100000 simulations, the normal program took 7.113 seconds wile the optimized program took 0.026 seconds. Making the optimized program 273.6 times faster.

Too see how to solve this problem using Bayes formula, see my youtube video [here](https://www.youtube.com/watch?v=6kZC7wf3Ar8).
