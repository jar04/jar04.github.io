#!/usr/bin/python3
#This fixes Syntax error: word unexpected (expecting ")") the command tells the terminal that when you run the script it should use bash to execute it
#The sheband only matters if you need to run in something that isn't just a shell, like python or pearl, or you don't use the bash shell
import random
import weeks.week1
import weeks.week0
import weeks.week2
import math

class Factorial:

  def fact(self,n):
        if n == 0:
            return 1 
        else:
            return n * self.fact(n - 1)
class calculator:
    a = 0
    b = 0
    def __init__(self, inputa):
        self.a = inputa
    def __init__(self, inputa, inputb):
        self.a = inputa
        self.b = inputb
    def add(self):
        return self.a+self.b
    def subtract(self):
        return self.a-self.b
    def multiply(self):
        return self.a*self.b
    def divide(self):
        if(self.b==0):
            print("Cannot divide by 0. Returning 0")
            return 0
        return self.a/self.b
    def squareroot(self):
        return math.sqrt(self.a)

def calcfunction():
    for i in range(5):
        a = random.randint(0, 100)
        b = random.randint(0, 10)
        calc = calculator(a,b)
        print("%d+%d = %d"%(a, b, calc.add()))
        print("%d-%d = %d"%(a, b, calc.subtract()))
        print("%d*%d = %d"%(a, b, calc.multiply()))
        print("%d/%d = %f"%(a, b, calc.divide()))
        print("Squareroot(%d) = %f"%(a, calc.squareroot()))
        del calc

class Palindrome:
  
  def palin_check(str):
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True

textpic = ["",
           "  ⣞⢽⢪⢣⢣⢣⢫⡺⡵⣝⡮⣗⢷⢽⢽⢽⣮⡷⡽⣜⣜⢮⢺⣜⢷⢽⢝⡽⣝ ",
           " ⠸⡸⠜⠕⠕⠁⢁⢇⢏⢽⢺⣪⡳⡝⣎⣏⢯⢞⡿⣟⣷⣳⢯⡷⣽⢽⢯⣳⣫⠇ ",
           "⠀⠀⢀⢀⢄⢬⢪⡪⡎⣆⡈⠚⠜⠕⠇⠗⠝⢕⢯⢫⣞⣯⣿⣻⡽⣏⢗⣗⠏ ",
           "⠀⠪⡪⡪⣪⢪⢺⢸⢢⢓⢆⢤⢀⠀⠀⠀⠀⠈⢊⢞⡾⣿⡯⣏⢮⠷⠁⠀⠀",
           "⠀⠀⠀⠈⠊⠆⡃⠕⢕⢇⢇⢇⢇⢇⢏⢎⢎⢆⢄⠀⢑⣽⣿⢝⠲⠉⠀⠀⠀⠀",
           "⠀⠀⠀⣴⣿⣾⣿⣿⣿⡿⡽⡑⢌⠪⡢⡣⣣⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
           "⠀⠀⠀⡟⡾⣿⢿⢿⢵⣽⣾⣼⣘⢸⢸⣞⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
           "⠀⠀⠀⠀⠁⠇⠡⠩⡫⢿⣝⡻⡮⣒⢽⠋⠀⠀"]

def fibonacci(num):
    if(num < 1):
      return Exception
    if(num == 1):
      return 0
    if(num == 2):
      return 1
    else:
      return fibonacci(num-1)+fibonacci(num-2)


def factorialFunction(num):
  if(num == 0):
    return 1
  if(num > 0):
    return num*factorialFunction(num - 1)

class palindrome:
    string = ""
    def __init__(self, s):
        self.string = s
    def ispalindrome(self):
        for i in range(0, int(len(self.string)/2)):
            if self.string[i] != self.string[len(self.string)-i-1]:
                return False
        return True

def palindromefunction():
    string = str(input("Input string to test if palindrome: "))
    stringChecker = palindrome(string)
    result = stringChecker.ispalindrome()

    if (result):
        print("%s is a palindrome"%(string))
    else:
        print("%s is not a palindrome"%(string))

phoneValues = [ [1,2,3],[4,5,6],[7,8,9] ]
def phone():
    print('*phone noises*')
    for i in phoneValues:
        for x in i:
            print(x, end =" ")
        print()

def menu():
  val = input("Enter the week(0-2): ")
  val = int(val)
  if(val == 0):
    print("1--Phone")
    print("2--Picture")
    print("3--Exit")
    val1 = input("What work would you like to view?  ")
    val1 = int(val1)
    if(val1 == 1):
      phone()
      menu()
    if(val1 == 2):
      print(textpic)
      menu()
    if(val1 == 3):
      menu() 
  if(val == 1):
    print("1--Loops")
    print("2--Fibonacci")
    print("3--Factorial")
    print("4--Exit")
    val1 = input("What work would you like to view?  ")
    val1 = int(val1)
    if(val1 == 1):
       weeks.week1.while_loop(0)
    if(val1 == 2):
      val2= input("Welcome to Fibonacci! Select the the term you would like to see  ")
      val2 = int(val2)
      print(fibonacci(val2))
      menu()
    if(val1 == 3):
      val2= input("Welcome to Factorial! Select the the term you would like to see  ")
      val2 = int(val2)
      print(factorialFunction(val2))
      menu()
    if(val1 == 4):
      print("See you later!")
  if(val == 2):
    print("1--Palindrome")
    print("2--Factorial Class")
    print("3--Calculator")
    print("4--Exit")
    val3 = input("What work would you like to view?")
    val3 = int(val3)
    if(val3 == 1):
      val4= input("Welcome to Palindrome Function! Select the the word you would like to see  ")
      val4 = str(val4)
      f = palindromefunction()
      menu()
    if(val3 == 2):
      val2= input("Welcome to Factorial Class! Select the the term you would like to see  ")
      val2 = int(val2)
      f = Factorial()
      print(f.fact(val2))
      menu()
    if(val3 == 3):
      calcfunction()
      
    

menu()
