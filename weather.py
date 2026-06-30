# -*- coding: utf-8 -*-
import requests
import time
import os

# 81 İlin Tam ve Doğru Listesi
sehirler = [
    "Adana", "Adıyaman", "Afyonkarahisar", "Ağrı", "Aksaray", "Amasya", "Ankara", "Antalya", "Ardahan", "Artvin",
    "Aydın", "Balıkesir", "Bartın", "Batman", "Bayburt", "Bilecik", "Bingöl", "Bitlis", "Bolu", "Burdur",
    "Bursa", "Çanakkale", "Çankırı", "Çorum", "Denizli", "Diyarbakır", "Düzce", "Edirne", "Elazığ", "Erzincan",
    "Erzurum", "Eskişehir", "Gaziantep", "Giresun", "Gümüşhane", "Hakkari", "Hatay", "Iğdır", "Isparta", "İstanbul",
    "İzmir", "Kahramanmaraş", "Karabük", "Karaman", "Kars", "Kastamonu", "Kayseri", "Kilis", "Kırıkkale", "Kırklareli",
    "Kırşehir", "Kocaeli", "Konya", "Kütahya", "Malatya", "Manisa", "Mardin", "Mersin", "Muğla", "Muş",
    "Nevşehir", "Niğde", "Ordu", "Osmaniye", "Rize", "Sakarya", "Samsun", "Siirt", "Sinop", "Sivas",
    "Şanlıurfa", "Şırnak", "Tekirdağ", "Tokat", "Trabzon", "Tunceli", "Uşak", "Van", "Yalova", "Yozgat", "Zonguldak"
]

def main():
    os.system('clear')
    # Terminale hacker havası veren sistem mesajları
    print("\033[1;32m[SYSTEM] BAŞLATILIYOR...\033[0m")
    time.sleep(0.5)
    print("\033[1;34m[SYSTEM] 81 İL İÇİN METEOROLOJİK TARAMA BAŞLADI...\033[0m")
    time.sleep(0.5)
    print("\033[1;37m[DATA] VERİ AKIŞI AKTİF:\033[0m\n")

    for sehir in sehirler:
        # wttr.in servisi API anahtarı istemez, doğrudan çalışır
        url = f"https://wttr.in/{sehir}?format=3"
        try:
            response = requests.get(url, timeout=3)
            if response.status_code == 200:
                print(f"\033[1;36m[*]\033[0m {response.text.strip()}")
            else:
                print(f"\033[1;31m[!]\033[0m {sehir}: Bağlantı hatası.")
        except:
            print(f"\033[1;31m[!]\033[0m {sehir}: Sunucu yanıt vermedi.")
        
        # Akış hızı (Videonun o "havalı" akması için 0.05 - 0.1 arası idealdir)
        time.sleep(0.08)

    print("\n\033[1;32m[SYSTEM] TÜM VERİLER İŞLENDİ. BAĞLANTI KESİLDİ.\033[0m")

if __name__ == "__main__":
    main()
 
