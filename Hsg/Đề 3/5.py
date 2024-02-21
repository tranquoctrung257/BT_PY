# Câu 5: Thiết lập lớp Circle (vòng tròn) bao gồm thuộc tính R (bán kính) và tọa độ âm X,Y. Thiết lập các phương thức tính chu vi và diện tích của đối tượng hình tròn.


import math

class Circle:
    def __init__(self, bankinh, x, y):
        self.bankinh = bankinh
        self.x = x
        self.y = y
    def ChuVi(self):
        return 2 * math.pi * self.bankinh
    def dientich(self):
        return  math.pi * (self.bankinh ** 2)


t = Circle(20,2,3)
print(t.ChuVi())
print(t.dientich())