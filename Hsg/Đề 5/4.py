# Câu 4: Cho trước 2 dãy(list) A,B và số tự nhiên k, 0<=k<len(A). Viết hàm số trả lại dãy (list) thu được từ A sau khi chèn dãy B vào vị trí của chỉ số k



a = [0,0,0,0,0,0,0,0]
b = [2,4,23,523,342,33]

def them_ds(a,b,k):
    return a[:k] + b + a[k:]
print(them_ds(a,b,2))
print(them_ds(a,b,91))
print(them_ds(a,b,-100))