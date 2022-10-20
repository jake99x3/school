#Intro To Python Exercise 5.3
# Description: Tells if a triangle can be formed given 3 numbers
# Input: x, y, z
# Output: Triangle yes or No Triangle
# Additional Comments: No comment

#First we write our function is_triangle
def is_triangle(x, y, z):
    if (x > y + z) or (y > z + x) or (z > x + y):
        print("no triangle")

    else:
        print("triangle yes")

    return

#Next we have our user input for 3 triangle sides
prompt1 = 'Input first stick length for your triangle please...'
x = input(prompt1)
x = int(x)

prompt2 = 'Input second stick length for your triangle please...'
y = input(prompt2)
y = int(y)

prompt3 = 'Input third stick length for your triangle please...'
z = input(prompt3)
z = int(z)

#Finally we run our function to determine if it forms a triangle
print (is_triangle(x, y, z))