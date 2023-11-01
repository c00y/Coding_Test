# 1. 2557

print("Hello World!")


# 2~5. 1000, 1001, 10998, 1008

a, b = map(int, input().split())

print(a+b)
print(a-b)
print(a*b)
print(a/b)


# 6. 10869

a, b = map(int, input().split())

print(a+b)
print(a-b)
print(a*b)
print(int(a/b))
print(a%b)


# 7. 10926

print(input() + "??!")


# 8. 18108

print(int(input()) - 543)


# 9. 10430

a, b, c = map(int, input().split())

print((a+b)%c)
print(((a%c) + (b%c))%c)
print((a*b)%c)
print(((a%c)*(b%c))%c)


# 10. 2588

a = int(input())
b = input()

for i in reversed(range(3)):
    print(a*int(b[i]))
    if(i == 0):
        print(a*int(b))


# 11. 11382

a, b, c = map(int, input().split())

print(a + b + c)


# 12. 10171

print("\\    /\\")
print(" )  ( ')")
print("(  /  )")
print(" \\(__)|")


# 13. 10172

print('|\_/|')
print('|q p|   /}')
print('( 0 )"""\\')
print('|"^"`    |')
print('||_/=\\\\__|')
