

'''
GCD algorithm
'''
def gcd(a, b):
    if a != 0 and b != 0:
        if a > b:
            return gcd(b, a % b)
        else:
            return gcd(b % a, a)
    else:
        if a == 0:
            return b
        else:
            return a


'''
Rectangles on a rubik's cube
'''
def rubiks(n):
    return (n * (n + 1) / 2) ** 2 * 6


'''
Guessing a number
'''
def guess_unlimited(n, is_this_it):
    # The code here is only for illustrating how is_this_it() may be used
    # Guess random number x between 1 and n (inclusive)
    # x = the_number
    # a = candidate
    # Can I make this O(log n)? No. I need to use the is_this_it fcn.
    for i in range(1, n + 1):
        guess = i
        if is_this_it(guess) == True:
            return guess
    return -1


'''
Guessing a number where you can only make two guesses that are larger
'''
def guess_limited(n, is_this_smaller):
    guess = (n - 1) / 2 + 1
    lower = 1
    upper = n
    # begin binary search
    while is_this_smaller(guess) == True:
        lower = guess + 1
        guess = (upper - lower) / 2 + lower
    #print "Lower:", lower, "Guess:", guess
    # checks if right-most node is the_number
    if lower == guess:
        return guess
    upper = guess
    guess = lower
    # begin linear search
    while is_this_smaller(guess) == True:
        guess += 1
    return guess

'''
Guessing a number, bonus problem
'''
def guess_limited_plus(n, is_this_smaller):
    return guess_limited_plus_helper(n, is_this_smaller, 0, 1, n)

def guess_limited_plus_helper(n, is_this_smaller, answer, l, r):
    if r >= l:
        guess = (r - l) / 2 + l
        result = is_this_smaller(guess)
        if result == False:
            answer = guess
            return guess_limited_plus_helper(n, is_this_smaller, answer, l, guess - 1)
        elif result == True:
            return guess_limited_plus_helper(n, is_this_smaller, answer, guess + 1, r)
    if r < l:
        if is_this_smaller(answer - 1) == True:
            return answer
    return -1
