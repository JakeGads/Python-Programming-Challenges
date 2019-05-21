"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""

def missing_number(intList):
    intList.sort()
    compare = intList[0]
    intList.append('eol')

    for i in intList:
        if type(i) is not type(5) and i != 'eol':
            return str(compare) + ' is not an integer'
        if i != compare:
            return "The first missing number is " + str(compare)
        compare += 1

def main():
    print(missing_number([6,1,2,4,5]))
    print(missing_number([3, 4, -1, 1]))
    print(missing_number([1, 2, 0]))
    


if __name__ == '__main__':
    main()
    