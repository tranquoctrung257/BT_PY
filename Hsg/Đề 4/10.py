# Câu 10: Viết chương trình nhập một xây ký tự từ bàn phím và in ra màn hình là các ký tự của xâu này.
# Ví dụ: Việt Nam ==> [“V”, “i”,….]

n = input("nhập một xây ký tự từ bàn phím: ")
lst = []
for i in n:
    lst.append(i)
# lst.remove(" ")
print(lst)