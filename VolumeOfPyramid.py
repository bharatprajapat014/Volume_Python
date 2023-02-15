import math

num_sides = int(input("Enter the number of sides of the base of the pyramid: "))
length_side = float(input("Enter the length of a side of the base of the pyramid: "))
height = float(input("Enter the height of the pyramid: "))

area_of_base = (num_sides * length_side**2) / (4 * math.tan(math.pi/num_sides))

volume = (1/3) * area_of_base * height

print("The volume of the pyramid is:", volume)
