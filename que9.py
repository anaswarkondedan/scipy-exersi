from scipy.integrate import quad
def function(x):
    return x**2+2*x+1
result,error=quad(function,0,5)
print("integrel:",result)
print("error:",error)