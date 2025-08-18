# ========================================
# Logika Percabangan (if, elif, else)
# ========================================

print("=== Belajar Percabangan ===")

# ----------------------------------------
# If sederhana
umur = int(input("Masukkan umur kamu: "))
if umur >= 17:
    print("Kamu sudah cukup umur untuk membuat KTP.")
print("-" * 40)

# ----------------------------------------
# If - Else
umur = int(input("Masukkan umur kamu: "))
if umur >= 17:
    print("Boleh membuat KTP.")
else:
    print("Belum boleh membuat KTP.")
print("-" * 40)

# ----------------------------------------
# If - Elif - Else (Nilai Ujian)
nilai = int(input("Masukkan nilai ujian: "))

if nilai >= 90:
    print("Nilai kamu A")
elif nilai >= 75:
    print("Nilai kamu B")
elif nilai >= 60:
    print("Nilai kamu C")
else:
    print("Nilai kamu D")
print("-" * 40)

# ----------------------------------------
# Latihan Logika 1: Ganjil / Genap
angka = int(input("Masukkan sebuah angka: "))
if angka % 2 == 0:
    print("Angka genap")
else:
    print("Angka ganjil")
print("-" * 40)

# ----------------------------------------
# Latihan Logika 2: Kategori Umur
usia = int(input("Masukkan usia kamu: "))
if usia < 13:
    print("Kategori: Anak-anak")
elif usia <= 17:
    print("Kategori: Remaja")
else:
    print("Kategori: Dewasa")
print("-" * 40)

# ----------------------------------------
# Latihan Logika 3: Password
password = input("Masukkan password: ")
if password == "python123":
    print("Akses diterima ✅")
else:
    print("Akses ditolak ❌")
print("-" * 40)
