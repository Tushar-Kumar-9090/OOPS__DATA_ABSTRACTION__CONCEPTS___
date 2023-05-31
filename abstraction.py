


## Example:-1

from abc import ABC,abstractmethod
class TimeTable(ABC):
    @abstractmethod
    def breakfast(self):
        pass
    @abstractmethod
    def lunch(self):
        pass
    @abstractmethod
    def dinner(self):
        pass
class Harshad(TimeTable):
    def breakfast(self):
        print('Dosa')
    def lunch(self):
        print('Biriyani')
    def dinner(self):
        print('Biriyani')

h=Harshad()
h.breakfast() ## Dosa
h.lunch()     ## Biriyani
h.dinner()    ## Biriyani



## Example-2

from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def move(self):
        pass
    @abstractmethod
    def speak(self):
        pass
class Dog(Animal):
    def move(self):
        print('i can walk')
    def speak(self):
        print('Bow Bow')
class Snake(Animal):
    def move(self):
        print('i can crawl')
    def speak(self):
        print('Ssssssss')
