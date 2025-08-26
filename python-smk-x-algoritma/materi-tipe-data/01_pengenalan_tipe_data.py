# ========================================
# Pengenalan Tipe Data di Python
# ========================================

# Integer (int) → bilangan bulat
umur = 17
tahun = 2025
print("Umur:", umur, "| Tipe:", type(umur))
print("Tahun:", tahun, "| Tipe:", type(tahun))
print("-" * 40)

# Data diri
nama = "Khoirur Rozaq"
alamat = "Jl. Contoh No. 123, Jakarta"
umur = 17
tahun = 2025

# Menampilkan data dengan format rapi
print("-" * 50)
print(f"{'DATA DIRI':^50}")  # Judul tengah
print("-" * 50)
print(f"{'Nama':<10}: {nama:<30} | Tipe: {type(nama).__name__}")
print(f"{'Alamat':<10}: {alamat:<30} | Tipe: {type(alamat).__name__}")
print(f"{'Umur':<10}: {umur:<30} | Tipe: {type(umur).__name__}")
print(f"{'Tahun':<10}: {tahun:<30} | Tipe: {type(tahun).__name__}")
print("-" * 50)

# Data diri
nama = "Khoirur Rozaq"
alamat = "Jl. Contoh No. 123, Jakarta"
umur = 17
tahun = 2025

# Membuat tabel
print("+" + "-"*15 + "+" + "-"*35 + "+" + "-"*10 + "+")
print(f"| {'Field':^13} | {'Nilai':^33} | {'Tipe':^8} |")
print("+" + "-"*15 + "+" + "-"*35 + "+" + "-"*10 + "+")

print(f"| {'Nama':<13} | {nama:<33} | {type(nama).__name__:^8} |")
print(f"| {'Alamat':<13} | {alamat:<33} | {type(alamat).__name__:^8} |")
print(f"| {'Umur':<13} | {umur:<33} | {type(umur).__name__:^8} |")
print(f"| {'Tahun':<13} | {tahun:<33} | {type(tahun).__name__:^8} |")

print("+" + "-"*15 + "+" + "-"*35 + "+" + "-"*10 + "+")


# Float (float) → bilangan pecahan/desimal
suhu = 36.5
pi = 3.14
print("Suhu:", suhu, "| Tipe:", type(suhu))
print("Nilai PI:", pi, "| Tipe:", type(pi))
print("-" * 40)

# String (str) → teks/kalimat
nama = "Rina"
pesan = "Halo Dunia!"
print("Nama:", nama, "| Tipe:", type(nama))
print("Pesan:", pesan, "| Tipe:", type(pesan))
print("-" * 40)

# Boolean (bool) → logika True/False
is_student = True
punya_motor = False
print("Apakah siswa?:", is_student, "| Tipe:", type(is_student))
print("Punya motor?:", punya_motor, "| Tipe:", type(punya_motor))
print("-" * 40)

# ========================================
# Latihan Logika
# ========================================
print("Tebak tipe data berikut:")

data1 = "123"
data2 = 123
data3 = True
data4 = 3.14
data5 = "False"

print(data1, "=>", type(data1))
print(data2, "=>", type(data2))
print(data3, "=>", type(data3))
print(data4, "=>", type(data4))
print(data5, "=>", type(data5))

# ========================================
# Kesimpulan
# int  → angka bulat
# float → angka desimal
# str  → teks
# bool → logika True/False
# ========================================

