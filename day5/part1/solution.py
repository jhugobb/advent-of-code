def main():

    with open("../input.txt", "r") as file:
        input = file.readlines()

        N = 1000
        # Format [y][x]
        m = []
        line = []

        for i in range(0, N):
            line.append(0)
        
        for i in range(0, N):
            m.append(line.copy())
        
        for line in input:
            tokens = line.split(" ")

            point1_str = tokens[0].split(",")
            point2_str = tokens[2].split(",")

            point1 = (int(point1_str[0]), int(point1_str[1]))
            point2 = (int(point2_str[0]), int(point2_str[1]))

            if point1[1] == point2[1]:
                if point1[0] < point2[0]:
                    for y in range(point1[0], point2[0]+1):
                        m[y][point1[1]] += 1
                else:
                    for y in range(point2[0], point1[0]+1):
                        m[y][point1[1]] += 1
            
            if point1[0] == point2[0]:
                if point1[1] < point2[1]:
                    for x in range(point1[1], point2[1]+1):
                        m[point1[0]][x] += 1
                else:
                    for x in range(point2[1], point1[1]+1):
                        m[point1[0]][x] += 1
        
        dangerous_total = 0
        for i in range(0, N):
            for j in range(0, N):
                if m[i][j] > 1:
                    dangerous_total += 1

        print(dangerous_total)

if __name__ == "__main__":
    main()