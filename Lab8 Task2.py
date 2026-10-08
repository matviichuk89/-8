import array
N = int(input("Введіть розмір масиву: "))
A = [[0]*N for i in range(N)]
number = 1
for j in range(N-1, -1, -1):
    for i in range(N):
        A[i][j] = number
        number += 1
print("Введений масив:")
for i in range(N):
    print(A[i])