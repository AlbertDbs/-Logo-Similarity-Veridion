from logo_scraper import extract_logo_urls
from image_utils import download_and_process_logos, extract_features
from similarity import compute_similarities, cluster_sites
from report import generate_report

import pandas as pd

print("\n Step 1: Reading the Parquet file...")
df = pd.read_parquet("logos.snappy.parquet")
urls = df.iloc[:, 0].dropna().unique().tolist()
print(f" Loaded a total of {len(urls)} URLs.")

print("\n Step 2: Automatically extracting logos from websites...")
logo_map = extract_logo_urls(urls)

print("\n Step 3: Downloading and preprocessing logo images...")
processed_logos = download_and_process_logos(logo_map)

print("\n Step 4: Extracting visual features (phash, histogram)...")
features = extract_features(processed_logos)

print("\n Step 5: Comparing and clustering based on logo similarity...")
similar_pairs = compute_similarities(features)
groups = cluster_sites(features, similar_pairs)

print("\n Step 6: Final groups of websites with similar logos:")
generate_report(groups)
