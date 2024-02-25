# Câu 9: Cho trước dãy A. Dãy B được thiết lập bằng cách tách các phần tử là số (số nguyên hoặc số thực) từ dãy A.
# Ví dụ:
# A=[1.2, “one”, 0.15, “A”, “B”, “C”, 1, 50, 4.56, “C”]
# Thì B=[1.2, 0.15, 1, 50, 4.56]
# (Gợi ý: Có 2 giải thuật cơ bản: Giải thuật sử dụng type và giải thuật dùng hàm isinstance() )


A=[1.2, "one", 0.15, "A", "B", "C", 1, 50, 4.56, "C"]
B = []
for i in A:
    if isinstance(i,(float,int)):
        B.append(i)

print(B)

# hoặc
print([i for i in A if isinstance(i,(float,int)) ])

# hoặc 
A=[1.2, "one", 0.15, "A", "B", "C", 1, 50, 4.56, "C"]
B = []
for i in A:
    if type(i) in (float,int):
        B.append(i)
print(B)