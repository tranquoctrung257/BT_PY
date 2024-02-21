# Nhập vào số nguyên dương a, nếu a là số chẵn thì in ra đây là số chẵn, ngược lại in ra đây là số lẻ

a = int(input("nhập vào số nguyên dương a: "))

if a % 2 == 0:print(f"{a} là số chẵn")
else:print(f"{a} là số lẻ")