# Câu 7: Viết chương trình nhập số tự nhiên n từ bàn phím và tính các giá trị sau: (dùng hàm)
# a) Tính tổng 12+22+32+…+n2
# b) Tính tổng 1+1/2+1/3+…+1/n
# c) Tính tổng 1/2+1/6+1/12+⋯+1/((n-1)n)

def a(n):
    tong = 0
    for i in range(1,n+1):
        tong+=i**2
    return tong
def b(n):
    tong = 0
    for i in range(1,n+1):
        tong += 1/i
    return tong
def c(n):
    tong = 0
    for i in range(2,n+2):
        tong+=1 / ((i-1) * i)
    return tong
