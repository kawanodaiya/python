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

import abc

class Person(metaclass=abc.ABCMeta):
    def __init__(self, age=1):
        self.age = age
    @abc.abstractmethod
    def drive(slef):
        pass

class Baby(Person):
    def __init__(self, age=1):
        if age < 18:
            super().__init__(age)
        else:
            raise ValueError
    def drive(self):
        raise Exception('no')

class Adult(Person):
    def __init__(self, age=18):
        if age >= 18:
            super().__init__(age)
        else:
            raise ValueError
    def drive(self):
        print('ok')

baby = Baby()
adult = Adult()

class Car(object):
    def __init__(self, model=None):
        self.model = model
    def run(self):
        print('run')
    def ride(self, person):
        person.drive()

class ToyotaCar(Car):
    pass

class TeslaCar(Car):
    def __init__(self, model='model S',
                enable_auto_run=False,
                password='123'):
        # 親の__init__を実行 self.model = model
        super().__init__(model)
        self._enable_auto_run = enable_auto_run
        self.password = password
    
    @property
    def enable_auto_run(self):
        return self._enable_auto_run
    @enable_auto_run.setter
    def enable_auto_run(self, is_enable):
        if self.password == '456':
            self._enable_auto_run = is_enable
        else:
            raise ValueError
    
    def run(self):
        print('super fast')
    def auto_run(self):
        print('auto run')

car = Car()
car.ride(adult)
car.run()
print('##########')
toyota_car = ToyotaCar('Lexus')
print(toyota_car.model)
toyota_car.run()
print('##########')
tesla_car = TeslaCar('Model S', password='456')
tesla_car.enable_auto_run = True
print(tesla_car.model)
print(tesla_car.enable_auto_run)
tesla_car.run()
tesla_car.auto_run()