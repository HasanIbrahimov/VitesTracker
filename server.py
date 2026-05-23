from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup
import json

app = Flask(__name__)
CORS(app) 

@app.route('/api/ara', methods=['GET'])
def ara():
    aranan_arac = request.args.get('q', '')
    # Kelimeler arasındaki boşlukları + işaretine çeviriyoruz
    arama_sorgusu = aranan_arac.replace(" ", "+")
    
    # İŞTE BÜTÜN SIR BURADA: q= yerine searchText= kullanıyoruz!
    kategoriler = [
        f"https://www.arabam.com/ikinci-el/otomobil?searchText={arama_sorgusu}",
        f"https://www.arabam.com/ikinci-el/motosiklet?searchText={arama_sorgusu}"
    ]
        
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
    }

    toplanan_veriler = []
    
    for base_url in kategoriler:
        for sayfa in range(1, 4): # Her kategori için ilk 3 sayfayı (yaklaşık 150 ilan) çekiyoruz
            url = f"{base_url}&page={sayfa}" if sayfa > 1 else base_url
            response = requests.get(url, headers=headers)
            
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "html.parser")
                ilanlar = soup.find_all("tr", class_="listing-list-item")
                
                if not ilanlar:
                    break 
                    
                for ilan in ilanlar:
                    try:
                        baslik_alani = ilan.find("td", class_="listing-modelname")
                        baslik = baslik_alani.text.strip().replace('\n', ' ') if baslik_alani else ""
                        
                        fiyat_alani = ilan.find("span", class_="listing-price")
                        fiyat = fiyat_alani.text.strip() if fiyat_alani else "0 TL"
                        
                        detaylar = ilan.find_all("td", class_="listing-text")
                        yil = detaylar[0].text.strip() if len(detaylar) > 0 else "Bilinmiyor"
                        kilometre = detaylar[1].text.strip() if len(detaylar) > 1 else "Bilinmiyor"
                        
                        # Eğer boş veya hatalı satır değilse listeye ekle
                        if baslik and fiyat != "0 TL":
                            toplanan_veriler.append({
                                "model": baslik,
                                "fiyat": fiyat,
                                "yil": yil,
                                "kilometre": kilometre
                            })
                    except:
                        pass
            else:
                break

    #with open("ilan_verileri.json", "w", encoding="utf-8") as dosya:
        #json.dump(toplanan_veriler, dosya, ensure_ascii=False, indent=4)
        
    return jsonify({"durum": "basarili", "adet": len(toplanan_veriler), "veriler": toplanan_veriler})

if __name__ == '__main__':
    print("\n🚀 VitesTracker Sunucusu (Nihai Sürüm) Çalışıyor! (Port: 5000)")
    app.run(debug=True, port=5000)