import requests
import csv
from bs4 import BeautifulSoup

#masukan link mau di web scarping
url = "https://"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    news_titles = soup.find_all("h3")

    data = []
    for i, news in enumerate(news_titles, 1):
        title = news.text.strip()
        link = news.find("a")["href"] if news.find("a") else "Tidak ada link"
        data.append([i, title, link])  # Simpan dalam list
    
    # Simpan ke CSV
    with open("baru.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["No", "Judul Berita", "Link"])  # Header
        writer.writerows(data)

    print("Data berhasil disimpan ke baru.csv!")

else:
    print(f"Gagal mengakses situs. Status code: {response.status_code}")
