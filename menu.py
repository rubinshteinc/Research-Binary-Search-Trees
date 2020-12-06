import random


# print to the user the options and accepted the input
def menu():
    print("welcome to project on Binary Search Tree!")
    n = int(input("Please enter a number for array's size: "))
    x = input("please choose:\n"
              "a - random numbers      b - give your own numbers: ")

    while x is not "a" and x is not "b":
        x = input("incorrect choosing, please try again:\n")

    if x == "a":
        r = int(input("Please enter number for range: "))
        arr = [random.randrange(0, r + 1) for i in range(0, n)]

    else:
        string = input("Please enter the numbers separated by space: \n")
        elements = string.split()

        while len(elements) != n:
            print(len(elements))
            string = input("There are too many/few numbers, please try again:\n")
            elements = string.split()

        for i in range(n):
            elements[i] = int(elements[i])

    print("The element are:", elements)

    return elements, n


# print out numbers' comparisons
def print_result(sorted_arr, sorted1_arr, sorted2_arr, sorted3_arr, count_0, count_1, count_2, count_3):
    print("\n")
    print("The sorted  sequence is:", sorted_arr)
    print("The sorted1 sequence is:", sorted1_arr)
    print("The sorted2 sequence is:", sorted2_arr)
    print("The sorted3 sequence is:", sorted3_arr)
    print("\n")
    print("Number of comparisons for building the tree:")
    print("Strategy:\t  0   a   b   c")
    print("----------------------------------------")
    print("comparisons:", count_0, "", count_1, "", count_2, "", count_3)
