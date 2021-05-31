from copy import deepcopy # use to copy the array


# get numebr array
def get_number_array():

    num_array = []

    n = int(input("\nEnter number of elements : "))
    num_array = list(map(int,input("Enter the numbers : ").strip().split()))[:n]

    return num_array


# find the traget two number sum from array
def target_two_sun(num_array, target_num):
    two_num = []
    temp_array = deepcopy(num_array)

    for i in range (0, len(num_array)):

        temp_array.pop(0)
        temp_num = target_num - num_array[i]

        if(temp_num in temp_array):
            two_num.append(num_array[i])
            two_num.append(temp_num)

            return two_num

    return "There is no answer"


#Main
# get numebr array
print("Enter the numebr of array use space to split the number")
array = get_number_array()

# get target number
target_num = int(input("\nEnter target_number: "))

two_num_array = target_two_sun(array, target_num)
print(two_num_array)


