# ========================================
# Masukan (Input) dan Keluaran (Output)
# ========================================

# Contoh output sederhana
print("=== Belajar Masukan dan Keluaran ===")
print("Halo, selamat datang di Python!")
print("-" * 40)

# ----------------------------------------
# Input string
nama = input("Masukkan nama kamu: ")
print("Halo,", nama, "! Senang bertemu denganmu.")
print("-" * 40)

# ----------------------------------------
# Input angka (perlu konversi)
umur = int(input("Masukkan umur kamu: "))
print("Umur kamu sekarang:", umur)
print("Tahun depan umurmu:", umur + 1)
print("-" * 40)

# ----------------------------------------
# Input dua angka untuk operasi matematika
angka1 = int(input("Masukkan angka pertama: "))
angka2 = int(input("Masukkan angka kedua: "))

print("Hasil penjumlahan:", angka1 + angka2)
print("Hasil pengurangan:", angka1 - angka2)
print("Hasil perkalian :", angka1 * angka2)
print("Hasil pembagian :", angka1 / angka2)
print("-" * 40)

# ----------------------------------------
# Latihan logika
print("=== Latihan Logika ===")

# Berapa tahun lagi menuju umur 20
umur_kamu = int(input("Masukkan umur kamu: "))
sisa = 20 - umur_kamu
print("Tinggal", sisa, "tahun lagi kamu berusia 20.")

# Apa yang terjadi kalau tidak dikonversi ke int?
angka_str1 = input("Masukkan angka (tanpa int): ")
angka_str2 = input("Masukkan angka lagi (tanpa int): ")
print("Hasil penjumlahan tanpa int:", angka_str1 + angka_str2)
# Catatan: hasilnya akan digabung sebagai string, bukan dijumlahkan
