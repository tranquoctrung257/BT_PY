# Câu 7: Cho trước 2 dãy(list) a,b. Viết chương trình thiết lập dãy c bao gồm các phần tử lấy lần lượt từ phần cuối của a,b.
# Gợi ý: sử dụng PT pop()

a = [1,2,2,4,532,5624,23]
b = [4,54,3,6,35,235,23,5]
c = []
temp1,temp2 = a.pop(),b.pop()
c.append(temp1)
c.append(temp2)
print(c)