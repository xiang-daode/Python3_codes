import statistics

data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]

v1=statistics.mean(data)
print('均值  :',v1)  # as: 1.6071428571428572

v2=statistics.median(data)
print('中位数  :',v2) # as: 1.25

v3=statistics.variance(data)
print('方差  :',v3) # as: 1.3720238095238095

