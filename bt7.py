#Viết chương trình Python cho phép nhập vào 3 số thực là điểm số của 3 môn thi. In ra man hinh "qua mon" neu diem trung binh >=5.0 nguoi lai in ra "ko qua mon".diem trung binh 4 chu so thap phan
mons1,mons2,mons3 = map(float,input("nhap diem so 3 mon: ").split())
diemtrungbinh = (mons1 + mons2 + mons3) / 3
print("diem trung binh cua 3 mon la:",diemtrungbinh)
if diemtrungbinh >= 5.0:
    print("qua mon")
else:
    print("khong qua mon")