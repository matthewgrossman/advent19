from typing import Iterator
import fileinput


def required_fuel(mass: int) -> int:
    return (mass // 3) - 2


def io() -> Iterator[int]:
    return (int(l) for l in fileinput.input())


if __name__ == '__main__':
    print(sum(required_fuel(m) for m in io()))
