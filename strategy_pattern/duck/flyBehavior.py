from .behavior import FlyBehavior

class FlyWithWings(FlyBehavior):

    def fly(self):
        print("> 저는 날고 있어요")


class FlyNoWay(FlyBehavior):

    def fly(self):
        print("> 저는 날지 못해요")


class FlyRocketPowered(FlyBehavior):

    def fly(self):
        print("> 로켓 추진으로 날아갑니다")