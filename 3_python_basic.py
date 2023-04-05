import math

num = 1
name = 'Mike'
is_ok = True

print(num, type(num))
print(name, type(name))
print(is_ok, type(is_ok))

new_name = '1'
new_num = int(new_name)
print(new_num, type(new_num))

print(50 - 5 * 6)
print(17 / 3)
print(17 // 3)
print(5 ** 5)

result = math.sqrt(25)
print(result)

print("I don't know")
print('I don\'t know\n')

word = 'python'
print(word[0])
print(word[-1])
print(word[2:3])
print(word[:4])
print(word[2:])
word = 'j' + word[1:]
print(word)
word_len = len(word)
print(word_len)

s = 'My name is Mike'
print(s)
is_start = s.startswith('My')
print(is_start)
print(s.find('Mike'))
print(s.rfind('Mike'))
print(s.count('Mike'))
print(s.capitalize())
print(s.title())
print(s.replace('Mike', 'Nancy'))