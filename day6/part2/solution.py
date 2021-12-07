def main():

    with open("../input.txt", "r") as file:
        input = file.readlines()

        N_DAYS = 256

        number_of_fish_in_day = [0, 0, 0, 0, 0, 0, 0, 0, 0]

        for line in input:
            first_gen = line.split(",")

            lanterns = []

            for first in first_gen:
                number_of_fish_in_day[int(first)] += 1

            current_day = 0
            while current_day < N_DAYS:
                current_day += 1
                new_fish_lineup = [0, 0, 0, 0, 0, 0, 0, 0, 0]
                for i in range(0, len(number_of_fish_in_day)):
                    if i == 0:
                        new_fish_lineup[8] += number_of_fish_in_day[i]
                        new_fish_lineup[6] += number_of_fish_in_day[i]

                    else:
                        new_fish_lineup[i - 1] += number_of_fish_in_day[i]

                number_of_fish_in_day = new_fish_lineup.copy()

            print(sum(number_of_fish_in_day))


if __name__ == "__main__":
    main()
