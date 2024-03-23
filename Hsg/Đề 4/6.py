# Câu 6: Nhập dãy A bao gồm n phần tử từ bàn phím và tính tổng các phần tử của A
n = list(map(int,input("nhập dãy A: ").split()))

print(sum(n))
# hoặc
tong = 0
for i in n:
    tong+=i
print(tong)
