# Simple Python program to calculate the area of a rectangle using width and length

# Function dfinition with width and length as parameters and calculating the area of a rectangle
def calculate_rectangle_area(width, length):
    # calculating area of a rectangle
    area = width * length
    # returning the area of the rectangle
    return area

# User input for width of rectangle
width = float(input("Enter the width of the rectangle: "))

# User input for length of rectangle
length = float(input("Enter the length of the rectangle: "))

# Function call to get the area of the rectangle
area = calculate_rectangle_area(width, length)

# Printing the area of rectangle
print(f"The area of the rectangle is: {area}")

