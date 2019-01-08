import numpy as np
import pandas as pd
import scipy.stats

data = pd.read_csv("../traditional_statistics/advertisement_clicks.csv").values

# # gaussian distributed samples so ttest-staistic is t-student distributed
# # H0 the means are the same
# # H1 the means are different

# # significance level
alpha = 0.05

# test_statistic
A_data = data[data[:, 0] == 'A'][:, 1]
B_data = data[data[:, 0] == 'B'][:, 1]


N_A = len(A_data)
N_B = len(B_data)
N = N_A

# # means
mean_A = np.mean(A_data)
mean_B = np.mean(B_data)

# pooled standard deviation
var_A = np.var(A_data, ddof=1)
var_B = np.var(B_data, ddof=1)

s_p = np.sqrt((var_A + var_B) / 2.)
t = (mean_A - mean_B)/(s_p * np.sqrt(2./N))
t = np.sign(t) * t
p = 2 * (1-scipy.stats.t.cdf(t, 2*N-2))

# test
print t
print p
print scipy.stats.ttest_ind(A_data, B_data)
