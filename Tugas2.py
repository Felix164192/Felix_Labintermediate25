kata = ('halo')
tebak = ['_']*len(kata)
kesempatan = 6
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
print('Tebak kata dengan jumlah huruf', len(kata))

sudah = []
while kesempatan > 0:
    huruf = input('Tebak:')
    
    if not huruf.isalpha() and huruf.islower():
        print('Input hanya boleh a-z')
        continue

    if huruf in sudah:
        print('Huruf sudah ditebak')
        continue
    sudah += [huruf]
    kesempatan -= 1

    for i in range(len(kata)):
        if kata[i] == huruf:
            tebak[i] = huruf

    print(hangman[6 - kesempatan])

    print("Kata:", end=" ")
    for x in tebak:
        print(x, end=" ")
    print()

if "_" not in tebak:
    print("Kamu Menang")
else:
    print("Kamu Kalah Katanya:", kata)