class ChuNhat:
    def __init__(self, chieu_dai, chieu_rong):
        self.__chieu_dai = chieu_dai
        self.__chieu_rong = chieu_rong

    def tinh_chu_vi(self):
        return (self.__chieu_dai + self.__chieu_rong) * 2

    def tinh_dien_tich(self):
        return self.__chieu_dai * self.__chieu_rong

    def hien_thi_thong_tin(self):
        print(f"Chiều dài: {self.__chieu_dai}")
        print(f"Chiều rộng: {self.__chieu_rong}")
        print(f"Chu vi: {self.tinh_chu_vi()}")
        print(f"Diện tích: {self.tinh_dien_tich()}")

    def xuat(self):
        self.hien_thi_thong_tin()


class HinhVuong(ChuNhat):
    def __init__(self, canh):
        self.canh = canh
        super().__init__(self.canh, self.canh)

    def hien_thi_thong_tin(self):
        print(f"Hình vuông - Cạnh: {self.canh}")
        print(f"Chu vi: {self.tinh_chu_vi()}")
        print(f"Diện tích: {self.tinh_dien_tich()}")

    def xuat(self):
        self.hien_thi_thong_tin()