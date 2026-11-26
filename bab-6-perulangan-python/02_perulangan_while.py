x = 2
angka = 1
jumlah_tampil = 0

angka_lewati = x + 1
angka_berhenti = x + 10

print("parameter: ")
print("x:", x)
print("angka_lewati:", angka_lewati)
print("angka_berhenti:", angka_berhenti)
print("-" * 20)

print("contoh program dasar")
while angka <= 10:
    print(angka)
    angka += 1
print("program selesai")

print("perulangan while")
while True:
    if angka == angka_berhenti:
       break

    if angka == angka_lewati:
        angka += 1
        continue

    print(angka)
    jumlah_tampil += 1
    angka += 1

print("-" * 20)   
print("jumlah tampil:", jumlah_tampil) 
print("program selesai.")