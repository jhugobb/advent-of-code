def main():

    with open("../input.txt", "r") as file:
        input = file.readlines()

        previous = input[0]
        result = 0

        for current in input[1:]:
            if int(current) >= int(previous):
                result += 1
            previous = current

        print(result)


if __name__ == "__main__":
    main()
