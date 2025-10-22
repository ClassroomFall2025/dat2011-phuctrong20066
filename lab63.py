from lab62 import SinhVienPoly

class SinhVienIT(SinhVienPoly):
    def __init__(self, ho_ten, java, html, css):
        super().__init__(ho_ten, "Công nghệ thông tin", 0)
        self.java = java
        self.html = html
        self.css = css

    def get_diem(self):
        return round((2 * self.java + self.html + self.css) / 4, 2)


class SinhVienBiz(SinhVienPoly):
    def __init__(self, ho_ten, marketing, sales):
        super().__init__(ho_ten, "Kinh doanh", 0)
        self.marketing = marketing
        self.sales = sales

    def get_diem(self):
        return round((2 * self.marketing + self.sales) / 3, 2)
