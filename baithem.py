import csv
import os
from datetime import datetime

FILE_CSV = "taikhoan.csv"
BACKUP_DIR = "backup"

class TaiKhoan:
    def __init__(self, soTaiKhoan, ten, loai, soDu):
        self.soTaiKhoan = soTaiKhoan
        self.ten = ten
        self.loai = loai.upper()
        self.soDu = float(soDu)

    def hienThiTaiKhoan(self):
        loai_text = "Tiết kiệm" if self.loai == "T" else "Cá nhân"
        print(f"{self.soTaiKhoan:<10} | {self.ten:<20} | {loai_text:<10} | {self.soDu:,.0f} VNĐ")

    def guiTien(self, soTien):
        self.soDu += soTien

    def rutTien(self, soTien):
        if soTien > self.soDu:
            print("❌ Số dư không đủ!")
            return False
        self.soDu -= soTien
        return True

    def toDict(self):
        return {
            "soTaiKhoan": self.soTaiKhoan,
            "ten": self.ten,
            "loai": self.loai,
            "soDu": self.soDu
        }

# ================= FILE CSV =================

def docTaiKhoanTuCSV():
    ds = []
    if not os.path.exists(FILE_CSV):
        return ds
    with open(FILE_CSV, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            ds.append(TaiKhoan(row["soTaiKhoan"], row["ten"], row["loai"], row["soDu"]))
    return ds

def ghiTaiKhoanVaoCSV(ds):
    with open(FILE_CSV, "w", newline="", encoding="utf-8") as f:
        fieldnames = ["soTaiKhoan", "ten", "loai", "soDu"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for tk in ds:
            writer.writerow(tk.toDict())

# ================= CHỨC NĂNG =================

def tao_tai_khoan(ds):
    print("\n=== TẠO TÀI KHOẢN MỚI ===")
    so_tk = input("Nhập số tài khoản: ").strip()
    for tk in ds:
        if tk.soTaiKhoan == so_tk:
            print("❌ Số tài khoản đã tồn tại!")
            return
    ten = input("Nhập tên chủ tài khoản: ").strip()
    loai = input("Loại tài khoản (T: Tiết kiệm / C: Cá nhân): ").upper()
    so_du = float(input("Nhập số dư ban đầu: "))

    if loai == "T" and so_du < 500000:
        print("❌ Tài khoản tiết kiệm phải >= 500,000 VNĐ!")
        return
    elif loai == "C" and so_du < 1000000:
        print("❌ Tài khoản cá nhân phải >= 1,000,000 VNĐ!")
        return

    tk_moi = TaiKhoan(so_tk, ten, loai, so_du)
    ds.append(tk_moi)
    ghiTaiKhoanVaoCSV(ds)
    print("✅ Tạo tài khoản thành công!")

def gui_tien(ds):
    so_tk = input("Nhập số tài khoản: ")
    so_tien = float(input("Nhập số tiền gửi: "))
    for tk in ds:
        if tk.soTaiKhoan == so_tk:
            tk.guiTien(so_tien)
            ghiTaiKhoanVaoCSV(ds)
            print("✅ Gửi tiền thành công!")
            return
    print("❌ Không tìm thấy tài khoản!")

def rut_tien(ds):
    so_tk = input("Nhập số tài khoản: ")
    so_tien = float(input("Nhập số tiền rút: "))
    for tk in ds:
        if tk.soTaiKhoan == so_tk:
            if tk.rutTien(so_tien):
                ghiTaiKhoanVaoCSV(ds)
                print("✅ Rút tiền thành công!")
            return
    print("❌ Không tìm thấy tài khoản!")

def xem_tat_ca(ds):
    print("\n=== DANH SÁCH TẤT CẢ TÀI KHOẢN ===")
    print(f"{'Số TK':<10} | {'Tên':<20} | {'Loại':<10} | {'Số dư':>15}")
    print("-"*60)
    for tk in ds:
        tk.hienThiTaiKhoan()

def sao_luu_du_lieu():
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)
    filename = f"{BACKUP_DIR}/backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    with open(FILE_CSV, "r", encoding="utf-8") as src, open(filename, "w", encoding="utf-8") as dst:
        dst.write(src.read())
    print(f"✅ Đã sao lưu dữ liệu vào {filename}")

