from functools import reduce
a = lambda a,b : a+b
l = [4,3,4,2]
# b = []
# for i in l:
#     b.append(a(i))
# print(b)
print(reduce(a, l, 4))