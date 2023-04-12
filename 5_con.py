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