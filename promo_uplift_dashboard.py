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
    """Load and preprocess the promotional uplift dataset"""
    df = pd.read_csv('promo_uplift_enriched.csv')
    
    # Create additional features for analysis
    # Adjust income bins based on actual data distribution
    income_bins = [0, 30000, 50000, float('inf')]
    income_labels = ['Low', 'Medium', 'High']
    df['income_segment'] = pd.cut(df['income'], 
                                 bins=income_bins, 
                                 labels=income_labels)
    
    # Create age segments
    df['age_segment'] = pd.cut(df['age'], 
                              bins=[0, 25, 35, 50, 65, float('inf')], 
                              labels=['18-25', '26-35', '36-50', '51-65', '65+'])
    
    return df

@st.cache_data
def calculate_customer_segments(df):
    """Calculate customer segments based on behavior and demographics"""
    # Create customer segments based on total spent and customer status
    def create_segment(row):
        if row['customer_status'] == 'New':
            return 'New Customers'
        elif row['customer_status'] == 'Lapsed':
            return 'Lapsed Customers'
        elif row['total_spent_last_month'] > 200:
            return 'High-Value Existing'
        else:
            return 'Regular Existing'
    
    df['customer_segment'] = df.apply(create_segment, axis=1)
    
    return df

@st.cache_data
def calculate_uplift_metrics(df):
    """Calculate uplift metrics for promotional campaigns"""
    # Calculate response rates by segment and promo exposure
    uplift_analysis = df.groupby(['customer_segment', 'promo_exposed']).agg({
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

def create_uplift_model(df):
    """Create uplift model using two-model approach"""
    # Create features
    features = ['age', 'income', 'total_spent_last_month', 'promo_exposed']
    categorical_features = ['customer_segment', 'channel', 'product_category', 'customer_status', 'promo_type']
    
    # Encode categorical features
    le = LabelEncoder()
    for feature in categorical_features:
        df[f'{feature}_encoded'] = le.fit_transform(df[feature].astype(str))
        features.append(f'{feature}_encoded')
    
    # Split data
    X = df[features]
    y = df['purchase_made']
    
    # Train model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)
    
    return model, features, df

def main():
    # Header
    st.markdown('<h1 class="main-header">📊 Retail Promo Uplift Dashboard</h1>', unsafe_allow_html=True)
    st.markdown("### Advanced Causal Analysis for Marketing Campaign Optimization")
    
    # Load data
    with st.spinner("Loading and processing data..."):
        try:
            df = load_data()
            if df is None:
                st.error("Failed to load data. Please check if 'promo_uplift_enriched.csv' exists.")
                return
                
            df = calculate_customer_segments(df)
            if df is None:
                st.error("Failed to calculate customer segments.")
                return
                
            uplift_analysis, uplift_pivot = calculate_uplift_metrics(df)
            if uplift_analysis is None or uplift_pivot is None:
                st.error("Failed to calculate uplift metrics.")
                return
                
            model, features, df_with_model = create_uplift_model(df)
            if model is None:
                st.error("Failed to create uplift model.")
                return
                
        except Exception as e:
            st.error(f"Error during data processing: {e}")
            return
    
    # Sidebar for filters
    st.sidebar.header("🎯 Dashboard Filters")
    
    # Income range filter
    income_range = st.sidebar.slider(
        "Income Range (£)",
        min_value=int(df['income'].min()),
        max_value=int(df['income'].max()),
        value=(int(df['income'].min()), int(df['income'].max()))
    )
    
    # Customer segment filter
    selected_segments = st.sidebar.multiselect(
        "Customer Segments",
        options=df['customer_segment'].unique(),
        default=df['customer_segment'].unique()
    )
    
    # Channel filter
    selected_channels = st.sidebar.multiselect(
        "Channels",
        options=df['channel'].unique(),
        default=df['channel'].unique()
    )
    
    # Apply filters
    filtered_df = df[
        (df['channel'].isin(selected_channels)) &
        (df['customer_segment'].isin(selected_segments)) &
        (df['income'] >= income_range[0]) &
        (df['income'] <= income_range[1])
    ]
    
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
    
    # Calculate insights with error handling
    try:
        best_uplift_segment = uplift_pivot.loc[uplift_pivot['uplift_percentage'].idxmax()]
        worst_uplift_segment = uplift_pivot.loc[uplift_pivot['uplift_percentage'].idxmin()]
    except Exception as e:
        st.error(f"Error calculating insights: {e}")
        return
    
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
    
    # Customer Status Analysis
    st.markdown("---")
    st.subheader("👥 Customer Status Performance")
    
    status_analysis = filtered_df.groupby(['customer_status', 'promo_exposed']).agg({
        'purchase_made': 'mean',
        'basket_size': 'mean',
        'customer_id': 'count'
    }).reset_index()
    
    fig_status = px.scatter(
        status_analysis,
        x='purchase_made',
        y='basket_size',
        size='customer_id',
        color='customer_status',
        symbol='promo_exposed',
        title='Customer Status Performance: Response Rate vs Basket Size',
        hover_data=['customer_status', 'promo_exposed']
    )
    fig_status.update_layout(
        xaxis_title="Response Rate",
        yaxis_title="Average Basket Size (£)"
    )
    st.plotly_chart(fig_status, use_container_width=True)
    
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