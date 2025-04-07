import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re

def extract_logo_urls(url_list):
    logo_images = {}
    headers = {'User-Agent': 'Mozilla/5.0'}

    for url in url_list:
        try:
            if not url.startswith(('http://', 'https://')):
                site_url = 'http://' + url
            else:
                site_url = url

            resp = requests.get(site_url, headers=headers, timeout=10)
            soup = BeautifulSoup(resp.text, 'html.parser')
        except Exception as e:
            print(f"[Error] {url} - {e}")
            continue

        logo_img_url = None

        img_tags = soup.find_all('img')
        for img in img_tags:
            src = img.get('src', '')
            alt = img.get('alt', '')
            if re.search(r'logo', src, re.IGNORECASE) or re.search(r'logo', alt, re.IGNORECASE):
                logo_img_url = urljoin(site_url, src)
                break

        if not logo_img_url:
            logo_img_url = urljoin(site_url, '/favicon.ico')

        logo_images[url] = logo_img_url

    print(f"Found logos for  {len(logo_images)} websites.")
    return logo_images
