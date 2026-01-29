# -*- coding: utf-8 -*-
"""
Project: ISO 10816-3 Based Asset Health Monitor
Engineer: Enes (Mechanical Engineer / AI Graduate Student)
Version: 1.1
"""

import os
import time

def endustriyel_analiz_motoru():
    # Terminali temizleyerek profesyonel bir baslangic yapar
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("="*65)
    print("   INDUSTRIAL ASSET ANALYTICS - ISO 10816-3 COMPLIANCE")
    print("   Predictive Maintenance & Condition Monitoring System")
    print("="*65)
    
    # Giris Parametreleri
    muhendis = input("Sorumlu Muhendis (Lead Engineer): ")
    unite = input("Varlik Kimligi (Asset ID / Unit): ")
    
    print(f"\n[SISTEM] Veri akisi dogrulaniyor... Lutfen bekleyiniz.")
    time.sleep(1.5)

    # Mühendislik Limitleri (ISO 10816-3 Standardi)
    # Machine Group 1/2 icin kritik vibrasyon degeri genellikle 4.5 mm/s'dir.
    LIMIT_VIB = 4.5  
    LIMIT_TEMP = 95.0 
    
    anomali_kayitlari = []

    # 3 Veri Seti Üzerinden Analiz (Video icin ideal sure)
    for i in range(1, 4):
        print(f"\n>>> ANALIZ DONGUSU {i} / 3")
        try:
            # Kullanici girislerini aliyoruz
            t_input = input(f"Sensor Sicaklik Degeri (Celsius): ")
            v_input = input(f"Sensor Vibrasyon Degeri (mm/s): ")
            
            temp = float(t_input)
            vib = float(v_input)

            if temp >= LIMIT_TEMP or vib >= LIMIT_VIB:
                print(f"🚨 KRITIK DURUM: Anomali Tespit Edildi!")
                if vib >= LIMIT_VIB: 
                    print(f"   [!] MEKANIK: ISO 10816-3 Limit Asimi! ({vib} mm/s)")
                if temp >= LIMIT_TEMP: 
                    print(f"   [!] TERMAL: Asiri Isinma Riski! ({temp} C)")
                anomali_kayitlari.append(f"Set {i}: {vib}mm/s - {temp}C")
            else:
                print(f"🟢 DURUM: NOMINAL. Sistem standartlara uygun calisiyor.")
            
            print("-" * 45)
        except ValueError:
            print("Hata: Gecersiz veri tipi! Lutfen sadece sayısal deger giriniz.")

    # Teknik Rapor Özeti
    print(f"\n{'#'*20} TEKNIK ANALIZ RAPORU {'#'*20}")
    final_status = "🚨 KRITIK MUDAHALE GEREKLI" if anomali_kayitlari else "🟢 OPTIMAL CALISMA"
    
    print(f"Muhendis: {muhendis}")
    print(f"Unite: {unite}")
    print(f"Genel Durum: {final_status}")
    print(f"{'#'*54}")

    # Teknik raporu bir dosyaya yazdirma (Portfolyo icin onemli bir detay)
    try:
        with open("Health_Report.txt", "w") as report:
            report.write(f"ISO 10816-3 Analysis Summary\n")
            report.write(f"Engineer: {muhendis}\nAsset: {unite}\nStatus: {final_status}")
    except Exception:
        pass

    input("\nAnaliz tamamlandi. Programdan cikmak icin ENTER'a basin...")

if __name__ == "__main__":
    endustriyel_analiz_motoru()
