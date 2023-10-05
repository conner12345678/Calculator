import math
def add(num1,num2):
    print(num1 + num2)
def minus(num1,num2):
    print(num1 - num2)
def times(num1,num2):
    print(num1 * num2)
def devide(num1,num2):
    print(num1/num2)
def exponet(num1,num2):
    print(num1 ** num2)
def remain(num1,num2):
    print(num1 % num2)
def log(num1):
    print(math.log(num1))
def sqroot (num1):
    print(math.sqrt(num1))
def clear ():
    add1 = 0
    add2 = 0
    minus1 = 0
    minus2 = 0
    times1 = 0
    times2 = 0
    devide1 = 0
    devide2 = 0
    exponet1 = 0
    exponet2 = 0
    remain1 = 0
    remain2 = 0
    log1 = 0
    sqroot1 = 0
    cos1 = 0
    tan1 = 0
    sin1 = 0
    print("Clear")
def cos(num1):
    print(math.cos(num1))
def tan(num1):
    print(math.tan(num1))
def sin(num1):
    print(math.sin(num1))

i = 0
while i == 0:
     Calculate = input("What do you want to do? (type add, minus, times, devide, exponet, remainder, log, sqroot, cos, tan, or sin) ")
     if (Calculate.upper() == "ADD"):
         add1 = input("What is the first number? ")
         add2 = input("What number are you adding to the first? ")
         add(int(add1),int(add2))
         continue1 = input("Would you like to continue? type y or n. ")
         if (continue1.upper() == "Y"):
             i = 0
             clear()
         elif (continue1.upper() == "N"):
             i = 1
     elif (Calculate.upper() == "MINUS"):
         minus1 = input("What is the first number? ")
         minus2 = input("What number are you subtracting from the first? ")
         minus(int(minus1),int(minus2))
         continue1 = input("Would you like to continue? type y or n. ")
         if (continue1.upper() == "Y"):
             i = 0
             clear()
         elif (continue1.upper() == "N"):
             i = 1
     elif (Calculate.upper() == "TIMES"):
         times1 = input("What is the first number? ")
         times2 = input("What number are you multiplying with the first? ")
         times(int(times1),int(times2))
         continue1 = input("Would you like to continue? type y or n. ")
         if (continue1.upper() == "Y"):
             i = 0
             clear()
         elif (continue1.upper() == "N"):
             i = 1
     elif (Calculate.upper() == "DEVIDE"):
         devide1 = input("What is the first number? ")
         devide2 = input("what number are you deviding from the first? ")
         devide(int(devide1),int(devide2))
         continue1 = input("Would you like to continue? type y or n. ")
         if (continue1.upper() == "Y"):
             i = 0
             clear()
         elif (continue1.upper() == "N"):
             i = 1
     elif (Calculate.upper() == "EXPONET"):
         exponet1 = input("What is the first number? ")
         exponet2 = input("How many times is the number multiplied by itself? ")
         exponet(int(exponet1),int(exponet2))
         continue1 = input("Would you like to continue? type y or n. ")
         if (continue1.upper() == "Y"):
             i = 0
             clear()
         elif (continue1.upper() == "N"):
             i = 1
     elif (Calculate.upper() == "REMAINDER"):
         remain1 = input("What is the first number? ")
         remain2 = input("What is the second number? ")
         remain(int(remain1),int(remain2))
         continue1 = input("Would you like to continue? type y or n. ")
         if (continue1.upper() == "Y"):
             i = 0
             clear()
         elif (continue1.upper() == "N"):
             i = 1
     elif (Calculate.upper() == "LOG"):
         log1 = input("What is the number? ")
         log(int(log1))
         continue1 = input("Would you like to continue? type y or n. ")
         if (continue1.upper() == "Y"):
             i = 0
             clear()
         elif (continue1.upper() == "N"):
             i = 1
     elif (Calculate.upper() == "SQROOT"):
         sqroot1 = input("What is the number being square rooted? ")
         sqroot(int(sqroot1))
         continue1 = input("Would you like to continue? type y or n. ")
         if (continue1.upper() == "Y"):
             i = 0
             clear()
         elif (continue1.upper() == "N"):
             i = 1
     elif (Calculate.upper() == "COS"):
         cos1 = input("what is the number? ")
         cos(int(cos1))
         continue1 = input("Would you like to continue? type y or n. ")
         if (continue1.upper() == "Y"):
             i = 0
             clear()
         elif (continue1.upper() == "N"):
             i = 1
     elif (Calculate.upper() == "TAN"):
         tan1 = input("What is the number? ")
         tan(int(tan1))
         continue1 = input("Would you like to continue? type y or n. ")
         if (continue1.upper() == "Y"):
             i = 0
             clear()
         elif (continue1.upper() == "N"):
             i = 1
     elif (Calculate.upper() == "SIN"):
         sin1 = input("What is the number? ")
         sin(int(sin1))
         continue1 = input("Would you like to continue? type y or n. ")
         if (continue1.upper() == "Y"):
             i = 0
             clear()
         elif (continue1.upper() == "N"):
             i = 1