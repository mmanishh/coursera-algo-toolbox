#Uses python3

import sys

def largest_number_naive(digits):
    #write your code here
    answer = []

    while len(digits)!=0:
        max_digit =-100000000
        for digit in digits:
            if digit>=max_digit:
                max_digit = digit
        answer.append(max_digit)
        digits.remove(max_digit)
    
    return answer

def largest_number(digits):
    #write your code here
    answer = []

    while len(digits)!=0:
        max_digit =-100000000
        for digit in digits:
            if is_greater_or_equal(digit,max_digit):
                max_digit = digit
        answer.append(max_digit)
        digits.remove(max_digit)
    
    result = "".join([str(x) for x in answer])
    
    return result

def is_greater_or_equal(digit, max_digit):
    max_digit_ = str(max_digit).strip('-')
    a = int(str(digit)+str(max_digit_))
    b = int(str(max_digit_)+str(digit))
    return a>=b


if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(list(map(int,a))))
    
