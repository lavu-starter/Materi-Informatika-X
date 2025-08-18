# ========================================
# Struktur Data Dasar di Python
# ========================================

print("=== Belajar Struktur Data Dasar ===")

# ----------------------------------------
# List
buah = ["apel", "jeruk", "mangga"]
print("\nList buah awal:", buah)

# Mengakses data
print("Buah pertama:", buah[0])

# Menambah data
buah.append("pisang")
print("List setelah ditambah:", buah)

# ----------------------------------------
# Tuple
warna = ("merah", "hijau", "biru")
print("\nTuple warna:", warna)

# Mengakses data
print("Warna kedua:", warna[1])

# Cek jika mencoba mengubah tuple
try:
    warna[0] = "kuning"
except TypeError as e:
    print("Error:", e)

# ----------------------------------------
# Dictionary
siswa = {
    "nama": "Budi",
    "umur": 16,
    "kelas": "XI"
}
print("\nDictionary siswa:", siswa)

# Mengakses value
print("Nama siswa:", siswa["nama"])

# Menambah key baru
siswa["hobi"] = "membaca"
print("Dictionary setelah ditambah hobi:", siswa)

# ----------------------------------------
# Latihan Logika
print("\n=== Latihan ===")

# 1. List nama teman
teman = ["Ani", "Budi", "Citra", "Dedi", "Eka"]
print("Nama teman ke-3:", teman[2])

# 2. Tuple hobi
hobi = ("membaca", "berenang", "bermain musik")
print("Hobi tuple:", hobi)
# hobi[0] = "lari"  # ❌ akan error

# 3. Dictionary buku
buku = {
    "judul": "Python untuk Pemula",
    "penulis": "Rina",
    "tahun": 2025
}
print("Data buku:", buku)
