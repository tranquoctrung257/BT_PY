# Câu 1: Viết các hàm số với đầu vào là dãy A (bao gồm số và xây ký tự)
# a) Tính tổng các phần tử trong dãy A
# b) Đếm số các phần tử là xây kỹ tự từ dãy A
# c) Đưa ra kết quả là 2 dãy B,C. Dãy B bao gồm các phần tử là số của A, dãy C bao gồm các phần tử là xâu ký tự của A
# * Gợi ý: Thiết lập một số hàm



def tong_A():
    # global A
    tong = []
    for i in A: 
        if type(i) in (int,float):
            tong.append(i)
    return sum(tong)

def xaukitu():
    xau = []
    for i in A:
        if isinstance(i,(str)):
            xau.append(i)
    return len(xau)
def C1():
    global B
    for i in A: 
        if type(i) in (int,float):
            B.append(i)
    for i in A:
        if isinstance(i,(str)):
            c.append(i)
    
if __name__ == "__main__":

    A = [1,2,3,4,"str","string"]
    B = []
    c = []

    # tong_A()
    print(tong_A())
    print(xaukitu())
    C1()
    print(B)
    print(c)