import time
import random

print("====================")
print("Random Seçim v1.0 - developed by whiskydev")
print("====================")

secim = input("Başlamak için bir işlem seçin \n[1] Programı Başlat \n[2] Krediler \n[3] Çıkış \n")

if (secim == "1"):
  print("Program Başlatıldı! \n")

  data = []
  sayac = 1
  kackez = int(input("Kaç tane seçenek olacak?: "))
  while sayac <= kackez:
    data1 = input(f"{sayac}. Seçeneği giriniz: ")
    data.append(data1)
    sayac += 1
  finaldata = random.choice(data)
  print("===== Seçim Yapılıyor.. =====")
  time.sleep(3)
  print("===== Seçim Yapıldı =========")
  print(f"Seçilen Seçenek: {finaldata} \nSeçenek Sayısı: {sayac-1}")

elif (secim == "2"):
  print("Github: github.com/whiskydev11 \nWeb: whiskydev.xyz \n©2022")
elif (secim == "3"):
  print("Çıkış Sağlandı.")
else:
  print("Geçersiz Kod")
