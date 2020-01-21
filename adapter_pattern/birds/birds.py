from abc import ABCMeta, abstractmethod


class Duck(metaclass=ABCMeta):

    @abstractmethod
    def quack(self):
        pass

    @abstractmethod
    def fly(self):
        pass


class Turkey(metaclass=ABCMeta):

    @abstractmethod
    def gobble(self):
        pass

    @abstractmethod
    def fly(self):
        pass


class MallardDuck(Duck):

    def quack(self):
        print('> 꽥!')

    def fly(self):
        print('저는 날고 있어요')


class WildTurkey(Turkey):

    def gobble(self):
        print('> 까르르륵 까르르륵')

    def fly(self):
        print('저는 짧은 거리만 날 수 있어요')
