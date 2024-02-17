# Câu 5: Viết chương trình nhập số tự nhiên n và tính các giá trị sau:
# a)	Tính tổng 1+2+…+3n
# b)	Tính tổng các số tự nhiên <n và là số lẻ
# c)	Tính tổng các số tự nhiên <n và là số chẵn

n = int(input('Nhập số tự nhiên n: '))

a = 0
for i in range(1,n+1):
    a+=i
print(f'tong cac so tu 1+2+...+{n} la {a}')

z =0
h = 0
for j in range(1,n+1):
    if j  % 2 != 0:
        z+=j
    elif j  % 2 == 0:
        h+=j
print(f'tổng các số lẻ từ 1 đến {n} là {z}')
print(f'tổng các số chẵn từ 1 đến {n} là {h}')

