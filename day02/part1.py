from typing import List
import fileinput


def io() -> List[int]:
    line = next(fileinput.input())
    return [int(i) for i in line.split(",")]


INSTRUCTION_SIZE = 4


class Opcode:
    ADD = 1
    MULTIPLY = 2
    STOP = 99


def run_program(memory: List[int]) -> None:
    instructions = [
        memory[i : i + INSTRUCTION_SIZE]
        for i in range(0, len(memory), INSTRUCTION_SIZE)
    ]

    for opcode, *params in instructions:
        if opcode == Opcode.ADD:
            memory[params[2]] = memory[params[0]] + memory[params[1]]
        elif opcode == Opcode.MULTIPLY:
            memory[params[2]] = memory[params[0]] * memory[params[1]]
        elif opcode == Opcode.STOP:
            return
        else:
            raise ValueError("unknown opcode")


if __name__ == "__main__":
    memory = io()
    run_program(memory)
    print(memory[0])
