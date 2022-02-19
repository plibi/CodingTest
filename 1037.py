N = input()
divisors = [int(i) for i in input().split()]
divisors.sort()
print(divisors[0]*divisors[-1])