# Viết chương trình nhập họ tên đầy đủ của người dùng, sau đó in thông báo tên và họ đệm của người đó.
s=input("Nhập họ tên: ")
A=s.split(" ")
print("Tên: ", A[len(A)-1])
print("Tên đệm: ", A[len(A)-2])