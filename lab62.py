class SinhVienPoly:
    def __init__(self, ho_ten, nganh, diem):
        self.ho_ten = ho_ten
        self.nganh = nganh
        self.diem = diem

    def get_diem(self):
        return self.diem

    def get_hoc_luc(self):
        diem = self.get_diem()
        if diem < 5:
            return "Yếu"
        elif diem < 7:
            return "Trung bình"
        elif diem < 8:
            return "Khá"
        elif diem < 9:
            return "Giỏi"
        else:
            return "Xuất sắc"

    def xuat(self):
        print(f"Họ và tên: {self.ho_ten}")
        print(f"Ngành: {self.nganh}")
        print(f"Điểm: {self.get_diem()}")
        print(f"Học lực: {self.get_hoc_luc()}")

