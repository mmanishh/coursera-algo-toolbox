#python3
import math
def euclidean_gcd(a,b):
    if b==0:
        return a
    
    a_ = a%b
    return euclidean_gcd(b,a_)
def lcm(a,b):
    return (a*b)//euclidean_gcd(a,b)



if __name__=="__main__":
    input = input()
    a, b = map(int, input.split())
    print(lcm(a,b))