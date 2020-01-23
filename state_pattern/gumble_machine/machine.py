from .state import (
    NoQuarterState,
    HasQuarterState,
    SoldState,
    SoldOutState,
    WinnerState
)


class GumbleMachine:

    def __init__(self, number_of_gumballs):

        self.count = number_of_gumballs

        self.no_quarter_state = NoQuarterState(self)
        self.has_quarter_state = HasQuarterState(self)
        self.sold_state = SoldState(self)
        self.sold_out_state = SoldOutState(self)
        self.winner_state = WinnerState(self)

        self.state = self.sold_out_state
        if number_of_gumballs > 0:
            self.state = self.no_quarter_state

    def insert_quarter(self):
        self.state.insert_quarter()

    def eject_quarter(self):
        self.state.eject_quarter()

    def turn_crank(self):
        self.state.turn_crank() # 손잡이를 돌라면 조건에 맞게 상태가 변경됨
        self.state.dispense()   # 껌볼이 상태에 맞게 나옴

    def set_state(self, state):
        self.state = state

    def release_ball(self):
        print('껌볼이 나오는 중입니다...')
        if self.count:
            self.count -= 1

    def get_no_quarter_state(self):
        return self.no_quarter_state

    def get_has_quarter_state(self):
        return self.has_quarter_state

    def get_sold_state(self):
        return self.sold_state

    def get_sold_out_state(self):
        return self.sold_out_state

    def get_winner_state(self):
        return self.winner_state

    def get_count(self):
        return self.count
