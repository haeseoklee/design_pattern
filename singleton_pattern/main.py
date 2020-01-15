class BaseClass:

    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def get_a(self):
        return self.a

    def get_b(self):
        return self.b


class Singleton:

    __instance = None

    @classmethod
    def __get_instance(cls):
        return cls.__instance

    @classmethod
    def instance(cls, *args, **kargs):
        Singleton.__instance = cls(*args, **kargs)
        Singleton.instance = cls.__get_instance
        return Singleton.__instance

class MyClass(BaseClass, Singleton):
    pass

def main():
    myclass = MyClass.instance(1, 2)
    print(myclass.get_a())
    print(myclass.get_b())
    print(myclass)
    myclass2 = MyClass.instance()
    print(myclass2)
    myclass3 = MyClass.instance()
    print(myclass3)


if __name__ == '__main__':
    main()