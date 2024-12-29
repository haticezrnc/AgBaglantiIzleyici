import socket
import threading
from queue import Queue
import logging
from colorama import Fore, Style, init

# Colorama'yı başlat
init()

# Log dosyasını ayarla
logging.basicConfig(
    filename="port_tarama_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

def tarama(ip, port, acik_portlar):
    """Bir portu kontrol eder ve sonucu ekrana ve loga yazar."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        sonuc = s.connect_ex((ip, port))
        if sonuc == 0:
            print(Fore.GREEN + f"[AÇIK] {ip}:{port}" + Style.RESET_ALL)
            logging.info(f"Açık port: {ip}:{port}")
            acik_portlar.append(port)
        else:
            print(Fore.RED + f"[KAPALI] {ip}:{port}" + Style.RESET_ALL)
        s.close()
    except Exception as e:
        logging.error(f"Port {port} taranırken hata oluştu: {e}")

def calistir(ip, port_araligi):
    """Portları paralel olarak tarar."""
    acik_portlar = []
    queue = Queue()

    # Portları sıraya ekle
    for port in port_araligi:
        queue.put(port)

    def worker():
        """Thread'lerin çalıştırdığı işlev."""
        while not queue.empty():
            port = queue.get()
            tarama(ip, port, acik_portlar)

    # Paralel tarama için thread oluştur
    threadler = []
    for _ in range(10):  # 10 thread
        t = threading.Thread(target=worker)
        t.start()
        threadler.append(t)

    # Tüm threadlerin tamamlanmasını bekle
    for t in threadler:
        t.join()

    print(Fore.CYAN + f"\nTarama tamamlandı! Açık portlar: {acik_portlar}" + Style.RESET_ALL)
    logging.info(f"Tarama tamamlandı! Açık portlar: {acik_portlar}")

if __name__ == "__main__":
    print(Fore.YELLOW + "Ağ Bağlantı İzleyici" + Style.RESET_ALL)
    hedef_ip = input("Hedef IP adresini girin (ör. 127.0.0.1): ").strip()
    baslangic_portu = int(input("Başlangıç portu (ör. 1): ").strip())
    bitis_portu = int(input("Bitiş portu (ör. 100): ").strip())

    # Port aralığı oluşturuldu ve taramayı başlat
    calistir(hedef_ip, range(baslangic_portu, bitis_portu + 1))
