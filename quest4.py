import numpy as np
from scipy import stats

height=np.array([150, 155, 160, 165, 170, 172, 175, 180, 185, 190])
weight = np.array([45, 48, 52, 55, 60, 62, 65, 70, 75, 80])

r,p_value=stats.pearsonr(height,weight)
print("correlation:,r")
print("p-value",p_value)

if p_value < 0.50:
   print("Height and weight are significantly correlated")
else:
   print("Height and weight are not significantly correlated")
 
