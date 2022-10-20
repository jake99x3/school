#Intro to Python Lab 5.2
# Description: Tests Fermats Theorem
# Input: a, b, n
# Output: Fermat was wrong or No that doesnt work.
# Additional Comments: No comment

#First we import math
import math

#Next we define our function and use conditionals
def check_fermat(a, b, n):
    number1 = a
    number2 = b
    number3 = n
    chk = (math.pow(a, n)) + (math.pow(b, n))


    if number3 > 2:
        print("Holy smokes, Fermat was wrong!")
        return chk
    else:
        2 > number3
        print("No, that doesn't work.")
        return chk

#Them we get our user input for numbers 1, 2 and 3, define chk and run our function

number1 = int(input("Enter a number"))
number2 = int(input("Enter a number"))
number3 = int(input("Enter a number"))

chk = check_fermat(number1, number2, number3)
print(chk)