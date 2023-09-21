#hitung luas segitiga sederhana
def luas_segitiga():
    a = int(input("masukkan alas segitiga: "))
    t = int(input("masukkan tinggi segitiga: "))
    luas = a * t / 2
    print("luas segitiga adalah: ", luas)

luas_segitiga()

#hitung luas persegi panjang
def luas_persegi_panjang():
    p = int(input("masukkan panjang persegi: "))
    l = int(input("masukkan lebar persegi: "))
    luas = p * l
    print("luas persegi panjang adalah: ", luas)

luas_persegi_panjang()

#hitung luas trapesium
def luas_trapesium():
    s1 = int(input("masukkan sisi 1 trapesium: "))
    s2 = int(input("masukkan sisi 2 trapesium: "))
    t = int(input("masukkan tinggi trapesium: "))
    luas = 1/2 * (s1+s2) * t
    print("luas trapesium adalah: ", luas)

luas_trapesium()

#hitung keliling persegi 
def keliling_persegi():
    s = int(input("masukkan sisi persegi: "))
    keliling = 4 * s
    print("keliling persegi adalah: ", keliling)

keliling_persegi()

#hitung keliling segitiga
def keliling_segitiga():
    s = int(input("masukkan sisi segitiga: "))
    keliling = 3 * s
    print("keliling segitiga adalah: ", keliling)

keliling_segitiga()