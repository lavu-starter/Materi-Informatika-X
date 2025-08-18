# Latihan Dictionary
# Membuat dictionary siswa
siswa = {
    "nama": "Budi",
    "umur": 16,
    "nilai": 85
}

# Menambahkan data baru
siswa["kelas"] = "X"

# Menampilkan seluruh data siswa
print("Data siswa:", siswa)

# Menghapus data
del siswa["umur"]
print("Setelah dihapus umur:", siswa)

# Iterasi dictionary
for key, value in siswa.items():
    print(f"{key}: {value}")
