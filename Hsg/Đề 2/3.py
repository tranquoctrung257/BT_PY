# Câu 3: Viết các hàm lambda mô tả các biểu thức sau:
# a)	x+y+z
# b)	x**(y+z)
# c)	(x+y)**2

# hàm lambda thực hiện những công việc tính toán cơ bản ngắn gọn chỉ trong 1 biếu thức trả về
# thường được dùng trong các hàm như max sort ,...

# a.
add_a = lambda x,y,z : x+y+z
print(add_a(1,4,7))

# b.
add_b = lambda x,y,z : x**(y+z)
print(add_b(4,2,5))

# c.
add_c = lambda x,y : (x+y)**2
print(add_c(3,5))