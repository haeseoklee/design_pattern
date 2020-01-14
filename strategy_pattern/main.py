from duck.duck import Duck
from duck.fly_behavior import(
    FlyWithWings,
    FlyNoWay,
    FlyRocketPowered)
from duck.quack_behavior import(
    Quack,
    MuteQuack)


class MallardDuck(Duck):

    def __init__(self):
        super().__init__()
        self.fly_behavior = FlyWithWings()
        self.quack_behavior = Quack()

    def display(self):
        print("저는 청둥오리 입니다")


class ModelDuck(Duck):

    def __init__(self):
        super().__init__()
        self.fly_behavior = FlyNoWay()
        self.quack_behavior = MuteQuack()

    def display(self):
        print("저는 모형오리 입니다")

def main():
    mallard_duck = MallardDuck()
    mallard_duck.display()
    mallard_duck.perform_fly()
    mallard_duck.perform_quack()

    print('-'*30)
    model_duck = ModelDuck()
    model_duck.display()
    model_duck.perform_fly()
    model_duck.perform_quack()

    model_duck.setFlyBehavior(FlyRocketPowered())
    model_duck.perform_fly()


if __name__ == '__main__':
    main()