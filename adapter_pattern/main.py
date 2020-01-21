from birds.birds import MallardDuck, WildTurkey
from birds.adapter import TurkeyAdapter


def test_duck(duck):
    duck.quack()
    duck.fly()


def main():

    mallard_duck = MallardDuck()
    turkey = WildTurkey()
    turkey_adapter = TurkeyAdapter(turkey)

    test_duck(mallard_duck)
    test_duck(turkey_adapter)


if __name__ == '__main__':
    main()
