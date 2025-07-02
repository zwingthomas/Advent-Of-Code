
from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass
from functools import wraps
import regex
import time
from types import TracebackType
from typing import Any, Callable, ClassVar, ParamSpec, TypeVar


class File:

    def __init__(self, filename: str, operation: str) -> None:
        self.file = open(filename, operation)

    def __enter__(self) -> File:
        return self.file

    def __exit__(self,
                 type: type[BaseException],
                 value: BaseException | None,
                 traceback: TracebackType | None
                 ) -> None | bool:
        self.file.close()
        if type:
            print(f"Exception caught: ({type=}, {value=}, {traceback=}")
            return True


PARAM = ParamSpec("P")
RET = TypeVar("R")


def strategy_timer(func: Callable[PARAM, RET]) -> Callable[PARAM, RET]:
    @wraps(func)
    def wrapper(*args, **kwargs) -> RET:
        start = time.perf_counter()
        ret = func(*args, **kwargs)
        end = time.perf_counter()
        print(
            f"Strategy {func.__qualname__} took {round(end - start, 10)} second{'s' if end - start != 1 else ''} to complete")
        return ret
    return wrapper


class PanicError(Exception):
    def __init__(self, message: str, value: Any) -> None:
        super().__init__(message)
        self.message = message
        self.value = value

    def __str__(self) -> str:
        return f"{self.message} (Value: {self.value})"

    # required to make exception pickle-able
    def __reduce__(self) -> tuple[Any, tuple[str, Any]]:
        return self.__class__, (self.message, self.value)


@dataclass
class TrebuchetStrategy(ABC):

    file_name: str = None
    file_arr: ClassVar[list[str]] = None

    @abstractmethod
    def read_calibration_document(self):
        ...

    @classmethod
    def __post_init__(cls):
        if not TrebuchetStrategy.file_arr and cls.file_name is not None:
            with File(cls.file_name, "r") as f:
                TrebuchetStrategy.file_arr = f.readlines()
                # notice how this is raised once per file,
                # this is because we are caching the file read
                raise PanicError("AHHHHHHH!!!", 9000)

    @classmethod
    def set_file_name(cls, new_file_name: str) -> None:
        TrebuchetStrategy.file_name = new_file_name
        TrebuchetStrategy.file_arr = None
        TrebuchetStrategy.__post_init__()


class Production(TrebuchetStrategy):
    """How I would implement this in production"""

    @strategy_timer
    def read_calibration_document(self):
        total = 0
        for line in type(self).file_arr:
            first = None
            for c in line:
                # Cannot just do "first" as first digit could be zero
                if c.isdigit() and first is None:
                    first = c
                if c.isdigit():
                    last = c
            total += int(f"{first}{last}")
        return total


class HelperMethod(TrebuchetStrategy):
    """Using walrus operator to show off"""

    def get_ints(self, line: str) -> list[int]:
        arr = []
        for c in line:
            try:
                arr.append(int(c))
            except ValueError:
                continue
        return arr

    @strategy_timer
    def read_calibration_document(self) -> int:
        # arr := self.get_ints(line)
        # Essentially this will mean that there is always something
        # in arr if we are to perform the casting
        # int(f"{arr[0]}{arr[-1]}". With this we avoid index out of
        # bounds errors.
        return sum(int(f"{arr[0]}{arr[-1]}")
                   for line in type(self).file_arr
                   if (arr := self.get_ints(line)))


class OneLiner(TrebuchetStrategy):
    """one-liner to show off"""

    @strategy_timer
    def read_calibration_document(self) -> int:
        # digits := (See comment in HelperMethod)
        return sum(
            int(f"{digits[0]}{digits[-1]}")
            for line in type(self).file_arr
            if (digits := [c for c in line if c.isdigit()]))


class Speedy(TrebuchetStrategy):
    """The fastest implementation"""

    @strategy_timer
    def read_calibration_document(self):
        total = 0
        for line in type(self).file_arr:
            first = last = None
            i = 0
            n = len(line)
            while i < n:
                number = ord(line[i]) - 48  # fast conversion
                if 0 <= number <= 9:
                    if first is None:
                        first = number
                        break
                i += 1
            first_i = i
            i = n - 1
            while i >= first_i:
                number = ord(line[i]) - 48
                if 0 <= number <= 9:
                    if last is None:
                        last = number
                        break
                i -= 1
            if first is not None:
                total += first * 10 + last
        return total


