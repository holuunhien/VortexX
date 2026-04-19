def tinh_tong(s):
    tong = 0
    for x in s:
        if '0' <= x <= '9':
            tong = tong + int(x)
    return tong
#chuong trinh chinh
xau = input("nhap 1 xau ki tu: ")
print("tong cac ki tu la chu so trong xau la:",tinh_tong(xau))