# get numebr array
def get_number_array():

    num_array = []

    n = int(input("\nEnter number of elements : "))
    num_array = list(map(int,input("Enter the numbers : ").strip().split()))[:n]

    return num_array


# find the traget two number sum from array
def target_two_sun(num_array, target_num):
    two_num = [1 ,2]
    return two_num


#Main
# get numebr array
print("Enter the numebr of array use space to split the number")
array = get_number_array()

# get target number
target_num = int(input("\nEnter target_number: "))

target_two_sun(array, target_num)


