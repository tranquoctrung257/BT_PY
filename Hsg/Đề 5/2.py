# Câu 2: Viết một hàm số thay thế cho phương thức sort() của dãy list. Tham số đầu vào là dãy A bao gồm các phần tử là số (nguyên hay thực). Hàm trả lại là một dãy bao gồm các số đã được sắp xếp theo thứ tự tăng dần các phần tử từ A.

def bubble_sort(arr):
    n = len(arr)
    # Lặp qua từng phần tử của danh sách
    for i in range(n):
        # Lặp qua các phần tử còn lại của danh sách
        for j in range(0, n-i-1):
            # So sánh hai phần tử liền kề và đổi chỗ nếu cần thiết
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
 
# Sử dụng thử hàm bubble_sort
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Danh sách đã được sắp xếp:",arr)
