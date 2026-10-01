# 🍽️ Cafeteria Order Analytics

A data analytics and demand forecasting project developed as part of the **Kanishka Software Pvt. Ltd. Internship Evaluation Challenge**.

The project analyzes cafeteria order transactions across branches and payment methods to identify sales trends, operational patterns, customer payment preferences, branch performance, and a 7-day demand forecast.

---

## 📌 Objectives

- Ingest and analyze cafeteria order data from MySQL
- Identify daily and hourly order trends
- Compare branch-level sales and order volumes
- Analyze customer payment preferences
- Calculate Average Order Value (AOV)
- Perform Exploratory Data Analysis (EDA)
- Generate a 7-day demand forecast
- Derive actionable business insights

---

## 📊 Dataset Summary

| Metric | Value |
| :--- | ---: |
| **Total Orders** | 24,444 |
| **Total Sales** | ₹15,81,186.20 |
| **Average Order Value (AOV)** | ₹64.69 |
| **Analysis Period** | 1 Apr 2024 – 2 Apr 2024 |
| **Active Branches** | 3 |

> **Note:** The above metrics are based on the currently validated cafeteria dataset.

---

## 📈 Visual Analytics

### 1. Branch-Wise Sales Performance

| Branch | Orders | Sales (₹) | Share |
| :--- | ---: | ---: | ---: |
| **Branch 2** | 12,483 | ₹7,90,096.20 | 49.97% |
| **Branch 1** | 10,326 | ₹7,06,472.00 | 44.68% |
| **Branch 4** | 1,635 | ₹84,618.00 | 5.35% |
| **Total** | **24,444** | **₹15,81,186.20** | **100%** |

```text
Branch 2  █████████████████████████  ₹7.90 Lakh
Branch 1  ██████████████████████     ₹7.06 Lakh
Branch 4  ███                        ₹0.85 Lakh
```

---

### 2. Payment Method Distribution

| Payment Method | Orders | Share |
| :--- | ---: | ---: |
| **Paytm** | 10,109 | 41.36% |
| **UPI** | 5,591 | 22.87% |
| **CCA** | 2,823 | 11.55% |
| **QR** | 2,353 | 9.63% |
| **Cash** | 2,062 | 8.44% |
| **Card** | 1,210 | 4.95% |
| **Blank** | 296 | 1.21% |
| **Total** | **24,444** | **100%** |

```text
Paytm  ████████████████████  41.36%
UPI    ███████████           22.87%
CCA    ██████                11.55%
QR     █████                  9.63%
Cash   ████                   8.44%
Card   ██                     4.95%
Blank  ▏                      1.21%
```

---

### 3. Daily Sales & Order Analysis

| Metric | 1 Apr 2024 | 2 Apr 2024 |
| :--- | ---: | ---: |
| **Sales** | ₹7,45,170.20 | ₹8,36,016.00 |
| **Orders** | 12,168 | 12,276 |
| **Average Order Value** | ₹61.24 | ₹68.10 |

### Change from 1 Apr to 2 Apr

- **Sales:** +12.19%
- **Orders:** +0.89%
- **Average Order Value:** +11.20%

This indicates that sales increased more than order volume, with the higher average order value contributing to the increase.

---

## 🔮 7-Day Demand Forecast

A baseline 7-day demand projection is included as part of the forecasting component.

| Date | Forecasted Orders | Demand Level |
| :--- | ---: | :--- |
| 2026-10-02 | 44 | Baseline Demand |
| 2026-10-03 | 48 | Moderate Demand |
| 2026-10-04 | 35 | Lower Demand |
| 2026-10-05 | 52 | Higher Demand |
| 2026-10-06 | 50 | Higher Demand |
| 2026-10-07 | 47 | Moderate Demand |
| 2026-10-08 | 49 | Above Average |

### Forecast Trend

```text
Orders

55 ┤
50 ┤                 ● 52   ● 50
45 ┤       ● 48                    ● 47   ● 49
40 ┤ ● 44
35 ┤             ● 35
30 ┤
   └──────────────────────────────────────
     Oct 2  Oct 3  Oct 4  Oct 5  Oct 6  Oct 7  Oct 8
```

> **Forecast Note:** The forecast is treated as a baseline projection. Forecast accuracy depends on the amount, quality, and historical coverage of the available data.

---

## 💡 Business Insights

### Branch Performance

Branch 2 generated the highest sales in the currently analyzed dataset, followed by Branch 1.

Together, Branch 1 and Branch 2 account for approximately **94.65% of total sales**.

### Payment Behaviour

Paytm represents the largest share of recorded payment transactions, followed by UPI.

### Daily Performance

Sales increased from **₹7.45 lakh to ₹8.36 lakh**, while order volume increased only slightly. The change was accompanied by an increase in Average Order Value.

### Demand Planning

The forecast can be used as a baseline for planning staffing, inventory, and operational capacity.

---

## 🛠️ Tech Stack

| Category | Technologies |
| :--- | :--- |
| **Database** | MySQL |
| **Programming** | Python |
| **Data Analysis** | Pandas, NumPy |
| **Visualization** | Matplotlib, Seaborn |
| **Forecasting** | Statsmodels, Scikit-learn |
| **Environment** | Jupyter Notebook |

---

## 📂 Project Structure

```text
Cafeteria-Order-Analytics/
│
├── README.md
├── Cafeteria_Analysis_Report.md
├── forecast.py
├── eda_analysis.py
├── requirements.txt
├── forecast_results.csv
├── cafeteria_forecast_trend.png
│
└── notebooks/
    └── cafeteria_analysis.ipynb
```

---

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/vu1f2324001/Cafeteria-Order-Analytics.git
cd Cafeteria-Order-Analytics
```

### 2. Install Dependencies

```bash
pip install pandas numpy matplotlib seaborn statsmodels jupyter mysql-connector-python
```

### 3. Run Jupyter Notebook

```bash
jupyter notebook
```

Open the analysis notebook and execute the cells step by step.

---

## 🧮 Example SQL Query

```sql
SELECT 
    DATE(order_date) AS order_day,
    COUNT(*) AS total_orders,
    SUM(grand_total) AS total_sales
FROM orders
GROUP BY DATE(order_date)
ORDER BY order_day;
```

This query calculates daily order volume and total sales.

---

## 📋 Analysis Workflow

```text
MySQL Order Data
       ↓
Data Cleaning & Validation
       ↓
SQL Analysis
       ↓
Exploratory Data Analysis
       ↓
Visualization
       ↓
Trend Analysis
       ↓
7-Day Demand Forecast
       ↓
Business Insights
       ↓
Final Report
```

---

## 📄 Project Report

The project report covers:

- Dataset overview
- Data preprocessing
- Exploratory Data Analysis
- Branch analysis
- Payment analysis
- Sales trends
- Demand forecasting
- Business insights
- Conclusion

---

## 👩‍💻 Author

**Akshada Valkunde**

Computer Engineering  
**Padmabhushan Vasantdada Patil Pratishthan's College of Engineering & Visual Arts (PVPPCOE)**

---

## 📌 Project Status

**🚧 In Progress**

Baseline data analysis and 7-day demand projection have been completed.

Final metrics and forecast evaluation will be updated after complete validation of the source dataset.
