def prime(n):
    c = 0
    k = 1
    while k < n:
        if n % k == 0:
            c = c + 1
        k = k + 1
    if c == 1:
        return True
    else:
        return False
n = int(input("nhập số tự nhiên n: "))
for i in range(1, n+1):
    if n % i == 0 and prime(i) == True:
        print(i, end = " ")
