# Câu 3: Viết hàm số kiểm tra xem số tự nhiên N có phải là số chính phương hay không?

# Gợi ý: Có thể sử dụng hàm isqrt() của module math.

# số chính phương (square) là số, căn bậc 2 của nó sẽ là một số nguyên
import math

def square(n):
    can = math.isqrt(n)
    if n == can*can:return True
    else:return False

if __name__ =="__main__":
    n = int(input())
    if square(n):print("là số chính phương")
    else:print("không phải là só chính phương")