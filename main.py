from P3d import P3d

# Задаем координаты точек
p1 = P3d(1, 2, 3)
p2 = P3d(4, 5, 7)
p3 = P3d(2, 5, 8)

# Рассчитываем длинну сторон между парой точек
a = p1.distance(p2)
b = p2.distance(p3)
c = p3.distance(p1)

# Рассчитываем площадь треугольника
s = P3d.compute_area(a, b, c)

print('Площадь треугольника = ' + str(s))
