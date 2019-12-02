import math


def get_fuel(mass):
    return math.floor(mass/3)-2


filepath = 'input-d1.txt'
sum = 0
with open(filepath) as fp:
    for cnt, line in enumerate(fp):
        mass = get_fuel(int(line))
        fuel_needed_by_fuel = 0
        sum += mass

        while mass > 0:
            mass = get_fuel(mass)
            if mass > 0:
                fuel_needed_by_fuel += mass

        sum += fuel_needed_by_fuel

print(sum)
