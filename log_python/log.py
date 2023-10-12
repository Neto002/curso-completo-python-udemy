from abc import ABC, abstractmethod
from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'


class Log(ABC):

    @abstractmethod
    def _log(self, msg: str):
        ...

    def log_error(self, msg: str):
        return self._log(f'Error: {msg}')

    def log_success(self, msg: str):
        return self._log(f'Success: {msg}')


class LogFileMixin(Log):
    def _log(self, msg: str) -> None:
        msg_formatada = f'{msg} {self.__class__.__name__}\n'
        print(f"Salvando no log: {msg_formatada}")
        with open(LOG_FILE, 'a', encoding='utf8') as file:
            file.write(msg_formatada)


class LogPrintMixin(Log):
    def _log(self, msg: str) -> None:
        print(msg, self.__class__.__name__)


if __name__ == '__main__':
    lp = LogPrintMixin()
    lp.log_error("a")
    lp.log_success("b")

    lf = LogFileMixin()
    lf.log_error("a")
    lf.log_success("b")
