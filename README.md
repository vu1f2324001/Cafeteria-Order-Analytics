# 🍽️ Cafeteria Order Analytics

## 📌 Overview

Cafeteria Order Analytics is a data analysis project focused on understanding cafeteria order and sales data.

The project uses SQL and Python-based data analysis techniques to identify sales trends, ordering patterns, branch performance, payment preferences, and other business insights.

It also includes a 7-day sales forecasting component based on historical order data.

---

## 🎯 Objectives

- Analyze cafeteria order and sales data
- Identify daily and hourly order patterns
- Analyze branch-wise sales performance
- Understand payment method preferences
- Identify popular food items
- Calculate important business metrics
- Perform Exploratory Data Analysis (EDA)
- Generate a 7-day sales forecast
- Present insights through meaningful visualizations

---

## 📊 Key Analysis

### Sales Analysis

- Total Sales
- Total Orders
- Average Order Value (AOV)
- Daily Sales Trends
- Daily Order Trends

### Branch Analysis

- Branch-wise Order Count
- Branch-wise Revenue
- Branch Performance Comparison

### Payment Analysis

- Cash Payments
- Card Payments
- UPI
- QR
- Other Payment Methods

### Time-Based Analysis

- Hour-wise Orders
- Peak Ordering Hours
- Sales Trends by Date

### Product Analysis

- Top-Selling Items
- Item-wise Order Frequency
- Revenue Contribution

---

## 🔮 7-Day Sales Forecast

Historical sales data is used to estimate sales for the upcoming 7 days.

The forecasting section includes:

- Historical Sales Trend
- Forecasted Sales
- Forecast Visualization
- Comparison of Historical and Predicted Values

> **Note:** Forecast results depend on the available historical data and forecasting methodology. Final metrics will be updated after complete data validation and pipeline execution.

---

## 🛠️ Technologies Used

- **MySQL** – Database management and SQL analysis
- **Python** – Data processing and analysis
- **Pandas** – Data manipulation
- **Matplotlib** – Data visualization
- **Seaborn** – Statistical visualization
- **Jupyter Notebook** – Analysis environment

---

## 🗂️ Project Structure

```text
Cafeteria-Order-Analytics/
│
├── data/
│   └── cafeteria_order_data
│
├── notebooks/
│   └── cafeteria_analysis.ipynb
│
├── sql/
│   └── analysis_queries.sql
│
├── visualizations/
│   ├── daily_sales.png
│   ├── branch_analysis.png
│   ├── payment_analysis.png
│   └── hourly_orders.png
│
├── report/
│   └── Cafeteria_Order_Analytics_Report.pdf
│
└── README.md
```

---

## 📈 Workflow

```text
Raw Cafeteria Data
        ↓
Data Cleaning
        ↓
MySQL Data Analysis
        ↓
Exploratory Data Analysis
        ↓
Data Visualization
        ↓
Sales Trend Analysis
        ↓
7-Day Sales Forecast
        ↓
Business Insights
```

---

## 💡 Key Insights

The analysis helps identify:

- High-performing branches
- Peak ordering periods
- Frequently used payment methods
- Popular products
- Daily sales patterns
- Customer ordering behaviour
- Expected sales for the next 7 days

---

## 🚀 How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/vu1f2324001/Cafeteria-Order-Analytics.git
```

### 2. Navigate to the Project Directory

```bash
cd Cafeteria-Order-Analytics
```

### 3. Install Required Python Libraries

```bash
pip install pandas matplotlib seaborn jupyter
```

### 4. Run Jupyter Notebook

```bash
jupyter notebook
```

Open the analysis notebook and execute the cells step by step.

---

## 🧮 Example SQL Analysis

```sql
SELECT 
    DATE(order_date) AS order_day,
    COUNT(*) AS total_orders,
    SUM(grand_total) AS total_sales
FROM orders
GROUP BY DATE(order_date)
ORDER BY order_day;
```

This query calculates the daily order count and total sales across the available operational timeline.

---

## 📊 Expected Outcomes

The project provides a data-driven view of cafeteria operations and helps understand:

- Sales performance
- Ordering behaviour
- Branch performance
- Payment trends
- Product demand
- Future sales expectations

---

## 👩‍💻 Author

**Akshada Valkunde**

Computer Engineering  
Vasantdada Patil Pratishthan's College of Engineering & Visual Arts

---

## 📄 Project Status

**🚧 In Progress**

Data analysis, visualization, and forecasting modules are being developed and refined. Final performance metrics and forecast evaluation results will be documented after complete database validation.
