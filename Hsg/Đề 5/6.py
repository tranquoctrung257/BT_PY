# Câu 6: Cho trước dãy(list) a bao gồm các số nguyên, cho trước 2 số nguyên k,m. Viết chương trình thay thế tất cả các phần tử của a có giá trị k bằng giá trị m.

# Gợi ý: Sử dụng phương thức index() của list trong Python

def thay_the_phan_tu_list_a(a, k, m):
    index = a.index(k)
    a[index] = m

# Sử dụng
a = [1, 2, 3, 4, 5, 1, 6, 7, 1]
k = 3
m = 83
thay_the_phan_tu_list_a(a, k, m)
print("Danh sách mới:", a)