# Câu 5: Cho trước xâu ký tự s. Hãy đếm số các ký tự và chữ cái tiếng Anh kể cả chữ hoa, thường trong xâu.


def xau(s):
    thuong = []
    hoa = []
    for i in s:
        if i.istitle():
           hoa.append(i)
        elif i.islower():
            thuong.append(i)
    return len(thuong+hoa) 

s = "Hello World"
print("các ký tự và chữ cái tiếng Anh kể cả chữ hoa, thường trong xâu là:",xau(s))