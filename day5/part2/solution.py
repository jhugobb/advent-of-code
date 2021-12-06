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

            high_x = -1
            low_x = -1

            high_y = -1
            low_y = -1

            if point1[1] < point2[1]:
                low_y = point1[1]
                high_y = point2[1]
            else:
                low_y = point2[1]
                high_y = point1[1]
            
            if point1[0] < point2[0]:
                low_x = point1[0]
                high_x = point2[0]
            else:
                low_x = point2[0]
                high_x = point1[0]

            # Vertical
            if point1[0] == point2[0]:
                for y in range(low_y, high_y+1):
                     m[y][point1[0]] += 1
            
            # Horizontal
            elif point1[1] == point2[1]:
                for x in range(low_x, high_x+1):
                    m[point1[1]][x] += 1
            
            # Diagonal
            else:
                curr_x = point1[0]
                curr_y = point1[1]

                interval_x = 1
                interval_y = 1
                if curr_x == high_x:
                    interval_x = -1
                
                if curr_y == high_y:
                    interval_y = -1
                while curr_x != point2[0] and curr_y != point2[1]:
                    m[curr_y][curr_x] += 1
                    curr_x += interval_x
                    curr_y += interval_y
                m[point2[1]][point2[0]] += 1

            
        
        dangerous_total = 0
        for i in range(0, N):
            for j in range(0, N):
                if m[i][j] > 1:
                    dangerous_total += 1

        print(dangerous_total)

if __name__ == "__main__":
    main()