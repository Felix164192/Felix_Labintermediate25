import random

while True:
    listkata = ['prasmul','teknologi','computer','digital','bisnis']
    kata = random.choice(listkata)
    kesempatan = 5
    menebak = []
    print('Welcome to Tebak Kata'.center(40))
    print('Selamat'.center(40))
    print('Berjuang!!!'.center(40))
    print('Sukses'.center(40))
    print('Tebak kata berikut ini:', '_' * len(kata))

    while kesempatan > 0:
        tampilkan = ''
        for huruf in kata:
            if huruf in menebak:
                tampilkan += huruf
            else:
                tampilkan += '_'
        print('Kesempatan kamu:', kesempatan)
        print('Kata:', tampilkan)
        
        if '_' not in tampilkan:
            print('Horee kamu menang!!!'.center(40))
            break
        tebak = input("Tebak: ").lower()

        if tebak in menebak:
            print('Huruf sudah ditebak!')
            continue
        menebak.append(tebak)

        if tebak not in kata:
            kesempatan -= 1

    if kesempatan == 0:
        print('Kamu belum berhasil, coba lagi ya'.center(40))
        ulang = input('Mau main lagi? (y/n): ').lower()
        if ulang != 'y':
            print('Terima kasih sudah bermain!')
            break
    else:
        break
