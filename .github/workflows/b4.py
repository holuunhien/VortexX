def tinh_hieu(a,b):
    return a - b
nhap = input("nhap 2 so cach nhau boi dau phay: ")
s1,s2 = nhap.split(',')
so1 = int(s1)
so2 = int(s2)
print("hieu cua 2 so nay:", tinh_hieu(so1,so2))