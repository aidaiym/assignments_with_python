
#5.  Given an array of numbers.Find the largest element, put it first, moving the rest elements to right.

from pickle import TRUE


lists = [16, -2, 7, -10, 21, 0, -5, 3, 6, 5, 6, -1, 4, 5, 6, 7, 3, -54, 567, 80, 116, 84, 28, -8, 34, 0]
resultOfNonPair = 0
pairs = 0
isIncreasing = TRUE

for x in range(0, len(lists)-1):

    if lists[0] < lists[x]:
        lists[0] = lists[x]
  
    x+=1

print("Largest element = " + str(lists[0]) )

