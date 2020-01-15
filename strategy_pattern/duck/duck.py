from abc import ABCMeta, abstractmethod
from .behavior import FlyBehavior, QuackBehavior

# 추상 클래스 구현
class Duck(metaclass = ABCMeta):

    def __init__(self):
        self.fly_behavior = None # FlyBehavior 인터페이스를 구현한 구상객체가 들어가야함
        self.quack_behavior = None  # QuackBehavior 인터페이스를 구현한 구상객체가 들어가야함

    @abstractmethod
    def display(self):
        pass

    def perform_fly(self):
        self.fly_behavior.fly()

    def perform_quack(self):
        self.quack_behavior.quack()

    def setFlyBehavior(self, fb):
        self.fly_behavior = fb

    def setQuackBehavior(self, qb):
        self.quack_behavior = qb
    
    def swim(self):
        print('모든 오리는 물에 뜹니다. 가짜 오리도 뜨죠')