# Câu 5: Viết hàm số f(m,n) với tham số m,n là số tự nhiên theo yêu cầu sau:
# a)Hàm đếm số các ước chung của các số m,n
# b)Hàm đếm số các ước số của m nhưng không là ước số của n
# c)Hàm tính tổng các ước số chung của m và n

# a.

def j(m,n):
    a = {i for i in range(1,m+1) if m%i==0}
    b = {i for i in range(1,n+1) if m%i==0}
    count = a.intersection(b)
    return len(count)
# print(j(33550336,33550336))

def b(m,n):
    lst = []
    for i in range(1,m+1):
        if m%i == 0:
            lst.append(i)
    lst_1 = []
    for j in range(1,n+1):
        if n%j == 0:
            lst_1.append(j)
    return len(lst)

def c(m,n):
    a = {i for i in range(1,m+1) if m%i==0}
    b = {i for i in range(1,n+1) if m%i==0}
    count = a.intersection(b)
    return sum(count)
