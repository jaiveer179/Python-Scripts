#function of addition 

def add(x,y):
    return x + y

def substracts(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
 if x == 0 :
    return "Error: division by zero is unidefinied"
    return x / y


#calculator menu 

print("select operation")
print("1. Addition")
print("2. subtraction")
print("3. multiply")
print("4. division")


#taking input from user that what he will choose

choice = input("enter choice(1/2/3/4):")

#taking two number as a input 
try: 
    num1 = float(input("Enter your first number:"))
    num2 = float(input("Enter your second number:"))

except ValueError:
    print("Error: Please enter a valid number.")
    exit()

    # Perform the chosen operation
if choice == '1':
    print(f"{num1} + {num2} = {add(num1, num2)}")
elif choice == '2':
    print(f"{num1} - {num2} = {substracts(num1, num2)}")
elif choice == '3':
    print(f"{num1} * {num2} = {multiply(num1, num2)}")
elif choice == '4':
    print(f"{num1} / {num2} = {divide(num1, num2)}")
else:
    print("Invalid input. Please choose a valid operation.")


def fibonacci(n):
    if n <= 1:
        return(n)
        return fibonacci(n-1),fibonacci(n-2)
        print(fibonacci(6))


