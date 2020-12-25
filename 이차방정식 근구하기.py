from math import *

a = 1
b = 10
c = 21
근1= (b*-1 + sqrt(b ** 2-4 * a * c)) / 2*a
근2= (b*-1 - sqrt(b ** 2-4 * a * c)) / 2*a

if b ** 2-4 * a * c == 0:
    if a==1:
        if b==1:
            print("x^2+x+" +str(c) +"=0의 근은 "+ str(근1))
        else:
            print("x^2+" + str(b) + "x+" +str(c) +"=0의 근은 "+ str(근1))
    else:
        if b==1:
            print(str(a) + "x^2+x+" +str(c) +"=0의 근은 "+ str(근1))
        else:
            print(str(a) + "x^2" + str(b) +"x+" +str(c) +"=0의 근은 "+ str(근1))
else:
    if a==1:
        if b==1:
            print("x^2+x+" +str(c) +"=0의 근은 "+ str(근1) +"," +str(근2))
        else:
            print("x^2+" + str(b) + "x+" +str(c) +"=0의 근은 "+ str(근1) +"," +str(근2))
    else:
        if b==1:
            print(str(a) + "x^2+x+" +str(c) +"=0의 근은 "+ str(근1) +"," +str(근2))
        else:
            print(str(a) + "x^2" + str(b) +"x+" +str(c) +"=0의 근은 "+ str(근1) +"," +str(근2))


