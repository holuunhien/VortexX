# Viết chương trình nhập vào sĩ số của một lớp và cho biết bạn có bao nhiêu người bạn trong lớp đó.
# Nếu sĩ số lớp lớn hơn 40 thì bạn sẽ có 40 người bạn, nếu sĩ số lớp nhỏ hơn hoặc bằng 40 thì bạn sẽ có số người bạn bằng với sĩ số lớp trừ đi 1 (bạn không thể là bạn của chính mình).
# Ví dụ: Nếu sĩ số lớp là 45 thì bạn sẽ có 40 người bạn, nếu sĩ số lớp là 30 thì bạn sẽ có 29 người bạn.
# Nhập vào sĩ số lớp
n =int(input("nhap si so cua lop bạn: "))
print("ban co", n-1, "nguoi ban trong lop")