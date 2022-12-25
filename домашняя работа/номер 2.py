#Даны три целых числа. Выведи значение наименьшего из них.
a=int(input("введите число"))
b=int(input("введите число"))
c=int(input("введите число"))
if a>=b<=c:
    print(b)
elif b>=c<=a:
    print(c)
elif c>=a<=b:
    print(a)