# Latihan Looping List dan Dictionary

# Looping list: menampilkan nilai genap
nilai = [80, 90, 70, 85]
print("Nilai genap:")
for n in nilai:
    if n % 2 == 0:
        print(n)

# Nested loop: tabel perkalian 1-5
print("\nTabel perkalian 1-5:")
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i*j}", end="\t")
    print()

# Looping dictionary: menampilkan data siswa
data = {"Ani": 80, "Budi": 90, "Cici": 85}
print("\nData siswa:")
for k, v in data.items():
    print(f"{k}: {v}")
