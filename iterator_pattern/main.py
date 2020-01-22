from restaurant.menu import PancakeHouseMenu, DinerMenu


class Waitress:

    def __init__(self, pancake_house_menu, diner_menu):
        self.pancake_house_menu = pancake_house_menu
        self.diner_menu = diner_menu

    def print_menu(self):
        p_iter = self.pancake_house_menu.create_iterator()
        d_iter = self.diner_menu.create_iterator()
        self.print_iter(p_iter)
        self.print_iter(d_iter)

    def print_iter(self, iterator):
        while iterator.has_next():
            menu_item = iterator.next()
            print('{}, {} -- {}'.format(
                menu_item.get_name(),
                menu_item.get_price(),
                menu_item.get_description()))


def main():
    pancake_house_menu = PancakeHouseMenu()
    diner_menu = DinerMenu()
    waitress = Waitress(pancake_house_menu, diner_menu)
    waitress.print_menu()


if __name__ == '__main__':
    main()
