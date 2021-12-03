def main():

    with open("../input.txt", "r") as file:
        input = file.readlines()

        gamma = ""
        epsilon = ""

        # array size of input
        num_of_zeros = []
        num_of_ones = []

        for i in range(0, len(input[0])-1):
            num_of_zeros.append(0)
            num_of_ones.append(0)

        print(len(input[0]))

        for line in input:
            for index in range(0, len(line)-1):

                if line[index] == '0':
                    num_of_zeros[index] += 1
                else:
                    num_of_ones[index] += 1
        
        for index in range(0, len(num_of_zeros)):
            if num_of_zeros[index] > num_of_ones[index]:
                gamma = gamma + "0"
                epsilon = epsilon + "1"
            else:
                gamma = gamma + "1"
                epsilon = epsilon + "0"             
            

        print(gamma)
        print(epsilon)
        gamma_dec = int(gamma, 2)
        epsilon_dec = int(epsilon, 2)
        print(gamma_dec)
        print(epsilon_dec)
        print(gamma_dec * epsilon_dec)
            


if __name__ == "__main__":
    main()