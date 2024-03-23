# Câu 3: Viết một hàm số tổng quát hơn phương thức sort() của dãy (list) như sau:
# - Đầu vào là dãy A bao gồm có thể là số hoặc ký tự
# - Đầu ra là dãy B thu được từ dãy A bằng cách sắp xếp các phần tử là số theo thứ tự tăng dần, còn các vị trí là ký tự thì giữ nguyên




def int_(a):
    temp_int = []
    for i in a: 
        if isinstance(i,(int,float)):
            temp_int.append(i)
    return temp_int
def str_(a):
    temp_str = []
    for i in range(len(a)):
        if not isinstance(a[i],(int,float)):
            temp_str.extend([a[i],i])
    return temp_str
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def sx1(a):
    vtri = []
    for i in range(len(temp_str)):
        if isinstance(temp_str[i],(int,float)):
            vtri.append(temp_str[i])
    return vtri

def sx2(a):
    ptu = []
    for i in range(len(temp_str)):
        if not isinstance(temp_str[i],(int,float)):
            ptu.append(temp_str[i])
    return(ptu)

if __name__ == "__main__":
    a = [1,2,"a",24,"e",12,2,423,1,543,0,"a"]
    b = int_(a)
    bubble_sort(b)
    temp_str = str_(a)
    for i in range(len(sx1(temp_str))):
        b.insert(sx1(temp_str)[i],sx2(temp_str)[i])
    print(a)
    print(b)