# ========================================
# Fungsi (Function) di Python
# ========================================

print("=== Belajar Fungsi ===")

# ----------------------------------------
# Fungsi sederhana
def sapa_dunia():
    print("Halo, dunia!")

sapa_dunia()
print("-" * 40)

# ----------------------------------------
# Fungsi dengan parameter
def sapa(nama):
    print("Halo,", nama)

sapa("Budi")
sapa("Ani")
print("-" * 40)

# ----------------------------------------
# Fungsi dengan nilai kembalian (return)
def kali(a, b):
    return a * b

hasil = kali(5, 3)
print("Hasil perkalian 5 x 3 =", hasil)
print("-" * 40)

# ----------------------------------------
# Latihan Logika 1: Luas persegi
def luas_persegi(sisi):
    return sisi * sisi

print("Luas persegi sisi 4 =", luas_persegi(4))
print("-" * 40)

# ----------------------------------------
# Latihan Logika 2: Cek genap / ganjil
def cek_genap(angka):
    if angka % 2 == 0:
        return True
    else:
        return False

print("Apakah 10 genap?", cek_genap(10))
print("Apakah 7 genap?", cek_genap(7))
print("-" * 40)

# ----------------------------------------
# Latihan Logika 3: Fungsi salam
def salam(nama):
    print("Selamat pagi,", nama)

salam("Rina")
salam("Budi")
