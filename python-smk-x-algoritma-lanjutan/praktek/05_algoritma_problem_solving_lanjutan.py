# Program Total Belanja dengan Diskon
harga = float(input("Masukkan total harga: "))
diskon = float(input("Masukkan diskon (%): "))
total = harga - (harga * diskon / 100)
print("Total harga setelah diskon:", total)

# Program Penentuan Grade Siswa
nilai = float(input("Masukkan nilai siswa: "))

if nilai >= 85:
    grade = "A"
elif nilai >= 70:
    grade = "B"
elif nilai >= 60:
    grade = "C"
elif nilai >= 50:
    grade = "D"
else:
    grade = "E"

print("Grade siswa:", grade)
