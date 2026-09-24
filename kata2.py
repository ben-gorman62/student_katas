# A2: What are the divisors of 111?
# 
# N.B. the divisors of a number are those that leave an integer when the number
# is divided i.e. 6's divisors are 1, 2, 3 and 6.

#decompose
# make an empty list
# loop from 1 till 111 - using range
# Divide 111 by each number
# check if the reminder 0
# if remainder 0 add number that can be divided to list
# print vales in nice sentence (i.e. 111's divisors are x, x, x, ... and x)
# Team decompose xx


# divisors_list.values()

divisors_list = ""
for number in range(1,112):
    if 111 % number == 0:
        divisors_list += str(number) + ", "
        
print(f"Divisors of 111 are: {divisors_list[:-2]}")

#print(f"{", ".join(divisors_list[:-2])}")
#print(f"{divisors_list}{", ".join(divisors_list)} and {divisors_list[-1]}.")
#print(f'{", ".join(str(divisors_list[:-2]))} and {divisors_list[-1]}')