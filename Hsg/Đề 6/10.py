# Câu 10: Xâu ký tự có độ dài n được gọi là xâu đối xứng nếu s[k]=s[n-k-1] với k=0,1,2….,n-1. Viết hàm số isSymmetry(s) kiểm tra xem xâu s có phải là xâu đối xứng hay không


def isSymmetry(n):
    n = int(n)
    rev = 0
    temp = n
    while n  != 0:
        rev = rev * 10 + n % 10
        n //=10
    return rev == temp
if __name__ == "__main__":
    xau = "12321"
    if isSymmetry(xau):
        print(f"{xau} là xâu đối xứng")
    else:print(f"{xau} không phải là xâu đối xứng")