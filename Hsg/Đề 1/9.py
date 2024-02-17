# Câu 9: Số tự nhiên được gọi là hoàn hảo nếu số đó bằng tổng các ước số thực sự của mình. Ví dụ 6=1+2+3 vậy 6 là số hoàn hảo. Viết chương trình nhập số tự nhiên n từ bàn phím và kiểm tra xem n có phải là số hoàn hảo hay không. Thông báo trên màn hình

# n = int(input("nhập số tự nhiên n: "))
n = 28
a = 0
for i in range(1,n):
    if n % i == 0:
        a += i
        
if a == n: 
    print(f"{n} là số hoàn hảo")
elif a != n:
    print(f"{n} không phải là số hoàn hảo")