#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the reverseArray function below.
def reverseArray(a):
    n=len(a)
    for i in range(int(n/2)):
        temp=a[i]
        a[i]=a[n-i-1]
        a[n-i-1]=temp

    return a

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input())

    """

    Let us break it down.

    input() 
    This is used to fetch input from the user. In this case. We are expecting the user       to provide a list of integers. How do I know? Look next.

    input().strip() 
    This will eliminate trailing spaces from the user input, if they are there. Why is       it required? Because some users will do that and that might break your program.

    Remember that input() will cast the input as string. So, now we have a string of         integers like so: “1 2 4 42”

    input.strip().split() 
    split() is used to create a Python list out of a string. If no delimiter is given,       this breaks the string by spaces. So, now we have: [“1”, “2”, “4”, “42”]

    map(int, input().strip().split()) 
    map() takes two arguments. The first one is the method to apply, the second one is       the data to apply it to. By this understanding, we can see this is doing nothing but     typecasting every element of the list to an integer value. Since map returns the         data type it was applied to, the list() method applied over map() is redundant. So       now we have covered the following:

    list(map(int, input().strip().split())) 
    And we have: [1, 2, 4, 42]

    Note the missing quotes. This means the elements are now all int"""

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
