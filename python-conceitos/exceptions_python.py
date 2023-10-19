class MyError(Exception):
    ...


class AnotherError(Exception):
    ...


def levantar():
    exception_ = MyError('a', 'b', 'c')
    exception_.add_note('nota')
    raise exception_


try:
    levantar()
except MyError as error:
    print(error.__class__.__name__)
    print(error)
    exception_ = AnotherError('aaaaa')
    exception_.add_note('nota 2')
    exception_.__notes__ += error.__notes__.copy()
    raise exception_ from error
