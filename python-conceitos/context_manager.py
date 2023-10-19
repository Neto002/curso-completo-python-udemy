from contextlib import contextmanager


class MyContextManager:

    def __init__(self, caminho_arquivo, modo, encoding='utf8') -> None:
        self.caminho_arquivo = caminho_arquivo
        self.modo = modo
        self.encoding = encoding

    def __enter__(self):
        self.__arquivo = open(self.caminho_arquivo,
                              self.modo, encoding=self.encoding)
        return self.__arquivo

    def __exit__(self, class_exception, exception_: Exception, traceback_):
        self.__arquivo.close()
        exception_.add_note('nota')


@contextmanager
def my_open(caminho_arquivo, modo, encoding='utf8'):
    try:
        print('Abrindo arquivo')
        arquivo = open(caminho_arquivo, modo, encoding=encoding)
        yield arquivo
    finally:
        print('Fechando arquivo')
        arquivo.close()

# with MyContextManager('./teste.txt', 'w') as arquivo:
#     arquivo.write("a")


with my_open('./teste.txt', 'w') as arquivo:
    arquivo.write("a")
