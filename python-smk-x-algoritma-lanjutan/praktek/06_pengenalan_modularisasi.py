# Contoh Modularisasi

# Pastikan membuat file modul hitung.py dengan isi:
# def tambah(a, b):
#     return a + b
# def kali(a, b):
#     return a * b

from hitung import tambah, kali

x = int(input("Masukkan nilai x: "))
y = int(input("Masukkan nilai y: "))

print("Hasil tambah:", tambah(x, y))
print("Hasil kali:", kali(x, y))
