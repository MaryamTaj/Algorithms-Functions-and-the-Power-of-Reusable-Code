# Author: Maryam Taj
# Name of Program: Algorithms, Functions and the Power of Reusable Code
# Description of Program: This program allows the user to solve for standard mathematical formulas such as the Quadratic formuala, Pythagorean Theorem,
# Einstein's Theory of Special Relativity, Area and Perimeter of a Regular Polygon and Circumference of a Circle

import math

# Quadratic Formula
def QFormula (a,b,c):
    # This function calculates the quadratic formula. It takes 3 arguments, a,b, and c and returns a x and y value
    x = (-b + (b**2 - 4*a*c)**0.5) /(2*a)
    y = (-b - (b**2 - 4*a*c)**0.5) /(2*a)
    return x,y
print(QFormula (1,14,48))

# Pythagorean Theorem
def PTheorem (a,b,c):
    # This function calculates the pythagorean theorem. It takes 3 arguments, a,b and c and returns the unknown, string value as an integer
    if type(a) == str:
        a = (c**2 - b**2)**0.5
        return a
    if type(b) == str:
        b = (c**2 - a**2)**0.5
        return b
    if type(c) == str :
        c = (a**2 + b**2)**0.5
        return c
print(PTheorem ("A",4,5))

# Einstein's Theory of Special Relativity
def ERelativity (E,m,c):
    # This function calculates Einstein's theory of special relativity. It takes 3 arguments, E, m and c, and returns the unknown, string value as an integer
    if type(E) == str:
        E = m*c**2
        return E
    if type(m) == str:
        m = E/(c**2)
        return m
    if type(c) == str:
        c = (E/m)**0.5
        return c
print(ERelativity("E",2,3))

# Area of a Regular Polygon
def APolygon (A,b,r,s):
    # This function calculates the area of a regular polygon. It takes 4 arguments, A, b, r and s, and returns the unknown, string value as an integer
    if type(A) == str:
        A = (b*r/2)*s
        return A
    if type(b) == str:
        b = (2*A)/(r*s)
        return b
    if type(r) == str:
        r = (2*A)/(b*s)
        return r
    if type(s) == str:
        s = (2*A)/(b*r)
        return s
print(APolygon ("A",5,3,4))

# Perimeter of a Regular Polygon
def PPolygon (P,b,s):
    # This function calculates the perimeter of a regular polygon. It takes 3 arguments, P, b and s, and returns the unknown, string value as an integer
    if type(P) == str:
        P = b*s
        return P
    if type(b) == str:
        b = P/s
        return b
    if type(s) == str:
        s = P/b
        return s
print(PPolygon ("P",3,3))

# Circumference of a Circle
def CCircle (C,r):
    # This function calculates the circumference of a circle. It takes 2 arguments,C and r, and returns the unknown, string value as an integer
    if type(C) == str:
        C = 2*math.pi*r
        return round(C,2)
    if type(r) == str:
        r = C/(2*math.pi)
print(CCircle ("C",6))
