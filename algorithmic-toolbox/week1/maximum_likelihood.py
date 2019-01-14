# python3
import random
def max_pairwise_product(A):
	n = len(A)
	index1 = 0
	for i in range(1,n):
		if A[i]>A[index1]:
			index1 = i

	if index1 == 0 :
		index2 = 1
	else:
		index2 = 0

	for i in range(0,n):
		if i!=index1 and A[i]>A[index2]:
			index2= i
	return A[index1]*A[index2]

def max_pairwise_product_naive(A):
	product = 0
	for i in range(len(A)):
		for j in range(i + 1, len(A)):
			product = max(product, A[i] * A[j])
	return product

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

if __name__ == '__main__':
	input_n = int(input())
	input_numbers = [int(x) for x in input().split()]
	print(max_pairwise_product(input_numbers))
	

