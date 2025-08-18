
# Smart Space Management Dashboard

This project demonstrates a proof-of-concept for AI-driven warehouse space optimization using synthetic data and Streamlit.

## Features

- Real-time simulation of SKU and zone data
- ABC classification of inventory
- KPI calculations:
  - Storage Utilization Rate
  - Inventory Consolidation Index
  - Average Pick Time
  - Slotting Accuracy
  - ABC Zone Efficiency
  - Space Cost per Unit Stored
- AI agent recommendations for each KPI

## How to Run

1. Clone the repository
2. Install dependencies: `pip install streamlit pandas`
3. Run the dashboard: `streamlit run dashboard.py`

## Files

- `dashboard.py`: Streamlit dashboard code
- `synthetic_sku_data.csv`: Simulated SKU data
- `synthetic_zone_data.csv`: Simulated zone data
- `classified_sku_data.csv`: ABC-classified SKU data
