import requests
import csv
from bs4 import BeautifulSoup

#masukan link mau di web scarping
url = "https://"


# Mengirim permintaan HTTP ke situs web dengan User-Agent
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)

# Cek apakah permintaan berhasil
if response.status_code == 200:
    # Parsing HTML menggunakan BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Menemukan semua film dalam kontainer yang sesuai (sesuaikan class di website)
    films = soup.find_all("div", class_="item movie")  # Gunakan class yang sesuai

    # Menyiapkan data untuk disimpan
    data = []
    for i, film in enumerate(films, 1):
        title_tag = film.find("h2")  # Ambil judul film dari <h2>
        category_tag = film.find("span", class_="moket")  # Ambil kategori dari <span>
        link_tag = film.find("a")  # Ambil tautan (link) dari <a>

        # Ambil informasi
        title = title_tag.text.strip() if title_tag else "N/A"
        category = category_tag.text.strip() if category_tag else "N/A"
        
        

        # Untuk link, ambil href dari tag <a>
        link = link_tag['href'] if link_tag and 'href' in link_tag.attrs else "N/A"

        # Menambahkan data ke dalam list
        data.append([i, title, category,  link])  # Menambahkan durasi sebagai pengganti playing

    # Menyimpan ke file CSV
    with open("film_list.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["No", "Judul Film", "Genre", "Link"])  # Header CSV
        writer.writerows(data)

    print("Data berhasil disimpan ke film_list.csv!")

else:
    print(f"Gagal mengakses situs. Status code: {response.status_code}")
