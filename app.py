import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Parcl Buyer Segmentation", layout="wide")

df = pd.read_csv("clients_segmented.csv")

st.title("Parcl Buyer Segmentation Dashboard")

st.sidebar.header("Filters")
country = st.sidebar.multiselect("Country", sorted(df["country"].unique()))
region = st.sidebar.multiselect("Region", sorted(df["region"].unique()))
purpose = st.sidebar.multiselect("Acquisition Purpose", sorted(df["acquisition_purpose"].unique()))
client_type = st.sidebar.multiselect("Client Type", sorted(df["client_type"].unique()))
segment = st.sidebar.multiselect("Segment", sorted(df["segment_label"].unique()))

filtered = df.copy()
if country:
    filtered = filtered[filtered["country"].isin(country)]
if region:
    filtered = filtered[filtered["region"].isin(region)]
if purpose:
    filtered = filtered[filtered["acquisition_purpose"].isin(purpose)]
if client_type:
    filtered = filtered[filtered["client_type"].isin(client_type)]
if segment:
    filtered = filtered[filtered["segment_label"].isin(segment)]
st.sidebar.write(f"{len(filtered)} / {len(df)} clients shown")

tab1, tab2, tab3, tab4 = st.tabs(["Overview", "Investor Behavior", "Geographic", "Segment Insights"])

with tab1:
    st.subheader("Cluster Distribution")
    dist = filtered["segment_label"].value_counts().reset_index()
    dist.columns = ["Segment", "Count"]
    st.plotly_chart(px.pie(dist, names="Segment", values="Count"), use_container_width=True)

with tab2:
    st.subheader("Average Spend by Segment")
    spend = filtered.groupby("segment_label")["total_spend"].mean().reset_index()
    st.plotly_chart(px.bar(spend, x="segment_label", y="total_spend"), use_container_width=True)

with tab3:
    st.subheader("Clients by Country")
    geo = filtered["country"].value_counts().reset_index()
    geo.columns = ["Country", "Clients"]
    st.plotly_chart(px.bar(geo, x="Country", y="Clients"), use_container_width=True)

with tab4:
    st.subheader("Full Client Table")
    st.dataframe(filtered)