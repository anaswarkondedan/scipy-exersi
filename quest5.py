from scipy import  stats

hours=[1,2,3,4,5,6]
marks=[35,40,45,50,55,65,70]
slope,intercept,r,p,std_err=stats.linregress(hours,marks)
print("slope:",slope)
print("intercept:",intercept)
print("correlation:",r)
print("p-value:",p)

predicted_marks= slope*7+intercept
print("Predicted marks:", predicted_marks)  
