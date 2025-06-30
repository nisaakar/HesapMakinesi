import math

hafiza = []
ans = 0

print("Basit Hesap Makinesi Programına Hoş Geldiniz!")

while True:
    print("\nYapmak istediğiniz işlemi seçin:")
    print("1. Toplama")
    print("2. Çıkarma")
    print("3. Çarpma")
    print("4. Bölme")
    print("5. Karekök")
    print("6. n-Kök")
    print("7. Yüzde hesaplama")
    print("8. Grand Total (tüm sonuçların toplamı)")
    print("9. Hesap makinesini sıfırla")
    print("0. Çıkış")

    secim = input("Seçiminiz: ")

    if secim == "0":
        print("Programdan çıkış")
        break

    elif secim == "9":
        hafiza.clear()
        ans = 0
        print("Hafıza temizlendi.")

    elif secim == "8":
        toplam = sum(hafiza)
        print("Grand Total (tüm sonuçların toplamı):", toplam)

    elif secim in ["1", "2", "3", "4", "7"]:
        try:
            x = input("Birinci sayı: ")
            if x == "ans":
                sayi1 = ans
            else:
                sayi1 = float(x)

            y = input("İkinci sayı: ")
            if y == "ans":
                sayi2 = ans
            else:
                sayi2 = float(y)
        except ValueError:
            print("Lütfen bir sayı girin.")
            continue

        if secim == "1":
            sonuc = sayi1 + sayi2
            print("Toplama sonucu:", sonuc)
        elif secim == "2":
            sonuc = sayi1 - sayi2
            print("Çıkarma sonucu:", sonuc)
        elif secim == "3":
            sonuc = sayi1 * sayi2
            print("Çarpma sonucu:", sonuc)
        elif secim == "4":
            if sayi2 == 0:
                print("Hata: Sıfıra bölme yapılamaz.")
                continue
            sonuc = sayi1 / sayi2
            print("Bölme sonucu:", sonuc)
        elif secim == "7":
            sonuc = (sayi1 * sayi2) / 100
            print(f"{sayi1}'in %{sayi2}'si =", sonuc)

        ans = sonuc
        hafiza.append(sonuc)

    elif secim == "5":
        x = input("Sayı: ")
        try:
            if x == "ans":
                sayi = ans
            else:
                sayi = float(x)
            if sayi < 0:
                print("Hata: Negatif sayıların karekökü alınamaz.")
                continue
            sonuc = math.sqrt(sayi)
            print("Karekök sonucu:", sonuc)
            ans = sonuc
            hafiza.append(sonuc)
        except ValueError:
            print("Lütfen sayı girin.")

    elif secim == "6":
        x = input("Sayı: ")
        n = input("Kök derecesi (ör: 3 için küpkök): ")
        try:
            if x == "ans":
                sayi = ans
            else:
                sayi = float(x)
            derecesi = float(n)
            if sayi < 0 and derecesi % 2 == 0:
                print("Hata: Negatif sayının çift kökü alınamaz.")
                continue
            sonuc = sayi ** (1/derecesi)
            print(f"{derecesi}-kök sonucu:", sonuc)
            ans = sonuc
            hafiza.append(sonuc)
        except ValueError:
            print("Lütfen sayı girin.")
        except ZeroDivisionError:
            print("Hata: 0. dereceden kök alınamaz.")

    else:
        print("Lütfen menüden bir sayı girin.")
