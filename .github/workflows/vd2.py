#  Viết chương trình nhập số tự nhiên n rồi nhập n họ tên học sinh. Sau đó yêu cầu nhập một tên và thông báo số bạn có cùng tên trong lớp.
n = int(input("Nhập số tự nhiên n: "))
A = []
t = 0
for i in range(0,n):
    A.append(input("nhập họ tên: "))
s = input("nhập 1 tên: ")
for i in range(0,n):
    B = A[i].split()
    if s == B[len(B)-1]:
        t = t + 1
print("vậy số người cùng tên là: ",t)