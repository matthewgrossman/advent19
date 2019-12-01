from day1_1 import required_fuel, io


def required_fuel_with_fuel(mass: int) -> int:
    total_fuel = required_fuel(mass)

    # opportunity for walrus
    next_fuel = required_fuel(total_fuel)
    while next_fuel > 0:
        total_fuel += next_fuel
        next_fuel = required_fuel(next_fuel)
    return total_fuel


if __name__ == '__main__':
    print(sum(required_fuel_with_fuel(m) for m in io()))
