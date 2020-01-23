from abc import ABCMeta, abstractmethod
from .machine import *
from random import choice


class State(metaclass=ABCMeta):

    @abstractmethod
    def insert_quarter(self):
        pass

    @abstractmethod
    def eject_quarter(self):
        pass

    @abstractmethod
    def turn_crank(self):
        pass

    @abstractmethod
    def dispense(self):
        pass


class NoQuarterState(State):

    def __init__(self, gumble_machine):
        self.gumble_machine = gumble_machine

    def insert_quarter(self):
        print('동전을 넣으셨습니다')
        self.gumble_machine.set_state(self.gumble_machine.get_has_quarter_state())

    def eject_quarter(self):
        print('동전을 넣어주세요')

    def turn_crank(self):
        print('동전을 넣어주세요')

    def dispense(self):
        print('동전을 넣어주세요')


class HasQuarterState(State):

    def __init__(self, gumble_machine):
        self.gumble_machine = gumble_machine

    def insert_quarter(self):
        print('동전은 한 개만 넣어주세요')

    def eject_quarter(self):
        print('동전이 반환됩니다')

    def turn_crank(self):
        print('손잡이를 돌리셨습니다')
        if 7 == choice(range(10)) and self.gumble_machine.get_count() >= 2:
            self.gumble_machine.set_state(self.gumble_machine.get_winner_state())
        else:
            self.gumble_machine.set_state(self.gumble_machine.get_sold_state())

    def dispense(self):
        print('껌볼이 나갈 수 없습니다')


class SoldState(State):

    def __init__(self, gumble_machine):
        self.gumble_machine = gumble_machine

    def insert_quarter(self):
        print('잠깐만 기다려 주세요. 알맹이가 나가고 있습니다')

    def eject_quarter(self):
        print('이미 알맹이를 뽑으셨습니다')

    def turn_crank(self):
        print('손잡이는 한 번만 돌려주세요')

    def dispense(self):
        self.gumble_machine.release_ball()
        if self.gumble_machine.get_count() >= 1:
            self.gumble_machine.set_state(self.gumble_machine.get_no_quarter_state())
        else:
            print('껌볼이 다 떨어졌습니다!')
            self.gumble_machine.set_state(self.gumble_machine.get_sold_out_state())


class SoldOutState(State):

    def __init__(self, gumble_machine):
        self.gumble_machine = gumble_machine

    def insert_quarter(self):
        print('죄송합니다 매진되었습니다')

    def eject_quarter(self):
        print('죄송합니다 매진되었습니다')

    def turn_crank(self):
        print('죄송합니다 매진되었습니다')

    def dispense(self):
        print('죄송합니다 매진되었습니다')


class WinnerState(State):

    def __init__(self, gumble_machine):
        self.gumble_machine = gumble_machine

    def insert_quarter(self):
        print('잠깐만 기다려 주세요. 알맹이가 나가고 있습니다')

    def eject_quarter(self):
        print('이미 알맹이를 뽑으셨습니다')

    def turn_crank(self):
        print('손잡이는 한 번만 돌려주세요')

    def dispense(self):
        print('축하드립니다 껌볼을 하나 더 드리겠습니다')
        self.gumble_machine.release_ball()
        self.gumble_machine.release_ball()
        if self.gumble_machine.get_count() >= 1:
            self.gumble_machine.set_state(self.gumble_machine.get_no_quarter_state())
        else:
            print('껌볼이 다 떨어졌습니다!')
            self.gumble_machine.set_state(self.gumble_machine.get_sold_out_state())
