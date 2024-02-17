# Câu 6: Viết chương trình nhập số tự nhiên n và tính các giá trị sau:
# a)	Tính tổng các ước số thực sự của n (không tính n)
# b)	Tính tổng 1^2+2^2+3^2+…+n^2

n = int(input('Nhập số tự nhiên n: '))
count = []
for i in range(1,n):
    if n % i == 0:
        count.append(i)
print("Tổng các ước số thực sự của n là:",sum(count))

print("-"*20)

# b
count_ = 0
for i in range(1,n+1):
    count_ += i**2
print(f"Tổng 1^2+2^2+3^2+…+{n}^2 là:",count_)