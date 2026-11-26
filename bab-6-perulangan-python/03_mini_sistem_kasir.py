x = 2
z = total_belanja = 0
jumlah_transaksi = 0

persen_diskon = 5 + x
batas_diskon = 50000 + z * 1000

print("=== PARAMETER KASIR ===")
print("persen diskon: ", persen_diskon, "%")
print("batas_diskon: Rp ", batas_diskon)

print("=== DAFTAR MENU ===")
print("1. nasi goreng - Rp12.000")
print("2. mie goreng - Rp10.000")
print("3. es teh - Rp3.000")
print("es jeruk - Rp5.000")
print("0. selesai")
print("=" * 25)

while True:
    pilihan = int(input("\nMasukkan kode menu (0 untuk selesai): "))

    if pilihan == 0:
        break
    elif pilihan == 1:
        harga = 12000
    elif pilihan == 2:
        harga = 10000
    elif pilihan == 3:
        harga = 3000
    elif pilihan == 4:
        harga = 5000
    else:
        print("pilihan menu tidak valid! silahakan pilih kode menu yang tersedia.")
        continue 

    jumlah = int (input("masukkan jumlah pembelian: "))
    if jumlah < 1:
        print("jumlah pembelian minimal 1! transaksi dibatalkan.")
        continue

    subtotal = harga * jumlah
    total_belanja += subtotal
    jumlah_transaksi += 1
    print(f"subtotal: Rp{subtotal}")

    if total_belanja >= batas_diskon:
        diskon = total_belanja * persen_diskon // 100
    else:
        diskon = 0

    total_bayar = total_belanja - diskon


    print("\n=== RINGKASA PEMBAYARAN ===") 
    print(f"jumlah transaksi     : {jumlah_transaksi}")   
    print(f"total sebelum diskon  : Rp{total_belanja}") 
    print(f"diskon ({persen_diskon}%)  : Rp{diskon}")
    print(f"total bayar            : Rp{total_bayar}") 
    print("transaksi selesai. terima kasihg!")              