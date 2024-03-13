# Câu 1: Viết chương trình nhập ma trận gồm n hàng m cột với các số nguyên ngẫu nhiên. Thực hiện các hàm:
# a)	Tính tổng từng hàng
# b)	Tính tổng từng cột
# c)	Sắp xếp tăng dần các hàng mang trận
# d)	Đếm có bao nhiêu số chẵn trong ma trận đã nhập


import random

def nhap_ma_tran(n, m):
    matran = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(random.randint(1, 100))
    return matran

def tinh_tong_hang(matran):
    return [sum(row) for row in matran]

def tinh_tong_cot(matran):
    return [sum(col) for col in zip(*matran)]

def sap_xep_tang_dan(matran):
    return [sorted(row) for row in matran]

def dem_so_chan(matran):
    count = 0
    for row in matran:
        for num in row:
            if num % 2 == 0:
                count += 1
    return count

# Nhập ma trận
n = int(input("Nhập số hàng: "))
m = int(input("Nhập số cột: "))
matrix = nhap_ma_tran(n, m)

# a) Tính tổng từng hàng
tong_hang = tinh_tong_hang(matrix)
print("Tổng của từng hàng:", tong_hang)

# b) Tính tổng từng cột
tong_cot = tinh_tong_cot(matrix)
print("Tổng của từng cột:", tong_cot)

# c) Sắp xếp tăng dần các hàng
sap_xep = sap_xep_tang_dan(matrix)
print("Ma trận sau khi sắp xếp tăng dần các hàng:")
for row in sap_xep:
    print(row)

# d) Đếm có bao nhiêu số chẵn trong ma trận
so_chan = dem_so_chan(matrix)
print("Số lượng số chẵn trong ma trận:", so_chan)
