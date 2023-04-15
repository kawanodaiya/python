# クローザー
def outer(a, b):
    
    def inner():
        return a + b
    
    return inner

f = outer(1, 2)
r = f()
print(r)

def circle_area_func(pi):
    def circle_area(radius):
        return pi * radius * radius
    
    return circle_area

ca1 = circle_area_func(3.14)
ca2 = circle_area_func(3.141592)
print(ca1(10))
print(ca2(10))

# デコレーター
def print_info(func):
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper

def print_more(func):
    def wrapper(*args, **kwargs):
        print('func:', func.__name__)
        print('args:', args)
        print('kwargs:', kwargs)
        result = func(*args, **kwargs)
        print('result:', result)
        return result
    return wrapper

@print_info
@print_more
def add_num(a, b):
    return a + b

r = add_num(10, 20)
print(r)

# ラムダ
l = ['Mon', 'tue', 'Wed', 'Thu', 'Fri', 'sat', 'Sun']

def change_words(words, func):
    for word in words:
        print(func(word))

# def sample_func(word):
#     return word.capitalize()
# sample_func = lambda word: word.capitalize()

change_words(l, lambda word: word.capitalize())

# ジェネレーター
def counter(num = 10):
    for _ in range(num):
        yield 'run'

def greeting():
    yield 'Good'
    yield 'Better'
    yield 'Best'

g = greeting()
c = counter()
print(next(g))
print(next(c))
print(next(g))
print(next(c))
print(next(g))

# リスト内包表記
t = {1, 2, 3, 4, 5}
t2 = {6, 7, 8, 9, 10}
r = []
for i in t:
    r.append(i)

print(r)

r = [i for i in t if i % 2 == 0]
print(r)

r = []
for i in t:
    for j in t2:
        r.append(i * j)
print(r)

r = [i * j for i in t for j in t2]
print(r)

# 辞書内括表記
w = ['mon', 'tue', 'wed']
f = ['coffee', 'milk', 'water']

d = {}
for x,y in zip(w,f):
    d[x] = y

print(d)

d = {x: y for x, y in zip(w, f)}
print(d)

# 集合内包表記
s = set()

for i in range(10):
    s.add(i)

print(s)

s = {i for i in range(10)}
print(s)

#ジェネレーター内包表記
def g():
    for i in range(10):
        yield i

g = (i for i in range(10))
print(type(g))

#名前空間とスコープ
animal = 'cat'

def f():
    animal = 'dog'
    print('local:',locals())

f()
print('global:', globals())

#例外処理
list = [1, 2, 3]
i = 5

try:
    list[i]
except IndexError as ex:
    print('except: {}'.format(ex))
except NameError as ex:
    print(ex)
finally:
    print('clean up')

class UppercaseError(Exception):
    pass

def check():
    words = ['APPLE', 'orange', 'banana']
    for word in words:
        if word.isupper():
            raise UppercaseError(word)

try:
    check()
except UppercaseError as exc:
    print('This is my fault. Go next')