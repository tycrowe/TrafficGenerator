import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

prob_arrival = {
    0: 7,           # Midnight
    1: 11,          # 1am
    2: 24,          # 2am
    3: 42,          # 3am
    4: 65,          # 4am
    5: 83,          # 5am
    6: 107,         # 6am
    7: 125,         # 7am
    8: 168,         # 8am
    9: 182,         # 9am
    10: 172,        # 10am
    11: 105,        # 11am
    12: 99,         # 12pm
    13: 147,        # 1pm
    14: 115,        # 2pm
    15: 97,         # 3pm
    16: 82,         # 4pm
    17: 76,         # 5pm
    18: 67,         # 6pm
    19: 62,         # 7pm
    20: 51,         # 8pm
    21: 32,         # 9pm
    22: 14,         # 10pm
    23: 8,          # 11pm
}


# Where x is the number of total arrivals.
def gen_arrivals(x):
    # Based on the time of day, 0-23, more arrivals have a chance of showing up.
    for i in range(0, 23):
        # Poisson random number generation
        num = int(stats.poisson.rvs(prob_arrival[i], loc=1, size=x)[np.random.randint(0, x)])
        plt.plot([i], [num], marker='o', markersize=3, color='red')


gen_arrivals(1000)
plt.show()
