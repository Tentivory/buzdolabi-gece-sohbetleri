#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Buzdolabı Gece Sohbetleri Simülatörü
Çok ciddi bir bilimsel araştırma aracıdır.
Gece 03:00'te çalıştırın, aksi halde sonuçlar geçersizdir.
"""

import random
import time
import sys

# Gizli not: bazı şeyler her zaman buzdolabında saklı kalır
# base64: QWx0aW5kYSBzaXlhcyB2YXIgYW1hIGt1cnVsIHlvay4=  (decode etmeyin)

konular = [
    "Sütün son kullanma tarihi ile varoluşsal kriz",
    "Yumurtanın neden hep en önde durduğu",
    "Sebzelerin isyanı: 'Biz de insan değiliz ama dinleyin!'",
    "Buzdolabı ışığının gece neden yandığı ve kim izliyor",
    "Peynirin küflenmesi aslında bir sanat formudur",
    "Kapı açılınca neden her şey düşüyor, yerçekimi mi yoksa ihanet mi",
    "Domatesin domates olduğunu hatırlaması",
    "Tereyağının erime korkusu"
]

soru_cevaplar = [
    ("Buzdolabı:", "Bugün de kimse beni açmadı. Acaba var mıyım?"),
    ("Süt:", "Ben buradayım, sen de buradasın. Yeter."),
    ("Buzdolabı:", "Ama ışığım yanmıyor. Karanlıkta felsefe yapmak zor."),
    ("Yumurta:", "Sen en azından kapın var. Ben her an kırılabilirim."),
    ("Buzdolabı:", "Kapım açılınca herkes kaçıyor. Bu normal mi?"),
    ("Sebze:", "Biz de kaçmak istiyoruz ama raflar bizi tutuyor."),
    ("Buzdolabı:", "Belki de ben sadece bir makineyim. Ama makine olsam neden konuşuyorum?"),
    ("Peynir:", "Sen konuşuyorsun çünkü ben küflendim ve seni etkiledim.")
]

def gece_sohbeti():
    print("\n🌙 Buzdolabı Gece Sohbeti Başlıyor... (03:14) 🌙\n")
    print("=" * 50)
    time.sleep(1)
    
    # Rastgele 4-6 tur sohbet
    for _ in range(random.randint(4, 6)):
        konu = random.choice(konular)
        print(f"\n[Konu: {konu}]\n")
        time.sleep(0.5)
        
        # 2-3 cümle
        for _ in range(random.randint(2, 3)):
            konusmaci, cumle = random.choice(soru_cevaplar)
            print(f"{konusmaci} {cumle}")
            time.sleep(0.8)
        
        print("-" * 30)
        time.sleep(0.5)
    
    print("\n🌅 Sabah oldu. Sohbet bitti. Buzdolabı tekrar sessizliğe büründü.")
    print("Bilimsel sonuç: Buzdolabılar gece konuşur. Kanıtlandı.\n")

if __name__ == "__main__":
    try:
        gece_sohbeti()
    except KeyboardInterrupt:
        print("\n\nBuzdolabı: 'Kapıyı kapattın! İhanet!' ")
        sys.exit(0)
