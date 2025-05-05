import numpy as np
import matplotlib.pyplot as plt

# Fungsi keanggotaan linear naik dan turun
def turun(x, x_min, x_max):
    return np.clip((x_max - x) / (x_max - x_min), 0, 1)

def naik(x, x_min, x_max):
    return np.clip((x - x_min) / (x_max - x_min), 0, 1)

# Fungsi segitiga (untuk visualisasi output fuzzy)
def segitiga(x, a, b, c):
    if a == b:
        left = 1.0 if x == a else 0.0
    else:
        left = (x - a) / (b - a)
    if b == c:
        right = 1.0 if x == b else 0.0
    else:
        right = (c - x) / (c - b)
    return np.clip(min(left, right), 0, 1)

# Fungsi keanggotaan
def cahaya_rendah(x): return turun(x, 0, 5000)
def cahaya_tinggi(x): return naik(x, 3000, 10000)
def tanah_kering(x): return turun(x, 0, 50)
def tanah_basah(x): return naik(x, 30, 100)

# Rentang output penyiraman
def penyiraman_pendek(): return 0, 10
def penyiraman_sedang(): return 5, 20
def penyiraman_panjang(): return 15, 30

# Fungsi inferensi fuzzy
def berkurang(α, z_min, z_max): return z_max - α * (z_max - z_min)
def bertambah(α, z_min, z_max): return α * (z_max - z_min) + z_min

# Input
cahaya = 6200
kelembapan = 40

# Derajat keanggotaan
μ_cahaya_rendah = cahaya_rendah(cahaya)
μ_cahaya_tinggi = cahaya_tinggi(cahaya)
μ_tanah_kering = tanah_kering(kelembapan)
μ_tanah_basah = tanah_basah(kelembapan)

# Cetak derajat keanggotaan
print("=== DERAJAT KEANGGOTAAN ===")
print(f"Intensitas Cahaya Rendah : {μ_cahaya_rendah:.4f}")
print(f"Intensitas Cahaya Tinggi : {μ_cahaya_tinggi:.4f}")
print(f"Kelembapan Kering        : {μ_tanah_kering:.4f}")
print(f"Kelembapan Basah         : {μ_tanah_basah:.4f}")

# Aturan fuzzy
α1 = min(μ_cahaya_tinggi, μ_tanah_kering)
z1 = bertambah(α1, *penyiraman_panjang())

α2 = min(μ_cahaya_tinggi, μ_tanah_basah)
z2 = berkurang(α2, *penyiraman_pendek())

α3 = min(μ_cahaya_rendah, μ_tanah_kering)
z3 = bertambah(α3, *penyiraman_sedang())

α4 = min(μ_cahaya_rendah, μ_tanah_basah)
z4 = berkurang(α4, *penyiraman_pendek())

print("\n=== ATURAN FUZZY ===")
for i, (α, z) in enumerate([(α1, z1), (α2, z2), (α3, z3), (α4, z4)], 1):
    print(f"Rule {i} -> α = {α:.4f}, z = {z:.2f}")

# Defuzzifikasi (metode centroid sederhana)
numerator = α1*z1 + α2*z2 + α3*z3 + α4*z4
denominator = α1 + α2 + α3 + α4
lama_siram = numerator / denominator if denominator != 0 else 0

print(f"\n=== DEFUZZIFIKASI ===")
print(f"Lama Penyiraman (menit): {lama_siram:.2f} menit")

# Visualisasi
x_cahaya = np.linspace(0, 10000, 200)
x_kelembapan = np.linspace(0, 100, 200)
x_output = np.linspace(0, 30, 200)

plt.figure(figsize=(15, 4))

# Plot Intensitas Cahaya
plt.subplot(1, 3, 1)
plt.plot(x_cahaya, [cahaya_rendah(x) for x in x_cahaya], label='Rendah')
plt.plot(x_cahaya, [cahaya_tinggi(x) for x in x_cahaya], label='Tinggi')
plt.axvline(cahaya, color='red', linestyle='--', label=f'Input = {cahaya} lux')
plt.title('Fungsi Keanggotaan Cahaya')
plt.xlabel('Cahaya (lux)')
plt.ylabel('Derajat')
plt.legend()
plt.grid(True)

# Plot Kelembapan
plt.subplot(1, 3, 2)
plt.plot(x_kelembapan, [tanah_kering(x) for x in x_kelembapan], label='Kering')
plt.plot(x_kelembapan, [tanah_basah(x) for x in x_kelembapan], label='Basah')
plt.axvline(kelembapan, color='red', linestyle='--', label=f'Input = {kelembapan}%')
plt.title('Fungsi Keanggotaan Kelembapan')
plt.xlabel('Kelembapan (%)')
plt.ylabel('Derajat')
plt.legend()
plt.grid(True)

# Plot Output
plt.subplot(1, 3, 3)
plt.plot(x_output, [turun(x, *penyiraman_pendek()) for x in x_output], label='Pendek')
plt.plot(x_output, [naik(x, *penyiraman_sedang()) for x in x_output], label='Sedang')
plt.plot(x_output, [naik(x, *penyiraman_panjang()) for x in x_output], label='Panjang')
plt.axvline(lama_siram, color='red', linestyle='--', label=f'Output = {lama_siram:.2f} menit')
plt.title('Lama Penyiraman')
plt.xlabel('Waktu (menit)')
plt.ylabel('Derajat')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
