

n = int(input('Введите количество элементов списка: '))
list_n = input('Введите элементы списка через пробел: ').split()
arr = list(map(int, list_n))
x = int (input('Введите число х: '))
count = 0
for i in range(n):
    if arr[i] == x:
        count += 1
print(f'Число {x} встречается  {count} раз.')