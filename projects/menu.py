def fibonacci(num):
    if(num < 1):
        return Exception
    if(num == 1):
        return 0
    if(num == 2):
        return 1
    else:
        return fibonacci(num-1)+fibonacci(num-2)

def menu():
    val = input("Enter the week(0-2): ")
    val = int(val)
    if(val == 0):
        return Exception

    if(val == 1):
        print("1--Loops")
        print("2--Fibonacci")
        print("3--Exit")
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
            print("See you later!")
    if(val == 1):
        print("What work would you like to view?")

    if(val == 2):
        print("What work would you like to view?")


menu()