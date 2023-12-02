# 2738

N, M = map(int, input().split())

A, B = [], []

for i in range(2):
    if i == 0:  p = A 
    else:       p = B

    for _ in range(N):
        p.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M):
        print(A[i][j] + B[i][j], end=' ')
    print()


# 2566

array = []
max = 0

for i in range(9):
    array.append(list(map(int, input().split())))

for i in range(len(array)):
    for j in range(len(array)):
        if array[i][j] >= max:
            max = array[i][j]
            row, col = i+1, j+1

print(max)
print(row, col)


# 10798

S = []

for _ in range(5):
    S.append(list(input()))

for i in range(15):
    for j in range(len(S)):
        if i < len(S[j]):
            print(S[j][i], end='')


# 2563

N = int(input())

array = [[0] * 100 for _ in range(100)]

result = 0

for _ in range(N):
    x, y = map(int, input().split())

    for i in range(x, x + 10):
        for j in range(y, y + 10):
            array[i][j] = 1

for i in range(100):
    result += array[i].count(1)

print(result)

