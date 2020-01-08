from .behavior import QuackBehavior

class Quack(QuackBehavior):

    def quack(self):
        print("> 꽥!")


class MuteQuack(QuackBehavior):

    def quack(self):
        print("> 조용!")


class Squeak(QuackBehavior):

    def quack(self):
        print("> 삑!")
