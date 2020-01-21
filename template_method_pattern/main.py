from starbuz.beverage import Tea, Coffee
from starbuz.beverage_with_hook import TeaWithHook, CoffeeWithHook


def main():
    tea = Tea()
    tea.prepare_recipe()

    print()
    coffee = Coffee()
    coffee.prepare_recipe()

    print()
    tea = TeaWithHook()
    tea.prepare_recipe()

    print()
    coffee = CoffeeWithHook()
    coffee.prepare_recipe()


if __name__ == '__main__':
    main()
