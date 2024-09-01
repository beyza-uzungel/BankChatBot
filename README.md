name: Banka Chatbotu

description: |
  Bu proje, kullanıcıların banka işlemleri ve soruları için otomatik yanıtlar sağlayan bir chatbot uygulamasıdır. Proje, Python, Flask ve JavaScript kullanılarak geliştirilmiştir.

features:
  - Veri İşleme ve Modelleme:
      - CSV dosyası üzerinden veri yüklenir.
      - Veriler temizlenir ve TF-IDF ile vektörize edilir.
      - Random Forest sınıflandırıcı kullanılarak metin kategorilere ayrılır.
      - SMOTE kullanılarak veri dengelenir ve GridSearchCV ile model optimizasyonu yapılır.
  - Web Uygulaması:
      - Flask framework kullanılarak bir web uygulaması geliştirilmiştir.
      - Kullanıcılar, metinlerini göndererek chatbot'tan yanıt alabilir.
      - Chatbot, en benzer soruyu bulmak için cosine similarity yöntemini kullanır.
  - Kullanıcı Arayüzü:
      - HTML ve CSS kullanılarak estetik bir sohbet penceresi tasarlanmıştır.
      - JavaScript ile etkileşimli bir kullanıcı deneyimi sunulmuştur, yazma göstergesi ve mesaj animasyonları ile kullanıcı etkileşimi artırılmıştır.

technologies:
  - Python:
      - Pandas
      - Scikit-learn
      - imbalanced-learn
      - joblib
  - Flask: Web sunucusu ve API
  - JavaScript: Dinamik sohbet penceresi
  - HTML/CSS: Kullanıcı arayüzü tasarımı

installation:
  requirements:
    - Python 3.x
    - Flask
    - scikit-learn
    - imbalanced-learn
    - joblib
  steps:
    - Install dependencies:
        ```bash
        pip install pandas scikit-learn imbalanced-learn flask joblib
        ```
    - Load model and vectorizer:
        Model ve vektörizer dosyaları `metin_siniflandirma_model.pkl` ve `vektorizer.pkl` olarak bu repo ile birlikte sağlanmıştır.
    - Start the web server:
        ```bash
        python app.py
        ```
    - Access the web application:
        Tarayıcınızda `http://127.0.0.1:5000` adresine gidin.

usage:
  - Web uygulamasında metin girerek chatbot ile etkileşime geçebilirsiniz.
  - Chatbot, en benzer soruyu bulur ve ilgili yanıtı size sunar.


