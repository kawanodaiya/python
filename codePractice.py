def exception3(x, y, z):
    if x == y:
        return z
    if x == z:
        return y
    if y == z:
        return x

def exception9(a):
    x = a[0] + a[1] + a[2]
    y = a[3] + a[4] + a[5]
    z = a[6] + a[7] + a[8]
    if x==y:
        return exception3(a[6], a[7], a[8])
    elif x==z:
        return exception3(a[3], a[4], a[5])
    else:
        return exception3(a[0], a[1], a[2])

print(exception3(1,2,2))
print(exception3(4,2,4))
print(exception3(9,3,9))

def reverse_lookup2(dic1):
    dic2 = {}  #辞書を初期化する
    for key, value in dic1.items():
        dic2[value] = key
    return dic2

print(reverse_lookup2({'apple': 3, 'pen': 5, 'orange': 7})
                        == {3: 'apple', 5: 'pen', 7: 'orange'})