# Latihan Fungsi Lanjutan

# Fungsi menghitung rata-rata
def rata_rata(nilai_list):
    return sum(nilai_list) / len(nilai_list)

# Fungsi menampilkan nilai lebih dari batas
def nilai_lebih_dari(nilai_list, batas=75):
    return [x for x in nilai_list if x > batas]

# Data nilai siswa
nilai = [70, 85, 90, 60]

print("Rata-rata nilai:", rata_rata(nilai))
print("Nilai lebih dari 75:", nilai_lebih_dari(nilai))
