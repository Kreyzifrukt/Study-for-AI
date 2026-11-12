a = float(input("Введите a: "))
b = float(input("Введите b: "))
c = float(input("Введите c: "))

if a == 0:
    print("Это не квадратное уравнение")
else:
    d = b*b - 4*a*c
    print("Дискриминант =", d)

    if d > 0:
        kor = d ** 0.5
        x1 = (-b + kor) / (2*a)
        x2 = (-b - kor) / (2*a)
        print("Два корня:")
        print("x1 =", x1)
        print("x2 =", x2)
    elif d == 0:
        x = -b / (2*a)
        print("Один корень:")
        print("x =", x)
    else:
        print("Корней нет")
