#Sử dụng hàm prime, em hãy viết chương trình in ra các số nguyên tố trong khoảng từ m đến n với m, n là hai số tự nhiên và 1< m< n
def prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True
m = int(input("Nhập m: "))
n = int(input("Nhập n: "))
print("Các số nguyên tố trong khoảng từ", m, "đến", n, "là:")
for i in range(m, n + 1):
    if prime(i):
        print(i, end=" ")