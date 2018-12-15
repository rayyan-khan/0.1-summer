#python tasks


#1 input two numbers and print the sum
import math
import string

def addNums(a,b):
    print("the sum is " + str(a+b))

#addNums(int(input("input a number")), int(input("input another number")))

#2 input a string and print every other letter
def everyOther(s):
    for i, c in enumerate(s):
        if i%2==0:
            print(c)

#everyOther(str(input("input a word")))

#3a input a string of numbers (with spaces between them) and print their sum
def str2arr(s): #assuming spaces between numbers
    array = s.split(" ")
    intarr = []
    for i in array:
        intarr.append(int(i))
    return intarr

def addAllNums(array):
    sum = 0
    for i in array:
        sum = sum + i
    return sum

#print(str(addAllNums(str2arr(input("input a string of numbers with spaces")))))

#3b print those divisible by 3
def div3(array):
    arr2 = []
    for i in array:
        if i%3 == 0:
            arr2.append(i)
    return arr2

#print(str(div3(str2arr(input("input a string of numbers with spaces")))))

#4 print the first n fibonacci numbers

def fib(n):
    arr3 = []
    for k in range (0, n):
        if k == 0:
            arr3.append(0)
        elif k == 1:
            arr3.append(1)
        else:
            arr3.append(arr3[k-1] + arr3[k-2])
    return arr3

#for n in range (0, 10):
#    print(fib(n))

def fibRecur(n):
    if n == 0:
        return "no 0th fibonacci number"
    elif (n-1) == 0:
        return 0
    elif (n-1) == 1:
        return 1
    else:
        return fibRecur(n-1) + fibRecur(n-2)

#for n in range (0,10):
 #  print(str(n) + ": " + str(fibRecur(n)))

#5a: check whether an input number is prime or not
def isPrime(n):
    if n < 2:
        return False
    elif n == 2 or n == 3 or n == 5 or n == 7:
        return True
    elif n%2 == 0:
        return False
    else:
        for k in range(3, int(n/2-.5)):
            if n % k == 0:
                return False
        return True

#for k in range (20, 50):
 #   print(str(k) + ": " + str(isPrime(k)))

#5b: Given an input of two space separated numbers, print all the prime numbers between then
def primesBtwn(s):
    arr4 = s.split()
    intArr = int(arr4[0]), int(arr4[1])
    arr5 = []
    for k in range(intArr[0], intArr[1]):
        if isPrime(k) == True:
            arr5.append(k)
    return(str(arr5))

#primesBtwn("10 50")

#5c: Given an input of one or two space separated numbers, determine whether to use 6a or 6b
def detPrimeFunc(s):
    if " " in str(s):
        return primesBtwn(s)
    else:
        return isPrime(s)

#print(detPrimeFunc("50 100"))
#print(detPrimeFunc(13))
#print(detPrimeFunc(52))

def isTriangle(a,b,c):
    if (a + b) > c and (b + c) > a and (a + c) > b:
        return True
    else:
        return False
#print(isTriangle(1,2,3))
#print(isTriangle(3,4,5))

def triangleArea(a,b,c):
    if isTriangle(a,b,c) == True:
        s = (a+b+c)/2
        return(math.sqrt(s*(s-a)*(s-b)*(s-c)))

#print(triangleArea(3,4,5))
#print(triangleArea(5,12,13))

#7: remove all punctuation from a string
def rmvPunc(s):
    newStr = ""
    for i in s:
        if i not in string.punctuation:
            newStr = newStr + i
    return newStr

#print(rmvPunc("Hi! Happy Birthday, have a good day."))



