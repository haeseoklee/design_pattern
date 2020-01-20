class Singleton:

    __instance = None

    @classmethod
    def get_instance(self):
        if Singleton.__instance is None:
            Singleton. __instance = self()
        return Singleton.__instance


class MyClass(Singleton):
    pass


class YourClass():
    pass


def main():

    print(MyClass().get_instance(), MyClass().get_instance(), MyClass().get_instance())

    print(MyClass(), MyClass(), MyClass())
    print(YourClass(), YourClass(), YourClass())
    print(Singleton(), Singleton(), Singleton())


if __name__ == '__main__':
    main()
