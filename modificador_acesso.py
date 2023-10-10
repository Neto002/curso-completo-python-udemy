# prop = public
# _prop = protected
# __prop = private
class Foo:
    def __init__(self) -> None:
        self.public = 'publico'
        self._protected = 'protected'
        self.__private = 'private'

    def test(self):
        print(self.__private)

    def __private_method():
        return None


f = Foo()
f.__private_method()
