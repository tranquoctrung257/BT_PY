# Câu 4: Viết chương trình nhập số tự nhiên n và đếm số các ước số thực sự của n. In kết quả ra màn hình

n = int(input("nhập số tự nhiên n: "))
# n = 10 
dem = 0

for i in range(1,n+1):
    if n % i == 0:
        dem += 1
print(dem)