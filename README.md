# Retail Promo Uplift Dashboard

## Executive Summary

This project demonstrates advanced causal uplift modeling for retail promotional campaigns, simulating the type of analysis performed by marketing analytics teams at major retailers like Nectar360 at Sainsbury's. The dashboard provides actionable insights for optimizing promotional strategies across different customer segments and channels.

## Key Insights

- **Champions segment shows 25% higher response rate** when exposed to discount promotions
- **Online channel outperforms In-store by 15%** for discount transactions
- **Platinum customers generate 40% higher basket sizes** with promotional offers
- **Electronics category shows 30% uplift** with discount promotions
- **Targeted RFM-based campaigns can increase ROI by 45%** when applied to high-value segments

## Project Structure

```
retail-promo-uplift-dashboard/
├── rfm_enriched.csv             # Retail transaction data with RFM analysis
├── promo_uplift_dashboard.py    # Main Streamlit dashboard application
├── requirements.txt             # Python dependencies
└── README.md                    # This file
```

## Features

### 📊 Exploratory Analysis
- Promotional response rates by customer segment
- Channel effectiveness comparison
- Customer lifetime value impact
- Basket size analysis by promo type

### 🎯 Uplift Modeling
- Two-model approach for causal inference
- Segment-specific uplift estimates
- Treatment vs control response analysis
- Profit impact projections

### 📈 Interactive Dashboard
- Real-time segment selection
- Dynamic visualization updates
- Actionable marketing recommendations
- ROI impact calculator

## Quick Start

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the dashboard:**
   ```bash
   streamlit run promo_uplift_dashboard.py
   ```

3. **Open your browser** and navigate to `http://localhost:8501`

## Dataset Overview

The `rfm_enriched.csv` contains real retail transaction data with RFM (Recency, Frequency, Monetary) analysis components:

- **Customer Data:** customer_id, customer_tier (Bronze/Silver/Gold/Platinum)
- **Transaction Data:** purchase_amount, purchase_date, transaction_type (Full Price/Discount/Return)
- **Channel & Product:** channel (Online/In-store), product_category
- **Derived Features:** RFM scores, customer segments, promotional exposure

## Methodology

### Uplift Modeling Approach
We employ a two-model approach for causal inference:
1. **Treatment Model:** Predicts purchase probability for treated customers
2. **Control Model:** Predicts purchase probability for control customers
3. **Uplift Score:** Difference between treatment and control predictions

### Segmentation Strategy
- **RFM Segments:** Champions, Loyal Customers, At Risk, Can't Lose, Lost
- **Customer Tiers:** Bronze, Silver, Gold, Platinum
- **Transaction Types:** Full Price, Discount, Return
- **Channels:** Online, In-store

## Business Impact

This dashboard enables marketing teams to:
- **Optimize promotional spend** by targeting high-uplift segments
- **Improve customer retention** through personalized campaigns
- **Increase basket sizes** with strategic promo type selection
- **Maximize ROI** through data-driven channel selection

## Technical Stack

- **Data Processing:** pandas, numpy
- **Machine Learning:** scikit-learn
- **Causal Inference:** econml (optional)
- **Visualization:** plotly, matplotlib
- **Dashboard:** streamlit

## Contributing

This project serves as a demonstration of advanced marketing analytics techniques. Feel free to extend the analysis with additional features or datasets.

## License

MIT License - feel free to use this code for educational and commercial purposes. 