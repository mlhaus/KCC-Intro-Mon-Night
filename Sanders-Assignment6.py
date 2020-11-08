from helpers import *
import random


def main():
    length = getInt(" How many numbers do you want in your list?: [Enter a number greater than 0]")
    while length < 1:
        print("Inlvalid input. Try again. Make sure the number is greater than 0...")
        length = getInt(" How many numbers do you want in your list?: [Enter a number greater than 0]")
    given_number = getNum(" Input a number!: ")
    list_numbers = create_list(length)
    for i in list_numbers:
        is_larger_than(i, given_number)
    print("Your list is " + str(list_numbers) + ", and the greater numbers in your list are " + str(greater_than_list))


def create_list(length):
    list_numbers = []
    for i in range (length):
        ran_number = random.randint(0,1000)
        list_numbers.append(ran_number)
        list_numbers.sort()
    return list_numbers


greater_than_list = []
def is_larger_than(list_numbers, given_number):
    if list_numbers > given_number:
        greater_than_list.append(list_numbers)
        greater_than_list.sort()


main()