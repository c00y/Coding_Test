# 25083

print("         ,r\'\"7")
print("r`-_   ,'  ,/")
print(" \\. \". L_r'")
print("   `~\\/")
print("      |")
print("      |")


# 3003

W = [1, 1, 2, 2, 2, 8]

C = list(map(int, input().split()))

for i in range(len(W)):
    print(W[i] - C[i], end = ' ')


# 2444

N = int(input())

for i in range(1, N):
    print(' ' * (N-i), end='')
    print('*' * (2 * i - 1))

for i in range(N, 0, -1):
    print(' ' * (N-i), end='')
    print('*' * (2 * i - 1))


# 10988

S = input()

if S == S[::-1]:    print(1)
else:               print(0)


# 1157

S = input().upper()

S_list = list(set(S))

cnt = []

for i in S_list:    cnt.append(S.count(i))

if cnt.count(max(cnt)) > 1:     print("?")

else: print(S_list[cnt.index(max(cnt))])


# 2941

S = input()

Alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in Alphabet:
    S = S.replace(i, '*')

print(len(S))


# 1316

N = int(input())

g_cnt = N

for _ in range(N):
    S = input()
    for i in range(len(S)-1):
        if S[i] == S[i+1]:
            continue
        
        elif S[i] in S[i+1:]:
            g_cnt -= 1
            break

print(g_cnt)


# 25206

score = 0

subject = 0

rank = ['D0', 'D+', 'C0', 'C+', 'B0', 'B+', 'A0', 'A+']

for _ in range(20):
    S = list(map(str, input().split())) 

    if S[2] == 'P':
        continue

    else:
        score += float(S[1])

        if S[2] == 'F':
            subject += float(S[1]) * 0.0

        else:
            subject += float(S[1]) * (rank.index(S[2]) * 0.5 + 1)

print(round(subject/score, 7))