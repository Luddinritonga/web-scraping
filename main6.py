#Contoh membaca CSV dan menyimpannya kembali
#pip install openpyxl

import pandas as pd

# Membaca file CSV
df = pd.read_csv('film_list.csv')

# Menampilkan 5 baris pertama
print(df.head(3))

# Menyimpan kembali ke format lain (misalnya Excel)
df.to_excel('test1.xlsx', index=False)
