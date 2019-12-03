from typing import List
import fileinput


def io() -> List[int]:
    line = next(fileinput.input())
    return [int(i) for i in line.split(",")]


INSTRUCTION_SIZE = 4


class Opcodes:
    ADD = 1
    MULTIPLY = 2
    STOP = 99


def run_program(memory: List[int]) -> List[int]:
    instructions = [
        memory[i : i + INSTRUCTION_SIZE]
        for i in range(0, len(memory), INSTRUCTION_SIZE)
    ]

    for opcode, *params in instructions:
        if opcode == Opcodes.ADD:
            memory[params[2]] = memory[params[0]] + memory[params[1]]
        elif opcode == Opcodes.MULTIPLY:
            memory[params[2]] = memory[params[0]] * memory[params[1]]
        elif opcode == Opcodes.STOP:
            break
        else:
            raise ValueError("unknown opcode")

    return memory


def program_result(memory: List[int]) -> int:
    copied_input = memory.copy()
    return run_program(copied_input)[0]


if __name__ == "__main__":
    memory = io()
    print(program_result(memory))
