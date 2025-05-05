# 🌱 Sistem Penyiraman Tanaman Otomatis Menggunakan Logika Fuzzy

Proyek ini adalah implementasi sistem penyiraman tanaman otomatis menggunakan logika fuzzy, yang mempertimbangkan **intensitas cahaya** (lux) dan **kelembapan tanah** (%) untuk menentukan **lama penyiraman** (menit). Sistem dirancang sebagai simulasi sederhana berbasis Python.

## 📌 Fitur Utama
- Menggunakan metode logika fuzzy dengan fungsi keanggotaan linear
- Menangani input tidak pasti secara linguistik, seperti "tanah agak kering"
- Menghasilkan output waktu penyiraman secara adaptif dan fleksibel
- Dapat dikembangkan untuk integrasi dengan IoT atau sensor fisik

## 📊 Input & Output
- **Input 1:** Intensitas cahaya (lux)
- **Input 2:** Kelembapan tanah (%)
- **Output:** Lama penyiraman (menit)

## 🧠 Aturan Fuzzy
1. Jika **cahaya tinggi** dan **tanah kering**, maka **lama penyiraman panjang**
2. Jika **cahaya tinggi** dan **tanah basah**, maka **lama penyiraman pendek**
3. Jika **cahaya rendah** dan **tanah kering**, maka **lama penyiraman sedang**
4. Jika **cahaya rendah** dan **tanah basah**, maka **lama penyiraman pendek**

## 🧮 Metode Defuzzifikasi
Menggunakan metode **centroid** untuk menghitung nilai crisp dari hasil fuzzy.

## 💻 Cara Menjalankan
1. Pastikan Python 3 sudah terinstal
2. Clone repositori ini:
