import random  
import time

optel1 = random.randint(0,10000)
optel2 = random.randint(0,10000)
def addition(number1:int, number2:int):
    return number1 + number2
for i in range(3):
    time.sleep(0.2)
    print(str(optel1) + ' + ' + str(optel2) + ' = ' + str(addition(optel1, optel2)))
    optel1 = random.randint(0,10000)
    optel2 = random.randint(0,10000)
print()


min1 = random.randint(0,10000)
min2 = random.randint(0,10000)
def subtraction(number1a:int, number2a:int):
    return number1a - number2a
for i in range(3):
    time.sleep(0.2)
    print(str(min1) + ' - ' + str(min2) + ' = ' + str(subtraction(min1, min2)))
    min1 = random.randint(0,10000)
    min2 = random.randint(0,10000)
print()


def multiplication(number1b:int, number2b:int):
    return number1b * number2b
for i in range(3):
    time.sleep(0.2)
    keer1 = random.randint(0,10000)
    keer2 = random.randint(0,10000)
    print(str(keer1) + ' x ' + str(keer2) + ' = ' + str(multiplication(keer1, keer2)))
print()

def division(number1c:int, number2c:int):
    return number1c / number2c
for i in range(3):
    time.sleep(0.2)
    delen1 = random.randint(0,10000)
    delen2 = random.randint(0,10000)
    print(str(delen1) + ' : ' + str(delen2) + ' = ' + str(division(delen1, delen2)))
print()

def increment(number1d:int, number2d:int):
    return number1d + number2d
for i in range(3):
    time.sleep(0.2)
    plusEen = random.randint(0,1000)
    print(str(plusEen) + ' + ' + str(1) + ' = ' + str(int(increment(plusEen, 1))))
print()

def decrement(number1e:int, number2e:int):
    return number1e - number2e
for i in range(3):
    time.sleep(0.2)
    minEen = random.randint(0,1000)
    print(str(minEen) + ' - ' + str(1) + ' = ' + str(int(decrement(minEen, 1))))
print()
