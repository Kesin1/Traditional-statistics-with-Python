import numpy as np
from scipy.stats import chi2
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("../a_b_testing/ab_testing/advertisement_clicks.csv").values

T = np.zeros((2, 2))
T[0, 0] = np.sum(data[data[:, 0] == 'A', 1] == 0)
T[0, 1] = np.sum(data[data[:, 0] == 'A', 1] == 1)
T[1, 0] = np.sum(data[data[:, 0] == 'B', 1] == 0)
T[1, 1] = np.sum(data[data[:, 0] == 'B', 1] == 1)

det = T[0, 0]*T[1, 1] - T[1, 0]*T[0, 1]
c2 = float(det)/T[0].sum() * det/T[1].sum() * \
    T.sum() / T[:, 1].sum() / T[:, 0].sum()


p = 1 - chi2.cdf(c2, df=1)
print p
