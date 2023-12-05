# 2745

# B, N = input().split()

# B = list(reversed(B))

# sum = 0

# array = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# for i in range(len(B)):
#     sum += array.index(B[i]) * (int(N) ** i)

# print(sum)


# 11005

# Q, N = map(int, input().split())

# array = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# M = ''

# while Q:
#     M += array[Q % N]
#     Q //= N

# print(M[::-1])


# 2720

# T = int(input())

# D = [25, 10, 5, 1]

# for _ in range(T):
#     C = int(input())

#     for j in D:
#         print(C//j, end=' ')
#         C %= j
    
#     print()
        

# 2903

# N = int(input())

# dot = 2

# for i in range(N):
#     dot += (dot - 1)

# print(dot**2)


# 2292

# N = int(input())

# S = 1
# room = 1

# while N > S:

#     S += 6 * room
#     room += 1

# print(room)


# 1193

# N = int(input())

# line = 1

# while N > line:
#     N -= line
#     line += 1

# if line % 2 == 0:
#     a = N
#     b = line - N + 1

# else:
#     a = line - N + 1
#     b = N

# print(f'{a}/{b}')


# 2869

# A, B, V = map(int, input().split())

# result = (V-B) // (A-B) 

# if (V-B) % (A-B) > 0:
#     result += 1

# math.ceil: 실수 입력 시 올림하여 정수 반환
 
# print(result)

