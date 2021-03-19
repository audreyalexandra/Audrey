#membuat dictionary

dict = {'Name': 'Audrey', 'Hobi1': 'Nonton', 'Hobi2': 'Jalan-jalan', 'Hobi3': 'Ngemil', 'Line': 'audrey.18', 'Instagram': 'audreyalexandraa', 'Snapchat': 'ordryy', 'Lagu1': 'Say Something', 'Lagu2': 'Fix You', 'Lagu3': 'Hall Of Fame', 'Lagu4': 'Supermarket Flowers', 'Makanan1': 'Nasi bebek', 'Makanan2': 'Martabak', 'Makanan3': 'Cumi Tepung'}

print(dict)

# Mengubah Hobi dan Sosial media
dict['Hobi2'] = 'Jalan-jalan'
dict['Sosmed1'] = 'Line: @audrey.18'
print(dict)

#menghapus dua makanan favorit

del dict['Makanan1']
del dict['Makanan2']

print(dict)
# Menambah 1 hobi baru
dict['Hobi4'] = 'Main game'
print(dict)