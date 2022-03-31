#!/usr/bin/python3
#This fixes Syntax error: word unexpected (expecting ")") the command tells the terminal that when you run the script it should use bash to execute it
#The sheband only matters if you need to run in something that isn't just a shell, like python or pearl, or you don't use the bash shell
import math

def fibonacci(num):
    if(num < 1):
      return Exception
    if(num == 1):
      return 0
    if(num == 2):
      return 1
    else:
      return fibonacci(num-1)+fibonacci(num-2)

def factorial(num):
  if(num == 0):
    return 1
  if(num > 0):
    return num*factorial(num - 1)

  
  

  
def menu():
  val = input("Enter the week(0-2): ")
  val = int(val)
  if(val == 0):
    return Exception
  
  if(val == 1):
    print("1--Loops")
    print("2--Fibonacci")
    print("3--Factorial")
    print("4--Exit")
    val1 = input("What work would you like to view?  ")
    val1 = int(val1)
    if(val1 == 1):
      menu()
    if(val1 == 2):
      val2= input("Welcome to Fibonacci! Select the the term you would like to see  ")
      val2 = int(val2)
      print(fibonacci(val2))
      menu()
    if(val1 == 3):
      val2= input("Welcome to Factorial! Select the the term you would like to see  ")
      val2 = int(val2)
      print(factorial(val2))
      menu()
    if(val1 == 4):
      print("See you later!")
  if(val == 2):
    print("1--Loops")
    print("2--Fibonacci")
    print("3--Factorial")
    print("4--Exit")
    print("What work would you like to view?")

menu()
