# Câu 1: Viết chương trình nhập số tự nhiên n từ bàn phím, sau đó kiểm tra xem số n có phải là số nguyên tố hay không, thông báo trên màn hình. 
# (Gợi ý: Số nguyên tố là số chỉ chia hết cho 1 và chính nó)

n = int(input("nhập số tự nhiên n từ bàn phím: "))

if n >= 2:
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            print(f"{n} không phải là số nguyên tố")
            break
    else:
        print(f"{n} là số nguyên tố")
else:
    print("bạn nhập sai điều kiện, số nguyên tố là số lớn hơn 1")
