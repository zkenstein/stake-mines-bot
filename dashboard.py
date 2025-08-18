
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Smart Space Management Dashboard", layout="wide")

st.title("📦 Smart Space Management: AI-Driven Warehouse Space Optimization")

# Load data
sku_data = pd.read_csv("synthetic_sku_data.csv")
zone_data = pd.read_csv("synthetic_zone_data.csv")
classified_data = pd.read_csv("classified_sku_data.csv")

# Sidebar KPI selection
kpi_options = [
    "Storage Utilization Rate (%)",
    "Inventory Consolidation Index",
    "Average Pick Time (seconds/order)",
    "Slotting Accuracy (%)",
    "ABC Zone Efficiency (%)",
    "Space Cost per Unit Stored"
]
selected_kpis = st.sidebar.multiselect("Select KPIs to Display", kpi_options, default=kpi_options)

# KPI Calculations
total_capacity = zone_data['Capacity'].sum()
total_utilization = zone_data['Current_Utilization'].sum()
storage_utilization = (total_utilization / total_capacity) * 100

consolidation_index = 100 - (classified_data.groupby('Category')['Zone_ID'].nunique().mean() / len(zone_data)) * 100
average_pick_time = classified_data['Pick_Time_sec'].mean()
slotting_accuracy = (classified_data['ABC_Category'] == classified_data['ABC_Category']).mean() * 100
abc_efficiency = classified_data.groupby('ABC_Category')['Demand_Score'].mean().to_dict()
space_cost_per_unit = round(1000 / total_utilization, 2)

# Display KPIs
st.subheader("📊 Key Performance Indicators")
if "Storage Utilization Rate (%)" in selected_kpis:
    st.metric("Storage Utilization Rate (%)", f"{storage_utilization:.2f}")
    st.info("Recommendation: Optimize zone usage by redistributing low-demand SKUs.")

if "Inventory Consolidation Index" in selected_kpis:
    st.metric("Inventory Consolidation Index", f"{consolidation_index:.2f}")
    st.info("Recommendation: Consolidate similar SKUs into fewer zones.")

if "Average Pick Time (seconds/order)" in selected_kpis:
    st.metric("Average Pick Time (seconds/order)", f"{average_pick_time:.2f}")
    st.info("Recommendation: Prioritize high-demand SKUs in easily accessible zones.")

if "Slotting Accuracy (%)" in selected_kpis:
    st.metric("Slotting Accuracy (%)", f"{slotting_accuracy:.2f}")
    st.info("Recommendation: Re-evaluate slotting strategy based on SKU category and turnover.")

if "ABC Zone Efficiency (%)" in selected_kpis:
    st.write("ABC Zone Efficiency (avg demand score by category):")
    st.write(abc_efficiency)
    st.info("Recommendation: Allocate prime zones to A-category SKUs.")

if "Space Cost per Unit Stored" in selected_kpis:
    st.metric("Space Cost per Unit Stored", f"${space_cost_per_unit}")
    st.info("Recommendation: Phase out low-performing SKUs to reduce cost.")

# Display classified data
with st.expander("🔍 View Classified SKU Data"):
    st.dataframe(classified_data)

# Refresh button
if st.button("🔄 Refresh Data"):
    st.warning("Please restart the app to refresh synthetic data.")
