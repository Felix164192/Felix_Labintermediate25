def main(kata):
        ditebak = []
        kesempatan = 6
        tebak = '_' * len(kata)
        hangman = ['''
________
    |   |     
        |
        |
        |
        |''','''
________
    |   |
    O   |
        |
        |
        |''','''
________
    |   |
    O   |
    |   |
        |
        |''','''
________
    |   |
    O   |
    |\  |
        |
        |''','''
________
    |   |
    O   |
   /|\  |
        |
        |''','''
________
    |   |
    O   |
   /|\  |
   /    |
        |''','''
________
    |   |
    O   |
   /|\  |
   / \  |
        |''']
        print(hangman[0])
        print('Welcome to Tebak Kata')
        
        while kesempatan > 0 and "_" in tebak:
            print (f"Tebak kata berikut:{tebak}")
            print (f"Kesempatan tersisa: {kesempatan}")

            nebak = input("Masukkan satu huruf: ").lower()
            if not nebak.isalpha() or len(nebak) != 1:
                print("Masukkan hanya satu huruf (a-z).")
                continue

            if nebak in ditebak: 
                print(f"Huruf {nebak} sudah ditebak.")
                continue

            ditebak = ditebak + [nebak]
            tebak_baru = ''
            for i in kata:
                if i in ditebak:
                    tebak_baru += i
                else:
                    tebak_baru += '_'
            tebak = tebak_baru
            
            if nebak in kata:
                print(f"Benar, huruf {nebak} ada dalam kata.")
            else:
                kesempatan -= 1
                print(f"Salah, huruf {nebak} tidak ada dalam kata.")
                print(hangman[6 - kesempatan])

        if "_" not in tebak:
            print(f"Selamat! Kamu menebak kata '{kata}' dengan benar!")
        else:
            print(f"Kamu kalah. Kata yang benar adalah '{kata}'.")   

main("business")
