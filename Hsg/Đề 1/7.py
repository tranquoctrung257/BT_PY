# Câu 7: Viết chương trình nhập số tự nhiên n từ bàn phím. Tính và kiểm tra tính đúng đắn của biểu thức sau:
# 1^2+2^2+3^2+…+n^2=(n(n+1)(2n+1))/6

n = int(input("nhập số tự nhiên n từ bàn phím: "))

vt = 0
if n > 0:
    for i in range(1,n+1):
        vt = vt + (i**2) 
        # vt+=(i**2)

    vp = (n*(n+1)*(2*n+1))//6

    if vt == vp:
        print(f"biểu thức đúng với n = {n}")
        print(f"vế trái {vt} | vế phải {vp}")
    else:
        print(f"biểu thức sai với n = {n}")
        print(f"vế trái {vt} | vế phải {vp}")
else:
    print("nhập số tự nhiên n lớn hơn 0!")
