"""
This problem was asked by Jane Street.

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
Implement car and cdr.
"""

def cons(a, b):
    def pair(f):
        return (a, b)
    return pair(())

def car(a,b):
    f = cons(a,b)
    return f[0]
 

def cdr(a,b):
    f = cons(a,b)
    return f[1]

def complete(a,b):
    print("CAR:\t" + str(car(a,b)))
    print("CDR:\t" + str(cdr(a,b)))

def main():
    complete(3,4)

if __name__ == '__main__':
    main()
    
