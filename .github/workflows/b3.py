def so_chia_het_cho_5(n):
    dem = 0
    for i in range (n):
        if i % 5 == 0:
            dem = dem + 1
    return dem
n = int(input("nhap so tu nhien n: "))
print("so nho hon n chia het cho 5:", so_chia_het_cho_5(n))