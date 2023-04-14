# 関数の定義
def say_something():
    # print('hello')
    s = 'hello'
    return s

# say_something()
result = say_something()
print(result)

def what_is_this(color):
    print(color)

what_is_this('red')

# 引数の宣言
def add_num(a: int, b: int) -> int:
    return a + b

def menu(entree, drink, dessert):
    print(entree)
    print(drink)
    print(dessert)

menu(entree='beef', drink='beer', dessert='ice')

def test_func(x, l=None):
    if l is None:
        l = []
    l.append(x)
    return l

y = [1, 2, 3]
r = test_func(100, y)
print(r)

#関数のタプル化
def say_something_2(*args):
    for arg in args:
        print(arg)

say_something_2('Hi', 'Mike', 'Nancy')

# 辞書化
def menu_kwargs(**kwargs):
    for k, v in kwargs.items():
        print(k, v)

d = {
    'entree' : 'beef',
    'drink'  : 'coffee',
    'dessert': 'ice'
}

menu_kwargs(**d)

def menu_some(food, *args, **kwargs):
    print(food)
    print(args)
    print(kwargs)

menu_some('banana', 'apple', 'orange', entree='beef', drink='coffee')

#関数内関数
def outer(a, b):
    
    def plus(c, d):
        return c + d
    
    r1 = plus(a, b)
    r2 = plus(b, a)
    print(r1 + r2)

outer(1, 2)