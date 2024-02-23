# Câu 3: Viết chương trình nhập số N, sau đó sẽ lần lượt nhập N tên học sinh, đưa các học sinh này vào một list và in list này ra màn hình

n = input("nhập tên học sinh: ")

lst = []
lst.append(n)
print(lst)

# hoặc nhập nhiều người cách nhau bởi dấu phẩy
z = list(map(str,input("nhập tên học sinh cách nhau bởi dấu cách: ").split(",")))
print(z)