def main():

    with open("../input.txt", "r") as file:
        input = file.readlines()

        previous = []
        current = []
        result = 0

        for index in range(0, len(input)):
            if len(previous) < 3:
                current.append(int(input[index]))
            else:
                current.append(int(input[index]))
                current.pop(0)
                # print(previous)
                # print(current)
                if sum(current) > sum(previous):
                    result += 1
            
            previous = current.copy()

        
        print(result)
            


if __name__ == "__main__":
    main()