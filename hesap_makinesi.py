import math

class HesapMakinesi:
    def __init__(self):
        self.hafiza = []
        self.ans = 0

    def toplama(self, a, b):
        return a + b

    def cikarma(self, a, b):
        return a - b

    def carpma(self, a, b):
        return a * b

    def bolme(self, a, b):
        if b == 0:
            print("Hata: Sıfıra bölme yapılamaz.")
            return None
        return a / b

    def karekok(self, a):
        if a < 0:
            print("Hata: Negatif sayıların karekökü alınamaz.")
            return None
        return math.sqrt(a)

    def kok_alma(self, a, n):
        if a < 0 and n % 2 == 0:
            print("Hata: Negatif sayının çift kökü alınamaz.")
            return None
        try:
            return a ** (1 / n)
        except ZeroDivisionError:
            print("Hata: 0. dereceden kök alınamaz.")
            return None

    def yuzde_hesapla(self, a, b):
        return (a * b) / 100

    def toplam_sonuc(self):
        return sum(self.hafiza)

    def hesap_ekle(self, sonuc):
        self.ans = sonuc
        self.hafiza.append(sonuc)

    def hafizayi_temizle(self):
        self.hafiza.clear()
        self.ans = 0
        print("Hafıza temizlendi.")

hm = HesapMakinesi()

print("Hesap Makinesi")

while True:
    print("\nYapmak istediğiniz işlemi seçin:")
    print("1. Toplama")
    print("2. Çıkarma")
    print("3. Çarpma")
    print("4. Bölme")
    print("5. Karekök")
    print("6. n-Kök")
    print("7. Yüzde hesaplama")
    print("8. Toplam Sonuç")
    print("9. Hesap makinesini sıfırla")
    print("0. Çıkış")

    secim = input("Seçiminiz: ")

    if secim == "0":
        print("Programdan çıkış yapılıyor...")
        break

    elif secim == "9":
        hm.hafizayi_temizle()

    elif secim == "8":
        print("Toplam Sonuç:", hm.toplam_sonuc())

    elif secim in ["1", "2", "3", "4", "7"]:
        try:
            x = input("Birinci sayı (veya 'ans'): ")
            sayi1 = hm.ans if x == "ans" else float(x)
            y = input("İkinci sayı (veya 'ans'): ")
            sayi2 = hm.ans if y == "ans" else float(y)
        except ValueError:
            print("Hatalı giriş! Lütfen sayı girin.")
            continue

        sonuc = None
        if secim == "1":
            sonuc = hm.toplama(sayi1, sayi2)
            print("Toplama sonucu:", sonuc)
        elif secim == "2":
            sonuc = hm.cikarma(sayi1, sayi2)
            print("Çıkarma sonucu:", sonuc)
        elif secim == "3":
            sonuc = hm.carpma(sayi1, sayi2)
            print("Çarpma sonucu:", sonuc)
        elif secim == "4":
            sonuc = hm.bolme(sayi1, sayi2)
            if sonuc is not None:
                print("Bölme sonucu:", sonuc)
        elif secim == "7":
            sonuc = hm.yuzde_hesapla(sayi1, sayi2)
            print(f"{sayi1}'in %{sayi2}'si =", sonuc)

        if sonuc is not None:
            hm.hesap_ekle(sonuc)

    elif secim == "5":
        x = input("Sayı (veya 'ans'): ")
        try:
            sayi = hm.ans if x == "ans" else float(x)
            sonuc = hm.karekok(sayi)
            if sonuc is not None:
                print("Karekök sonucu:", sonuc)
                hm.hesap_ekle(sonuc)
        except ValueError:
            print("Lütfen sayı girin.")

    elif secim == "6":
        x = input("Sayı (veya 'ans'): ")
        n = input("Kök derecesi (ör: 3): ")
        try:
            sayi = hm.ans if x == "ans" else float(x)
            derece = float(n)
            sonuc = hm.kok_alma(sayi, derece)
            if sonuc is not None:
                print(f"{derece}-kök sonucu:", sonuc)
                hm.hesap_ekle(sonuc)
        except ValueError:
            print("Lütfen sayı girin.")

    else:
        print("Geçersiz seçim! Lütfen menüden bir işlem seçin.")
