# Câu 8: Cho trước 2 dãy A,B. Dãy C được thiết lập bằng cách lần lượt lấy các phần tử từ A, B đưa vào C theo thứ tự tăng dần.
# Ví dụ:
# A=[0.2.4.6.8.10]
# B=[1,3,5,7,9,11]
# Thì C=[0,1,2,3,4,5,6,7,8,910,11]

A=[0,2,4,6,8,10]
B=[1,3,5,7,9,11]

# cách 1
C = A + B
C.sort()
print(C)

# cách 2

