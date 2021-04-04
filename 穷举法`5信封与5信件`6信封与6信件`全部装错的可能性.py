# 穷举法,5信封与5信件,6信封与6信件:全部装错的可能性

'''
# 用5个元素中的5个元素组成字符串_排列,第几位上不可出现几
m = ['1','2','3','4','5']

n = 0
for a in m:
    for b in m:
        for c in m:
            for d in m:
                for e in m:
                       if (a is not '1') & (b  is not '2') & (c  is not '3') & (d is not '4') & (e is not '5') :
                           mi=[a,b,c,d,e]
                           if ('1' in mi) &  ('2' in mi)  &  ('3' in mi) &  ('4' in mi) &  ('5' in mi) :
                               print(mi)
                               n = n + 1
print(n)  # 44
'''


# 用6个元素中的6个元素组成字符串_排列,第几位上不可出现几
m = ['1','2','3','4','5','6']

n = 0
for a in m:
    for b in m:
        for c in m:
            for d in m:
                for e in m:
                    for f in m:
                       if (a is not '1') & (b  is not '2') & (c  is not '3') & (d is not '4') & (e is not '5') & (f  is not '6'):
                           mi=[a,b,c,d,e,f]
                           if ('1' in mi) &  ('2' in mi)  &  ('3' in mi) &  ('4' in mi) &  ('5' in mi) &  ('6' in mi):
                               print(mi)
                               n = n + 1

print(n) #265








