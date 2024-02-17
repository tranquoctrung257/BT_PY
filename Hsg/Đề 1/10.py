# Câu 10: Viết chương trình nhập số tự nhiên n từ bàn phím và in ra tất cả các số hoàn hảo <n.

def tonguoc(num):
    o = 0
    for i in range(1,num):
        if num % i == 0:
            o+=i
    return o
def tong_so_hoan_hao(n):
    count = []
    for i in range(2,n):
        result = tonguoc(i)
        if i == result:
            count.append(i)
    return count

def main():
    n = int(input("Nhập số tự nhiên n: "))
    print(f"Tất cả các số hoàn hảo < {n} là:",*tong_so_hoan_hao(n))


main()