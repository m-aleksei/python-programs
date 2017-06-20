def printroots(a,b,c):
    D = b**2 - 4*a*c
    import math
    x1 = (-b+math.sqrt(D))/2*a
    x2 = (-b-math.sqrt(D))/2*a	
    print("x1 = ", x1, "\nx2 = ", x2)

a=1
b=0
c=-1
printroots(a,b,c)

input("Press Enter to exit...")
