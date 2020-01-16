class Singleton:

    __instance = None

    @classmethod
    def get_instance(self):
        if Singleton.__instance is None:
           Singleton. __instance = self()
        return Singleton.__instance


class MyClass(Singleton):
    pass


def main():

    myclass = MyClass()
    print(myclass.get_instance())
    myclass2 = MyClass()
    print(myclass2.get_instance())
    myclass3 = MyClass()
    print(myclass3.get_instance())

    singleton = Singleton()
    print(singleton)
    singleton2 = Singleton()
    print(singleton2)
    singleton3 = Singleton()
    print(singleton3)

if __name__ == '__main__':
    main()
