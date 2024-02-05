# Simple Python program to calculate the area of a rectangle using width and breadth

def calculate_rectangle_area(width, breadth):
    area = width * breadth
    return area

width = float(input("Enter the width of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))

area = calculate_rectangle_area(width, breadth)

print(f"The area of the rectangle is: {area}")

