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
Retail companies face increasing pressure to optimise marketing spend whilst maintaining customer engagement. Traditional A/B testing approaches often fail to capture the true causal impact of promotional campaigns, leading to:
- Suboptimal budget allocation
- Missed opportunities with high-value customer segments
- Inefficient channel mix strategies
- Lack of actionable insights for marketing teams

### The Solution
This dashboard implements **causal uplift modelling** to measure the true incremental impact of promotional campaigns, enabling:
- **Precision targeting** of customer segments with highest uplift potential
- **Channel optimisation** based on segment-specific performance
- **Budget allocation** informed by causal impact rather than correlation
- **Actionable recommendations** for marketing strategy refinement

---

## 🚀 Features & Capabilities

### 📈 Advanced Analytics
- **Causal Uplift Modelling**: Two-model approach using Random Forest Classifiers
- **Customer Segmentation**: RFM-based segmentation with behavioural overlays
- **Channel Effectiveness Analysis**: Multi-channel performance comparison
- **Product Category Insights**: Category-specific promotional performance
- **Real-time Filtering**: Dynamic data exploration with interactive filters

### 🎨 Professional Dashboard
- **Interactive Visualizations**: Plotly charts with drill-down capabilities
- **Smart Metrics**: Contextual delta calculations and trend indicators
- **Responsive Design**: Optimized for desktop and tablet viewing
- **British English Localization**: Professional UK market presentation

### 🔧 Technical Excellence
- **Production-Ready Code**: Error handling, caching, and performance optimisation
- **Modular Architecture**: Clean separation of data processing, modelling, and visualisation
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
- **Channel Optimisation**: SMS shows highest engagement for urgent promotions
- **Product Strategy**: Electronics category demonstrates highest basket size impact

### Strategic Recommendations
1. **Prioritise Lapsed Customer Re-engagement**: Highest ROI segment
2. **Develop New Customer Welcome Series**: Strong conversion potential
3. **Optimise Channel Mix**: SMS for urgent, Email for relationship building
4. **Category-Specific Promotions**: Electronics focus for basket size growth

---

## 🔍 Results Analysis & Insights

### The Hidden Story Behind the Numbers

Our analysis reveals a fascinating narrative about customer behaviour that challenges conventional marketing wisdom. The data tells us that **not all customers are created equal** when it comes to promotional responsiveness, and the traditional "spray and pray" approach is costing retailers millions.

### Key Findings Explained

#### 🎯 **The Lapsed Customer Paradox (152% Uplift)**
*"The customers you've given up on are actually your golden geese"*

This counterintuitive finding reveals that lapsed customers—often written off by marketing teams—represent the highest potential for revenue recovery. Why? These customers have already demonstrated purchasing intent and brand affinity, but have drifted away due to lack of engagement. A well-timed, personalised re-engagement campaign can reignite their connection with the brand, often resulting in purchases that exceed their historical spending patterns.

**The Psychology**: Lapsed customers experience a "rediscovery effect" when re-engaged, often feeling valued and special, leading to higher-than-average conversion rates and basket sizes.

#### 🌱 **The New Customer Window of Opportunity (125% Uplift)**
*"First impressions last forever, but second impressions drive sales"*

New customers are in a critical "honeymoon phase" where they're most receptive to brand messaging and most likely to establish long-term purchasing habits. Our analysis shows that strategic welcome campaigns can dramatically accelerate customer lifetime value.

**The Psychology**: New customers are actively evaluating whether they made the right choice. Timely, relevant promotions validate their decision and establish positive brand associations.

#### 📱 **The Channel Preference Revolution**
*"SMS isn't just for urgent messages—it's for urgent customers"*

Our channel analysis reveals that SMS outperforms email by 25% for high-income customers, challenging the assumption that affluent customers prefer email communication. This suggests that high-value customers prioritise convenience and immediacy over detailed information.

**The Psychology**: High-income customers often have limited time and appreciate direct, actionable communication. SMS cuts through the noise of overflowing inboxes.

#### 🛒 **The Electronics Category Phenomenon**
*"Big-ticket items drive big-ticket thinking"*

Electronics promotions don't just increase basket size—they fundamentally change customer purchasing behaviour. Customers buying electronics are more likely to add complementary items, creating a "halo effect" that benefits the entire category.

**The Psychology**: Electronics purchases are considered investments, making customers more receptive to premium add-ons and extended warranties.

---

## 🎭 The Human Side of Data: Creative Conclusions

### Beyond the Numbers: What This Really Means

