def persiapan_ke_kampus():
    print("Selamat pagi! 🌞")
    
    # Langkah 1: Bangun tidur
    input("Tekan Enter jika kamu sudah bangun tidur...")
    
    # Langkah 2: Sikat gigi
    sikat_gigi = input("Apakah kamu sudah sikat gigi? (ya/tidak): ").strip().lower()
    if sikat_gigi != "ya":
        print("Silakan sikat gigi dulu 🪥")
        return
    
    # Langkah 3: Mandi
    input("Sudah sikat gigi, lanjut mandi. Tekan Enter jika kamu sudah mandi 🚿...")
    
    # Langkah 4: Sarapan
    sarapan = input("Apakah kamu sudah sarapan? (ya/tidak): ").strip().lower()
    if sarapan != "ya":
        print("Jangan lupa sarapan dulu 🍽️")
        return
    
    # Langkah 5: Berangkat ke kampus
    print("Kamu sudah siap! 🎒")
    print("Berangkat ke kampus sekarang 🚶‍♂️🚶‍♀️")

# Jalankan program
persiapan_ke_kampus()
    