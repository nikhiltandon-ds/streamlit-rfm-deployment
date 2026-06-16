# Retail RFM Customer Segmentation - Streamlit Application
## Live Application

🚀 Streamlit App:
https://retail-rfm-segmentation.streamlit.app

### Project Overview
#### Data Analytics Advanced Portfolio Additions

This module adds advanced analytics components to your data analytics workspace repository, highlighting your skills in time-based modeling and cloud dashboard engineering.

## 📁 Repository Integration Blueprint
To integrate these updates into your portfolio repository, save the files in the following directory layout:

```text
├── 📊 Time_Series_Forecasting/
│   ├── time_series_forecasting_report.html  <-- Premium Web Analytics Summary Report
│   └── Sales_Forecasting_Engine.ipynb      <-- Data Prep, Stationarity Validation & ARIMA Steps
├── 🚀 Streamlit_RFM_Deployment/
│   ├── app.py                               <-- Active Streamlit Python App Implementation Code
│   ├── requirements.txt                     <-- Cloud Infrastructure App Dependencies
│   └── retail_rfm_streamlit_app.html        <-- App Portfolio Documentation Report Page
└── README.md                                <-- Core Project Reference Summary
```

---

## ⚡ 1. Retail Monthly Sales Forecasting Engine
* **Directory Folder:** `📊 Time_Series_Forecasting/`
* **Core Analytics Report Document:** `time_series_forecasting_report.html`

### Technical Summary
* **Pipeline Infrastructure:** Resampled multi-year transaction databases into equidistant month-start date series (`.resample('MS').sum()`).
* **Stationarity Tests:** Conducted Augmented Dickey-Fuller (ADF) checks to evaluate time-series variance and applied structural transformations to remove trend variations.
* **Algorithmic Evaluation:** Compared classical statistical parameters (**SARIMAX**) against structural additive frameworks (**Facebook Prophet**). Minimizing structural errors yielded an optimal baseline validation **MAPE of 4.28%**.
* **Business Impact:** Provides logistics controllers with reliable forward-demand estimates, reducing stockout risks and optimizing warehouse space allocation ahead of peak sales seasons.

---

## 🎯 2. Interactive Streamlit RFM Application Hub
* **Directory Folder:** `🚀 Streamlit_RFM_Deployment/`
* **Production Deployment Code File:** `app.py`
* **App Infrastructure Configuration File:** `requirements.txt`
* **Core Application Showcase Document:** `retail_rfm_streamlit_app.html`

### Technical Summary
* **App Features:** Developed a responsive data interface using the Streamlit cloud framework. Includes an integrated drag-and-drop tool for uploading CSV files, automatic validation routines, and interactive metric filters.
* **Engine Core:** Automatically computes Recency, Frequency, and Monetary (RFM) values from raw customer data. It groups customer accounts into four clear target tiers: *VIP Champions*, *Core Loyalists*, *Regular Value Shoppers*, and *At-Risk accounts*.
* **Visual Presentation:** Uses integrated seaborn and matplotlib elements to generate real-time charts that update automatically as filtering criteria change.

---

## 🚀 Live Cloud Deployment Setup (Streamlit Community Cloud)
To publish your interactive `app.py` dashboard onto a public web URL for recruiters:
1. Commit `app.py` and `requirements.txt` to your public GitHub repository.
2. Log into [Streamlit Community Cloud](https://share.streamlit.io/) using your GitHub account link.
3. Click the **"New App"** button in the dashboard view.
4. Select your portfolio repository name, match the source branch to `main`, and enter `🚀 Streamlit_RFM_Deployment/app.py` into the main file path block.
5. Click **"Deploy"**. Your application will build automatically and generate a live public URL (e.g., `https://your-app.streamlit.app`) to add to your resume.
