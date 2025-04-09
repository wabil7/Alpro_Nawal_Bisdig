# Konstanta nilai tukar
KURS_RUPIAH_TO_DOLLAR = 15000

# Input jumlah rupiah dari pengguna
rupiah = int(input("Masukkan jumlah rupiah: "))

# Konversi ke dollar
dollar = rupiah / KURS_RUPIAH_TO_DOLLAR

# Menampilkan hasil
print(f"{rupiah} rupiah setara dengan {dollar:.2f} dollar")