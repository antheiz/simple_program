"""
Fungsi untuk Mengurutkan Bilangan Terkecil sampai yang terbesar.
Dan Fungsi untuk Mencari Nilai Tengah, Nilai Rata-rata dan Hasil 
Perkalian Semua Bilangan. 
"""

def urutan_angka(data):
    return sorted(data)

def nilai_rata2(data):   
    return sum(data) / len(data)

def nilai_tengah(data):
  data.sort()
  n = len(data) # ambil panjang data
  nilai_tengah = n // 2 # dibulatkan ke bawah

  # jika n adalah ganjil
  if n % 2 == 1:
    return data[nilai_tengah]

  # jika n genap
  return (data[nilai_tengah - 1] + data[nilai_tengah]) / 2


def hasil_perkalian(data):
    return sum(data)
