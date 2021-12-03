def main():

    with open("../input.txt", "r") as file:
        input = file.readlines()

        oxygen_candidates = input.copy()
        co2_candidates = input.copy()
        index = 0
        for index in range(0, len(input[0])):
            
            oxygen_zero_candidates = []
            oxygen_one_candidates = []
            num_of_zeros_oxy = 0
            num_of_ones_oxy = 0

            co2_zero_candidates = []
            co2_one_candidates = []
            num_of_zeros_co2 = 0
            num_of_ones_co2 = 0
            if len(oxygen_candidates) > 1:
                for candidate in oxygen_candidates:
                    if candidate[index] == "0":
                        num_of_zeros_oxy += 1
                        oxygen_zero_candidates.append(candidate)
                    elif candidate[index] == "1":
                        num_of_ones_oxy += 1
                        oxygen_one_candidates.append(candidate)
                
                if num_of_zeros_oxy <= num_of_ones_oxy:
                    oxygen_candidates = oxygen_one_candidates.copy()
                else:
                    oxygen_candidates = oxygen_zero_candidates.copy()

            
            if len(co2_candidates) > 1:
                for candidate in co2_candidates:
                    if candidate[index] == "0":
                        num_of_zeros_co2 += 1
                        co2_zero_candidates.append(candidate)
                    elif candidate[index] == "1":
                        num_of_ones_co2 += 1
                        co2_one_candidates.append(candidate)

                if num_of_zeros_co2 > num_of_ones_co2:
                    co2_candidates = co2_one_candidates.copy()
                else:
                    co2_candidates = co2_zero_candidates.copy()

        print(oxygen_candidates)
        print(co2_candidates)

        print(int(oxygen_candidates[0], 2) * int(co2_candidates[0], 2))

            
            

if __name__ == "__main__":
    main()