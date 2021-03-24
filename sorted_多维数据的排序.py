
alist=[('21','34','09'),('14','21','08'),('54','06','51')]
print("按第3关键字进行排序:")
print(sorted(alist, key = lambda x:int(x[2])))
