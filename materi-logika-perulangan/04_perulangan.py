# ========================================
# Perulangan (Looping) di Python
# ========================================

print("=== Belajar Perulangan ===")

# ----------------------------------------
# Perulangan for dengan range
print("\nPerulangan for (1 sampai 5):")
for i in range(1, 6):
    print("Angka:", i)

# ----------------------------------------
# Perulangan while dengan kondisi
print("\nPerulangan while (1 sampai 5):")
angka = 1
while angka <= 5:
    print("Angka:", angka)
    angka += 1

# ----------------------------------------
# For untuk mencetak string per huruf
print("\nPerulangan huruf dalam string:")
for huruf in "PYTHON":
    print(huruf)

# ----------------------------------------
# Latihan Logika 1: Cetak 1 - 10
print("\nLatihan 1: Cetak angka 1 - 10 dengan for")
for i in range(1, 11):
    print(i, end=" ")

print("\n")

# ----------------------------------------
# Latihan Logika 2: Cetak 10 - 1
print("Latihan 2: Cetak angka 10 - 1 dengan while")
x = 10
while x >= 1:
    print(x, end=" ")
    x -= 1

print("\n")

# ----------------------------------------
# Latihan Logika 3: Tabel perkalian
print("Latihan 3: Tabel Perkalian")
n = int(input("Masukkan angka: "))
for i in range(1, 11):
    print(n, "x", i, "=", n * i)
