# Câu 8: Viết chương trình nhập số tự nhiên n từ bàn phím. Tính và kiểm tra tính đúng đắn của biểu thức sau:
# 1^3+2^3+3^3+…+n^3=(1+2+3+…+n)^2

# n = int(input("nhập số tự nhiên n từ bàn phím: "))
n = 10
if n>0:
    count_vt = 0
    for i in range(1,n+1):
        count_vt+=(i**3)
    # print(count_vt)

    count_vp = 0
    for j in range(1,n+1):
        count_vp+=j
    count_vp = count_vp**2
    # print(count_vp)
    # hoặc sum(range(1,10+1))**2

    # Kiểm tra tính đúng đắn của biểu thức
    if count_vt == count_vp:
        print(f"biểu thức đúng với n = {n}")
        print(f"vế trái {count_vt} | vế phải {count_vp}")
    else:
        print(f"biểu thức sai với n = {n}")
        print(f"vế trái {count_vt} | vế phải {count_vp}")
        
else:
    print("nhập số tự nhiên lớn hơn 0")