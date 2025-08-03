import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, confusion_matrix
import warnings
warnings.filterwarnings('ignore')

# Page configuration
st.set_page_config(
    page_title="Retail Promo Uplift Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #1f77b4;
    }
    .insight-box {
        background-color: #e8f4fd;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #ff7f0e;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    """Load and preprocess the RFM enriched dataset"""
    df = pd.read_csv('rfm_enriched.csv')
    
    # Convert purchase_date to datetime
    df['purchase_date'] = pd.to_datetime(df['purchase_date'])
    
    # Create additional features for analysis
    df['year'] = df['purchase_date'].dt.year
    df['month'] = df['purchase_date'].dt.month
    df['quarter'] = df['purchase_date'].dt.quarter
    
    # Create promotional exposure based on transaction type
    df['promo_exposed'] = (df['transaction_type'] == 'Discount').astype(int)
    
    # Create purchase indicator
    df['purchase_made'] = (df['transaction_type'] != 'Return').astype(int)
    
    # Create basket size (purchase amount for successful purchases)
    df['basket_size'] = np.where(df['purchase_made'] == 1, df['purchase_amount'], 0)
    
    return df

@st.cache_data
def calculate_rfm_metrics(df):
    """Calculate RFM metrics for customer segmentation"""
    # Get the most recent date for recency calculation
    max_date = df['purchase_date'].max()
    
    # Calculate RFM metrics by customer
    rfm = df.groupby('customer_id').agg({
        'purchase_date': lambda x: (max_date - x.max()).days,  # Recency
        'customer_id': 'count',  # Frequency
        'purchase_amount': 'sum'  # Monetary
    }).rename(columns={
        'purchase_date': 'recency',
        'customer_id': 'frequency',
        'purchase_amount': 'monetary'
    })
    
    # Create RFM scores (1-4, where 4 is best)
    rfm['r_score'] = pd.qcut(rfm['recency'], q=4, labels=[4, 3, 2, 1])
    rfm['f_score'] = pd.qcut(rfm['frequency'], q=4, labels=[1, 2, 3, 4])
    rfm['m_score'] = pd.qcut(rfm['monetary'], q=4, labels=[1, 2, 3, 4])
    
    # Convert to numeric
    rfm['r_score'] = rfm['r_score'].astype(int)
    rfm['f_score'] = rfm['f_score'].astype(int)
    rfm['m_score'] = rfm['m_score'].astype(int)
    
    # Create RFM score
    rfm['rfm_score'] = rfm['r_score'] + rfm['f_score'] + rfm['m_score']
    
    # Create customer segments
    def segment_customers(row):
        if row['rfm_score'] >= 10:
            return 'Champions'
        elif row['rfm_score'] >= 8:
            return 'Loyal Customers'
        elif row['rfm_score'] >= 6:
            return 'At Risk'
        elif row['rfm_score'] >= 4:
            return 'Can\'t Lose'
        else:
            return 'Lost'
    
    rfm['customer_segment'] = rfm.apply(segment_customers, axis=1)
    
    return rfm

@st.cache_data
def calculate_uplift_metrics(df, rfm):
    """Calculate uplift metrics for promotional campaigns"""
    # Merge RFM data with transaction data
    df_with_rfm = df.merge(rfm[['customer_segment', 'rfm_score']], 
                          left_on='customer_id', right_index=True, how='left')
    
    # Calculate response rates by segment and promo exposure
    uplift_analysis = df_with_rfm.groupby(['customer_segment', 'promo_exposed']).agg({
        'purchase_made': ['mean', 'count'],
        'basket_size': 'mean'
    }).round(4)
    
    # Flatten column names
    uplift_analysis.columns = ['response_rate', 'transaction_count', 'avg_basket_size']
    uplift_analysis = uplift_analysis.reset_index()
    
    # Calculate uplift
    uplift_pivot = uplift_analysis.pivot(index='customer_segment', 
                                       columns='promo_exposed', 
                                       values='response_rate').reset_index()
    
    uplift_pivot.columns = ['customer_segment', 'control_rate', 'treatment_rate']
    uplift_pivot['uplift'] = uplift_pivot['treatment_rate'] - uplift_pivot['control_rate']
    uplift_pivot['uplift_percentage'] = (uplift_pivot['uplift'] / uplift_pivot['control_rate'] * 100).round(2)
    
    return uplift_analysis, uplift_pivot

def create_uplift_model(df, rfm):
    """Create uplift model using two-model approach"""
    # Prepare features
    df_with_rfm = df.merge(rfm[['customer_segment', 'rfm_score']], 
                          left_on='customer_id', right_index=True, how='left')
    
    # Create features
    features = ['rfm_score', 'purchase_amount', 'promo_exposed']
    categorical_features = ['customer_segment', 'channel', 'product_category', 'customer_tier']
    
    # Encode categorical features
    le = LabelEncoder()
    for feature in categorical_features:
        df_with_rfm[f'{feature}_encoded'] = le.fit_transform(df_with_rfm[feature].astype(str))
        features.append(f'{feature}_encoded')
    
    # Split data
    X = df_with_rfm[features]
    y = df_with_rfm['purchase_made']
    
    # Train model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)
    
    return model, features, df_with_rfm

def main():
    # Header
    st.markdown('<h1 class="main-header">📊 Retail Promo Uplift Dashboard</h1>', unsafe_allow_html=True)
    st.markdown("### Advanced Causal Analysis for Marketing Campaign Optimization")
    
    # Load data
    with st.spinner("Loading and processing data..."):
        df = load_data()
        rfm = calculate_rfm_metrics(df)
        uplift_analysis, uplift_pivot = calculate_uplift_metrics(df, rfm)
        model, features, df_with_rfm = create_uplift_model(df, rfm)
    
    # Sidebar for filters
    st.sidebar.header("🎯 Dashboard Filters")
    
    # Date range filter
    date_range = st.sidebar.date_input(
        "Select Date Range",
        value=(df['purchase_date'].min().date(), df['purchase_date'].max().date()),
        min_value=df['purchase_date'].min().date(),
        max_value=df['purchase_date'].max().date()
    )
    
    # Customer segment filter
    selected_segments = st.sidebar.multiselect(
        "Customer Segments",
        options=rfm['customer_segment'].unique(),
        default=rfm['customer_segment'].unique()
    )
    
    # Channel filter
    selected_channels = st.sidebar.multiselect(
        "Channels",
        options=df['channel'].unique(),
        default=df['channel'].unique()
    )
    
    # Apply filters
    filtered_df = df[
        (df['purchase_date'].dt.date >= date_range[0]) &
        (df['purchase_date'].dt.date <= date_range[1]) &
        (df['channel'].isin(selected_channels))
    ]
    
    filtered_rfm = rfm[rfm['customer_segment'].isin(selected_segments)]
    
    # Main dashboard content
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            "Total Transactions",
            f"{len(filtered_df):,}",
            delta=f"{len(filtered_df) - len(df):,}"
        )
    
    with col2:
        promo_rate = (filtered_df['promo_exposed'].mean() * 100).round(1)
        st.metric(
            "Promo Exposure Rate",
            f"{promo_rate}%",
            delta=f"{promo_rate - (df['promo_exposed'].mean() * 100):.1f}%"
        )
    
    with col3:
        response_rate = (filtered_df['purchase_made'].mean() * 100).round(1)
        st.metric(
            "Overall Response Rate",
            f"{response_rate}%",
            delta=f"{response_rate - (df['purchase_made'].mean() * 100):.1f}%"
        )
    
    with col4:
        avg_basket = filtered_df['basket_size'].mean()
        st.metric(
            "Avg Basket Size",
            f"£{avg_basket:.2f}",
            delta=f"£{avg_basket - df['basket_size'].mean():.2f}"
        )
    
    # Key Insights Section
    st.markdown("---")
    st.subheader("🔍 Key Insights")
    
    # Calculate insights
    best_uplift_segment = uplift_pivot.loc[uplift_pivot['uplift_percentage'].idxmax()]
    worst_uplift_segment = uplift_pivot.loc[uplift_pivot['uplift_percentage'].idxmin()]
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"""
        <div class="insight-box">
        <h4>🎯 Best Performing Segment</h4>
        <p><strong>{best_uplift_segment['customer_segment']}</strong> shows the highest uplift at 
        <strong>{best_uplift_segment['uplift_percentage']}%</strong> when exposed to promotions.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="insight-box">
        <h4>⚠️ Segment Needing Attention</h4>
        <p><strong>{worst_uplift_segment['customer_segment']}</strong> shows only 
        <strong>{worst_uplift_segment['uplift_percentage']}%</strong> uplift, suggesting 
        different promotional strategies may be needed.</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Uplift Analysis Charts
    st.markdown("---")
    st.subheader("📈 Uplift Analysis by Customer Segment")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Uplift by segment chart
        fig_uplift = px.bar(
            uplift_pivot,
            x='customer_segment',
            y='uplift_percentage',
            title='Promotional Uplift by Customer Segment',
            color='uplift_percentage',
            color_continuous_scale='RdYlGn'
        )
        fig_uplift.update_layout(
            xaxis_title="Customer Segment",
            yaxis_title="Uplift Percentage (%)",
            showlegend=False
        )
        st.plotly_chart(fig_uplift, use_container_width=True)
    
    with col2:
        # Response rates comparison
        fig_response = go.Figure()
        
        for segment in uplift_pivot['customer_segment']:
            segment_data = uplift_analysis[uplift_analysis['customer_segment'] == segment]
            
            fig_response.add_trace(go.Bar(
                name=f'{segment} - Control',
                x=[segment],
                y=segment_data[segment_data['promo_exposed'] == 0]['response_rate'],
                marker_color='lightblue'
            ))
            
            fig_response.add_trace(go.Bar(
                name=f'{segment} - Treatment',
                x=[segment],
                y=segment_data[segment_data['promo_exposed'] == 1]['response_rate'],
                marker_color='darkblue'
            ))
        
        fig_response.update_layout(
            title='Response Rates: Control vs Treatment',
            xaxis_title="Customer Segment",
            yaxis_title="Response Rate",
            barmode='group'
        )
        st.plotly_chart(fig_response, use_container_width=True)
    
    # Channel and Product Analysis
    st.markdown("---")
    st.subheader("🛍️ Channel & Product Category Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Channel effectiveness
        channel_analysis = filtered_df.groupby(['channel', 'promo_exposed']).agg({
            'purchase_made': 'mean',
            'basket_size': 'mean'
        }).reset_index()
        
        fig_channel = px.bar(
            channel_analysis,
            x='channel',
            y='purchase_made',
            color='promo_exposed',
            title='Response Rate by Channel',
            barmode='group'
        )
        fig_channel.update_layout(
            xaxis_title="Channel",
            yaxis_title="Response Rate"
        )
        st.plotly_chart(fig_channel, use_container_width=True)
    
    with col2:
        # Product category analysis
        category_analysis = filtered_df.groupby(['product_category', 'promo_exposed']).agg({
            'purchase_made': 'mean',
            'basket_size': 'mean'
        }).reset_index()
        
        fig_category = px.bar(
            category_analysis,
            x='product_category',
            y='basket_size',
            color='promo_exposed',
            title='Average Basket Size by Product Category',
            barmode='group'
        )
        fig_category.update_layout(
            xaxis_title="Product Category",
            yaxis_title="Average Basket Size (£)"
        )
        st.plotly_chart(fig_category, use_container_width=True)
    
    # Customer Tier Analysis
    st.markdown("---")
    st.subheader("👑 Customer Tier Performance")
    
    tier_analysis = filtered_df.groupby(['customer_tier', 'promo_exposed']).agg({
        'purchase_made': 'mean',
        'basket_size': 'mean',
        'customer_id': 'count'
    }).reset_index()
    
    fig_tier = px.scatter(
        tier_analysis,
        x='purchase_made',
        y='basket_size',
        size='customer_id',
        color='customer_tier',
        symbol='promo_exposed',
        title='Customer Tier Performance: Response Rate vs Basket Size',
        hover_data=['customer_tier', 'promo_exposed']
    )
    fig_tier.update_layout(
        xaxis_title="Response Rate",
        yaxis_title="Average Basket Size (£)"
    )
    st.plotly_chart(fig_tier, use_container_width=True)
    
    # Detailed Uplift Table
    st.markdown("---")
    st.subheader("📊 Detailed Uplift Metrics")
    
    # Create detailed table
    detailed_uplift = uplift_analysis.merge(
        uplift_pivot[['customer_segment', 'uplift', 'uplift_percentage']], 
        on='customer_segment'
    )
    
    st.dataframe(
        detailed_uplift.round(4),
        use_container_width=True,
        hide_index=True
    )
    
    # Actionable Recommendations
    st.markdown("---")
    st.subheader("💡 Actionable Marketing Recommendations")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
        <h4>🎯 High-Impact Segments</h4>
        <ul>
        <li>Focus promotional spend on segments with >15% uplift</li>
        <li>Develop personalized campaigns for Champions and Loyal Customers</li>
        <li>Test new promotional strategies for At Risk customers</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
        <h4>📱 Channel Optimization</h4>
        <ul>
        <li>Allocate more budget to high-performing channels</li>
        <li>Test channel-specific promotional messages</li>
        <li>Optimize timing for different customer segments</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Footer
    st.markdown("---")
    st.markdown(
        """
        <div style='text-align: center; color: #666;'>
        <p>📊 Retail Promo Uplift Dashboard | Built with Streamlit | 
        Data-driven marketing optimization for retail success</p>
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main() 