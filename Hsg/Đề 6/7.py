from math import isqrt
# Câu 7: Cho trước hoặc nhập xâu từ bàn phím, xâu s. Hãy xóa đi tất cả các ký tự cả s không là số, xâu còn lại là số. In ra kết quả này và thông báo nó có phải là nguyên tố hay không




def tach_so(s):
    x = ''
    for i in range(len(s)):
        if s[i].isdigit():
            x+=s[i]
    return x

def check_ngto(n):
    if n <= 1: return False
    for i in range(2,isqrt(n)+1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    s = "qưe1dwer1"
    # s = 'ưqw'
    if not tach_so(s):
        print("sâu không có số nào. ")
    else:
        if check_ngto(int(tach_so(s))):
            print("phải là nguyên tố")
        else:print("không phải là số nguyên tố")