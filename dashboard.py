import streamlit as st
import boto3
import pandas as pd
import plotly.express as px

# 1. Page Configuration
st.set_page_config(page_title="Global Logistics Telemetry", page_icon="📊", layout="wide")
st.title("🛰️ Real-Time Supply Chain & Logistics Dashboard")
st.markdown("Retrieving live inventory processing events directly from Amazon DynamoDB telemetry layers.")

# 2. Secure Cloud Data Extraction Loop
@st.cache_data(ttl=5) # Refreshes and updates data cache every 5 seconds
def fetch_cloud_metrics():
    try:
        # Connects natively to your active AWS configuration
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
        table = dynamodb.Table('LogisticsInventoryMetrics')
        
        # Scan and pull active data rows
        response = table.scan()
        data = response.get('Items', [])
        
        if not data:
            return pd.DataFrame(columns=["timestamp", "item", "warehouse", "quantity_delta", "status"])
            
        df = pd.DataFrame(data)
        df['quantity_delta'] = df['quantity_delta'].astype(int)
        return df
    except Exception as e:
        st.error(f"⚠️ Unable to query AWS Backend Datastore: {e}")
        return pd.DataFrame()

# Execute Extraction
df = fetch_cloud_metrics()

if df.empty:
    st.info("🔄 Awaiting cloud data payloads... Launch your pipeline to view telemetry data.")
else:
    # 3. High-Density High-Level Metrics Layout
    total_events = len(df)
    total_restocks = len(df[df['status'] == '📉 RESTOCK REQ'])
    total_inbound = len(df[df['status'] == '📈 INBOUND'])
    
    col1, col2, col3 = st.columns(3)
    col1.metric("📦 Total Logged Events", total_events)
    col2.metric("📉 Active Restock Requests", total_restocks, delta="-Alerts active", delta_color="inverse")
    col3.metric("📈 Inbound Freight Actions", total_inbound)

    # 4. Interactive Data Visualizations
    st.markdown("---")
    left_chart, right_chart = st.columns(2)
    
    with left_chart:
        st.subheader("🏭 Distribution Hub Load Balancing")
        fig_bar = px.bar(df, x='warehouse', y='quantity_delta', color='status', title="Inventory Deltas Across Warehouses")
        st.plotly_chart(fig_bar, use_container_width=True)
        
    with right_chart:
        st.subheader("📋 Inbound Logs Audit Stream")
        st.dataframe(df.sort_values(by="timestamp", ascending=False), use_container_width=True)
