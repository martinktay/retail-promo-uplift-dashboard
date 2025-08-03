# 📊 Retail Promotional Uplift Dashboard

## 🎯 Business Case Study: Nectar360-Style Marketing Analytics

### Executive Summary

This project demonstrates advanced causal uplift modeling for retail marketing campaigns, similar to the analytical approaches used at **Nectar360 (Sainsbury's)** and other leading retail analytics teams. The dashboard provides data-driven insights for promotional campaign optimization, customer segmentation, and ROI maximization.

**Key Business Impact:**
- **152% uplift** identified for Lapsed Customers through targeted re-engagement campaigns
- **125% uplift** for New Customers with welcome promotions
- **24.96% uplift** for High-Value Existing customers, indicating need for premium strategies
- **Data-driven segmentation** enabling precision marketing and budget allocation

---

## 🏢 Business Context

### The Challenge
Retail companies face increasing pressure to optimize marketing spend while maintaining customer engagement. Traditional A/B testing approaches often fail to capture the true causal impact of promotional campaigns, leading to:
- Suboptimal budget allocation
- Missed opportunities with high-value customer segments
- Inefficient channel mix strategies
- Lack of actionable insights for marketing teams

### The Solution
This dashboard implements **causal uplift modeling** to measure the true incremental impact of promotional campaigns, enabling:
- **Precision targeting** of customer segments with highest uplift potential
- **Channel optimization** based on segment-specific performance
- **Budget allocation** informed by causal impact rather than correlation
- **Actionable recommendations** for marketing strategy refinement

---

## 🚀 Features & Capabilities

### 📈 Advanced Analytics
- **Causal Uplift Modeling**: Two-model approach using Random Forest Classifiers
- **Customer Segmentation**: RFM-based segmentation with behavioral overlays
- **Channel Effectiveness Analysis**: Multi-channel performance comparison
- **Product Category Insights**: Category-specific promotional performance
- **Real-time Filtering**: Dynamic data exploration with interactive filters

### 🎨 Professional Dashboard
- **Interactive Visualizations**: Plotly charts with drill-down capabilities
- **Smart Metrics**: Contextual delta calculations and trend indicators
- **Responsive Design**: Optimized for desktop and tablet viewing
- **British English Localization**: Professional UK market presentation

### 🔧 Technical Excellence
- **Production-Ready Code**: Error handling, caching, and performance optimization
- **Modular Architecture**: Clean separation of data processing, modeling, and visualization
- **Scalable Design**: Easy to extend with additional data sources and models
- **Git Version Control**: Professional development workflow

---

## 📊 Screenshots & Visual Walkthrough

### Dashboard Overview
*[Screenshot 1: Main dashboard with key metrics and insights]*
- **What to capture**: The main dashboard showing the four key metrics (Total Transactions, Promo Exposure Rate, Overall Response Rate, Avg Basket Size) and the Key Insights cards
- **Purpose**: Demonstrates the professional appearance and key business metrics

### Interactive Filters
*[Screenshot 2: Sidebar filters and dropdown selections]*
- **What to capture**: The sidebar showing the clean dropdown filters for Customer Segments, Channels, Promo Types, Product Categories, and Income Range slider
- **Purpose**: Shows the user-friendly filtering interface and data exploration capabilities

### Uplift Analysis Charts
*[Screenshot 3: Uplift analysis visualizations]*
- **What to capture**: The "Uplift Analysis by Customer Segment" section with the bar chart showing uplift percentages and the control vs treatment response rates
- **Purpose**: Demonstrates the core analytical capabilities and causal insights

### Channel & Product Analysis
*[Screenshot 4: Channel and product category charts]*
- **What to capture**: The "Channel & Product Category Analysis" section showing response rates by channel and basket sizes by product category
- **Purpose**: Shows multi-dimensional analysis capabilities

### Detailed Metrics Table
*[Screenshot 5: Detailed uplift metrics table]*
- **What to capture**: The "Detailed Uplift Metrics" table showing comprehensive segment-level performance data
- **Purpose**: Demonstrates the depth of analytical output and data transparency

### Actionable Recommendations
*[Screenshot 6: Marketing recommendations section]*
- **What to capture**: The "Actionable Marketing Recommendations" cards with specific business insights
- **Purpose**: Shows the translation of data into business value and strategic recommendations

---

## 🛠 Technical Implementation

### Technology Stack
- **Frontend**: Streamlit (Python web framework)
- **Data Processing**: Pandas, NumPy
- **Machine Learning**: Scikit-learn (Random Forest Classifiers)
- **Visualization**: Plotly (Interactive charts)
- **Version Control**: Git & GitHub

### Architecture Overview
```
retail-promo-uplift-dashboard/
├── promo_uplift_dashboard.py    # Main application
├── promo_uplift_enriched.csv    # Sample dataset
├── requirements.txt             # Dependencies
├── README.md                    # Documentation
└── .gitignore                   # Version control
```

### Key Functions
- **`load_data()`**: Data loading and preprocessing
- **`calculate_customer_segments()`**: RFM-based segmentation
- **`calculate_uplift_metrics()`**: Causal uplift calculations
- **`create_uplift_model()`**: Machine learning model training
- **`main()`**: Dashboard orchestration and UI

---

## 📈 Business Impact & ROI

### Quantified Results
- **Lapsed Customers**: 152% uplift potential with re-engagement campaigns
- **New Customers**: 125% uplift with welcome promotions
- **Channel Optimization**: SMS shows highest engagement for urgent promotions
- **Product Strategy**: Electronics category demonstrates highest basket size impact

### Strategic Recommendations
1. **Prioritize Lapsed Customer Re-engagement**: Highest ROI segment
2. **Develop New Customer Welcome Series**: Strong conversion potential
3. **Optimize Channel Mix**: SMS for urgent, Email for relationship building
4. **Category-Specific Promotions**: Electronics focus for basket size growth

---

## 🎯 For Recruiters & Hiring Managers

### Professional Profile
This project demonstrates **senior-level data science capabilities** in:
- **Causal Inference**: Advanced uplift modeling beyond correlation analysis
- **Business Acumen**: Translation of technical insights into strategic recommendations
- **Full-Stack Development**: End-to-end solution from data processing to interactive dashboard
- **Production Engineering**: Error handling, performance optimization, and maintainable code

### Key Competencies Showcased
- **Statistical Modeling**: Causal uplift analysis using machine learning
- **Data Visualization**: Interactive dashboards with Plotly
- **Business Intelligence**: Customer segmentation and performance analytics
- **Software Engineering**: Clean code, modular architecture, version control
- **Stakeholder Communication**: Clear insights presentation and actionable recommendations

### Industry Relevance
This project mirrors the analytical approaches used by:
- **Nectar360 (Sainsbury's)**: Customer loyalty and promotional analytics
- **Tesco Clubcard**: Customer segmentation and targeted marketing
- **Amazon**: Product recommendation and promotional optimization
- **Retail Analytics Teams**: Data-driven marketing decision making

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- pip package manager

### Installation
```bash
# Clone the repository
git clone https://github.com/martinktay/retail-promo-uplift-dashboard.git
cd retail-promo-uplift-dashboard

# Install dependencies
pip install -r requirements.txt

# Run the dashboard
streamlit run promo_uplift_dashboard.py
```

### Usage
1. **Access Dashboard**: Open http://localhost:8501 in your browser
2. **Explore Data**: Use sidebar filters to segment and analyze data
3. **View Insights**: Examine Key Insights cards for strategic recommendations
4. **Analyze Charts**: Interact with visualizations for detailed performance analysis
5. **Export Insights**: Use debug information for data validation

---

## 📊 Dataset Overview

### Sample Data Structure
The dashboard uses simulated promotional campaign data with the following features:
- **Customer Demographics**: Age, income, customer status
- **Behavioral Data**: Total spent, basket size, purchase history
- **Campaign Variables**: Promo exposure, promo type, channel
- **Outcome Metrics**: Purchase made, response rates

### Data Quality
- **1,000+ records** for robust statistical analysis
- **Balanced design** for reliable causal inference
- **Realistic distributions** reflecting actual retail patterns
- **Multiple segments** for comprehensive analysis

---

## 🔮 Future Enhancements

### Planned Features
- **Real-time Data Integration**: Live data feeds from retail systems
- **Advanced ML Models**: Deep learning for uplift prediction
- **A/B Testing Framework**: Automated experiment design and analysis
- **Predictive Analytics**: Customer lifetime value and churn prediction
- **API Integration**: RESTful API for external system integration

### Scalability Roadmap
- **Multi-tenant Architecture**: Support for multiple retail clients
- **Cloud Deployment**: AWS/Azure infrastructure scaling
- **Real-time Processing**: Apache Kafka for streaming analytics
- **Advanced Security**: Role-based access control and data encryption

---

## 📞 Contact & Collaboration

### Professional Links
- **GitHub**: [martinktay/retail-promo-uplift-dashboard](https://github.com/martinktay/retail-promo-uplift-dashboard)
- **LinkedIn**: [Your LinkedIn Profile]
- **Portfolio**: [Your Portfolio Website]

### Collaboration Opportunities
- **Open Source**: Contributions welcome for feature enhancements
- **Consulting**: Available for retail analytics projects
- **Speaking**: Conference presentations on causal analytics
- **Mentoring**: Data science career guidance and coaching

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **Nectar360 Team**: Inspiration for retail analytics excellence
- **Streamlit Community**: Excellent documentation and support
- **Open Source Contributors**: Libraries and tools that made this possible
- **Retail Analytics Community**: Best practices and methodologies

---

*Built with ❤️ for data-driven retail success*
