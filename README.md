# 📊 Brand Visibility Intelligence Dashboard

## 📌 Project Overview

The **Brand Visibility Intelligence Dashboard** is an e-commerce analytics project designed to analyze product visibility, search rankings, pricing, ratings, reviews, brands, and platform competition across online shopping search results.

The project combines data collected through the **Google Shopping API using SerpAPI** with a pre-existing CSV dataset. The data is cleaned, transformed, stored in a SQLite database, analyzed using SQL and Python, and presented through an interactive Streamlit dashboard.

---

## 🎯 Project Objectives

* Extract product information from Google Shopping search results.
* Combine API data with an existing CSV dataset.
* Clean and standardize noisy product data.
* Perform exploratory data analysis using SQL and Python.
* Engineer useful business features such as brand, price range, and visibility score.
* Store the processed data in a SQLite database.
* Build an interactive dashboard using Streamlit.
* Analyze brand performance, pricing strategies, platform competition, and product visibility.
* Generate actionable business insights.

---

## 📂 Data Sources

### Dataset 1 — CSV Dataset

The project includes a pre-generated product dataset containing product information from online shopping platforms.

### Dataset 2 — Google Shopping API

Product data was extracted using **SerpAPI / Google Shopping search results**.

The API dataset contains information such as:

* Keyword
* Product Title
* Price
* Rating
* Reviews
* Platform
* Position
* Delivery
* Product Link
* Product Thumbnail

---

## 🔍 Search Keywords

The project uses multiple e-commerce product keywords, including:

* Phone
* Television
* Laptop
* Fridge
* Dryer
* Headset
* Lamp
* Microwave
* Guitar
* Mixer

Additional keyword records were also present in the provided CSV dataset.

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* SQLite
* SQL
* Streamlit
* Plotly
* SerpAPI
* Google Shopping API
* VS Code
* Git & GitHub

---

## 🔄 Project Workflow

```text
Google Shopping API
        ↓
API Data Extraction
        ↓
CSV Dataset
        ↓
Data Integration
        ↓
Data Cleaning
        ↓
Feature Engineering
        ↓
SQLite Database
        ↓
SQL Analysis / EDA
        ↓
Streamlit Dashboard
        ↓
Business Insights
```

---

## 🧹 Data Cleaning

The combined dataset was cleaned using Python and Pandas.

Major cleaning activities included:

* Standardizing column names
* Converting price values to numeric format
* Removing invalid and negative prices
* Handling missing values
* Converting ratings to numeric values
* Cleaning review counts
* Validating ranking/position values
* Filling missing delivery information with `Unknown`
* Cleaning noisy characters from product titles
* Removing duplicate records
* Standardizing categorical values
* Handling missing ranking information

---

## ⚙️ Feature Engineering

The following features were created:

### Brand

Brand information was extracted from the product title.

### Price Range

Products were categorized into:

* Budget
* Mid Range
* Premium
* Luxury

### Visibility Score

A visibility score was calculated using search position.

```text
Visibility Score = ((41 - Position) / 40) × 100
```

Therefore:

* Position 1 → Visibility Score 100
* Position 10 → Visibility Score 77.5
* Position 20 → Visibility Score 52.5
* Position 40 → Visibility Score 2.5

### Top 10 Flag

Products appearing in positions 1–10 were identified as top-ranking products.

---

## 🗄️ Database

The cleaned and feature-engineered data was stored in a SQLite database.

### Database

```text
brand_visibility.db
```

### Table

```text
products
```

The database is used by the Streamlit dashboard for analytics and product exploration.

---

## 📊 Exploratory Data Analysis

The project includes analysis of 30 business questions covering:

* Products per keyword
* Overall average price
* Price distribution
* Average rating
* Review engagement
* Brand frequency
* Brand visibility
* Brand ranking
* Top 10 brand presence
* Brand ratings
* Brand pricing
* Price range distribution
* Price vs ranking
* Platform pricing
* Highest-priced products
* Discount analysis
* Platform product count
* Platform ratings
* Platform average price
* Platform ranking
* Brand-platform distribution
* Ranking distribution
* Visibility score
* Rating vs ranking
* Reviews vs ranking
* Factors influencing top-ranking products

