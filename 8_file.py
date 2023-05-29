import string
import csv
import os
import tarfile
import zipfile
import tempfile
import subprocess
import datetime

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

print(os.path.exists('test.txt')) # ファイル操作
print(os.path.isfile('test.txt'))
print(os.path.isdir('paiza'))

os.rename('test.txt', 'rename.txt')
os.symlink('rename.txt', 'symlink.txt')

os.mkdir('test_dir')
os.rmdir('test_dir')

os.mkdir('test_dir')
os.mkdir('test_dir/test_dir2')
print(os.listdir('test_dir'))

with tarfile.open('test.tar.gz', 'w:gz') as tr: # tarfileの圧縮
    tr.add('test_dir')

with tarfile.open('test.tar.gz', 'r:gz') as tr: # tarfileの展開
    tr.extractall(path='test_tar')

with zipfile.ZipFile('test.zip', 'w') as z: # zipfileの圧縮
    z.write('test_dir')
    z.write('test_dir/test.txt')

with zipfile.ZipFile('test.zip', 'r') as z: # zipfileの展開
    z.extractall('zzz2')

with tempfile.TemporaryFile(mode='w+') as t: # tempfile
    t.write('hello')
    t.seek(0)
    print(t.read())

with tempfile.NamedTemporaryFile(delete=False) as t:
    print(t.name)
    with open(t.name, 'w+') as f:
        f.write('test\n')
        f.seek(0)
        print(f.read())

with tempfile.TemporaryDirectory() as td:
    print(td)

temp_dir = tempfile.mkdtemp()
print(temp_dir)

subprocess.run(['ls', '-al']) # subprocessでターミナルコマンドを実行する
p1 = subprocess.Popen(['ls', '-al'], stdout=subprocess.PIPE)
p2 = subprocess.Popen(
    ['grep', 'test'], stdin=p1.stdout, stdout=subprocess.PIPE
)
p1.stdout.close()
output = p2.communicate()[0]
print(output)

now = datetime.datetime.now()
print(now)
print(now.isoformat())
print(now.strftime('%d/%m/%y-%H%M%S%f'))

today = datetime.date.today()
print(today)
print(today.isoformat())
print(today.strftime('%d/%m/%y'))

t = datetime.time(hour=1, minute=10, second=5, microsecond=100)
print(t)
print(t.isoformat())
print(t.strftime('%H_%M_%S_%f'))

print(now)
d = datetime.timedelta(weeks=-1)
print(now + d)