@dataclass
class SpeedyWithWords(TrebuchetStrategy):
    """Using regex to quickly find matches"""
    _numbers_as_words: ClassVar[dict[str, int]]
    _pattern: ClassVar[regex.Pattern]

    def __post_init__(self):
        super().__post_init__()
        # zero was not listed in the requirements
        self._numbers_as_words = {"one": 1,
                                  "two": 2,
                                  "three": 3,
                                  "four": 4,
                                  "five": 5,
                                  "six": 6,
                                  "seven": 7,
                                  "eight": 8,
                                  "nine": 9,
                                  **{str(i): i for i in range(10)}}
        # Regex that matches either a single digit or word
        # Sorted by length decending so we try three before thr
        self._pattern = regex.compile(
            "|".join(sorted(self._numbers_as_words, key=len, reverse=True)))

    @strategy_timer
    def read_calibration_document(self):
        print(self._numbers_as_words)
        total = 0
        for line in type(self).file_arr:
            first = last = None
            # find iter is very fast and only gives back matches
            for m in self._pattern.finditer(line, overlapped=True):
                value = self._numbers_as_words[m.group()]
                if first is None:
                    first = value
                last = value
            if first is not None:
                total += first * 10 + last
        return total


class Calibrater:
    """Holds a reference to a strategy and delegates the work"""

    def __init__(self, strategy: TrebuchetStrategy) -> None:
        self._strategy = strategy
        if isinstance(self._strategy, (Production, HelperMethod, OneLiner, Speedy)):
            strategy.set_file_name("input.txt")
        if isinstance(self._strategy, SpeedyWithWords):
            strategy.set_file_name("input2.txt")

    def set_strategy(self, strategy: TrebuchetStrategy):
        if isinstance(self._strategy, (Production, HelperMethod, OneLiner, Speedy))\
                and isinstance(strategy, SpeedyWithWords):
            strategy.set_file_name("input2.txt")
        if isinstance(self._strategy, SpeedyWithWords) \
                and isinstance(strategy, (Production, HelperMethod, OneLiner, Speedy)):
            strategy.set_file_name("input.txt")
        self._strategy = strategy

    def calibrate(self) -> int:
        return self._strategy.read_calibration_document()


def main():
    calibrater = Calibrater(Production())
    print("Solution to problem 1 using strategy I would use in Production:",
          calibrater.calibrate(), "\n")
    calibrater.set_strategy(
        HelperMethod())
    print("Solution to problem 1 using a helper method for readability:",
          calibrater.calibrate(), "\n")
    calibrater.set_strategy(OneLiner())
    print("Solution to problem 1 using one line:", calibrater.calibrate(), "\n")
    calibrater.set_strategy(Speedy())
    print("Solution to problem 1, best big O:", calibrater.calibrate(), "\n")
    calibrater.set_strategy(SpeedyWithWords())
    print("Solution to problem 2, best big O:", calibrater.calibrate(), "\n")
    calibrater.set_strategy(Speedy())
    print("Solution to problem 1, best big O:", calibrater.calibrate(), "\n")


if __name__ == "__main__":
    main()


"""
Outputs:

Exception caught: (type=<class '__main__.PanicError'>, value=PanicError('AHHHHHHH!!!'), traceback=<traceback object at 0x101153e80>
Strategy Production.read_calibration_document took 0.000761 seconds to complete
Solution to problem 1 using strategy I would use in Production: 54630 

Strategy HelperMethod.read_calibration_document took 0.010170208 seconds to complete
Solution to problem 1 using a helper method for readability: 54630 

Strategy OneLiner.read_calibration_document took 0.000610709 seconds to complete
Solution to problem 1 using one line: 54630 

Strategy Speedy.read_calibration_document took 0.000934417 seconds to complete
Solution to problem 1, best big O: 54630 

Exception caught: (type=<class '__main__.PanicError'>, value=PanicError('AHHHHHHH!!!'), traceback=<traceback object at 0x101164f80>
{'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
Strategy SpeedyWithWords.read_calibration_document took 0.002332041 seconds to complete
Solution to problem 2, best big O: 54770 

Exception caught: (type=<class '__main__.PanicError'>, value=PanicError('AHHHHHHH!!!'), traceback=<traceback object at 0x101164f40>
Strategy Speedy.read_calibration_document took 0.000914334 seconds to complete
Solution to problem 1, best big O: 54630

"""
