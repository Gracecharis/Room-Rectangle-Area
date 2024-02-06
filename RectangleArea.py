# Simple Python program to calculate the area of a rectangle using width and length

def calculate_rectangle_area(width, length):
    area = width * length
    return area

width = float(input("Enter the width of the rectangle: "))
length = float(input("Enter the length of the rectangle: "))

area = calculate_rectangle_area(width, length)

print(f"The area of the rectangle is: {area}")

