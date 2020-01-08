from abc import ABCMeta, abstractmethod

# 행동 캡슐화 하기, 자바에서는 인터페이스로 구현, Family of Algorithms
class FlyBehavior(metaclass = ABCMeta):

    @abstractmethod
    def fly(self):
        pass


class QuackBehavior(metaclass = ABCMeta):

    @abstractmethod
    def quack(self):
        pass
