# if文
x = 10
if x < 0:
    print('negative')
elif x == 0:
    print('zero')
else:
    print('positive')

a = 5
b = 10
if a > 0:
    print('a is positive')
    if b > 0:
        print('b is positive')

#演算子
a1 =1
b1 = 1
a1 > 0 and b1 > 0
a1 > 0 or b1 > 0

# in not
y = [1, 2, 3]
x = 1
if x in y:
    print('in')
if 100 not in y:
    print('not in')

a2 = 1
b2 = 2
if not a == b:
    print('Not equal')
if a < b:
    print('Not equal')

is_ok = True
if not is_ok:
    print('hello')

is_ok1 = ''
if is_ok1:
    print('ok')
else:
    print('no')

is_empty = None
if is_empty is None:
    print('none')

# while文
count = 0
while count < 5:
    if count >= 6:
        break
    if count == 2:
        count += 1
        continue
    print(count)
    count += 1
else:
    print('done')

# input関数
# while True:
#     word = input('Enter:')
#     if word == 'ok':
#         break
#     print('next')

#for文
some_list = [1, 2, 3, 4, 5]
for i in some_list:
    if i >= 4:
        break
    if i == 2:
        continue
    print(i)
else:
    print('else')

# range関数
for i in range(5, 10):
    print(i, 'hello')

# enumerate関数
for i, fruit in enumerate(['apple', 'banana', 'orange']):
    print(i, fruit)

# zip関数
days = ['Mon', 'Tue', 'Wed']
fruits = ['apple', 'banana', 'orange']
drinks = ['coffee', 'tea', 'beer']
for day,fruit,drink in zip(days, fruits, drinks):
    print(day, fruit, drink)

# 辞書をfor文で処理する
d = {'x': 100, 'y': 200}
for k, v in d.items():
    print(k, ':', v)