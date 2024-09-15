import math

def perimeter_of_circle(radius):
    return 2 * math.pi * radius
radius = float(input("Enter the radius of the circle: "))
perimeter = perimeter_of_circle(radius)
print(f"The perimeter (circumference) of the circle with radius {radius} is {perimeter:.2f}")
