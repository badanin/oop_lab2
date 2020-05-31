import math
from P2d import P2d


class P3d(P2d):
    def __init__(self, X, Y, Z):

        P2d.__init__(self, X, Y)
        self.Z = Z

    def getZ(self):
        return self.Z

    # Определение длинны стороны треугольника
    def distance(self, Po3d):
        dist = math.sqrt(((self.X - Po3d.getX()) ** 2) + ((self.Y - Po3d.getY()) ** 2) + ((self.Z - Po3d.getZ()) ** 2))
        return dist

    # Статичный метод, расчет площади по формуле Герона
    @staticmethod
    def compute_area(a, b, c):
        p = (a+b+c)/2
        s = math.sqrt(p*(p-a)*(p-b)*(p-c))
        return s
