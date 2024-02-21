# Câu 2: Thiết lập lớp Hocsinh dùng để quản lý các đối tượng học sinh trong lớp em
# Các thuộc tính của mỗi học sinh bao gồm:
# -	Họ và tên
# -	Địa chỉ
# -	Chiều cao
# -	Cân nặng
# -	Học lực

class HocSinh():
    def __init__(self,Ten,DiaChi,ChieuCao,CanNang,HocLuc) :
        self.Ten = Ten
        self.DiaChi = DiaChi
        self.ChieuCao = ChieuCao 
        self.CanNang = CanNang
        self.HocLuc = HocLuc
    def thay_doi_hoc_luc(self,HocLucMoi):
        self.HocLuc = HocLucMoi

hocsinh1 = HocSinh("Tèo","Gia lai","1m6","48kg","khá")
print(hocsinh1.Ten)
print(hocsinh1.DiaChi)
print(hocsinh1.ChieuCao)
print(hocsinh1.CanNang)
print(hocsinh1.HocLuc)
# để đổi học lưc
hocsinh1.thay_doi_hoc_luc("gioi")
print(hocsinh1.HocLuc)



# class HocSinh():
#     def __init__(self,Ten,DiaChi,ChieuCao,CanNang,HocLuc) :
#         self.Ten = Ten
#         self.DiaChi = DiaChi
#         self.ChieuCao = ChieuCao 
#         self.CanNang = CanNang
#         self.HocLuc = HocLuc
#     def __str__(self):
#         # trả về các giả trị đã khởi tạo ở hàm __init__
#         return f"Tên: {self.Ten} \nĐịa chỉ: {self.DiaChi} \nChiềuCao:{self.ChieuCao} \nCân Nặng:{self.CanNang} \nHọc lực:{self.HocLuc}"
# ten = HocSinh("Tèo","Xã Ia Băng","1m6","48kg","khá")
# print(ten)