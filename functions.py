# Create a function to receive number 5 as parameter and return square of it to main script.
#  Display the return value using print inside main script .
def num (a):
    return a*a
print(num(5))

# Ask user to enter one number and then use the function 
# to display square of it inside the function without returning any data to calling script.
def number(a):
    number=a*a
    print("enter one number:",a)

# Ask user to enter one number, pass this number to a function,
# return the number to main script after adding 10 to the value.
def number(a,b):
    return number(a*a)+b
print("enter one number",number())


# Ask the user to input two numbers and display the sum of it ( without using any function )
number1 = number("Enter first number")
number2 = number("Enter second number")
print("First number:", number1)
print("Second number:", number2)
sum= number1+ number2
print("Addition of two number is: ", sum)

# Ask for two user input numbers, pass to a function and then display highest number.
def greater(number1,number2):
    if number1>=number2:
        print("number1 is greater than number2")
    else:
        print("number2 is greater than number1")








    





      

    


