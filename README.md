# 🏎️ VitesTracker - Gelişmiş Araç ve Motosiklet Fiyat Analiz Platformu

VitesTracker, dinamik web kazıma (web scraping) teknikleri ile otomobil ve motosiklet piyasasındaki canlı ilan verilerini anlık olarak çekip analiz eden, modern ve kullanıcı dostu bir Full-Stack veri analitiği paneli (dashboard) projesidir. 

Proje, ilan sitelerindeki karmaşık arama parametrelerini akıllıca çözerek tam eşleşen sonuçları listeler, ortalama/min/max fiyatları hesaplar ve kilometre ile fiyat arasındaki ilişkiyi dinamik bir grafik üzerinde görselleştirir.

---

## 🚀 Öne Çıkan Özellikler

- **Canlı Piyasa Taraması (Real-time Scraping):** Kullanıcı arama çubuğuna araç modelini girip Enter'a bastığı an backend sunucusu canlı olarak ilan sayfalarını tarar ve temiz verileri anında ön yüze aktarır.
- **Akıllı Yenileme (Live Scrape Controls):** Tek tıkla mevcut arama sorgusunu sayfayı yenilemeden günceller ve anlık yüklenme animasyonları ile kullanıcıya görsel geri bildirim sağlar.
- **Gelişmiş Filtreleme Paneli:**
  - Maksimum Kilometre süzgeci
  - Minimum ve Maksimum Model Yılı Aralığı filtrelemesi
  - Araç Durumu (Sıfır / İkinci El) seçimi
- **Dinamik Fiyat & Kilometre Grafiği (Chart.js):** Çekilen verileri kilometreye göre sıralayarak fiyat-kilometre eğrisini canlı olarak çizer. Filtreler değiştikçe grafik saniyeler içinde kendini günceller.
- **Gelişmiş Ön Yüz Tasarımı (Premium Glassmorphic UI):** Tamamen modern, karanlık mod odaklı, neon ışık geçişlerine sahip cam morfolojisi (glassmorphism) tasarımı.
- **Empty State (Boş Durum) Yönetimi:** Arama yapılmadığında veya metin silindiğinde sistemi otomatik olarak sıfırlayan akıllı durum yönetimi.
- **Çift Dil Desteği:** Tek tıkla TR/EN dilleri arasında dinamik geçiş imkanı.

---

## 🛠️ Teknoloji Yığını (Tech Stack)

### Arka Plan (Backend)
- **Python 3**
- **Flask** (Yerel API Sunucusu)
- **Flask-CORS** (Ön yüz ve arka plan güvenli iletişim köprüsü)
- **BeautifulSoup4 & Requests** (Veri kazıma ve HTML ayrıştırma motoru)

### Ön Yüz (Frontend)
- **HTML5 & CSS3** (Custom Grid/Flexbox sistemleri ve özel CSS Değişkenleri)
- **JavaScript (ES6+)** (Asenkron API Fetch işlemleri, dinamik DOM manipülasyonu ve filtreleme algoritmaları)
- **Chart.js** (Piyasa trend çizgileri ve veri görselleştirme)
- **Lucide Icons** (Premium modern vektörel ikon seti)

---

## 📦 Kurulum ve Çalıştırma

Projeyi yerel makinenizde çalıştırmak için aşağıdaki adımları sırasıyla uygulayabilirsiniz:

### 1. Projeyi Klonlayın veya İndirin
```bash
git clone https://github.com/HasanIbrahimov/VitesTracker.git
cd VitesTracker
```

### 2. Gerekli Python Kütüphanelerini Kurun
```bash
pip install flask flask-cors requests beautifulsoup4
```

### 3. Backend Sunucusunu Başlatın
```bash
python server.py
```
Sunucu başarıyla başladığında terminalde `🚀 VitesTracker Sunucusu (Nihai Sürüm) Çalışıyor! (Port: 5000)` mesajını göreceksiniz.

### 4. Ön Yüzü Yayına Alın
`index.html` dosyasını VS Code üzerinden **Live Server** eklentisiyle açın veya tarayıcınızda doğrudan çalıştırın.

---

## 📄 Lisans
Bu proje MIT Lisansı altında lisanslanmıştır. Akademik ve kişisel portfolyo kullanımlarına tamamen açıktır.
