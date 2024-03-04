# Câu 9: Cho trước 2 dãy A,B có số phần tử bằng nhau và đều là các số tự nhiên. Viết chương trình tạo dãy C cũng có số phần tử bằng A, B và các phần tử của C là ước số chung lớn nhất của các phần tử tương ứng của A,B.

def gcd(a,b):
    # print(a,b)
    while b != 0:
        # đổi a,b => b,a % b
        a,b = b,a % b
        # print(a,b)
    return(a)
def main():
    if len(a) == len(b):
        for i in range(len(a)):
            c.append(gcd(a[i],b[i]))
    else: return None
if __name__ == "__main__":
    a = [1,2,4,5,65,6,7,3]
    b = [23,5,4,34,5,3,5,6]
    c = []
    main()
    print(c)