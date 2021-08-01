print("======================================================================")
print("| Nama    : Dortheis Andatu                                          |")
print("| NRP     : 05211940007003                                           |")
print("| Jurusan : Sistem Informasi                                         |")
print("| Kampus  : Institut Teknologi Sepuluh Nopember                      |")
print("|                                                                    |")
print("| Masukan deret Bilangan pisahkan dengan Koma. (misalnya: 1,2,3,4,5) |")
print("======================================================================")
print()

# import fungsi
from fungsi import hasil_perkalian, nilai_rata2, nilai_tengah, urutan_angka

# meminta input user
bilangan = input('Masukkan bilangan : ')
print()

# variable untuk menyimpan data dengan tipe list
data = []

""" 
melakukan perulangan dari input user
dan menambah tanda koma lalu ditambah 
ke dalam variable data yang bertipe list
"""
for i in bilangan.split(','):
    data.append(int(i))

# Mencetak Urutan Angka Kecil ke Besar
print("Urutkan angka Kecil ke Besar : ", urutan_angka(data))

# membuat space

# Mencetak Nilai rata-rata
print("Nilai rata-rata : ", nilai_rata2(data))

# Mencetak Nilai tengah
print("Nilai tengah    : ", nilai_tengah(data))

# Mencetak hasil perkalian
print("Hasil perkalian : ", hasil_perkalian(data))
