# クラス
class Person(object):
    # コンストラクタ
    def __init__(self, name='default'):
        self.name = name
    def say_something(self):
        print('I am {}. hello'.format(self.name))
        self.run(10)
    def run(self, num):
        print('run' * num)
    # デストラクタ
    def __del__(self):
        print('Good bye')

person = Person('Mike')
person.say_something()

del person

print('##########')

class Car(object):
    def run(self):
        print('run')

class ToyotaCar(Car):
    pass

class TeslaCar(Car):
    def auto_run(self):
        print('auto run')

car = Car()
car.run()
print('##########')
toyota_car = ToyotaCar()
toyota_car.run()
print('##########')
tesla_car = TeslaCar()
tesla_car.run()
tesla_car.auto_run()