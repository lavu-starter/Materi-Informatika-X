# ========================================
# Studi Kasus Mini: Penilaian Siswa
# ========================================

print("=== Program Penilaian Siswa ===")

# ----------------------------------------
# Fungsi untuk menghitung rata-rata
def hitung_rata(nilai_list):
    return sum(nilai_list) / len(nilai_list)

# Fungsi untuk menentukan kategori
def kategori_nilai(rata):
    if rata >= 90:
        return "A"
    elif rata >= 75:
        return "B"
    elif rata >= 60:
        return "C"
    else:
        return "D"

# ----------------------------------------
# Input data siswa
nama = input("Masukkan nama siswa: ")
jumlah_mapel = int(input("Masukkan jumlah mata pelajaran: "))

# ----------------------------------------
# Input nilai
nilai_list = []
for i in range(1, jumlah_mapel + 1):
    nilai = float(input(f"Masukkan nilai mata pelajaran ke-{i}: "))
    nilai_list.append(nilai)

# ----------------------------------------
# Hitung rata-rata
rata = hitung_rata(nilai_list)
kat = kategori_nilai(rata)

# Cari nilai tertinggi dan terendah
nilai_tertinggi = max(nilai_list)
nilai_terendah = min(nilai_list)

# ----------------------------------------
# Menampilkan laporan akhir
print("\n=== Laporan Siswa ===")
print("Nama Siswa      :", nama)
print("Nilai Semua Mapel:", nilai_list)
print("Nilai Tertinggi :", nilai_tertinggi)
print("Nilai Terendah  :", nilai_terendah)
print("Rata-rata       :", rata)
print("Kategori Nilai  :", kat)
print("-" * 40)
