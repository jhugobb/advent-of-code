def main():

    with open("../input.txt", "r") as file:
        input = file.readlines()

        depth = 0
        horizontal = 0

        for line in input:
            parsed = line.split(" ")
            if parsed[0] == "forward":
                horizontal += int(parsed[1])
            elif parsed[0] == "down":
                depth += int(parsed[1])
            elif parsed[0] == "up":
                depth -= int(parsed[1])
        
        print(depth*horizontal)
            


if __name__ == "__main__":
    main()