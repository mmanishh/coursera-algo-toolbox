#Uses python3

import sys
import random

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
    
    return answer

def is_greater_or_equal(digit, max_digit):
    max_digit_ = str(max_digit).strip('-')
    a = int(f'{digit}{max_digit_}')
    b = int(f'{max_digit_}{digit}')
    return a>=b



def stress_test(N,M):

	while True:
		n = random.randint(2,N)
		print("n:",n)
		A = []
		for i in range(n):
			randm = random.randint(1,M)
			A.append(randm)
		print(A)

		result_1 = max_pairwise_product_naive(A)
		result_2 = max_pairwise_product(A)

		if result_1 == result_2:
			print("-ok-")
		else:
			print("Wrong answer:",result_1," ",result_2)
			return