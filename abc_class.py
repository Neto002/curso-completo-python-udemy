from abc import ABC, abstractmethod


class AbstractFoo(ABC):
    def __init__(self, name) -> None:
        self._name = None
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    @abstractmethod
    def name(self, name):
        ...


class Foo(AbstractFoo):
    def __init__(self, name) -> None:
        super().__init__(name)
        # print('a')

    @AbstractFoo.name.setter
    def name(self, name):
        self._name = name


foo = Foo('Bar')
print(foo.name)
