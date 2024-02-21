# Câu 3: Thiết lập lớp Triple bao gồm các đối tượng là một bộ 3 số thực (a,b,c). Thuộc tính của mỗi đối tượng bao gồm:
# Tên của đối tượng
# Bộ 3 số a,b,c
# Tổng 3 số này, ký hiệu S
# Thiết lập các phương thức sau:
# Hàm __init__() dùng để khởi tạo 1 bộ triple
# Hàm Update() dùng để cập nhật giá trị S
# Hàm Change() có chức năng thay đổi các giá trị a,b,c và đồng thời cập nhật S
# Hàm isTriange() kiểm tra xem bộ 3 số này có tạo thành một tam giác hay không?

class Triple:
	def __init__(self,a,b,c):
		self.a = a
		self.b = b
		self.c = c
		self.S = self.a + self.b + self.c
	def Update(self,CapNhatGiaTriS):
		self.S = CapNhatGiaTriS
	def Change(self,CapNhatGiaTriA,CapNhatGiaTriB,CapNhatGiaTriC):
		self.a = CapNhatGiaTriA
		self.b = CapNhatGiaTriB
		self.c = CapNhatGiaTriC
		self.S = self.a + self.b + self.c
	def isTriange(self):
		if self.a > 0 and self.b > 0 and self.c > 0 and self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
			return True
		return False

if __name__ == "__main__":
		
	t1 = Triple(1,2,3)
	print(t1.S)

	# cập nhật giá trị của S
	t1.Update(100)
	print(t1.S)

	# cập nhật giá trị a,b,c
	t1.Change(11,20,30)
	print(t1.S)

	# kiểm tra có phải là tam giác hay không
	if t1.isTriange(): print("Là 1 tam giác")
	else: print("Không phải là một tam giác")