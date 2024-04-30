from collections import namedtuple

# Membuat definisi namedtuple untuk mahasiswa
Mahasiswa = namedtuple('Mahasiswa', ['nama', 'umur', 'jurusan', 'nilai'])

# Mendefinisikan fungsi untuk menghitung IPK
def hitung_ipk(nilai):
    return sum(nilai) / len(nilai)

# Fungsi untuk menentukan status mahasiswa
def status_mahasiswa(ipk):
    if ipk >= 3.5:
        return 'Cum Laude'
    elif ipk >= 3.0:
        return 'Lulus'
    else:
        return 'Perlu Perbaikan'

# Membuat instance namedtuple Mahasiswa
Mahasiswa1 = Mahasiswa(nama='Zidan', umur=20, jurusan='TRE', nilai=[3.5, 3.2, 3.4, 4.0])
Mahasiswa2 = Mahasiswa(nama='Alya', umur=21, jurusan='TRI', nilai=[3.2, 3.9, 3.8, 3.6])

# Menghitung IPK untuk setiap mahasiswa
ipk_mhs1 = hitung_ipk(Mahasiswa1.nilai)
ipk_mhs2 = hitung_ipk(Mahasiswa2.nilai)

# Menampilkan informasi tentang setiap mahasiswa
print(f"Informasi Mahasiswa 1:\nNama: {Mahasiswa1.nama}\nUmur: {Mahasiswa1.umur}\nJurusan: {Mahasiswa1.jurusan}\nIPK: {ipk_mhs1}\nStatus: {status_mahasiswa(ipk_mhs1)}\n")
print(f"Informasi Mahasiswa 2:\nNama: {Mahasiswa2.nama}\nUmur: {Mahasiswa2.umur}\nJurusan: {Mahasiswa2.jurusan}\nIPK: {ipk_mhs2}\nStatus: {status_mahasiswa(ipk_mhs2)}")
