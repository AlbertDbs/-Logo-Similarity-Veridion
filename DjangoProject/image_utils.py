import requests
from PIL import Image
from io import BytesIO
import numpy as np
import imagehash
import os

def download_and_process_logos(logo_map):
    processed = {}

    if not os.path.exists("output_logos"):
        os.makedirs("output_logos")

    for site, img_url in logo_map.items():
        try:
            resp = requests.get(img_url, timeout=10)
            img = Image.open(BytesIO(resp.content)).convert('L')
            img = img.resize((128, 128))
            img_array = np.array(img) / 255.0
            processed[site] = img_array

            safe_name = site.replace("/", "_")
            img.save(f"output_logos/{safe_name}.png")

        except Exception as e:
            print(f"[Skip] {site} - {e}")
            continue
    return processed

def extract_features(processed_logos):
    features = {}
    for site, img in processed_logos.items():
        img_pil = Image.fromarray((img * 255).astype('uint8'))
        hash_val = imagehash.phash(img_pil)
        hist, _ = np.histogram(img, bins=256, range=(0.0, 1.0))
        hist = hist / hist.sum()
        features[site] = {'hash': hash_val, 'hist': hist, 'img': img}
    return features
