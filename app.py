import streamlit as st
import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
import seaborn as sns

# Configure page settings
st.set_page_config(page_title="RFM Customer Segmentation Engine", page_icon="🎯", layout="wide")

st.markdown("""
    <style>
    .main-header { font-size:2.5rem; font-weight: 800; color: #0f172a; margin-bottom: 0.5rem; }
    .sub-header { font-size:1.1rem; color: #64748b; margin-bottom: 2rem; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header">🎯 Retail Customer Behavioral RFM Segmentation Engine</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Upload corporate transactional ledgers to instantly compute Recency, Frequency, and Monetary parameters and divide accounts into clear marketing cohorts.</div>', unsafe_allow_html=True)

# Sidebar configurations
st.sidebar.header("📁 Data Ingestion Pipeline")
uploaded_file = st.sidebar.file_uploader("Upload Retail Transaction Logs (CSV)", type=["csv"])

# Function to generate high-quality sample metrics if no file is provided
def get_mock_data():
    np.random.seed(42)
    n_records = 400
    customer_ids = np.random.randint(12000, 18000, size=50)
    
    mock_df = pd.DataFrame({
        'CustomerID': np.random.choice(customer_ids, size=n_records),
        'InvoiceNo': np.random.randint(536365, 581587, size=n_records),
        'Quantity': np.random.randint(1, 12, size=n_records),
        'UnitPrice': np.random.uniform(1.5, 15.0, size=n_records),
        'InvoiceDate': [dt.datetime(2025, 1, 1) + dt.timedelta(days=int(np.random.randint(0, 360))) for _ in range(n_records)]
    })
    mock_df['TotalRevenue'] = mock_df['Quantity'] * mock_df['UnitPrice']
    return mock_df

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
        st.sidebar.success("Custom Dataset Ingested Successfully!")
    except Exception as e:
        st.sidebar.error(f"Error parsing file: {e}")
        df = get_mock_data()
else:
    st.sidebar.info("💡 Displaying baseline analytical dashboard using synthetic retail ledger data. Upload your own file to evaluate custom data.")
    df = get_mock_data()

# Data Preprocessing Logic
df = df.dropna(subset=['CustomerID'])
df['Revenue'] = df['Quantity'] * df['UnitPrice']
snapshot_date = df['InvoiceDate'].max() + dt.timedelta(days=1)

# Compute RFM Parameters
rfm = df.groupby('CustomerID').agg({
    'InvoiceDate': lambda x: (snapshot_date - x.max()).days,
    'InvoiceNo': 'nunique',
    'Revenue': 'sum'
}).rename(columns={'InvoiceDate': 'Recency', 'InvoiceNo': 'Frequency', 'Revenue': 'Monetary'})

# Formulate Scoring Quintiles
rfm['R_Score'] = pd.qcut(rfm['Recency'], 4, labels=[4, 3, 2, 1])
rfm['F_Score'] = pd.qcut(rfm['Frequency'].rank(method='first'), 4, labels=[1, 2, 3, 4])
rfm['M_Score'] = pd.qcut(rfm['Monetary'], 4, labels=[1, 2, 3, 4])

# Calculate Segment Indexes
def segment_cohorts(row):
    score = int(row['R_Score']) + int(row['F_Score']) + int(row['M_Score'])
    if score >= 10:
        return "VIP Champions"
    elif score >= 7:
        return "Core Loyalists"
    elif score >= 5:
        return "Regular Value Shoppers"
    else:
        return "At-Risk / Churn Risk"

rfm['Segment Portfolio'] = rfm.apply(segment_cohorts, axis=1)

# Layout Structure Matrix
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total Revenue Transacted", f"${df['Revenue'].sum():,.2f}")
with col2:
    st.metric("Unique Customer Accounts", f"{rfm.index.nunique():,}")
with col3:
    st.metric("VIP Champion Accounts", f"{len(rfm[rfm['Segment Portfolio']=='VIP Champions'])}")
with col4:
    st.metric("Avg Order Frequency", f"{rfm['Frequency'].mean():.1f} Orders")

st.markdown("---")

# Data Visualization Matrix Split
v_col1, v_col2 = st.columns(2)

with v_col1:
    st.subheader("📊 Customer Distribution Across Segments")
    fig, ax = plt.subplots(figsize=(7, 4.5))
    segment_counts = rfm['Segment Portfolio'].value_counts()
    colors = ['#10b981', '#2563eb', '#f59e0b', '#ef4444']
    sns.barplot(x=segment_counts.values, y=segment_counts.index, palette=colors, ax=ax)
    ax.set_xlabel("Account Volumes")
    ax.set_ylabel("")
    st.pyplot(fig)

with v_col2:
    st.subheader("💰 Financial Volume Contribution")
    fig, ax = plt.subplots(figsize=(7, 4.5))
    segment_monetary = rfm.groupby('Segment Portfolio')['Monetary'].sum()
    ax.pie(segment_monetary, labels=segment_monetary.index, autopct='%1.1f%%', 
           colors=['#ef4444', '#f59e0b', '#2563eb', '#10b981'], startangle=140,
           wedgeprops={'edgecolor': 'w', 'linewidth': 1})
    st.pyplot(fig)

st.markdown("---")

# Display Segment Data Filter Grid
st.subheader("📋 Segment Explorer Registry")
selected_segment = st.selectbox("Isolate Specific Behavioral Segment Portfolio:", rfm['Segment Portfolio'].unique())
st.dataframe(rfm[rfm['Segment Portfolio'] == selected_segment][['Recency', 'Frequency', 'Monetary', 'Segment Portfolio']].style.format({
    'Monetary': '${:,.2f}'
}), use_container_width=True)
