import itertools
from typing import List, Tuple
from part1 import program_result, io


def find_inputs_for_output(memory: List[int], output: int) -> Tuple[int, int]:
    for noun, verb in itertools.product(range(99), range(99)):
        memory[1] = noun
        memory[2] = verb
        if program_result(memory) == output:
            return noun, verb

    raise ValueError("no inputs exist for expected output")


if __name__ == "__main__":
    memory = io()
    print(find_inputs_for_output(memory, 19690720))
