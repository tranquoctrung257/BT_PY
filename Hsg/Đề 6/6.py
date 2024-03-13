"""
Câu 6: Cho trước 2 xâu s1, s2. Viết chương trình:
a)	Kiểm tra xem xâu s2 có trong s1 hay không?
b)	Nếu có thì đếm số lần xuất hiện của s2 trong s1
c)	In ra màn hình xâu s2 được viết theo thứ tự ngược lại
d)	Trộn 2 xâu trên lại, in ra kết quả. Việc trộn xâu theo nguyên tắc:
-	Lần lượt từ trái sang phải, viết các ký tự của s1 sau đó đến s2
-	Nếu 1 trogn 2 xâu kết thúc thì chỉ viết ra các ký tự của xâu còn lại

"""
def check_substring(s1, s2):
    if s2 in s1:
        return True
    else:
        return False

def count_substring_occurrences(s1, s2):
    count = 0
    index = 0
    while index < len(s1):
        index = s1.find(s2, index)
        if index == -1:
            break
        count += 1
        index += 1
    return count

def reverse_string(s):
    return s[::-1]

def mix_strings(s1, s2):
    result = ''
    min_length = min(len(s1), len(s2))
    for i in range(min_length):
        result += s1[i] + s2[i]
    result += s1[min_length:] + s2[min_length:]
    return result

s1 = input("Nhập xâu s1: ")
s2 = input("Nhập xâu s2: ")

# a) Kiểm tra xem xâu s2 có trong s1 hay không?
if check_substring(s1, s2):
    print("Xâu s2 có trong s1.")
else:
    print("Xâu s2 không có trong s1.")

# b) Đếm số lần xuất hiện của s2 trong s1
count = count_substring_occurrences(s1, s2)
print("Số lần xuất hiện của xâu s2 trong s1 là:", count)

# c) In ra màn hình xâu s2 được viết theo thứ tự ngược lại
reversed_s2 = reverse_string(s2)
print("Xâu s2 được viết theo thứ tự ngược lại là:", reversed_s2)

# d) Trộn 2 xâu trên lại, in ra kết quả
mixed_string = mix_strings(s1, s2)
print("Xâu sau khi trộn là:", mixed_string)
