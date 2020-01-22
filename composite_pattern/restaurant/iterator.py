from operator import itemgetter
top = itemgetter(-1)


class CompositeIterator:

    def __init__(self, *iterator):
        self.stack = list(iterator)

    def next(self):
        if self.has_next():
            iterator = top(self.stack)
            component = iterator.next()
            # isinstance(component, Menu):
            if type(component).__name__ == 'Menu':
                self.stack.append(component.create_iterator())
            return component
        else:
            return None

    def has_next(self):
        if not self.stack:
            return False
        else:
            iterator = top(self.stack)
            print(iterator)
            if not iterator.has_next():
                self.stack.pop()
                return self.has_next()
            else:
                return True


class NullIterator:

    def next(self):
        return None

    def has_next(self):
        return False
