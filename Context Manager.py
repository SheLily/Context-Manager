from pprint import pprint
import datetime
from abc import ABC, abstractmethod

class Timer():
  def __enter__(self):
    self.start = datetime.datetime.now()
    print(self.start.time())

  def __exit__(self, type, value, traceback):
    self.stop = datetime.datetime.now()
    diff = self.stop - self.start
    print(self.stop.time())
    print(diff)

with Timer():
  class Animal(ABC):
    def __init__(self, name, weight, voice, type_animal):
        self.name = name
        self.weight = weight
        self.voice = voice
        self.starv = True
        self.type_animal = type_animal

    def get_voice(self):
        print(self.voice)

    @abstractmethod
    def eat(self):
      pass
        #raise NotImplementedError('Метод eat не определен')


  class Mammals(Animal):
      def __init__(self, name, weight, voice):
          super(Mammals, self).__init__(name, weight, voice, 'Зверь')
          self.milk = 10

      # Переопределение метода eat
      def eat(self):
          if self.starv:
              print(f'{self.type_animal} {self.name} покушал и доволен')
              self.startv = False
          else:
              print(f'{self.type_animal} {self.name} нагулял молока')
              self.milk += 10

      # Дойка
      def milking(self):
          if self.milk > 0:
              print(f'{self.type_animal} {self.name} подоен')
              self.milk = 0
          else:
              print(f'{self.type_animal} {self.name} уже был подоен')

          # птицы


  class Avifauna(Animal):
      def __init__(self, name, weight, voice):
          super(Avifauna, self).__init__(name, weight, voice, 'Птица')
          self.eggs = 1

      def eat(self):
          if self.starv:
              print(f'{self.type_animal} {self.name} покушала и довольна')
              self.startv = False
          else:
              print(f'{self.type_animal} {self.name} снесла яйцо')
              self.eggs += 1

      def collect(self):
          if self.eggs > 0:
              print(f'У {self.type_animal} {self.name} собрали яйца')
              self.eggs = 0
          else:
              print(f'У {self.type_animal} {self.name} нет яиц')


  class Goose(Avifauna):
      def __init__(self, name, weight):
          super(Goose, self).__init__(name, weight, 'Го-го-го')
          self.type_animal = 'Гусь'


  class Hen(Avifauna):
      def __init__(self, name, weight):
          super(Hen, self).__init__(name, weight, 'Куд-кудах')
          self.type_animal = 'Курица'


  class Duck(Avifauna):
      def __init__(self, name, weight):
          super(Duck, self).__init__(name, weight, 'Кря-кря')
          self.type_animal = 'Утка'


  class Cow(Mammals):
      def __init__(self, name, weight):
          super(Cow, self).__init__(name, weight, 'Му-му')
          self.type_animal = 'Корова'


  class Sheep(Mammals):
      def __init__(self, name, weight):
          super(Sheep, self).__init__(name, weight, 'Беееее')
          self.type_animal = 'Овца'
          self.wool = 10

      def shearing(self):
          if self.wool > 0:
              print(f'{self.type_animal} {self.name} подстрижена')
              self.wool = 0
          else:
              print(f'{self.type_animal} {self.name} была подстрижена ранее')


  class Goat(Mammals):
      def __init__(self, name, weight):
          super(Goat, self).__init__(name, weight, 'Меее')
          self.type_animal = 'Коза'

  # temp = Animal('Vasya', 100, 'Гыгы', 'Человек')
  # temp.eat()

  farm = [
      Goose('Серый', 10),
      Goose('Белый', 11),
      Cow('Манька', 450),
      Sheep('Барашек', 150),
      Sheep('Кудрявый', 145),
      Hen('Ко-ко', 8),
      Hen('Кукареку', 9),
      Goat('Рога', 160),
      Goat('Копыта', 163),
      Duck('Кряква', 8),

  ]

  for animal in farm:
      animal.eat()
      if isinstance(animal, Mammals):
          animal.milking()
      if isinstance(animal, Sheep):
          animal.shearing()
      if isinstance(animal, Avifauna):
          animal.collect()

  weight = 0
  for animal in farm:
      weight += animal.weight

  # weight = sum([animal.weight for animal in farm])

  print(f'Суммарный вес всех животных: {weight}')

  max_weight = max(farm, key=lambda x: x.weight)
  print(f'Самый большой вес имеет {max_weight.type_animal} {max_weight.name} с весом {max_weight.weight}')