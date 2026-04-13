# Viết chương trình thực hiện: Nhập hai số tự nhiên từ bàn phím, hai số cách nhau bởi dấu cách. Tính và in ra tổng của các số này.
a, b = map(int, input("Nhập hai số tự nhiên cách nhau bởi dấu cách: ").split(" "))
tong = a + b
print("Tổng của hai số là:", tong)