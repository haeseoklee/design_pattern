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


class MenuIterator:

    def __init__(self, *args):
        self.items = list(args)
        self.position = 0

    def __iter__(self):
        # 이터레이터로 사용하고 싶을때 자기 자신을 호출한다.
        return self

    def __next__(self):
        # 이터레이터로 순회할때 값을 리턴해준다
        if self.position >= len(self.items):
            raise StopIteration
        else:
            item = self.items[self.position]
            self.position += 1
            return item


class MenuIteratorFactory:

    def __init__(self, *args):
        self.args = args

    def __iter__(self):
        # 이터레이터로 사용하고 싶을때 MenuIterator 객체를 생성한 후에 리턴한다
        return MenuIterator(*self.args)


menus = MenuIterator(
    MenuItem(
        name='K&B 팬케이크 세트',
        description='스크램블드 에그와 토스트가 곁들어진 팬케이크',
        vegetarian=True,
        price=2.99),
    MenuItem(
        name='K&B 팬케이크 세트',
        description='스크램블드 에그와 토스트가 곁들어진 팬케이크',
        vegetarian=True,
        price=2.99))

for item in menus:
    print(item)


menus = MenuIteratorFactory(
    MenuItem(
        name='K&B 팬케이크 세트',
        description='스크램블드 에그와 토스트가 곁들어진 팬케이크',
        vegetarian=True,
        price=2.99),
    MenuItem(
        name='K&B 팬케이크 세트',
        description='스크램블드 에그와 토스트가 곁들어진 팬케이크',
        vegetarian=True,
        price=2.99))

menu_iter = iter(menus)
print(next(menu_iter))
print(next(menu_iter))
