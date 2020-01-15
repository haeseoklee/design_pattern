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
    myclass2 = Singleton()
    print(myclass2.get_instance())
    myclass3 = Singleton()
    print(myclass3.get_instance())

if __name__ == '__main__':
    main()
