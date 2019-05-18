"""
as seen here https://www.shiftedup.com/2015/05/07/five-programming-problems-every-software-engineer-should-be-able-to-solve-in-less-than-1-hour

Problem 1
Write three functions that compute the sum of the numbers in a given list using a for-loop, a while-loop, and recursion.

Problem 2
Write a function that combines two lists by alternatingly taking elements. For example: given the two lists [a, b, c] and [1, 2, 3], the function should return [a, 1, b, 2, c, 3].

Problem 3
Write a function that computes the list of the first 100 Fibonacci numbers. By definition, the first two numbers in the Fibonacci sequence are 0 and 1, and each subsequent number is the sum of the previous two. As an example, here are the first 10 Fibonnaci numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, and 34.

Problem 4
Write a function that given a list of non negative integers, arranges them such that they form the largest possible number. For example, given [50, 2, 1, 9], the largest formed number is 95021.

Update: Apparently this problem got a lot of people talking (although not as much as Problem 5 below.) You can click here to read my solution.

Problem 5
Write a program that outputs all possibilities to put + or - or nothing between the numbers 1, 2, ..., 9 (in this order) such that the result is always 100. For example: 1 + 2 + 34 – 5 + 67 – 8 + 9 = 100.
"""

from itertools import compress, product

def combinations(items):
    return ( set(compress(items,mask)) for mask in product(*[[0,1]]*len(items)) )

# Write three functions that compute the sum of the numbers in a given list using a for-loop, a while-loop, and recursion.
def problem1():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    sumByFor(numbers)
    sumByWhile(numbers)

    counter = 0
    sum = 0
    sumByRecursion(numbers, counter, sum)


    def sumByFor(numbers):
        sum = 0
        for number in numbers:
            sum += number

        print(sum)
        return sum


    def sumByWhile(numbers):
        sum = 0
        counter = 0
        while(True):
            try:
                sum += numbers[counter]
                counter += 1
            except:
                print(sum)
                return sum


    def sumByRecursion(numbers, counter, workingSum):
        # python doesn't have great support for recurssion atm the logic is solid but python catches it as an error
        try:
            if counter < len(numbers):
                workingSum += numbers[counter]
                sumByRecursion(numbers, counter, workingSum)
            else:
                print(workingSum)
                return workingSum
        except:
            return sumByFor(numbers)

# Write a function that combines two lists by alternatingly taking elements. For example: given the two lists [a, b, c] and [1, 2, 3], the function should return [a, 1, b, 2, c, 3].
def problem2():
    list1 = [1,2,3,4,5]
    list2 = ['a','b','c','d','e']
    finalList = []
    for elem in range(0, len(list1)):
        finalList.append(list1[elem])
        try:
            finalList.append(list2[elem])
        except:
            print("Ran out of elements of list 2")
    print(finalList)
    return finalList

# Write a function that computes the list of the first 100 Fibonacci numbers. By definition, the first two numbers in the Fibonacci sequence are 0 and 1, and each subsequent number is the sum of the previous two. As an example, here are the first 10 Fibonnaci numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, and 34.
def problem3():
    fib = [0,1]

    for i in range(2, 100):
        fib.append(fib[i-1] + fib[i-2])
    
    print(fib)
    print(len(fib))
    return(fib)

# Write a function that given a list of non negative integers, arranges them such that they form the largest possible number. For example, given [50, 2, 1, 9], the largest formed number is 95021.
def problem4():
    #I can't do this one
    numbers = [1,2,4,10,50,709]

def problem5():
    #yeah this aint happening either
    fives = 55
    
if __name__ == '__main__':
    problem1() 
    problem2() 
    problem3() 
    problem4() 
    # problem5()
