# Nhập vào 3 số thực dương a, b, c. Kiểm tra xem a, b, c có cấu thành độ dài của 1 tam giác được không

a = float(input("nhập vào số a: "))
b = float(input("nhập vào số b: "))
c = float(input("nhập vào số c: "))

if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and c + b > a:
    print("a,b,c có thể tạo thành 1 tam giác.")
else:print("a,b,c không thể tạo thành 1 tam giác.")