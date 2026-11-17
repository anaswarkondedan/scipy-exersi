from scipy import stats
exam1=[78,85,90,65,88,76,95]
exam2 = [70, 72, 68, 75, 80, 69, 74]
t_stat,p_value=stats.ttest_ind(exam1,exam2)

print("t_statistic:",t_stat)
print("p_value",p_value)

if p_value<0.05:
    print("significant deffrence between the exams")
else:
    print("no significant diffrence between the exams")