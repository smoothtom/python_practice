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
      print("congrats, you guessed the number", a, "in", tries, "tries")
      break 
# guessing_game_one()

def list_overlap_comprehensions():
    a = random.sample([1, 1, 2, 3, 5, 8, 13, 21, 55, 89], 6)
    b = random.sample([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], 6)
    new_list = set(a+b)
    print(list(new_list))
# list_overlap_comprehensions()

def check_primality_functions():
  user = int(input("Please enter a number to check, if its a prime number: "))
  if user > 1:
    for i in range(2,user):
      if (user % i) == 0:
        print("this isn't a prime number")
        break
    else:
      print("this is a prime number")
# check_primality_functions()

def list_ends():
  a = random.sample(range(1, 100), 6) # Generate a random list 
  print(a)  
  first_element = a[0]
  last_element = a[-1]
  print("the first element is " + str(first_element) + ", and the last element is " + str(last_element))  
  # print only the first and last element of this list 
# list_ends()

def fibanocci():
  user = int(input("Please Enter how many fibanocci numbers you want to generate: "))
  n1, n2 = 0, 1 # first two terms 
  count = 0
  while count < user:
    print(n1)
    count += 1
    new = n1 + n2
    n1 = n2
    n2 = new
# fibanocci()  

def list_remove_duplicates():
  items = [1, 1, 2, 3, 5, 8, 13, 21, 55, 89]
  print(items, "- this is the original list")
  new_items = set(items)  # removes all the duplicates
  print(list(new_items), "- this is the list without any duplicates")
# list_remove_duplicates()

def reverse_word_oder():
  user = str(input("Please Enter something: "))
  new = user.split()
  new.reverse()
  result = " ".join(new)
  print(result)
# reverse_word_oder()

import os
import string 
def password_generator():
  number = int(input("Please Enter how long your password should be: "))
  chars = string.ascii_letters + string.digits + "!@#$%^&*()"
  random.seed = (os.urandom(1024))
  print(''.join(random.choice(chars) for i in range(number)))
# password_generator()

import requests
from bs4 import BeautifulSoup
def decode_webpage():
  url = "https://www.nytimes.com"
  articles = []
  r = requests.get(url)
  soup = BeautifulSoup(r.text,"lxml")
  title = soup.find_all("h3") # searches the webpage for all h3 elements 
  for news in title:
    articles.append(news.text)
  del articles[-3:] # removes the last 3 elements from the list, because they aren't headers lol
  for x in articles:
    print(x,"\n")
# decode_webpage()

def cows_and_bulls():
    count = 0 
    number = [random.randint(0,9) for n in range(4)] # generate a random 4 digit number
    print(number)
    user = input("Please guess the 4 digit number: ")
    listnum  = list(map(int, user)) # converts the user input into a list
    while True:
        count += 1 
        if listnum == number:
            print("Well done, you won!, it took you only", str(count), "tries")
            break
        else:
            cow = 0 
            bull = 0

            for x in range(0,4):
                if listnum[x] == number[x]:
                    cow += 1 
                elif listnum[x] in number:
                    bull += 1
        print("Cows: ", cow, "Bulls: ", bull)
# cows_and_bulls()

def decode_webpage_two():
    url = "https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")
    item = soup.find_all("div", class_="grid--item body body__container article__body grid-layout__content") # findAll = find_all 
    for x in item:
        print(x.text)
# decode_webpage_two()

def element_search():
