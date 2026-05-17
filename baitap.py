import math

# 1. Hàm tính giai thừa
def tinh_giai_thua(n):
    return math.factorial(n)

# 2. Hàm tính giá trị trung bình của dãy số
def tinh_trung_binh(danh_sach):
    if len(danh_sach) == 0: 
        return 0
    return sum(danh_sach) / len(danh_sach)

# 3. Hàm tính lợi nhuận sau 12 tháng (gốc + tỷ lệ lãi suất năm)
def tinh_loi_nhuan(goc, lai_suat_nam):
    lai_suat_thang = lai_suat_nam / 12 / 100
    tong_tien = goc * ((1 + lai_suat_thang) ** 12)
    loi_nhuan = tong_tien - goc
    return loi_nhuan

# --- CHẠY THỬ NGHIỆM CÁC HÀM ---
if __name__ == "__main__":
    print("================ KẾT QUẢ BÀI TẬP PYTHON ================")
    
    # Thử nghiệm hàm 1
    n = 5
    print(f"1. Giai thừa của {n} là: {tinh_giai_thua(n)}")
    
    # Thử nghiệm hàm 2
    day_so = [10, 20, 30, 40, 50]
    print(f"2. Giá trị trung bình của dãy số {day_so} là: {tinh_trung_binh(day_so)}")
    
    # Thử nghiệm hàm 3 (Ví dụ: Gốc 20 triệu, lãi suất 6.5% một năm)
    tien_goc = 20000000
    lai_nam = 6.5
    loi_nhuan_12_thang = tinh_loi_nhuan(tien_goc, lai_nam)
    print(f"3. Lợi nhuận sau 12 tháng (Gốc: {tien_goc:,.0f}đ, Lãi: {lai_nam}%/năm) là: {loi_nhuan_12_thang:,.0f} VNĐ")
    print("========================================================")