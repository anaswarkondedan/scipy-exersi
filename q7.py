from scipy.optimize import minimize
def function (x):
      return x[0]**2 + 5*x[0] + 6
result=minimize(function,x0=[0])
print("minimum x:",result,x[0])
print("minimum value:",result.fun)