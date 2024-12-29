# AgBaglantiIzleyici

Belirtilen bir IP adresi ve port aralığındaki açık portları tarayan bir Python projesi.

Bu Python projesi, belirli bir IP adresi ve port aralığını tarayarak açık portları tespit eden bir ağ bağlantı izleyicidir. Proje, renkli çıktı, loglama ve paralel tarama özellikleri ile ağ analizi yapmak için kullanışlı bir araç sunar.

---

## Özellikler

- **Renkli Çıktılar**: `colorama` kullanılarak açık ve kapalı portlar farklı renklerde gösterilir.
- **Loglama**: Tüm tarama sonuçları bir log dosyasına kaydedilir (`port_tarama_log.txt`).
- **Paralel Tarama**: `threading` kullanılarak hızlı port tarama yapılır.

---

 Kurulum

Gereksinimler

- **Python 3.7** veya üzeri yüklü olmalıdır.
- Gerekli Python kütüphaneleri:
  - `colorama`
  - `socket`
  - `threading`
  - `logging`

 Adım 1: Depoyu Klonlayın

```bash
git clone https://github.com/kullaniciadi/AgBaglantiIzleyici.git
cd AgBaglantiIzleyici

Adım 2: Sanal Ortam Oluşturun 

python3 -m venv .venv
source .venv/bin/activate  # Mac ve Linux
.venv\Scripts\activate     # Windows
Adım 3: Gerekli Kütüphaneleri Yükleyin
pip install -r requirements.txt
Eğer requirements.txt dosyası yoksa şu komutu çalıştırın:

pip install colorama
Kullanım

python network_monitor.py
Hedef IP adresini girin (ör. 127.0.0.1).
Tarama yapılacak başlangıç ve bitiş portlarını belirleyin (ör. 1-100).
Açık ve kapalı portlar terminalde gösterilecek, ayrıca sonuçlar port_tarama_log.txt dosyasına kaydedilecektir.
Örnek Kullanım

Terminalde:
Hedef IP adresini girin (ör. 127.0.0.1): 127.0.0.1
Başlangıç portu (ör. 1): 1
Bitiş portu (ör. 100): 100
[AÇIK] 127.0.0.1:22
[KAPALI] 127.0.0.1:23
...
Tarama tamamlandı! Açık portlar: [22]
Log Dosyası:
2024-12-22 14:30:45,123 - Tarama Başladı! Hedef: 127.0.0.1, Port aralığı: range(1, 101)
2024-12-22 14:30:46,456 - Açık port: 127.0.0.1:22
2024-12-22 14:30:50,789 - Tarama tamamlandı! Açık portlar: [22]
Proje Yapısı

AgBaglantiIzleyici/
│
├── network_monitor.py       # Ana Python dosyası
├── port_tarama_log.txt      # Tarama sonuçlarının log dosyası
├── README.md                # Proje açıklama dosyası
└── requirements.txt         # Gereksinim dosyası
