#1. Calculate the value of a function with x varying from 1 to 20 in increments of 0.5.
count = 1
while (count < 20):   
    count += 0.5
    print(count)

#2 Calculate the value of the function a=2.6, b=5, x varies from 0 to 10 in steps of 0.5.
from cmath import cos, exp, sin
a =  2.6
b = 5
t =0
for x in range(0,10):
    if  x < 2:
        s = a + (b / exp(x) + cos(x))
        print("x = " + str(x) + "; x<2; s= " + str(s))
    elif x >= 6:
        s = (a + b) / (x + 1)
        print("x = " + str(x) + "; x >= 6; s= " + str(s))
    elif 2 <= x & x < 6:
        s = (a + b) / (x + 1)
        print("x = " + str(x) + "; 2 <= x & x < 6; s= " + str(s))
    
    x+=0.5


#3  A natural n is given. Find function:

from cmath import sin
result = 1
sum_sin = 0
number =   input ("Enter natural number:") 
for x in range(1,number):
    sum_sin+= sin(x)
    result += 1. / sum_sin
    x+=1
print("The answer is =  " + str(result))


#4  A natural n is given. Find function:

from cmath import sin, cos
result = 1.0
sin_sum = 0.0
cos_sum = 0.0
number =   input ("Enter natural number:") 
for x in range(1,number):
    cos_sum += cos(x)
    sin_sum += sin(x)
    result *= cos_sum / sin_sum
print("The answer is =  " + str(result))


#5  Calculate the value of a function with x varying from 1 to 20 in increments of 0.5.

from cmath import sin, cos
result = 1.0
for x in range(1,20):
    result = 2 * x * x + 15
    x+=0.5
print("The answer is =  " + str(result))

# 1. Information about the amount of precipitation during the week is given as an array. Determine the total amount of precipitation for the week.
lists = [16, 2, 77, 40, 21, 0, 55]
amount = 0
for x in range(len(lists)):
    amount += lists[x]
    x+=1
print(amount)


#2 The air temperatures for the week are given. Determine the average air temperature for the week and how many times the temperature dropped below 0 degrees.
lists = [16, -2, 7, -10, 21, 0, -5]
amount = 0
counter = 0
for x in range(0, len(lists)):
    amount += lists[x]
    avarage = amount/7
    if lists[x]<0:
        counter +=1
    x+=1
print("Avarege = " + str(avarage))
print("T dropped below 0 = " + str(counter) + " times")


#3. Given natural numbers N, a0,a1,....,a(N-1). Determine the number of members of the sequence that have even ordinal numbers and are odd numbers.

lists = [16, -2, 7, -10, 21, 0, -5, 3, 6, 5, 6, -1, 4, 5, 6, 7, 3]
counter = 0
for x in range(0, len(lists)):

    if lists[x] % 2 == 1 & (x + 1) % 2 == 0:
        counter +=1
    x+=1

print("Answer = " + str(counter) )


#4.  There is an array of numbers. Determine how many pairs of nonidentical adjacent elements it contains.

lists = [16, -2, 7, -10, 21, 0, -5, 3, 6, 5, 6, -1, 4, 5, 6, 7, 3,3,33,33,5, 6, 7, 3]
resultOfNonPair = 0
pairs = 0

for x in range(0, len(lists)-1):

    if lists[x] != lists[x + 1]:
        resultOfNonPair +=1
    elif lists[x] == lists[x + 1]:
        pairs+=1
    x+=1

print("Nonidentical adjacent elements = " + str(resultOfNonPair) )
print("pairs = " + str(pairs) )


#5.  Given an array of numbers.Find the largest element, put it first, moving the rest elements to right.

lists = [16, -2, 7, -10, 21, 0, -5, 3, 6, 5, 6, -1, 4, 5, 6, 7, 3, -54, 567, 80, 116, 84, 28, -8, 34, 0]
for x in range(0, len(lists)-1):
    if lists[0] < lists[x]:
        lists[0] = lists[x]
    x+=1

print("Largest element = " + str(lists[0]) )