This project isn't just about algorithms and statistical models—it's about understanding the human beings behind the data points. Every percentage point represents real people making real decisions, influenced by emotions, circumstances, and subconscious biases.

### The Marketing Team's New Playbook

#### 🎪 **The "Comeback Kid" Strategy**
*Transform your lapsed customers into brand advocates*

Instead of treating lapsed customers as lost causes, view them as "comeback kids" waiting for their moment to shine. Design campaigns that acknowledge their previous relationship with the brand whilst offering compelling reasons to return. Think personalised "We miss you" messages with exclusive offers that make them feel special.

#### 🎁 **The "Welcome to the Family" Approach**
*Turn first-time buyers into lifetime customers*

New customers are like guests at a dinner party—they need to feel welcomed, valued, and excited about what's to come. Create a multi-touchpoint welcome series that educates, entertains, and encourages repeat purchases. Don't just sell—tell your brand story and show them how you can make their lives better.

#### ⚡ **The "Speed Dating" Channel Strategy**
*Match message urgency with customer urgency*

High-income customers aren't just wealthy—they're time-poor. They need information fast, decisions made quickly, and results delivered immediately. SMS becomes their preferred channel not because they can't read emails, but because they won't. Respect their time, and they'll respect your brand.

#### 🎯 **The "Category Catalyst" Effect**
*Use big purchases to drive bigger thinking*

Electronics purchases are gateway drugs to premium shopping behaviour. When customers buy electronics, they're already in a "big purchase" mindset, making them more receptive to additional investments. Use this psychological state to introduce complementary products and services.

### The Future of Retail Marketing

#### 🤖 **AI-Powered Personalisation**
The next evolution isn't just segment-based targeting—it's individual-level personalisation powered by machine learning. Imagine campaigns that adapt in real-time based on customer behaviour, weather conditions, and even social media sentiment.

#### 🧠 **Behavioural Economics Integration**
Understanding the psychology behind purchasing decisions allows us to design campaigns that work with human nature, not against it. From scarcity tactics to social proof, behavioural economics principles can dramatically improve campaign performance.

#### 🌍 **Omnichannel Orchestration**
The future isn't about choosing between channels—it's about orchestrating them like a symphony. Each touchpoint should build upon the previous one, creating a seamless customer journey that feels personal and purposeful.

### The Bottom Line: Why This Matters

In an era where every marketing pound is scrutinised, this analysis provides the roadmap for maximising ROI whilst building stronger customer relationships. It's not just about increasing sales—it's about creating customers who choose your brand not because of price, but because of value.

**The real insight?** The best customers aren't always the ones who spend the most—they're the ones who respond the most. And sometimes, the customers you've forgotten about are the ones who will surprise you the most.

---

*"Data tells us what happened. Analysis tells us why. But only human insight tells us what to do about it."*

---

## 🎯 For Recruiters & Hiring Managers

### Professional Profile
This project demonstrates **senior-level data science capabilities** in:
- **Causal Inference**: Advanced uplift modelling beyond correlation analysis
- **Business Acumen**: Translation of technical insights into strategic recommendations
- **Full-Stack Development**: End-to-end solution from data processing to interactive dashboard
- **Production Engineering**: Error handling, performance optimisation, and maintainable code

### Key Competencies Showcased
- **Statistical Modelling**: Causal uplift analysis using machine learning
- **Data Visualisation**: Interactive dashboards with Plotly
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

## 🎯 Final Thoughts: The Art of Data-Driven Marketing

### Why This Project Matters

In today's hyper-competitive retail landscape, the difference between success and failure often lies in understanding not just *what* customers do, but *why* they do it. This project bridges the gap between raw data and human insight, transforming numbers into narratives that drive business decisions.

### The Competitive Advantage

Whilst many companies collect data, few truly understand it. This dashboard doesn't just report metrics—it reveals the hidden patterns that drive customer behaviour. It's the difference between shooting in the dark and hitting the bullseye every time.

### For the Data Scientist

This project demonstrates that technical excellence and business impact aren't mutually exclusive. The most sophisticated algorithms are worthless without clear communication and actionable insights. Here, we've shown how to build something that both impresses engineers and empowers executives.

### For the Business Leader

This isn't just another dashboard—it's a strategic weapon. In boardrooms across the country, marketing budgets are being scrutinised like never before. This analysis provides the ammunition needed to defend and expand marketing investments with confidence.

### The Human Element

Behind every data point is a person making a decision. Understanding the psychology, emotions, and circumstances that drive those decisions is what separates good analytics from great insights. This project doesn't just crunch numbers—it tells stories.

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
