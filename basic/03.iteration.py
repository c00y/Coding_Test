# 2739

n = int(input())

for i in range(1, 10):
    print("{0} * {1} = {2}".format(n, i, n * i))


# 10950

t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    print(a+b)
    

# 8393

sum = 0

for n in range(1, int(input())+1):
    sum += n

print(sum)


# 25304

sum =0

x = int(input())

for n in range(int(input())):
    a, b = map(int, input().split())
    sum += a*b

if x == sum:
    print("Yes")

else:
    print("No")


# 25314

n = int(input())

if (n % 4) == 0:
    n /= 4

else:
    n = (n / 4) + 1

for i in range(int(n)):
    print("long", end = " ")

print("int")
    

# 15552

import sys

for n in range(int(sys.stdin.readline())):

    a, b = map(int, sys.stdin.readline().split())
    print(a + b)


# 11021

import sys

for n in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())
    print("Case #{0}: {1}".format(n + 1, a + b))


# 11022

import sys

for n in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())
    print("Case #{0}: {1} + {2} = {3}".format(n + 1, a, b, a + b))


# 2438

import sys

for n in range(1, int(sys.stdin.readline()) + 1):
    print("*" * n)


# 2439

import sys

a = int(sys.stdin.readline())

for n in range(1, a + 1):
    print(" "* (a-n), end = '')
    print("*" * n)


# 10952

import sys

while(True):
    a, b = map(int, sys.stdin.readline().split())
    if a == 0 & b == 0: break
    print(a + b)


# 10951

import sys

while(True):
    try: a, b = map(int, sys.stdin.readline().split())
    except: break

    print(a + b)

