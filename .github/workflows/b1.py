def dem_so(s):
    dem = 0
    for x in s:
        if '0' <= x <= '9':
            dem = dem + 1
    return dem
#chuong trinh chinh
xau = input("nhap xau ki tu: ")
print("ki tu la chu so la:", dem_so(xau))