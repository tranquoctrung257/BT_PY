# Câu 1: Thiết lập lớp QuadriSquare bao gồm đối tượng hình chữ nhật hoặc hình vuông.
# -	Mỗi đối tượng sẽ có 2 thuộc tính chiều dài w và chiều cao h
# -	Các method chính của lớp này là các hàm tính chu vi (Chuvi()) và diện tích (Dientich()) của mỗi đối tượng
# Bài mẫu cho các em tham khảo:
class QuadriSquare:
    def __init__(self, w, h):
        self.w = w
        self.h = h
    def dientich(self):
        return self.w * self.h
    def chuvi(self):
        return (self.w + self.h) *2

hinh_vuong = QuadriSquare(10, 5)

print(hinh_vuong.dientich())  # In ra 50
print(hinh_vuong.chuvi()) # In ra 30