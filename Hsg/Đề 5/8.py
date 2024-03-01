# Câu 8: Cho trước dãy(list) A. Viết chương trình tạo dãy B bao gồm các phần tử lấy từ A nhưng theo thứ tự ngược lại. Chú ý giữ nguyên A không thay đổi
# Gợi ý: Có nhiều cách giải

A = [2,3,423,523,5234,5322,4324,523,True,False,None,"str"]
B = []
A.reverse()
B.extend(A)
print(B)

# hoặc  
A = [2,3,4,52,423,234,"str",True,None]
B = []
for i in range(len(A)-1,-1,-1):B.append(A[i])
print(B)