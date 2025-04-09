# Input Biodata dengan Casting Tipe Data yang Tepat

nama = input("Masukkan Nama: ")
nim = input("Masukkan NIM: ")
alamat = input("Masukkan Alamat: ")
tanggal_lahir = input("Masukkan Tanggal Lahir (DD-MM-YYYY): ")
jenis_kelamin = input("Masukkan Jenis Kelamin (L/P): ")

umur = int(input("Masukkan Umur: "))  
berat_badan = float(input("Masukkan Berat Badan (kg): "))  
tinggi_badan = float(input("Masukkan Tinggi Badan (cm): "))  
no_hp = input("Masukkan No. HP: ")  

# Menampilkan Biodata
print("\n===== BIODATA =====")
print("Nama          :", nama)
print("NIM           :", nim)
print("Alamat        :", alamat)
print("Tanggal Lahir :", tanggal_lahir)
print("Jenis Kelamin :", jenis_kelamin)
print("Umur          :", umur, "tahun")
print("Berat Badan   :", berat_badan, "kg")
print("Tinggi Badan  :", tinggi_badan, "cm")
print("No. HP        :", no_hp)