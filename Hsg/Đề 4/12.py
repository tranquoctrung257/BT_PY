# Câu 12: Cho trước 2 dãy số A,B. Dãy C được tạo theo quy tắc sau:
# Giả sử số phần tử của A là n và nhỏ hơn số phần tử của B. Trường hợp ngược lại làm tương tự.
# -	n phần tử đầu tiên của C là tổng các số hạng tương ứng của A,B
# -	Các phần tử còn lại lấy từ B
# Viết thủ tục với 2 tham số đầu vào là A,B và in ra màn hình dãy C
# (Gợi ý: Dùng hàm randint() để sinh bộ dữ liệu ngẫu nhiên và dùng các phương thức copy)
import random
A = []
B = []
for i in range(10):
    z = random.randint(1,100)
    s = random.randint(1,100)
    A.append(z)
    B.append(s)

C = [sum(A+B)]
C.extend(B)
print(C)
