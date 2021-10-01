c1 = float(input ("Введите длину первого катета: "))
c2 = float(input ("Введите длину второго катета: "))
hypotenuse = (c1 ** 2 + c2 ** 2) ** 0.5
perimeter = (c1 + c2 + hypotenuse)
square = (c1 * c2) / 2
print ("Площадь прямоугольного треугольника: " + str(square))
print("Периметр прямоугольного треугольника: " + str(perimeter))
input()