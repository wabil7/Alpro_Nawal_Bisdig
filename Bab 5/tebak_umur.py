# Program: tebak_umur.py
# Tujuan: Menentukan kategori usia seseorang berdasarkan input

# Meminta pengguna memasukkan usia
usia = int(input("Masukkan usia kamu: "))

# Menentukan kategori berdasarkan usia
if usia <= 5:
    kategori = "balita"
elif usia <= 12:
    kategori = "anak-anak"
elif usia < 18:
    kategori = "remaja"
else:
    kategori = "dewasa"

# Menampilkan hasil kategori usia
print("Kamu termasuk kategori:", kategori)
