# Câu 11: Cho trước 2 xâu hoặc nhập từ bàn phím xâu s1 và s2. Hãy tìm ra xâu con chung có độ dài lớn nhất của 2 xâu trên.

def longest_common_substring(s1, s2):
    m = len(s1)
    n = len(s2)
    
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    max_length = 0

    end_index = 0
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end_index = i
            else:
                dp[i][j] = 0
    

    longest_substring = s1[end_index - max_length: end_index]
    return longest_substring


s1 = input("Nhập xâu thứ nhất: ")
s2 = input("Nhập xâu thứ hai: ")


result = longest_common_substring(s1, s2)
if result:
    print("Xâu con chung lớn nhất là:", result)
else:
    print("Không có xâu con chung.")
