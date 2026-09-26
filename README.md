# Parcl Buyer Segmentation & Investment Profiling

Machine learning-based buyer segmentation for real estate market intelligence — 
built for Parcl Co. Limited in collaboration with Unified Mentor.

## Overview

This project segments Parcl's real estate buyers into distinct groups using 
unsupervised machine learning (KMeans + Hierarchical Clustering), based on 
demographic, financing, and transaction behavior. The goal is to move Parcl 
from treating all buyers the same to targeted, segment-aware marketing and 
investment strategies.

## What's in this repo

- `clients.csv` — raw client data (2,000 records)
- `properties.csv` — raw property listing/transaction data (10,000 records)
- `[notebook name].ipynb` — full data science pipeline: cleaning, feature 
  engineering, encoding, clustering, and cluster interpretation
- `clients_segmented.csv` — final output: every client with their assigned 
  segment label
- `elbow_silhouette.png` — chart used to select the optimal number of clusters
- `app.py` — the Streamlit dashboard that visualizes the segments
- `requirements.txt` — Python packages needed to run the dashboard

## Methodology

1. **Data Cleaning** — standardized categorical fields, parsed mixed date 
   formats, cleaned currency-formatted prices, checked referential integrity
2. **Feature Engineering** — aggregated each client's transaction history into 
   behavioral features (spend, units purchased, financing usage, etc.)
3. **Encoding & Scaling** — label encoding, one-hot encoding, and frequency 
   encoding (for high-cardinality region data), followed by StandardScaler
4. **Clustering** — KMeans (primary) validated against Ward Hierarchical 
   Clustering, with cluster count chosen via the Elbow Method and Silhouette 
   Score
5. **Segment Interpretation** — each cluster profiled and labeled based on 
   spend tier, financing behavior, satisfaction, and demographics

## Segments identified

| Segment | Description |
|---|---|
| Luxury / High-Value Buyers | Highest spend, highest satisfaction, oldest average age |
| Leveraged Growth Investors | High spend, highest loan usage, highest unit price |
| Core Market Investors | Largest segment, lowest spend, lowest satisfaction |
| Emerging Mid-Market Buyers | Mid-tier spend, youngest average age |

## Running the dashboard locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Live demo

[Add your Streamlit Cloud deployment link here once deployed]

## Author

[Your name] — Data Analytics Internship Project
