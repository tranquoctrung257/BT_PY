# Câu 2: Thiết lập lớp Hocsinh dùng để quản lý các đối tượng học sinh trong lớp em
# Các thuộc tính của mỗi học sinh bao gồm:
# -	Họ và tên
# -	Địa chỉ
# -	Chiều cao
# -	Cân nặng
# -	Học lực

class HocSinh():
    def __init__(self,Ten) :
        self.Ten = Ten
        # self.DiaChi = DiaChi
        # self.ChieuCao = ChieuCao 
        # self.CanNang = CanNang
        # self.HocLuc = HocLuc
    def Prints(self):
        print(self.Ten)
ten = HocSinh("trung")
print(ten)