from flask import Flask, request, jsonify, render_template
import pandas as pd
import joblib
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

def veri_yukle(dosya_adı):
    kodlamalar = ['utf-8', 'ISO-8859-1', 'cp1254']
    for kodlama in kodlamalar:
        try:
            df = pd.read_csv(dosya_adı, sep=';', encoding=kodlama)
            print(f"Başarıyla {kodlama} kodlaması ile okundu.")
            return df
        except UnicodeDecodeError:
            print(f"{kodlama} kodlaması ile okuma hatası.")
        except Exception as e:
            print(f"Bir hata oluştu: {e}")
    raise ValueError("Dosya okunamadı. Desteklenen kodlamaları kontrol et.")


model = joblib.load('metin_siniflandirma_model.pkl')
vektorizer = joblib.load('vektorizer.pkl')


df = veri_yukle('Kitap2.csv')


def metin_temizle(metin):
    metin = metin.lower()
    metin = re.sub(r'\s+', ' ', metin)
    metin = re.sub(r'[^\w\s]', '', metin)
    return metin.strip()

@app.route('/')
def ana_sayfa():
    return render_template('index.html')

@app.route('/tahmin', methods=['POST'])
def tahmin():
    try:
        veri = request.json
        metin = veri.get('text', '')
        if not metin:
            return jsonify({'hata': 'Metin sağlanmadı'}), 400

        metin_temiz = metin_temizle(metin)

        df['temizlenmiş_soru'] = df['soru'].apply(metin_temizle)
        tum_sorular_vetorler = vektorizer.transform(df['temizlenmiş_soru'])

        kullanıcı_vector = vektorizer.transform([metin_temiz])

        kosinüs_benzerlik = cosine_similarity(kullanıcı_vector, tum_sorular_vetorler).flatten()

        max_indeks = kosinüs_benzerlik.argmax()
        en_benzer_soru = df.iloc[max_indeks]['soru']
        bulunan_yanit = df.iloc[max_indeks]['yanit']

        print(f"Temizlenen Metin: {metin_temiz}")
        print(f"En Benzer Soru: {en_benzer_soru}")
        print(f"Bulunan Yanıt: {bulunan_yanit}")

        return jsonify({'yanit': bulunan_yanit})

    except Exception as e:
        return jsonify({'hata': f'Bir hata oluştu: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=False)
