#Viết chương trình nhập nhiều số (số nguyên hoặc số thực) từ bàn phím, các số cách nhau bởi dấu cách. Sau đó in ra màn hình tổng các số đã nhập.
s = input("nhập dãy các số cách nhau bởi dấu cách:")
A = s.split()
n = []
for x in A:
    n.append(float(x))
S = 0
for i in n:
    S = S + i
print(S)