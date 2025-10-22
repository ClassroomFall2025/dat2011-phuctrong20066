class NhanVien:
    def __init__(self, ma_nv, ten_nv, thu_nhap):

        self.ma_nv = ma_nv
        self.ten_nv = ten_nv
        self.thu_nhap = float(thu_nhap)

    def xuat(self):
        print(f"{self.ma_nv:10} | {self.ten_nv:25} | {self.thu_nhap:10.2f}")

FILE_NAME = r"H:\Python\ASM.txt"
def ghi_file(ds_nv):
    try:
        f = open(FILE_NAME, "w", encoding="utf-8")
        for nv in ds_nv:
            dong = nv.ma_nv + "," + nv.ten_nv + "," + str(nv.thu_nhap) + "\n"
            f.write(dong)
        f.close()
        print(f">>> Đã lưu danh sách nhân viên vào file {FILE_NAME}")
    except Exception as e:
        print(">>> Lỗi khi ghi file:", e)
def doc_file():
    ds_nv = []
    try:
        f = open(FILE_NAME, "r", encoding="utf-8")
        for dong in f:
            du_lieu = dong.strip().split(",")
            if len(du_lieu) == 3:
                ma = du_lieu[0]
                ten = du_lieu[1]
                thu_nhap = float(du_lieu[2])
                nv = NhanVien(ma, ten, thu_nhap)
                ds_nv.append(nv)
        f.close()
    except FileNotFoundError:
        print(">>> File chưa tồn tại. Hãy nhập danh sách trước.")
    except Exception as e:
        print(">>> Lỗi khi đọc file:", e)
    return ds_nv
def cn1():
    ds_nv = []
    while True:
        print("\n--- Nhập thông tin nhân viên ---")
        ma = input("Nhập mã nhân viên: ")
        ten = input("Nhập họ tên nhân viên: ")
        thu_nhap = input("Nhập thu nhập: ")

        nv = NhanVien(ma, ten, thu_nhap)
        ds_nv.append(nv)

        tiep = input("Nhập thêm nhân viên khác (y/n)? ").lower()
        if tiep != "y":
            break

    ghi_file(ds_nv)
def cn2():
    ds_nv = doc_file()
    if len(ds_nv) == 0:
        return
    print("\n=== DANH SÁCH NHÂN VIÊN ===")
    print(f"{'MÃ NV':10} | {'HỌ TÊN':25} | {'THU NHẬP':10}")
    print("-" * 50)
    for nv in ds_nv:
        nv.xuat()
def cn3():
    ds_nv = doc_file()
    if len(ds_nv) == 0:
        return
    ma_can_tim = input("Nhập mã nhân viên cần tìm: ")
    tim_thay = False
    for nv in ds_nv:
        if nv.ma_nv == ma_can_tim:
            print("\n>>> Thông tin nhân viên cần tìm:")
            print(f"{'MÃ NV':10} | {'HỌ TÊN':25} | {'THU NHẬP':10}")
            print("-" * 50)
            nv.xuat()
            tim_thay = True
    if not tim_thay:
        print(">>> Không tìm thấy nhân viên có mã này.")
def cn4():
    ds_nv = doc_file()
    if len(ds_nv) == 0:
        return
    ma = input("Nhập mã nhân viên cần xóa: ")
    tim_thay = False
    for nv in ds_nv:
        if nv.ma_nv == ma:
            ds_nv.remove(nv)
            tim_thay = True
            break
    if tim_thay:
        ghi_file(ds_nv)
        print(">>> Đã xóa nhân viên thành công.")
    else:
        print(">>> Không tìm thấy nhân viên cần xóa.")
def cn5():
    ds_nv = doc_file()
    if len(ds_nv) == 0:
        return
    ma = input("Nhập mã nhân viên cần cập nhật: ")
    tim_thay = False
    for nv in ds_nv:
        if nv.ma_nv == ma:
            print(">>> Thông tin cũ:")
            nv.xuat()
            ten_moi = input("Nhập tên mới (Enter để bỏ qua): ")
            if ten_moi != "":
                nv.ten_nv = ten_moi
            thu_nhap_moi = input("Nhập thu nhập mới (Enter để bỏ qua): ")
            if thu_nhap_moi != "":
                nv.thu_nhap = float(thu_nhap_moi)
            tim_thay = True
            break
    if tim_thay:
        ghi_file(ds_nv)
        print(">>> Đã cập nhật thông tin nhân viên.")
    else:
        print(">>> Không tìm thấy mã nhân viên.")
def cn6():
    ds_nv = doc_file()
    if len(ds_nv) == 0:
        return
    luong_min = float(input("Nhập lương tối thiểu: "))
    luong_max = float(input("Nhập lương tối đa: "))

    print("\n=== NHÂN VIÊN TRONG KHOẢNG LƯƠNG ===")
    co_nv = False
    for nv in ds_nv:
        if luong_min <= nv.thu_nhap <= luong_max:
            nv.xuat()
            co_nv = True
    if not co_nv:
        print(">>> Không có nhân viên nào trong khoảng này.")
def cn7():
    ds_nv = doc_file()
    if len(ds_nv) == 0:
        return
    n = len(ds_nv)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if ds_nv[j].ten_nv > ds_nv[j + 1].ten_nv:
                tam = ds_nv[j]
                ds_nv[j] = ds_nv[j + 1]
                ds_nv[j + 1] = tam
    print("\n=== DANH SÁCH THEO HỌ TÊN (A->Z) ===")
    for nv in ds_nv:
        nv.xuat()
def cn8():
    ds_nv = doc_file()
    if len(ds_nv) == 0:
        return
    n = len(ds_nv)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if ds_nv[j].thu_nhap < ds_nv[j + 1].thu_nhap:
                tam = ds_nv[j]
                ds_nv[j] = ds_nv[j + 1]
                ds_nv[j + 1] = tam
    print("\n=== DANH SÁCH THEO THU NHẬP (GIẢM DẦN) ===")
    for nv in ds_nv:
        nv.xuat()
def cn9():
    ds_nv = doc_file()
    if len(ds_nv) == 0:
        return
    n = len(ds_nv)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if ds_nv[j].thu_nhap < ds_nv[j + 1].thu_nhap:
                tam = ds_nv[j]
                ds_nv[j] = ds_nv[j + 1]
                ds_nv[j + 1] = tam

    print("\n=== 5 NHÂN VIÊN CÓ THU NHẬP CAO NHẤT ===")
    dem = 0
    for nv in ds_nv:
        nv.xuat()
        dem += 1
        if dem == 5:
            break
