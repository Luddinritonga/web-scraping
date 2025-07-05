import requests
import csv
from bs4 import BeautifulSoup

#masukan link mau di web scarping
base_url = "https://"  # Cek struktur pagination situs
max_pages = 5  # Ubah sesuai kebutuhan

# Tambahkan headers agar tidak terdeteksi sebagai bot
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

data = []

for page in range(1, max_pages + 1):
    url = f"{base_url}{page}"  
    response = requests.get(url, headers=headers)  # Tambahkan headers

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        news_titles = soup.find_all("h2")  # Sesuaikan dengan struktur HTML

        if not news_titles:
            print(f"Tidak ada berita di halaman {page}, mungkin struktur berubah.")
            continue

        for news in news_titles:
            title = news.text.strip()
            link = news.find("a")["href"] if news.find("a") else "Tidak ada link"
            data.append([title, link])  

        print(f"✅ Berhasil mengambil halaman {page}")

    else:
        print(f"❌ Gagal mengambil halaman {page}, status: {response.status_code}")

# Simpan ke CSV
with open("berita_pagination.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Judul Berita", "Link"])
    writer.writerows(data)

print("Scraping selesai! Data disimpan ke berita_pagination.csv")
