# Câu 4: Thiết lập lớp Tam_giac là lớp con của lớp Triple trong bài tập trên. Bổ sung các phương thức sau cho lớp con này:
# Hàm tính diện tích tam giác
# Hàm tính bán kính vòng tròn ngoại tiếp tam giác
# Hàm tính bán kính vòng tròn nội tiếp tam giác
# Ta có các công thức sau tính diện tích S, bán kính vòng tròn ngoại tiếp R và bán kính vòng tròn nội tiếp r của tam giác có các cạnh a,b,c.
#  với p = nửa chu vi tam giác

class Triple:
	def get_class(self,a,b,c):
		self.a = a
		self.b = b
		self.c = c
		self.S = self.a + self.b + self.c

class Tam_giac(Triple):
	def tam_giac(self,a,b,c):
		super().get_class(a,b,c)
	def getpchuvi(self):
		return self.S/2
	def BanKInhNoiTiep(self):
		return self.S / (self.S / 2)

if __name__ == "__main__":

	t1 = Tam_giac()
	t1.tam_giac(1,2,3)

	# chu vi hình tròn
	print(t1.getpchuvi())

	# bán kính hình tròn
	print(t1.BanKInhNoiTiep())
