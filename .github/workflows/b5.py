def uoc_chung_lon_nhat(m,n):
    while m != n:
        if m > n:
            m = m - n
        else:
            n = n - m
    return m
#chuong trinh trinh
nhap = input("nhap 2 so cach nhau boi dau cach: ")
s1,s2 = nhap.split()
a = int(s1)
b = int(s2)
print("uoc chung lon nhat cua 2 so nay la:", uoc_chung_lon_nhat(a,b))