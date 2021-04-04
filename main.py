cube = lambda x: x * x * x
n = int(input("Input n:"))
mas = []
for i in range(n):
    if i <= 1:
        mas.append(i)
    else:
        mas.append(int(mas[i-1])+int(mas[i-2]))

print(list(map(cube, mas)))