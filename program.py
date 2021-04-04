import collections
from collections import Counter
X = int(input("kol obuvi v magaze: "))     #  --
my_list = collections.Counter(map(int, input().split()))
print(Counter(my_list))
n = int(input('Klient:'))
counter = 0
i = 0
for i in range(n):
    size, price = map(int, input().split(' '))
    if my_list[size]:
        counter += price
        my_list[size] -= 1

print(counter)