---

# 📈 Streamlit Dashboard

The interactive dashboard contains six major sections.

## 1. Overview

### KPIs

* Total Products
* Average Price
* Average Rating
* Total Reviews

### Charts

* Price Distribution
* Products per Keyword
* Platform Share

---

## 2. Brand Insights

### KPIs

* Top Brand
* Average Visibility Score

### Charts

* Brand vs Product Count
* Brand vs Average Rating
* Top Brands in Top 10 Positions

---

## 3. Pricing Analysis

### KPIs

* Average Price
* Maximum Price
* Discounted Products Percentage

### Charts

* Price Distribution
* Price vs Ranking
* Price vs Rating

---

## 4. Platform Analysis

### KPIs

* Total Platforms
* Best Platform by Average Rating

### Charts

* Platform vs Product Count
* Platform vs Average Price
* Platform vs Average Rating

---

## 5. Visibility & Ranking

### KPIs

* Average Position
* Average Visibility Score

### Charts

* Ranking Distribution
* Rating vs Ranking
* Reviews vs Ranking

---

## 6. Product Explorer

The Product Explorer provides:

* Product title search
* Interactive filtering
* Sortable product table
* Product-level exploration
* Highlighting of top-performing products

### Table Columns

* Title
* Brand
* Price
* Rating
* Reviews
* Platform
* Position
* Discount

---

## 🔎 Dashboard Filters

The dashboard provides dynamic filters for:

* Brand
* Platform
* Price Range
* Rating Range
* Keyword
* Position / Ranking

These filters allow users to explore the dataset interactively.

---

## 💡 Key Business Insights

The analysis helps identify:

* High-visibility brands
* Strong-performing products
* Brands frequently appearing in top search positions
* Platform-level competition
* Differences in average pricing between platforms
* Relationship between price and ranking
* Relationship between rating and ranking
* Relationship between reviews and ranking
* Distribution of products across price segments

The analysis also shows that product ranking is influenced by multiple factors rather than price alone.

---

## ⚠️ Data Limitations

The dataset contains some limitations that should be considered while interpreting the results.

### Missing Ranking Data

Ranking/position information is primarily available for API-extracted products. Therefore, ranking and visibility analysis represents the ranked subset of products.

### Missing Original Price

The `raw_price` field is missing in the available dataset. Therefore, reliable discount percentages could not be calculated.

Discount-related analysis has therefore been treated as unavailable rather than using estimated values.

---

## 📌 Business Recommendations

* Brands should monitor their search visibility and top-10 ranking performance.
* Product pricing should be evaluated along with ratings, reviews, and competitive positioning.
* Brands should compare performance across different e-commerce platforms.
* High-performing products should be monitored regularly for changes in ranking and visibility.
* Customer ratings and review engagement should be considered important indicators of product competitiveness.
* Future data collection should include original price and discount information.
* Regular API-based data collection can be used to build a continuous brand visibility monitoring system.

---

## 📁 Project Files

```text
Brand Visibility Intelligence Dashboard/
│
├── app.py
├── brand_visibility.ipynb
├── brand_visibility_data.db
├── cleaned_dataset.csv
├── dashboard_queries.sql
├── requirements.txt
├── project_report.md
└── screenshots/
```

---

## ▶️ How to Run the Application

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run Streamlit

```bash
python -m streamlit run app.py
```

The dashboard will open in the browser.

---

## 👨‍💻 Project Skills Demonstrated

This project demonstrates practical experience in:

* API Data Extraction
* Data Cleaning
* Data Preprocessing
* Feature Engineering
* SQL
* SQLite Database Integration
* Exploratory Data Analysis
* Data Visualization
* Streamlit Dashboard Development
* Business Intelligence
* Business Insight Generation

---

## 🏁 Conclusion

The Brand Visibility Intelligence Dashboard provides a unified analytical view of e-commerce products across brands and platforms.

By combining API-based product extraction, data cleaning, feature engineering, SQL analytics, and interactive visualization, the project demonstrates an end-to-end data analytics and business intelligence workflow.

The dashboard can help businesses understand product visibility, competitive positioning, pricing patterns, customer engagement, and marketplace performance.
