from statistics import median


def main():

    with open("../input_small.txt", "r") as file:
        input = file.readlines()

        positions = input[0].split(",")

        for i in range(0, len(positions)):
            positions[i] = int(positions[i])

        median_position = median(positions)

        print("Median: " + str(median_position))

        total_fuel = 0
        for pos in positions:
            total_fuel += abs(median_position - pos)

        print("Total fuel: " + str(total_fuel))


if __name__ == "__main__":
    main()
