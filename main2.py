import requests
from bs4 import BeautifulSoup

#masukan link mau di web scarping
url = "https://"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    
    news_titles = soup.find_all("h3")  # Cek struktur HTML terbaru

    for i, news in enumerate(news_titles, 1):
        title = news.text.strip()  
        link = news.find("a")["href"] if news.find("a") else "Tidak ada link"  
        print(f"{i}. {title}\n   Link: {link}\n")

else:
    print(f"Gagal mengakses situs. Status code: {response.status_code}")
