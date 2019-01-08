import numpy as np
from scipy import stats
import pandas as pd

N = 10

a = np.random.randn(N) + 2
b = np.random.randn(N)

var_a = np.var(a, ddof=1)
var_b = np.var(b, ddof=1)

s = np.sqrt((var_a + var_b)/2)
t = (a.mean() - b.mean())/(s*np.sqrt(2./N))
df = 2*N - 2
p = 1-stats.t.cdf(t, df=df)     # p_value

print "t:\t", t, "p:\t", 2*p

t2, p2 = stats.ttest_ind(a, b)
print "t2:\t", t2, "p2:\t", p2

print stats.t.ppf(1-p, df=df)


data = pd.read_csv(
    "../traditional_statistics/advertisement_clicks.csv").values
print data[:10]

a = data[data[:, 0] == 'A', 1]
b = data[data[:, 0] == 'B', 1]
N = len(a)

alpha = 0.05/N
t2, p2 = stats.ttest_ind(a, b, )
print "p2: \t", p2
print "alpha:", alpha
