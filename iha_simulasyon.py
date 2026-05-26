import socket
import time
import random

HEDEF_IP = "127.0.0.1"
HEDEF_PORT = 50005

iha_soketi = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("[İHA] Yer kontrol istasyonuna bağlanılıyor...")
iha_soketi.connect((HEDEF_IP, HEDEF_PORT))
print("[İHA] Bağlantı kuruldu! Telemetri gönderimi başlıyor...")

try:
    for saniye in range(1, 11):
        sicaklik = round(random.uniform(20.0, 25.0), 2)
        hareket = random.choice(["SABIT", "HAREKETLI"])
        
        paket = f"Sure:{saniye}s | Sicaklik:{sicaklik}C | Durum:{hareket}"
        
        iha_soketi.send(paket.encode('utf-8'))
        print(f"[İHA] Gönderildi -> {paket}")
        
        time.sleep(1)

except Exception as e:
    print(f"[HATA] Veri gönderilirken hata oluştu: {e}")

finally:
    iha_soketi.close()
    print("[İHA] Telemetri bitti, soket kapatıldı.")
