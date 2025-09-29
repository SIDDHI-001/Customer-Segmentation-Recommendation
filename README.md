# 🛍️ Customer Segmentation & Recommendation System

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](
https://colab.research.google.com/github/SIDDHI-001/Customer-Segmentation-Recommendation/blob/main/Final_Project_Customer_Segmentation.ipynb)


## 📌 Project Overview
This project demonstrates **AI-powered customer segmentation** and **product recommendation** using clustering techniques (K-Means, DBSCAN) and a simple recommendation engine.  

We use the **Retailrocket E-commerce Dataset** from Kaggle to analyze customer behavior and build a recommender system. A small **Flask web app (`app.py`)** is provided for demo purposes.

---

## 📊 Dataset
- **Source**: [Retailrocket Recommender System Dataset](https://www.kaggle.com/datasets/retailrocket/ecommerce-dataset)  
- Contains:
  - `events.csv` → user interactions (view, add-to-cart, purchase)  
  - `item_properties.csv` → product metadata  
  - `category_tree.csv` → product category hierarchy  

⚠️ The dataset is **very large (GBs)**, so it is not uploaded here.  
👉 For quick testing, a **small sample file** is included: `customer_features_sample.csv`.

---

## 🛠️ How to Run the Web App

### 1. Clone the repository
```bash
git clone https://github.com/SIDDHI-001/Customer-Segmentation-Recommendation.git
cd Customer-Segmentation-Recommendation
