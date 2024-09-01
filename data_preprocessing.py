import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import GridSearchCV
import joblib


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
    raise ValueError("Dosya okunamadı. Desteklenen kodlamaları kontrol edin.")


df = veri_yukle('Kitap2.csv')


print("İlk 5 satır:")
print(df.head())


if df.isnull().values.any():
    print("Uyarı: Verilerde boş değerler var. Boş değerleri temizliyorum...")
    df = df.dropna()


def metin_temizle(metin):
    metin = metin.lower()
    metin = re.sub(r'\s+', ' ', metin)
    metin = re.sub(r'[^\w\s]', '', metin)
    metin = re.sub(r'\d+', '', metin)
    return metin.strip()

df['soru'] = df['soru'].apply(metin_temizle)

vektorizer = TfidfVectorizer(ngram_range=(1, 2))

X = vektorizer.fit_transform(df['soru'])

y = df['kategori']


X_egitim, X_test, y_egitim, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# SMOTE
min_örnek = min(pd.Series(y_egitim).value_counts())  # En küçük sınıf örnek sayısı
komşu_sayısı = min(5, min_örnek - 1)  # k_neighbors değerini ayarladık
smote = SMOTE(sampling_strategy='auto', k_neighbors=komşu_sayısı)
X_egitim_dengelenmiş, y_egitim_dengelenmiş = smote.fit_resample(X_egitim, y_egitim)

parametre_izgara = {
    'n_estimators': [50, 100, 150],
    'max_depth': [10, 20, 30]
}

model = GridSearchCV(RandomForestClassifier(random_state=42), parametre_izgara, cv=5)
model.fit(X_egitim_dengelenmiş, y_egitim_dengelenmiş)

print(f"En iyi parametreler: {model.best_params_}")


y_tahmin = model.predict(X_test)

print("\nModel Doğruluğu:")
print(accuracy_score(y_test, y_tahmin))
print("\nSınıflandırma Raporu:")
print(classification_report(y_test, y_tahmin, zero_division=0))

joblib.dump(model, 'metin_siniflandirma_model.pkl')
joblib.dump(vektorizer, 'vektorizer.pkl')

print("\nModel ve vektörizer başarıyla kaydedildi.")
