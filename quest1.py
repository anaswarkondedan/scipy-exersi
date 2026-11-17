import numpy as np
from scipy import stats

data=np.array([4,8,15,16,23,42])

mean=np.mean(data)
median=np.median(data)

variance=stats.tvar(data)
std=stats.tstd(data)

print("mean:",mean)
print("median:",median)
print("variance:",variance)
print("standard deviation",std)