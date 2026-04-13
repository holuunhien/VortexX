# Thiết lập hàm power(a,b,c) với a, b, c là số nguyên. Hàm trả lại giá trị (a+b)c
a = int(input("nhap a: "))
b = int(input("nhap b: "))
c = int(input("nhap c: "))
def power(a, b, c):
    return (a + b) ** c
print(power(a, b, c))
