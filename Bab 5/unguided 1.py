# seleksi.py

# Membaca input nilai dari user
nilai = int(input("Masukkan nilai: "))

# Menentukan grade berdasarkan nilai
if nilai >= 90:
    grade = "A"
elif nilai >= 70 and nilai < 90:
    grade = "B"
elif nilai >= 60 and nilai < 70:
    grade = "C"
elif nilai >= 50 and nilai < 60:
    grade = "D"
else:
    grade = "E"

# Menampilkan grade
print("Grade:", grade)