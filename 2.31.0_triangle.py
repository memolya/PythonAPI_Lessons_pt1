a, b, c = int(input()), int(input()), int(input())

if a == b == c:
    print('Равносторонний треугольник')
elif a == b or b == c or a == c:
    print('Равнобедренный треугольник')
elif a + b == c or a + c == b or b + c == a:
    print('Прямоугольный треугольник')
else:
    print('Разносторонний треугольник')
