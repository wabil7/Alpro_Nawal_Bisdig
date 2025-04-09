# Program: seleksi.py
# Tujuan: Menentukan grade berdasarkan nilai yang dimasukkan

# Baca input dari pengguna
nilai = float(input("Masukkan nilai kamu: "))

# Tentukan grade berdasarkan nilai
if nilai >= 90:
    grade = "A"
elif nilai >= 70:
    grade = "B"
elif nilai >= 60:
    grade = "C"
elif nilai >= 50:
    grade = "D"
else:
    grade = "E"

# Tampilkan hasil grade
print("Grade kamu adalah:", grade)