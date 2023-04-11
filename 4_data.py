# リスト型
r = [1, 2, 3, 4, 5, 1, 2, 3]

print(r.index(3, 3))
print(r.count(3))

r.sort()
print(r)
r.sort(reverse=True)
print(r)
r.reverse()
print(r)

s = 'My name is Mike'
to_split = s.split(' ')
print(to_split)

x = '##'.join(to_split)
print(x)

y = r.copy()
y[0] = 100
print("y = ", y)
print("r = ", r)

num_tuple = (10, 20)
print(num_tuple)

x, y = num_tuple
print(x, y)

x, y = 10, 20
print(x, y)

#タプル型
"""
i = 10
j = 20
tmp = i
i = j
j = tmp
print(i, j)
"""

a = 100
b = 200
print(a, b)
a, b = b, a
print(a, b)

# 辞書型
# x1 = {'a' : 1}
# y1 = x1
# y1['a'] = 1000
# print(x1)
# print(y1)

x1 = {'a' : 1}
y1 = x1.copy()
y1['a'] = 1000
print(x1)
print(y1)

fruits = {
    'apple':100,
    'banana':200,
    'orange':300,
}
print(fruits['apple'])

# 集合型
my_friends = {'A', 'C', 'D'}
A_friends = {'B', 'D', 'E', 'F'}
print(my_friends & A_friends)
print(my_friends | A_friends)

f = ['apple', 'banana', 'apple', 'banana']
kind = set(f)
print(kind)