from math import sqrt

print("The standard format of a quadratic equation is as follows: ax^2 + bx + c = 0")
a = float(input("Please enter a: "))
b = float(input("Please enter b: "))
c = float(input("Please enter c: "))
delta = b**2 - 4*a*c

if delta > 0:
    x1 = (-b + sqrt(delta)) / (a*2)
    x2 = (-b - sqrt(delta)) / (a*2)
    print("x =", x1, ",", x2)
elif delta == 0:
    x = (-b) / (a*2)
    print("x =", x)
elif delta < 0:
    print("The equation has no real roots.")