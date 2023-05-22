n = input("Введите шестизнаяное число:")
n = int (n)
d1 = int(n%10)
n =n//10
d2 = int(n%10)
n = n//10
d3 = int(n%10)
n = n//10
d4 = int(n%10)
n = n//10
d5 = int(n%10)
n = n//10
if d1+ d2 +d3 == d4+ d5+ n:
    print("Счастливый")
else: 
    print("Нет")
    