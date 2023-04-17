try:
    import package6.utils
except:
    import package6.utils

r = package6.utils.say_twice('hello')
print(r)

# 組み込み関数
import builtins

builtins.print()

ranking = {
    'A': 100,
    'B': 85,
    'C': 95
}

print(sorted(ranking, key=ranking.get, reverse=True))

# 標準ライブラリ
s = "asdfghjkjhgfrtgb"

d = {}
for c in s:
    if c not in d:
        d[c] = 0
    d[c] += 1
print(d)

d = {}
for c in s:
    d.setdefault(c, 0)
    d[c] += 1
print(d)

from collections import defaultdict

d = defaultdict(int)
for c in s:
    d[c] += 1
print(d)

# importする際の記述の仕方
import collections
import os
import sys

# import termcolor

# import lesson_package

# import config

print(__name__)