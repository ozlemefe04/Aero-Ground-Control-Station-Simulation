import socket
import threading
import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

XOR_KEY = "AERO_SECRET_123"

def sifre_coz(sifreli_metin, anahtar):
    return "".join(chr(ord(c) ^ ord(anahtar[i % len(anahtar)])) for i, c in enumerate(sifreli_metin))


class YerKontrolUygulamasi(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("AERO-GROUND CONTROL STATION | İHA YER KONTROL")
        self.geometry("900x500")
        
        self.zaman_verileri = []
        self.sicaklik_verileri = []
        
        self.arayuz_tasarla()
        
        self.network_thread = threading.Thread(target=self.server_baslat, daemon=True)
        self.network_thread.start()

    def arayuz_tasarla(self):
        self.sol_panel = ctk.CTkFrame(self, width=300, corner_radius=10)
        self.sol_panel.pack(side="left", fill="y", padx=10, pady=10)
        
        self.baslik = ctk.CTkLabel(self.sol_panel, text="TELEMETRİ VERİLERİ", font=("Arial", 16, "bold"))
        self.baslik.pack(pady=20)
        
        self.lbl_sicaklik = ctk.CTkLabel(self.sol_panel, text="Sıcaklık: -- °C", font=("Arial", 20))
        self.lbl_sicaklik.pack(pady=15)
        
        self.lbl_durum = ctk.CTkLabel(self.sol_panel, text="Durum: BEKLENİYOR", font=("Arial", 16))
        self.lbl_durum.pack(pady=15)
        
        self.led_isigi = ctk.CTkLabel(self.sol_panel, text="● SİSTEM DURUMU", text_color="gray", font=("Arial", 14, "bold"))
        self.led_isigi.pack(pady=20)

        self.sag_panel = ctk.CTkFrame(self, corner_radius=10)
        self.sag_panel.pack(side="right", fill="both", expand=True, padx=10, pady=10)
        
        self.fig, self.ax = plt.subplots(figsize=(5, 4), facecolor='#2b2b2b')
        self.ax.set_facecolor('#1e1e1e')
        self.ax.tick_params(colors='white')
        self.ax.set_title("Anlık Sıcaklik Değişimi", color='white', fontsize=12)
        self.ax.set_xlabel("Zaman (s)", color='white')
        self.ax.set_ylabel("Sıcaklık (°C)", color='white')
        self.line, = self.ax.plot([], [], color='#1f77b4', linewidth=2)
        
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.sag_panel)
        self.canvas.get_tk_widget().pack(fill="both", expand=True, padx=5, pady=5)

    def server_baslat(self):
        IP_ADRESI = "127.0.0.1"
        PORT = 50005
        
        server_soketi = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_soketi.bind((IP_ADRESI, PORT))
        server_soketi.listen(1)
        
        baglanti, adres = server_soketi.accept()

        while True:
            try:
                gelen_byte = baglanti.recv(1024)
                if not gelen_byte:
                    break
                
                sifreli_metin = gelen_byte.decode('utf-8', errors='ignore')
                
                orijinal_metin = sifre_coz(sifreli_metin, XOR_KEY)
            
                parcalar = orijinal_metin.split(" | ")
                sure = float(parcalar[0].split(":")[1].replace("s", ""))
                sicaklik = float(parcalar[1].split(":")[1].replace("C", ""))
                durum = parcalar[2].split(":")[1]
                
                self.lbl_sicaklik.configure(text=f"Sıcaklık: {sicaklik} °C")
                self.lbl_durum.configure(text=f"Durum: {durum}")
                
                if durum == "HAREKETLI":
                    self.led_isigi.configure(text_color="red", text="● TEHLİKE: HAREKET VAR")
                else:
                    self.led_isigi.configure(text_color="green", text="● STABİL: HAREKET YOK")
                
                self.zaman_verileri.append(sure)
                self.sicaklik_verileri.append(sicaklik)
                
                self.line.set_data(self.zaman_verileri, self.sicaklik_verileri)
                self.ax.relim()
                self.ax.autoscale_view()
                self.canvas.draw()
                
            except Exception as e:
                print(f"Hata: {e}")
                break



        

if __name__ == "__main__":
    app = YerKontrolUygulamasi()
    app.mainloop()
