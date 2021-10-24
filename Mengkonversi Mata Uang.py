# Mengkonversi mata uang 
def print_menu():
    print("Menu Pilihan:")
    print("[1] IDR - USD")
    print("[2] IDR - SGD")
    print("[3] IDR - EUR")
    print("[4] IDR - JPY")
    print("[0] Keluar")
# Program Utama
print("Mengkonversi Mata Uang Rupiah (IDR)")
print("=======================================")
loop = 1
while loop == 1:
    print_menu()
    print("=======================================")
    pilihan = int(input("Nomor Menu Pilihan Anda? "))
    print("=======================================")
    if pilihan == 1:
        print("=====IDR-USD=====")
        IDR = int(input("Jumlah Uang Yang Ingin Anda Konversikan: Rp "))
        USD = IDR/14203.15
        print("Jumlah Total Uang Yang Telah Dikonversikan sebesar $ ", USD)
    elif pilihan == 2:
        print("=====IDR-SGD=====")
        IDR = int(input("Jumlah Uang Yang Ingin Anda Konversikan: Rp "))
        SGD = IDR/10532.42
        print ("Jumlah Total Uang Yang Telah Dikonversikan sebesar S$ ", SGD)
    elif pilihan == 3:
        print("=====IDR-EUR=====")
        IDR = int(input("Jumlah Uang Yang Ingin Anda Konversikan: Rp "))
        EUR = IDR/16529.89
        print("Jumlah Total Uang Yang Telah Dikonversikan sebesar € ", EUR)
    elif pilihan == 4:
        print("=====IDR-JPY=====")
        IDR = int(input("Jumlah Uang Yang Ingin Anda Konversikan: Rp "))
        JPY = IDR/125.18
        print("Jumlah Total Uang Yang Telah Dikonversikan sebesar ¥ ", JPY)
    elif pilihan == 0:
        print("Terima Kasih Telah Menggunakan Program Kami")
        loop = 0
    else:
        print("Nomor Pilihan Yang Anda Masukkan Tidak Valid")