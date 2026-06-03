#!/usr/bin/python3
def fizzbuzz():
    a = [3,6,9,12,15,18,21,24,27,30,33,36,39,42,45,48,51,54,57,60,63,66,69,72,75,78,81,84,87,90,93,96,99]
    b = [5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]

    for i in range(1, 101):
        if (i in a and i in b):
            print("FizzBuzz ", end="")
        elif (i in a):
            print("Fizz ", end="")
        elif (i in b):
            print("Buzz ", end="")
        else:
            print(f"{i} ", end="")

