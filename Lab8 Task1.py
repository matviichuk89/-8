import array
result = []
a=list(map(int, input("Введіть 10 чисел масиву: ").split()))
k = len(a)
G = sum(a)/k
print("Середнє арифметичне:", G)
for x in a:
    if x > G:
        result.append(x)
for x in result:
    a.remove(x)
print("Масив після видалення елементів, що більші за середнє арифметичне:", a)