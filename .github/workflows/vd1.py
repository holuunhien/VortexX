# Viết chương trình nhập hai số tự nhiên từ bàn phím, cách nhau bởi dấu cách và đưa ra kết quả UCLN của hai số này.
s = input("nhập 2 số tự nhiên bất kì: ")
A = s.split(" ")
a = int(A[0])
b = int(A[1])
r = a % b
while r != 0:
    a = b
    b = r
    r = a % b
print("ƯCLN của a và b là: ",b)