from scipy.differentiate import derivative
def function(x):
    return x**3 + 2*x**2 + 5
result=derivative(function,x=2)
print("derivate",result.df)