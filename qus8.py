from scipy.optimize import root
def equation(x):
    return x[0]**3 - 4*x[0] - 9
result=root(equation,x0=[2])
print("root:",result.x[0])