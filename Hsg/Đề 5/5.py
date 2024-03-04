# Câu 5: Cho trước dãy(list) A bao gồm các số nguyên, cho trước số nguyên k. Biết rằng dãy(list) trong Python có 2 phương thức count() và remove() có ý nghĩa như sau:

# a.count(<giá trị>) sẽ trả lại số lần tìm thấy của <giá trị> trong a, nếu không tìm thấy sẽ trả lại 0

# a.remove(<giá trị>) sẽ xóa phần tử đầu tiên có <giá trị> trong a, nếu không tìm thấy phần tử có <giá trị> sẽ báo lỗi

# Viết chương trình xóa tất cả các phần tử trong dãy a có giá trị k. Chú ý khi viết chương trình không được để gặp lỗi

a = [1112,312,4,12,42,43,3,4,234,54,3,3,4,56,6,5,5,5]

def xoa_ptu(lst,value):
    k = value
    for i in lst:
        count = lst.count(k)
        if count != 0:
            a.remove(k)

xoa_ptu(a,5)
print(a)
