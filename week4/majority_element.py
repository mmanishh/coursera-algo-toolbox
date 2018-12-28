# Uses python3
import sys
import random


def get_majority_element_dict(a, left=0, right=0):
    a = sorted(a)
    count = {}
    half = len(a) // 2
    for i in range(len(a)):
        count[a[i]] = 0
    for i in range(len(a)):
        count[a[i]] += 1

    for key in count:
        if count[key] > half:
            return key
        else:
            return -1


def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]

    mid = (left + right - 1) // 2 + 1
    left_m = get_majority_element(a, left, mid)
    right_m = get_majority_element(a, mid, right)

    left_count = 0
    for i in range(left, right):
        if a[i] == left_m:
            left_count += 1
    if left_count > (right - left) // 2:
        return left_m

    right_count = 0
    for i in range(left, right):
        if a[i] == right_m:
            right_count += 1
    if right_count > (right - left) // 2:
        return right_m

    return -1


def get_majority_element_naive(a):
    n = len(a)
    for i in range(n):
        current = a[i]
        count = 0

        for j in range(n):
            if a[j] == current:
                count += 1

        if count > (n // 2):
            return a[i]

    return -1


def stress_test(N, M):
    while True:
        n = random.randint(2, N)
        A = []
        for i in range(n):
            randm = random.randint(1, M)
            A.append(randm)
        i = random.randint(1, N)
        common = [random.randint(1, M)] * i
        A.extend(common)
        result_1 = get_majority_element_naive(A)
        result_2 = get_majority_element(A)

        if result_1 == result_2:
            print("-ok-")
        else:
            print(A)
            print("Wrong answer:", result_1, " ", result_2)
            print("For : {0} , {1}".format(N, M))
            return


if __name__ == '__main__':

    # stress_test(10000,1000)
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)

