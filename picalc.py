import math
from decimal import *
getcontext().prec = 35

L = 1
polygon_sides = 4 #2**62

radius = L/2/math.sin(math.radians(360/2/polygon_sides))

pi = (L * polygon_sides)/(2 * radius)


while polygon_sides < 2**62:
    mycalc = Decimal(pi)
    comppi = Decimal(math.pi)

    print(f"{polygon_sides}-gon | My Calc: {mycalc} | Pi: {comppi} | Error: {comppi - mycalc}")

#need to add loop to print all sides
#refine calc (more readable?)
#clean print out

#rewrite this shit in FORTRAN