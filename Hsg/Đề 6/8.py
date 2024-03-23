# Câu 8: Cho trước xâu hoặc nhập từ bàn phím xâu s. Hãy dồn các số là chữ số về bên trái (giữ nguyên thứ tự) và in kết quả ra màn hình.

def chuoi(s):
    temp = []
    temp1 = []
    for i in s:
        try:
            temp.append(int(i))
        except:
            temp1.append(i)
        # if isinstance(i,int):
        #     print(i)
            # s.remove(i)
    print(temp)
    print(*temp1)



if __name__ == "__main__":
    s = "xin2 3chào423"
    chuoi(s)
