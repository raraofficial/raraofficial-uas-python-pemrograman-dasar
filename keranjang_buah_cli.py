def beli_buah():
    try:
        jumlah_buah = int(input("Masukkan jumlah jenis buah yang akan anda beli: "))
        keranjang = []
        for i in range(1, jumlah_buah+1):
            buah = input(f"Masukkan Jenis Buah Pada Keranjang {i}: ")
            keranjang.append(buah)

        while True:
            try:
                index = int(input("Lihat buah pada keranjang urutan ke: "))
                if index <= len(keranjang):
                    print(f"Buah pada urutan ke {index}: {keranjang[index-1]}")
                else:
                    print("PERINGATAN: Buah pada urutan tersebut tidak tersedia")
            except ValueError:
                print("PERINGATAN: Masukan jumlah bilangan bulat, bukan string")
            else:
                break
    except ValueError:
        print("PERINGATAN: Masukan jumlah bilangan bulat, bukan string")

beli_buah()