from math import floor
from statistics import mean


def main():

    with open("../input.txt", "r") as file:
        input = file.readlines()

        positions = input[0].split(",")

        for i in range(0, len(positions)):
            positions[i] = int(positions[i])

        avg_position = floor(mean(positions))

        print("Average: " + str((avg_position)))

        total_fuel = 0
        for pos in positions:
            dist = abs(avg_position - pos)

            total_fuel += dist * ((dist + 1) / 2)

        print("Total fuel: " + str(total_fuel))


if __name__ == "__main__":
    main()
