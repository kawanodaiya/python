import string
import csv
s = """\
AAA
BBB
CCC
DDD
"""
with open('test.txt', 'w+') as f: # textファイルへの書き込み w+,r+ 書き込み読み込みモード
    f.write(s)
    f.seek(0)
    print(f.read())

with open('test.txt', 'r') as f: # textファイルへの読み込み
    print(f.read())
    while True:
        chunk = 2
        line = f.readline(chunk)
        print(line)
        if not line:
            break
    print(f.tell()) # seekを使って移動する
    print(f.read(1))
    f.seek(5) # 何文字目かを呼び出す
    print(f.read(1))
    f.seek(14)
    print(f.read(1))
    f.seek(15)
    print(f.read(1))

with open('template.txt') as f: # テンプレート
    t = string.Template(f.read())

contents = t.substitute(name='Mike', contents='How are you')
print(contents)

with open('test.csv', 'w', newline='') as csv_file: # csvファイルの書き込み読み込み
    fieldnames = ['Name', 'Count']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'Name': 'A', 'Count': 1})
    writer.writerow({'Name': 'B', 'Count': 2})

with open('test.csv', 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        print(row['Name'], row['Count'])