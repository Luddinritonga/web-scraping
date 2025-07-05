import requests
import csv
from bs4 import BeautifulSoup

# Fungsi untuk mengambil data dari halaman
def scrape_page(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        films = soup.find_all("div", class_="item movie")

        data = []
        for i, film in enumerate(films, 1):
            title_tag = film.find("h2")
            category_tag = film.find("span", class_="moket")
            link_tag = film.find("a")

            title = title_tag.text.strip() if title_tag else "N/A"
            category = category_tag.text.strip() if category_tag else "N/A"

            # Mengambil link
            link = link_tag['href'] if link_tag and 'href' in link_tag.attrs else "N/A"

            data.append([i, title, category, link])  # Menghilangkan "playing"

        return data, soup
    else:
        print(f"Gagal mengakses situs. Status code: {response.status_code}")
        return [], None

#masukan link mau di web scarping
url = ""

# Menyimpan data ke file CSV
with open("film_list.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["No", "Judul Film", "Genre", "Link"])  # Mengubah header sesuai permintaan

    page_number = 1
    while True:
        print(f"Scraping halaman {page_number}...")
        data, soup = scrape_page(url)
        
        if not data:
            break

        writer.writerows(data)

        # Mencari link ke halaman berikutnya
        next_page = soup.find("a", string="Next")  # Gunakan string bukan text
        if next_page and 'href' in next_page.attrs:
            url = next_page['href']
            page_number += 1
        else:
            print("Tidak ada halaman berikutnya.")
            break

print("Data berhasil disimpan ke film_list.csv!")
