import numpy as np
from scipy import stats

marks = np.array([65, 70, 75, 80, 85, 90])
print("mean:", np.mean(marks))
print("median", np.median(marks))
print("standard deviation",np.std(marks))

class_a=[70,75,80,85,90]
class_b=[60,65,70,75,80]
result=stats.ttest_ind(class_a,class_b)
print("t-statistic:",result.statistic)
print("p-value:",result.pvalue)