# Membuat Biodata Mahasiswa
Nama = []
NIM = []
Fakultas = []
Prodi = []
TTL = []
Gender = []
Umur = []
Alamat = []
data = int(input('Berapa banyak biodata yang ingin Anda buat? '))
for i in range(data):
    a = input('Nama mahasiswa: ')
    Nama.append(a)
    b = input('NIM mahasiswa: ')
    NIM.append(b)
    c = input('Nama Fakultas mahasiswa: ')
    Fakultas.append(c)
    d = input('Nama Program Studi mahasiswa: ')
    Prodi.append(d)
    e = input('Tempat tanggal lahir mahasiswa: ')
    TTL.append(e)
    f = input('Jenis Kelamin mahasiswa: ')
    Gender.append(f)
    g = input('Umur mahasiswa: ')
    Umur.append(g)
    h = input('Alamat mahasiswa: ')
    Alamat.append(h)
for i in range(data):
    print('')
    print('         BIODATA MAHASISWA         ')
    print('===================================')
    print('Nama                 :', Nama[i])
    print('NIM                  :', NIM[i])
    print('Fakultas             :', Fakultas[i])
    print('Program Studi        :', Prodi[i])
    print('Tempat tanggal lahir :', TTL[i])
    print('Jenis Kelamin        :', Gender[i])
    print('Umur                 :', Umur[i])
    print('Alamat               :', Alamat[i])
    print('===================================') 