# Câu 2: Viết chương trình tạo list bao gồm N số nguyên tố đầu tiên với N số tự nhiên cho trước (hoặc được nhập từ bàn phím)

import math
def chek_ngto(n):
    if n < 2: return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0: 
            return False
    return True
if __name__ == "__main__":
    lst = []
    n = 100
    for i in range(1,n+1):
        if chek_ngto:
            lst.append(i)
    print(lst)