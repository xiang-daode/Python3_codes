#list下关于数字的选择性搜索
a=['1858','1778','8588','7658','8533','3854','7878','8858']
for m in a:
    if '88' in m:
        print(m)
print()
for m in a:
    if m[0]=='8':
        print(m)
print()
for m in a:
    if m[-1]=='8':
        print(m)
