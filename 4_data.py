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

# i = 10
# j = 20
# tmp = i
# i = j
# j = tmp
# print(i, j)

a = 100
b = 200
print(a, b)
a, b = b, a
print(a, b)