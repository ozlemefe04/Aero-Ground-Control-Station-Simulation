import socket
import time
import random

XOR_KEY = "AERO_SECRET_123"

def veriyi_sifrele(metin, anahtar):
    sifreli_metin = "".join(chr(ord(c) ^ ord(anahtar[i % len(anahtar)])) for i, c in enumerate(metin))
    return sifreli_metin

HEDEF_IP = "127.0.0.1"
HEDEF_PORT = 50005

iha_soketi = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
iha_soketi.connect((HEDEF_IP, HEDEF_PORT))

sicaklik = 25.0

try:
    for saniye in range(1, 15):
        sicaklik -= 0.4 + random.uniform(-0.1, 0.1)
        sicaklik = round(sicaklik, 2)
        durum = "SABIT" if sicaklik > 21 else "HAREKETLI"
        
        ham_paket = f"Sure:{saniye}s | Sicaklik:{sicaklik}C | Durum:{durum}"
        print(f"[İHA - HAM VERİ] {ham_paket}")
        
        sifreli_paket = veriyi_sifrele(ham_paket, XOR_KEY)
        
        iha_soketi.send(sifreli_paket.encode('utf-8'))
        print(f"[İHA - AĞA GÖNDERİLEN] {sifreli_paket.encode('utf-8')} (Şifreli)")
        print("-" * 40)
        
        time.sleep(1)

except Exception as e:
    print(f"Hata: {e}")
finally:
    iha_soketi.close()
