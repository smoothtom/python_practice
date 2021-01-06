#!/usr/bin/python3

# Practice Python - Beginner Python exercises 

def character_input():
    name = input("Please Enter your name: ")
    age = int(input("Please Enter your age: "))
    year = (2020-age)+100
    print(name, "will be 100 in year", year)
# character_input()

def odd_or_even():
    num = int(input("Please Enter a number to check: "))
    check = int(input("Please Enter number to divide: "))
    if (num % 4) == 0:
        print(num, "is a multiple of 4")
    elif (num % 2) == 0:
        print(num, "is even")
    else:
        print(num, "is odd")

    if (num % check) == 0:
        print(num, "divides evenly by", check)
    else:
        print(num, "does not divide evenly by", check)
# odd_or_even()

def list_less_than_ten():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    
    new_list = a
    for x in list(new_list):     # prints all the elements less than 5 from list[a]
      if x <= 5:
        new_list.remove(x)
    print(new_list)
list_less_than_ten()
