import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px


# Page Configuration

st.set_page_config(
    page_title="Brand Visibility Intelligence Dashboard",
    page_icon="📊",
    layout="wide"
)


# Database Connection

conn = sqlite3.connect("brand_visibility_data.db")

# Load data
df = pd.read_sql_query("SELECT * FROM products", conn)


# Title

st.title("📊 Brand Visibility Intelligence Dashboard")
st.markdown("Analyze product visibility, pricing, brands, platforms and rankings.")


# Sidebar Filters

st.sidebar.header("🔎 Filters")

# Brand
brands = sorted(df["brand"].dropna().unique().tolist())
selected_brands = st.sidebar.multiselect(
    "Brand",
    brands
)

# Platform
platforms = sorted(df["platform"].dropna().unique().tolist())
selected_platforms = st.sidebar.multiselect(
    "Platform",
    platforms
)

# Keyword
keywords = sorted(df["Keyword"].dropna().unique().tolist())
selected_keywords = st.sidebar.multiselect(
    "Keyword",
    keywords
)

# Price Range
price_ranges = ["Budget", "Mid Range", "Premium", "Luxury"]
selected_price_ranges = st.sidebar.multiselect(
    "Price Range",
    price_ranges
)

# Rating Range
min_rating = st.sidebar.slider(
    "Minimum Rating",
    min_value=1.0,
    max_value=5.0,
    value=1.0,
    step=0.1
)

# Position
max_position = st.sidebar.slider(
    "Maximum Position",
    min_value=1,
    max_value=40,
    value=40
)


# Apply Filters

filtered_df = df.copy()

if selected_brands:
    filtered_df = filtered_df[
        filtered_df["brand"].isin(selected_brands)
    ]

if selected_platforms:
    filtered_df = filtered_df[
        filtered_df["platform"].isin(selected_platforms)
    ]

if selected_keywords:
    filtered_df = filtered_df[
        filtered_df["Keyword"].isin(selected_keywords)
    ]

if selected_price_ranges:
    filtered_df = filtered_df[
        filtered_df["price_range"].isin(selected_price_ranges)
    ]

filtered_df = filtered_df[
    (filtered_df["rating"].isna()) |
    (filtered_df["rating"] >= min_rating)
]

filtered_df = filtered_df[
    (filtered_df["position"].isna()) |
    (filtered_df["position"] <= max_position)
]


# KPIs

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric(
    "Total Products",
    len(filtered_df)
)

col2.metric(
    "Average Price",
    f"₹{filtered_df['price'].mean():,.2f}"
    if filtered_df["price"].notna().any()
    else "N/A"
)

col3.metric(
    "Average Rating",
    f"{filtered_df['rating'].mean():.2f}"
    if filtered_df["rating"].notna().any()
    else "N/A"
)

col4.metric(
    "Total Reviews",
    f"{filtered_df['Reviews'].sum():,.0f}"
)

col5.metric(
    "Avg Visibility Score",
    f"{filtered_df['visibility_score'].mean():.2f}"
    if filtered_df["visibility_score"].notna().any()
    else "N/A"
)

st.divider()


# Tabs

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "📈 Overview",
    "🏷️ Brand Insights",
    "💰 Pricing Analysis",
    "🏪 Platform Analysis",
    "🎯 Visibility & Ranking",
    "🔍 Product Explorer"
])


# TAB 1 - OVERVIEW


with tab1:

    st.subheader("Market Overview")

    col1, col2 = st.columns(2)

    with col1:

        price_data = filtered_df[
            filtered_df["price"].notna() &
            (filtered_df["price"] > 0)
        ]

        fig = px.histogram(
            price_data,
            x="price",
            nbins=30,
            title="Price Distribution"
        )

        st.plotly_chart(
            fig,
            width="stretch",
            key="chart_1"
        )

    with col2:

        keyword_data = (
            filtered_df
            .groupby("Keyword")
            .size()
            .reset_index(name="product_count")
            .sort_values("product_count", ascending=False)
        )

        fig = px.bar(
            keyword_data,
            x="Keyword",
            y="product_count",
            title="Products per Keyword"
        )

        st.plotly_chart(
            fig,
            width="stretch",
            key="chart_2"
        )

    platform_data = (
        filtered_df
        .groupby("platform")
        .size()
        .reset_index(name="product_count")
        .sort_values("product_count", ascending=False)
    )

    fig = px.pie(
        platform_data,
        names="platform",
        values="product_count",
        title="Platform Share"
    )

    st.plotly_chart(
            fig,
            width="stretch",
            key="chart_3"
        )



# TAB 2 - BRAND INSIGHTS


with tab2:

    st.subheader("Brand Analysis")

    brand_count = (
        filtered_df
        .groupby("brand")
        .size()
        .reset_index(name="product_count")
        .sort_values("product_count", ascending=False)
    )

    col1, col2 = st.columns(2)

    with col1:

        fig = px.bar(
            brand_count.head(15),
            x="brand",
            y="product_count",
            title="Top Brands by Product Count"
        )

        st.plotly_chart(
            fig,
            width="stretch",
            key="chart_4"
        )

    with col2:

        brand_rating = (
            filtered_df
            .dropna(subset=["brand", "rating"])
            .groupby("brand")["rating"]
            .mean()
            .reset_index(name="avg_rating")
            .sort_values("avg_rating", ascending=False)
        )

        fig = px.bar(
            brand_rating.head(15),
            x="brand",
            y="avg_rating",
            title="Average Rating by Brand"
        )

        st.plotly_chart(
            fig,
            width="stretch",
            key="chart_5"
        )

    top10 = filtered_df[
        filtered_df["position"].notna() &
        (filtered_df["position"] <= 10)
    ]

    top10_brand = (
        top10
        .groupby("brand")
        .size()
        .reset_index(name="top10_products")
        .sort_values("top10_products", ascending=False)
    )

    fig = px.bar(
        top10_brand.head(15),
        x="brand",
        y="top10_products",
        title="Brands Appearing in Top 10"
    )

    st.plotly_chart(
        fig,
        width="stretch",
        key="chart_6"
    )



