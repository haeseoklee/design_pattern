from restaurant.component import Menu, MenuItem


class Waitress:

    def __init__(self, all_menus):
        self.all_menus = all_menus

    def print_menu(self):
        print('전체메뉴를 출력합니다')
        iterator = self.all_menus.create_iterator()

        while iterator.has_next():
            menu_component = iterator.next()
            try:
                menu_component.print_menu()
            except Exception as e:
                print(e)

    def print_vegetarian_menu(self):
        print('채식주의자용 메뉴를 출력합니다')
        iterator = self.all_menus.create_iterator()
        while iterator.has_next():
            menu_component = iterator.next()
            try:
                if menu_component.is_vegetarian():
                    menu_component.print_menu()
            except Exception as e:
                print(e)


def main():
    all_menus = Menu(name='전체메뉴', description='전체메뉴')
    pancake_house_menu = Menu(name='팬케이크 하우스 메뉴', description='팬케이크 하우스 메뉴')
    pancake_house_menu.add(
        MenuItem(
            name='K&B 팬케이크 세트',
            description='스크램블드 에그와 토스트가 곁들어진 팬케이크',
            vegetarian=True,
            price=2.99,
        ))
    pancake_house_menu.add(
        MenuItem(
            name='레귤러 팬케이크 세트',
            description='달걀 후라이와 소시지가 곁들어진 팬케이크',
            vegetarian=False,
            price=2.99,
        ))
    pancake_house_menu.add(
        MenuItem(
            name='블루베리 팬케이크',
            description='신선한 블루베리와 블루베리 시럽으로 만든 팬케이크',
            vegetarian=True,
            price=3.49,
        ))
    pancake_house_menu.add(
        MenuItem(
            name='와플',
            description='와플, 취향에 따라 블루베리나 딸기를 얹을 수 있습니다',
            vegetarian=True,
            price=3.59,
        ))

    dinner_menu = Menu(name='저녁메뉴', description='저녁메뉴')
    dinner_menu.add(
        MenuItem(
            name='채식주의자용 BLT',
            description='통밀 위에 (식물성)베이컨, 상추, 토마토를 얹은 메뉴',
            vegetarian=True,
            price=2.99
        )
    )
    dinner_menu.add(
        MenuItem(
            name='BLT',
            description='통밀 위에 베이컨, 상추 토마토를 얹은 메뉴',
            vegetarian=False,
            price=2.99
        )
    )

    all_menus.add(pancake_house_menu)
    all_menus.add(dinner_menu)

    waitress = Waitress(all_menus)
    waitress.print_menu()


if __name__ == '__main__':
    main()
