# Logo Similarity Clustering – Project Overview

## 🚀 Objective
The goal of this project is to **automatically group websites based on the visual similarity of their logos**. It does so **without using traditional Machine Learning clustering algorithms** like k-means or DBSCAN, relying instead on image processing, similarity metrics, and graph-based grouping.

---

## 🔍 What the Code Does

### 1. **Reads website list**  
It loads a list of websites from a `.parquet` file (`logos.snappy.parquet`) using `pandas`.

### 2. **Scrapes logos from websites**  
For each website, it attempts to identify and download the logo using:
- HTML parsing with `BeautifulSoup`
- Heuristics (looking for `<img>` tags containing `logo` in `alt`, `src`, `class`, or `id`)
- Fallback: `/favicon.ico` if no clear logo is found

### 3. **Preprocesses logos**  
Downloaded images are:
- Converted to grayscale
- Resized to 128×128 pixels
- Normalized to range [0.0, 1.0]
- Saved to the `output_logos/` directory as `.png` files

### 4. **Extracts image features**  
Each image is analyzed with:
- **Perceptual hash (phash)** – shape-based hash
- **Histogram** – grayscale tone distribution
- **SSIM** (Structural Similarity Index) – structure and contrast comparison

### 5. **Compares logos and builds similarity pairs**  
Two logos are considered similar if **2 out of 3** criteria are met:
- Hamming distance between hashes <= 5
- Histogram Bhattacharyya coefficient >= 0.9
- SSIM score >= 0.8

### 6. **Groups similar websites using graph traversal**  
A graph is created where each site is a node, and an edge links sites with similar logos.
DFS is used to find **connected components**, which form the final logo similarity clusters.

### 7. **Outputs results**
- Prints clusters to the terminal
- Saves grouped domains to `grupuri_logo.csv`
- Saves each site’s logo as `output_logos/{domain}.png`

---

## 💡 Why It Works Without Machine Learning
Instead of ML algorithms, this solution:
- Defines visual similarity with deterministic rules
- Uses perceptual hashing and structural metrics
- Applies a custom graph-based grouping method (no k-means or DBSCAN)

This ensures transparency, reproducibility, and interpretability of results, while keeping high accuracy on a real-world dataset of 3000+ websites.

## 🧬Could You Use Genetic Algorithms?
Not used here, but you could! For example:
- Each individual = a way of grouping logos
- Fitness = how consistent logos are in each group
- Apply crossover and mutation to find better partitions


## ✅ How to Test It Quickly
If you don't want to run all 3000+ websites:

Edit `main.py`:
```python
urls = urls[:20]  # Limit to first 20 sites for testing
```
Then run the script and check:
- Saved logos in `output_logos/`
- `groups_logo.csv` output file

## 🏁 Summary
This project demonstrates a reliable, interpretable, and ML-free approach to the hard problem of visual logo clustering across thousands of domains. It is built for scalability and practical real-world application.

