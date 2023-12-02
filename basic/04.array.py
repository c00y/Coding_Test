# 10807

n = int(input())

while(True):
    n_list = input()

    if len(n_list.split()) == n:
        n_list = list(map(int, n_list.split()))
        break

    else: print("error: out of range, input again")

v = int(input())

print(n_list.count(v))


# 10871

n, x = map(int, input().split())

while(True):
    n_list = input()

    if len(n_list.split()) == n:
        n_list = list(map(int, n_list.split()))
        break

    else: print("error: out of range, input again")

for i in n_list:
    if i < x:
        print(i, end = ' ')


# 10818

n = int(input())

while(True):
    n_list = list(map(int, input().split()))

    if len(n_list) == n: break
    else: print("error: out of range, input again")

print(min(n_list), max(n_list))


# 2562

n = 9
n_list = []

for i in range(n):
    n_list.append(int(input()))

print(max(n_list))
print(n_list.index(max(n_list)) + 1)


# 10810

N, M = map(int, input().split())

basket = [0] * N

for _ in range(M):
    i, j, k = map(int, input().split())
    for n in range(i-1, j):
        basket[n] = k

for p in (basket):
    print(p, end=' ')


# 10813

N, M = map(int, input().split())

basket = [0] * N

for n in range(1, N+1):
    basket[n-1] = n

for n in range(M):
    i, j = map(int, input().split())
    k = basket[i-1]
    basket[i-1] = basket[j-1]
    basket[j-1] = k

for n in basket:
    print(n, end=' ')


# 5597

s = [0] * 30

for i in range(1, 31):
    s[i-1] = i

for _ in range(28):
    i = int(input())
    s.remove(i)

for n in range(len(s)):
    print(s[n])


# 3052

k = []

for i in range(10):
    n = int(input()) % 42
    if n not in k:
        k.append(n)

print(len(k))


# 10811

N, M = map(int, input().split())

basket = [0] * N

for n in range(1, N+1):
    basket[n-1] = n

for n in range(M):
    i, j = map(int, input().split())
    r = basket[i-1:j]
    r.reverse()
    basket[i-1:j] = r

for n in basket:
    print(n, end=' ')


#1546

n = int(input())
score = list(map(int, input().split()))

M = max(score)

for i in range(n):
    score[i] = score[i]/M*100

print(sum(score)/n)

