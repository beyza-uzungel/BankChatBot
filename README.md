name: Banka Chatbotu
![Resim1](Ekran Görüntüsü (324).png)
description: |
  Bu proje, banka işlemleri ve soruları için otomatik yanıtlar sağlayan bir chatbot uygulamasıdır. Python, Flask ve JavaScript kullanılarak geliştirilmiştir. Kullanıcıların sorularına hızlı ve doğru cevaplar sunan bu chatbot, veri işleme ve doğal dil işleme tekniklerini kullanarak etkili bir çözüm sunar.

features:
  - **Veri İşleme ve Modelleme:**
    - CSV dosyasından veri yüklenir.
    - Veriler temizlenir ve TF-IDF ile vektörize edilir.
    - Random Forest sınıflandırıcı kullanılarak metinler kategorilere ayrılır.
    - SMOTE kullanılarak veri dengelenir ve GridSearchCV ile model optimizasyonu yapılır.
  - **Web Uygulaması:**
    - Flask framework kullanılarak bir web uygulaması geliştirilmiştir.
    - Kullanıcılar metinlerini göndererek chatbot'tan yanıt alabilir.
    - Chatbot, en benzer soruyu bulmak için cosine similarity yöntemini kullanır.
  - **Kullanıcı Arayüzü:**
    - HTML ve CSS ile estetik bir sohbet penceresi tasarlanmıştır.
    - JavaScript ile etkileşimli bir kullanıcı deneyimi sağlanmıştır; yazma göstergesi ve mesaj animasyonları ile kullanıcı etkileşimi artırılmıştır.

technologies:
  - **Python:**
    - Pandas
    - Scikit-learn
    - imbalanced-learn
    - joblib
  - **Flask:** Web sunucusu ve API
  - **JavaScript:** Dinamik sohbet penceresi
  - **HTML/CSS:** Kullanıcı arayüzü tasarımı

installation:
  steps:
    - **Gereksinimleri Kurun:**
      ```bash
      pip install pandas scikit-learn imbalanced-learn flask joblib
      ```
    - **Model ve Vektörizer'i Yükleyin:**
      Model ve vektörizer dosyaları `metin_siniflandirma_model.pkl` ve `vektorizer.pkl` olarak bu repo ile birlikte sağlanmıştır.
    - **Web Sunucusunu Başlatın:**
      ```bash
      python app.py
      ```
    - **Web Uygulamasına Erişin:**
      Tarayıcınızda `http://127.0.0.1:5000` adresine gidin.

usage:
  - Web uygulamasında metin girerek chatbot ile etkileşime geçebilirsiniz.
  - Chatbot, en benzer soruyu bulur ve ilgili yanıtı sunar.

contributors:
  - [Adınız]

license:
  - MIT
