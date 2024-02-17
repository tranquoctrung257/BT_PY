# Câu 3: Viết chương trình nhập số tự nhiên n và in ra trên màn hình tất cả các ước số thực sự của n 
# (Gợi ý: Sử dụng for và range(start,stop). Ước số của n là những số n chia hết cho số đó)


n = int(input("nhập số tự nhiên n: "))

z = []

for i in range(1,n+1):
    if n % i == 0:
        z.append(i)
print(f"Ước của {n} là:",*z)