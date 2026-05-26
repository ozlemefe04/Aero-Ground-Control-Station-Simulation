import socket
IP_ADRESI = "127.0.0.1" 
PORT = 50005
server_soketi = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_soketi.bind((IP_ADRESI, PORT))
server_soketi.listen(1)
print(f"[YER KONTROL] {PORT} portunda İHA bağlantısı bekleniyor...")

baglanti, adres = server_soketi.accept()
print(f"[BAĞLANTI] İHA başarıyla bağlandı! IP/Port: {adres}")

while True:
    try:
        gelen_veri = baglanti.recv(1024).decode('utf-8')
        if not gelen_veri:
            break   
        print(f"[TELEMETRİ] Gelen Veri: {gelen_veri}")
        
    except ConnectionResetError:
        print("[HATA] İHA ile bağlantı ansızın koptu!")
        break

baglanti.close()
server_soketi.close()
print("[SİSTEM] Yer kontrol istasyonu kapatıldı.")
