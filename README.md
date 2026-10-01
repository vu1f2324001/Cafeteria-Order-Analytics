# 🍽️ Cafeteria Order Analytics

## 📌 Overview

Cafeteria Order Analytics is a data analysis project focused on understanding cafeteria order and sales data.

The project uses SQL and Python-based data analysis techniques to identify sales trends, ordering patterns, branch performance, payment preferences, and other useful business insights.

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

## 📊 Dataset Summary

The currently analyzed cafeteria dataset contains:

| Metric | Value |
|---|---:|
| Total Orders | 24,444 |
| Total Sales | ₹15,81,186.20 |
| Average Order Value | ₹64.69 |
| Available Dates | 1 Apr 2024 – 2 Apr 2024 |
| Branches | 3 |

> **Note:** These figures are based on the currently validated `cafeteria_db` dataset. Final dataset metrics will be updated after complete validation of the original SQL dump.

---

## 📈 Visual Analysis

### 1. Daily Sales

| Date | Sales |
|---|---:|
| 1 Apr 2024 | ₹7,45,170.20 |
| 2 Apr 2024 | ₹8,36,016.00 |

The second day recorded higher sales than the first day.

---

### 2. Daily Order Count

| Date | Orders |
|---|---:|
| 1 Apr 2024 | 12,168 |
| 2 Apr 2024 | 12,276 |

The order volume remained relatively consistent across the two available days.

---

### 3. Branch-wise Sales

| Branch | Orders | Sales |
|---|---:|---:|
| Branch 2 | 12,483 | ₹7,90,096.20 |
| Branch 1 | 10,326 | ₹7,06,472.00 |
| Branch 4 | 1,635 | ₹84,618.00 |

---

### 4. Payment Method Analysis

| Payment Method | Orders | Sales |
|---|---:|---:|
| Paytm | 10,109 | ₹6,05,197.70 |
| UPI | 5,591 | ₹4,36,978.00 |
| CCA | 2,823 | ₹1,94,752.00 |
| QR | 2,353 | ₹1,14,031.00 |
| Cash | 2,062 | ₹1,08,379.00 |
| Card | 1,210 | ₹1,02,551.00 |
| Blank | 296 | ₹19,297.50 |

---

## 📊 Key Visualizations

The project includes visual analysis for:

- Daily Sales
- Daily Order Count
- Branch-wise Sales
- Payment Method Distribution
- Hour-wise Orders
- Sales Trends
- Product Performance
- 7-Day Sales Forecast

Visualization tools include **Matplotlib** and **Seaborn**.

---

## 🔍 Key Insights

Based on the currently validated dataset:

- Total analyzed orders are **24,444**.
- Total sales are approximately **₹15.81 lakh**.
- The average order value is approximately **₹64.69**.
- Branch 2 has the highest sales among the currently analyzed branches.
- Paytm is the most frequently used payment method in the available data.
- Order volumes on 1 Apr and 2 Apr 2024 are relatively close.
- Time-based analysis is used to identify peak ordering periods.

---

## 🔮 7-Day Sales Forecast

The project includes a forecasting component to estimate sales for the upcoming 7 days using historical sales data.

The forecasting section includes:

- Historical sales trend
- Forecasted sales
- Forecast visualization
- Comparison between historical and predicted values
- Forecast evaluation

> **Note:** The 7-day forecast will be finalized after validating the complete historical dataset. Forecast results depend on the amount and quality of available historical data and the selected forecasting methodology.

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
│   ├── daily_orders.png
│   ├── branch_analysis.png
│   ├── payment_analysis.png
│   ├── hourly_orders.png
│   └── sales_forecast.png
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
        ↓
Final Report
```

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

## 💡 Business Insights

The analysis can help cafeteria management understand:

- Sales performance
- Branch performance
- Customer ordering behaviour
- Payment preferences
- Peak ordering periods
- Product demand
- Future sales expectations

These insights can support better operational planning, inventory management, and sales monitoring.

---

## 📄 Report

The project report contains:

- Introduction
- Dataset Description
- Data Cleaning
- Exploratory Data Analysis
- Visualizations
- Sales Forecasting
- Key Insights
- Conclusion

---

## 👩‍💻 Author

**Akshada Valkunde**

Computer Engineering  
Vasantdada Patil Pratishthan's College of Engineering & Visual Arts

---

## 📌 Project Status

**🚧 In Progress**

The data analysis and visualization pipeline is being developed and refined.

Final dataset metrics, forecasting results, and evaluation metrics will be updated after complete validation of the original cafeteria SQL dataset.
