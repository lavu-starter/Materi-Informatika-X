# Total belanja setelah diskon
harga = float(input("Masukkan total harga: "))
diskon = float(input("Masukkan persen diskon: "))
total = harga - (harga * diskon / 100)
print("Total harga setelah diskon:", total)

# Hitung jumlah huruf vokal dalam kalimat
kalimat = input("Masukkan kalimat: ").lower()
vokal = "aiueo"
jumlah = sum(1 for huruf in kalimat if huruf in vokal)
print("Jumlah huruf vokal:", jumlah)
