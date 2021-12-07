def main():

    with open("../input.txt", "r") as file:
        input = file.readlines()

        N_DAYS = 80

        for line in input:
            first_gen = line.split(",")

            lanterns = []

            for first in first_gen:
                lanterns.append(int(first))

            current_day = 0
            while current_day < N_DAYS:
                current_day += 1
                current_fish = len(lanterns)
                for i in range(0, current_fish):
                    lanterns[i] -= 1
                    if lanterns[i] < 0:
                        lanterns.append(8)
                        lanterns[i] = 6

            print(len(lanterns))


if __name__ == "__main__":
    main()
