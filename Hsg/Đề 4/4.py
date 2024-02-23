# Câu 4: Viết chương trình nhập số N từ bàn phím, in và liệt kê danh sách các ước số thực của n như một list
# Ví dụ: Nếu N=15 thì kết quả list là [1,3,5]

# cách cở bản nhưng chậm
def liet_ke_uoc(n):
    lst = []
    for i in range(1,n+1):
        if n % i == 0:
            lst.append(i)
    return lst

# cách nhanh 
import math
def liet_ke_uoc_1(n):
    lst = []
    for i in range(1,math.isqrt(n)+1):
        if n % i == 0:
            lst.append(i)
            if i != n//i:
                lst.append(n//i)
    lst.sort()
    return(lst)

if __name__ == "__main__":
    n = int(input("nhập số nguyên n từ bàn phím: "))
    print(liet_ke_uoc(n))