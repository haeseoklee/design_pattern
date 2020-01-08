from cafe.beverage import Espresso, HouseBlend
from cafe.condiment import Mocha, Whip


def main():
    espresso = Espresso()
    print(espresso.get_description())
    print(espresso.cost())

    espresso = Whip(Whip(Mocha(Espresso()))) # 데코레이터로 계속 감싸준다
    print(espresso.get_description())
    print(espresso.cost())

    houseblend = HouseBlend()
    print(houseblend.get_description())
    print(houseblend.cost())

    houseblend = Mocha(Mocha(Mocha(HouseBlend()))) # 데코레이터로 계속 감싸준다
    print(houseblend.get_description())
    print(houseblend.cost())


if __name__ == '__main__':
    main()