from .iterator import PancakeHouseMenuIterator, DinerMenuIterator


class MenuItem:

    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.description = kwargs['description']
        self.vegetarian = kwargs['vegetarian']
        self.price = kwargs['price']

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_price(self):
        return self.price

    def is_vegetarian(self):
        return self.vegetarian


class PancakeHouseMenu:

    def __init__(self):
        self.menu_items = []

        self.add_item(
            name='K&B 팬케이크 세트',
            description='스크램블드 에그와 토스트가 곁들어진 팬케이크',
            vegetarian=True,
            price=2.99)
        self.add_item(
            name='레귤러 팬케이크 세트',
            description='달걀 후라이와 소시지가 곁들어진 팬케이크',
            vegetarian=False,
            price=2.99)
        self.add_item(
            name='블루베리 팬케이크',
            description='신선한 블루베리와 블루베리 시럽으로 만든 팬케이크',
            vegetarian=True,
            price=3.49)
        self.add_item(
            name='와플',
            description='와플, 취향에 따라 블루베리나 딸기를 얹을 수 있습니다',
            vegetarian=True,
            price=3.59)

    def add_item(self, **kwargs):
        menu_item = MenuItem(
            name=kwargs['name'],
            description=kwargs['description'],
            vegetarian=kwargs['vegetarian'],
            price=kwargs['price'])
        self.menu_items.append(menu_item)

    """ def get_menu_items(self):
        print(self.menu_items) """

    def create_iterator(self):
        return PancakeHouseMenuIterator(self.menu_items)


class DinerMenu:

    MAX_ITEMS = 6

    def __init__(self):
        self.menu_items = dict()
        self.number_of_items = 0
        self.add_item(
            name='채식주의자용 BLT',
            description='통밀 위에 (식물성)베이컨, 상추, 토마토를 얹은 메뉴',
            vegetarian=True,
            price=2.99)
        self.add_item(
            name='BLT',
            description='통밀 위에 베이컨, 상추 토마토를 얹은 메뉴',
            vegetarian=False,
            price=2.99)
        self.add_item(
            name='오늘의 스프',
            description='감자 샐러드를 곁들인 오늘의 스프',
            vegetarian=False,
            price=3.29)
        self.add_item(
            name='핫도그',
            description='사워크라우트, 갖은 양념, 양파, 치즈가 곁들여진 핫도그',
            vegetarian=False,
            price=3.05)

    def add_item(self, **kwargs):
        menu_item = MenuItem(
            name=kwargs['name'],
            description=kwargs['description'],
            vegetarian=kwargs['vegetarian'],
            price=kwargs['price'])
        if self.number_of_items >= DinerMenu.MAX_ITEMS:
            print('죄송합니다, 메뉴가 꽉 찼습니다. 더 이상 추가할 수 없습니다.')
        else:
            self.menu_items[self.number_of_items] = menu_item
            self.number_of_items += 1

    """ def get_menu_items(self):
        print(self.menu_items) """

    def create_iterator(self):
        return DinerMenuIterator(self.menu_items)
