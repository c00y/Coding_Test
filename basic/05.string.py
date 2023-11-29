# 27866

S = list(input())

i = int(input())

print(S[i-1])


# 2743

S = input()

print(len(S))


# 9086

n = int(input())

S = []

for i in range(n):
    S.append(input())
    print(S[i][0], end='')
    print(S[i][len(S[i])-1])


# 11654

S = input()

print(ord(S))


# 11720

N = int(input())

while(True):
    S = list(map(int, input()))

    if N == len(S):
        break

    else: print("error: out of range, input again")

print(sum(S))


# 10809

S = input()

alphabet = 'abcdefghijklmnopqrstuvwxyz'

for i in alphabet:
    print(S.find(i), end=' ')


# 2675

T = int(input())

for _ in range(T):
    R, S = input().split()

    for s in S:
        print(s*int(R), end='')

    print()


# 1152

S = list(input().split())

print(len(S))


# 2908

S = list(input().split())

for i in range(len(S)):
    S[i] = S[i][::-1]


print(max(S))


# 5622

S = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

call = list(input())

sum = 0

for i in S:
    for j in call:
        if j in i:
            sum += S.index(i) + 3

print(sum)


# 11718

while (True):
    try:
        print(input())

    except:
        break
