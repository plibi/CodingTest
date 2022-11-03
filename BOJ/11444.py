import sys
sys.setrecursionlimit(10**7)
def fib(n):
 
    if n <= 1:
        return n
 
    return fib(n - 1) + fib(n - 2)
 
 
if __name__ == '__main__':
 
    n = int(input())
    mod = 1000000007
    print(fib(n) % mod)