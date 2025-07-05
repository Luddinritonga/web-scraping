import requests
from bs4 import BeautifulSoup

#masukan link mau di web scarping
url = "https://"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Ambil semua judul berita
    news_titles = soup.find_all("h3")  # Ganti tag sesuai struktur website

    for i, news in enumerate(news_titles, 1):
        print(f"{i}. {news.text.strip()}")  # Menampilkan teks berita
else:
    print(f"Gagal mengakses situs. Status code: {response.status_code}")
