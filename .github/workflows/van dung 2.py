s = input("nhap ho ten: ")
c = int(input("nhap so c: "))
def change(s, c):
    if c == 0:
        return s.upper()
    if c != 0:
        return s.lower()
print(change(s, c))