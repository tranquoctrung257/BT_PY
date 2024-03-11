# Câu 4: Cho trước xâu ký tự s. Viết chương trình tách các ký tự là số của xâu trên và chuyển vào một dãy A.

def xau(s):
    A = []
    for i in s:
        if i.isdigit():
            A.append(int(i))
    return A

if __name__=="__main__":
    s = "việt nam 2024"
    f = xau(s)
    print(f)