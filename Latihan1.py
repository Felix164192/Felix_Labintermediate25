nama1 = 'Bagus'
nama2 = 'Bagas'
nama1,nama2 = nama2, nama1
print (f"nama 1 jadi : {nama1}")
print (f"nama 2 jadi : {nama2}")

tebak_aku = ['a', 'b', 'c', 'd']
tebakaku = input('tebak alphabet aku =')
if tebakaku in tebak_aku:
    print("YES SIR")
else:
    print("OH NO")