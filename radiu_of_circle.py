from math import pi
def radius_of_circle():
    r = float(input("Input the radius of the circle :"))
    # area = 3.8013271108436504
    print("The area of the circle with radius ", str(r) + " is: " + str(pi * r**2))

radius_of_circle()