# TAB 3 - PRICING ANALYSIS


with tab3:

    st.subheader("Pricing Analysis")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Average Price",
        f"₹{filtered_df['price'].mean():,.2f}"
        if filtered_df["price"].notna().any()
        else "N/A"
    )

    col2.metric(
        "Highest Price",
        f"₹{filtered_df['price'].max():,.2f}"
        if filtered_df["price"].notna().any()
        else "N/A"
    )

    discounted_percentage = "N/A"

    col3.metric(
        "% Discounted Products",
        discounted_percentage
    )

    col1, col2 = st.columns(2)

    with col1:

        price_data = filtered_df[
            filtered_df["price"].notna() &
            (filtered_df["price"] > 0)
        ]

        fig = px.histogram(
            price_data,
            x="price",
            nbins=30,
            title="Price Distribution"
        )

        st.plotly_chart(
            fig,
            width="stretch",
            key="chart_7"
        )

    with col2:

        ranking_price = filtered_df[
            filtered_df["price"].notna() &
            (filtered_df["price"] > 0) &
            filtered_df["position"].notna()
        ]

        fig = px.scatter(
            ranking_price,
            x="price",
            y="position",
            hover_data=["title", "brand", "platform"],
            title="Price vs Ranking"
        )

        fig.update_yaxes(autorange="reversed")

        st.plotly_chart(
            fig,
            width="stretch",
            key="chart_8"
        )

    rating_price = filtered_df[
        filtered_df["price"].notna() &
        (filtered_df["price"] > 0) &
        filtered_df["rating"].notna()
    ]

    fig = px.scatter(
        rating_price,
        x="price",
        y="rating",
        hover_data=["title", "brand", "platform"],
        title="Price vs Rating"
    )

    st.plotly_chart(
            fig,
            width="stretch",
            key="chart_9"
        )



# TAB 4 - PLATFORM ANALYSIS


with tab4:

    st.subheader("Platform Analysis")

    platform_count = (
        filtered_df
        .groupby("platform")
        .size()
        .reset_index(name="product_count")
        .sort_values("product_count", ascending=False)
    )

    platform_price = (
        filtered_df
        .groupby("platform")["price"]
        .mean()
        .reset_index(name="avg_price")
        .sort_values("avg_price")
    )

    platform_rating = (
        filtered_df
        .groupby("platform")["rating"]
        .mean()
        .reset_index(name="avg_rating")
        .sort_values("avg_rating", ascending=False)
    )

    col1, col2 = st.columns(2)

    with col1:

        fig = px.bar(
            platform_count,
            x="platform",
            y="product_count",
            title="Products per Platform"
        )

        st.plotly_chart(
            fig,
            width="stretch",
            key="chart_10"
        )

    with col2:

        fig = px.bar(
            platform_price,
            x="platform",
            y="avg_price",
            title="Average Price by Platform"
        )

        st.plotly_chart(
            fig,
            width="stretch",
            key="chart_11"
        )

    fig = px.bar(
        platform_rating,
        x="platform",
        y="avg_rating",
        title="Average Rating by Platform"
    )

    st.plotly_chart(
        fig,
        width="stretch",
        key="chart_12"
    )



# TAB 5 - VISIBILITY & RANKING


with tab5:

    st.subheader("Visibility & Ranking Analysis")

    ranked_df = filtered_df[
        filtered_df["position"].notna()
    ]

    col1, col2 = st.columns(2)

    col1.metric(
        "Average Position",
        f"{ranked_df['position'].mean():.2f}"
        if not ranked_df.empty
        else "N/A"
    )

    col2.metric(
        "Average Visibility Score",
        f"{ranked_df['visibility_score'].mean():.2f}"
        if not ranked_df.empty
        else "N/A"
    )

    col1, col2 = st.columns(2)

    with col1:

        fig = px.histogram(
            ranked_df,
            x="position",
            nbins=40,
            title="Ranking Distribution"
        )

        st.plotly_chart(
            fig,
            width="stretch",
            key="chart_13"
        )

    with col2:

        rating_rank = ranked_df[
            ranked_df["rating"].notna()
        ]

        fig = px.scatter(
            rating_rank,
            x="rating",
            y="position",
            hover_data=["title", "brand"],
            title="Rating vs Ranking"
        )

        fig.update_yaxes(autorange="reversed")

        st.plotly_chart(
            fig,
            width="stretch",
            key="chart_14"
        )

    reviews_rank = ranked_df[
        ranked_df["Reviews"].notna()
    ]

    fig = px.scatter(
        reviews_rank,
        x="Reviews",
        y="position",
        size="Reviews",
        hover_data=["title", "brand", "platform"],
        title="Reviews vs Ranking"
    )

    fig.update_yaxes(autorange="reversed")

    st.plotly_chart(
            fig,
            width="stretch",
            key="chart_15"
        )



# TAB 6 - PRODUCT EXPLORER


with tab6:

    st.subheader("Product Explorer")

    search = st.text_input(
        "🔍 Search Product Title"
    )

    explorer_df = filtered_df.copy()

    if search:
        explorer_df = explorer_df[
            explorer_df["title"]
            .str.contains(
                search,
                case=False,
                na=False
            )
        ]

    display_columns = [
        "title",
        "brand",
        "price",
        "rating",
        "Reviews",
        "platform",
        "position"
    ]

    st.dataframe(
        explorer_df[display_columns],
        use_container_width=True,
        hide_index=True
    )