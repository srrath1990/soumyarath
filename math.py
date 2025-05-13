from streamlit import status

from math import degrees,radians
#Write a Python program to convert degree to radian.
j=radians(15)
print(j)

#Write a Python program to convert radian to degree
h=degrees(.52)
print(h)

import math

#Write a Python program to calculate the area of a parallelogram.
base = 5
Height = 6
area= base * Height
print(area)

# Write a Python program to calculate surface volume and area of a cylinder
base = 4
Height = 6
surface_area = 2 * math.pi * base**2 + 2 * math.pi * base * Height
print(surface_area)

volume = math.pi * base**2 * Height
print(volume)

# Find the area of a Circle
rad=5
Area=math.pi * rad**2
print(Area)

#Find the smallest value from the given List of numbers
x = [ 45, -5, 0, 5, 45 ]
print(min(x))

#Find the highest value from the given List of numbers
y = [ 45, -5, 0, 5, 45 ]
print(max(y))

#Question 1: Accept two numbers from the user and calculate multiplication
a=int(input("enter a number"))
b=int(input("enter another number"))
c=a*b
d=f"The multipliction value is {a}*{b}={c}"
print(d)

#Question2: Display “My Name Is James” by entering your name instead of the hardcoded name "James"

z=input("enter your name")
print("My Name is", z)

#Question 3: Accept length and width measurement of a square from the user and display the area square
length=int(input("enter your length"))
width=int(input("enter your width"))
area_square=length*width
print("Area of square is" ,area_square)

#Question 4: Accept radius measurement of a circle from the user and display the area of the circle
radius=int(input("enter your radius"))
Area_of_circle=radius*radius
print("Area of circle is" ,Area_of_circle)

#Question 5: Accept radius measurement of a sphere from the user and display the volume of the sphere
radius=int(input("enter your radius"))
vol_of_sphere=4/3 * math.pi * radius**3
print("Volume of sphere is" ,vol_of_sphere)

#
git status