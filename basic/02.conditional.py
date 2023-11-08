# 1. 1330

a, b = map(int, input().split())

if(a > b):   print(">")
elif(a < b): print("<")
else:        print("==")


# 2. 9498

a = int(input())

if(90 <= a <= 100):     print("A")
elif(80 <= a <= 89):    print("B")
elif(70 <= a <= 79):    print("C")
elif(60 <= a <= 69):    print("D")
else:                   print("F")


# 3. 2753

a = int(input())

if ((a % 4 == 0) and (a % 100 != 0)) or (a % 400 == 0):
    print('1')
else:                   
    print('0')


# 4. 14681

x = int(input())
y = int(input())

if(x>=0):
    if(y>=0): print(1)
    else:     print(4)

else:
    if(y>=0): print(2)
    else:     print(3)


# 5. 2884

H, M = map(int, input().split())

if(M-45 < 0):
    if(H == 0):
        H = 24
    print((H - 1), (60 + (M - 45)))

else:
    print(H, (M - 45))


# 6. 2525

H, M = map(int, input().split())
T = int(input())

if((M + T) >= 60):

    H += int((M + T) / 60)
    M = (M + T) % 60

    if(H >= 24):
        H -= 24

    print(H, M)

else:
    print(H, (M + T))


# 7. 2480

f, s, t = map(int, input().split())

if(f == s == t):    print(10000 + f * 1000)

elif(f == s or f == t or s == t):
    if(f == s):     n = f    
    if(f == t):     n = t
    if(t == s):     n = s

    print(1000 + n * 100)

else:
    if(f > s):
        if (f > t): n = f
        else:       n = t
    
    else:
        if(s > t):  n = s
        else:       n = t
    
    print(n * 100)