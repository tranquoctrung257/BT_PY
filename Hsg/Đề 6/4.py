# Câu 4: Cho trước xâu ký tự s. Viết chương trình tách các ký tự là số của xâu trên và chuyển vào một dãy A.

def tach_so(s):
    A = []
    for i in range(len(s)):
        if s[i].isdigit():
            A.append(s[i])
    return A
if __name__=="__main__":
    s = "việt nam 2024"
    A = tach_so(s)
    print(A)