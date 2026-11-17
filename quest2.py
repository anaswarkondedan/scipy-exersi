
from scipy import stats
data=stats.norm.rvs(size=1000)
mean=data.mean()
std=data.std()
print("mean:",mean)
print("standard Deviation:",std)