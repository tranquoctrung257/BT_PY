# Nhập vào 3 số a, b, c. Tính và in ra d = (a + b)^c
# Nếu d là số trong khoảng từ 100 - 200 thì in ra True, ngược lại in ra False

a = int(input("nhập vào số a: "))
b = int(input("nhập vào số b: "))
c = int(input("nhập vào số c: "))

d = (a + b) ** c
print(d)

print(100<=d<=200)
# if d >= 100 and d <= 100:print(True)
# else:print(False)