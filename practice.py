#!/usr/bin/python3

import random

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
    # prints all the elements less than five 
    for x in list(new_list):     
      if x <= 5:
        new_list.remove(x)
    print(new_list)
# list_less_than_ten()

def divisors():
   number = int(input("Enter a number: "))
   for i in range(1, number+1):
    if (number % i) == 0:
      print(i)
# divisors()

def list_overlap():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    new_list = list(dict.fromkeys(a,b)) # removes all the duplicates from two list above 
    print(new_list)
# list_overlap()

def string_lists():
  palindrome = str(input("Please Enter a number to check if its a Polindrome: "))
  palindrome = palindrome.casefold()
  reverse = reversed(palindrome)
  if list(palindrome) == list(reverse): # Checks if string is a palindrome
    print("This string is a palindrome")
  else:
    print("This string is not a palindrome")
# string_lists()

def list_comprehensions():
  a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
  print([i for i in a if i % 2 == 0]) # makes a new list, that contains only the even elements of this list
  """ for i in a: 
        if i % 2 == 0:
          print(i)"""
# list_comprehensions()

def rock_paper_scissors():
  user_one = input("Please choose between [Rock] [Paper] [Scissors] : ")
  user_two = input("Please choose between [Rock] [Paper] [Scissors] : ")
  if user_one == user_two:
    print("It's a tie")
  elif user_one == "Rock":
    if user_two == "Scissors":
      print("User one win")
    else:
      print("User two win")
  elif user_one == "Scissors":
    if user_two == "Paper":
      print("User one win")
    else:
      print("User two win")
  elif user_one == "Paper":
    if user_two == "Rock":
      print("User one win")
    else:
      print("User two win")
  else:
    print("Please try again!") # If it's not working lol
# rock_paper_scissors()
    
def guessing_game_one():
  a = random.randint(1,9)
  tries = 0 
  while 1:
    user = int(input("Guess the number: "))
    tries += 1 # start counting the tries, you'll need to guess the number
    if user < a:
      print("to low")
    elif user > a:
      print("to high")
    elif user == a:
      print("congrats, you guessed the number", a, "with", tries, "tries")
      break 
# guessing_game_one()

def list_overlap_comprehensions():

