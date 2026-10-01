
# 🍽️ Cafeteria Order Analytics & Demand Forecasting

A data analytics and demand forecasting project developed as part of the **Kanishka Software Pvt. Ltd. Internship Evaluation Challenge**.

The project focuses on analyzing cafeteria order data across multiple branches and counters, identifying operational patterns, and forecasting order demand for the next 7 days for a selected branch.

---

## 📌 Project Objective

The main objectives of this project are:

- Import and process cafeteria order data
- Clean and prepare the dataset for analysis
- Perform Exploratory Data Analysis (EDA)
- Analyze branch-wise order patterns
- Identify peak ordering periods
- Analyze menu/item performance
- Select a branch for demand forecasting
- Forecast the next 7 days of orders
- Generate meaningful business insights and recommendations

---

## 🛠️ Technologies Used

| Technology | Purpose |
| :--- | :--- |
| Python | Data analysis and forecasting |
| Pandas | Data manipulation and preprocessing |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| MySQL | SQL data storage and querying |
| Scikit-learn | Machine learning utilities |
| Statsmodels | Time-series analysis |

---

## 🔄 Project Workflow

```text
SQL Dataset
     │
     ▼
Data Import
     │
     ▼
Data Cleaning & Validation
     │
     ▼
Exploratory Data Analysis (EDA)
     │
     ├──────────────┐
     ▼              ▼
Branch Analysis   Time Analysis
     │              │
     └──────┬───────┘
            ▼
   Menu / Item Analysis
            │
            ▼
   Select One Branch
            │
            ▼
   Daily Order Aggregation
            │
            ▼
   Forecast Next 7 Days
            │
            ▼
 Business Insights & Recommendations
            │
            ▼
       Final Report


---

📊 Analysis Areas

1. Data Cleaning

The dataset will be checked for:

Missing values

Duplicate records

Invalid dates

Incorrect data types

Invalid or inconsistent values


2. Exploratory Data Analysis

The analysis will explore:

Total order volume

Branch-wise order distribution

Daily and weekly order trends

Peak operating periods

Menu/item performance

Sales and order patterns


3. Branch Analysis

Branches will be compared using metrics such as:

Total orders

Average daily orders

Order frequency

Peak-period activity


4. Demand Forecasting

One branch will be selected based on the available dataset.

The selected branch's historical order data will be aggregated by date and used to generate a 7-day order forecast.

The forecasting approach will be selected based on the characteristics and quality of the available data.


---

📈 Visualizations

The project includes visualizations such as:

Daily Order Trend

Branch-wise Order Distribution

Peak-Period Analysis

Top Menu/Item Analysis

Actual vs. Forecasted Orders

7-Day Demand Forecast



---

💡 Business Insights & Recommendations

The current analysis report identifies the following operational insights:

Dynamic Shift Staffing

Increase counter and kitchen support during the reported 12:00 PM – 2:00 PM peak lunch window.

Inventory Stock Pre-allocation

Pre-batch high-selling items before 11:30 AM to reduce potential stock-outs during peak operating hours.

Branch-Level Allocation

The current report identifies Branch_A as the highest-performing branch during the reported rush intervals.


---

📂 Project Structure

Cafeteria-Order-Analytics/
│
├── README.md
├── Cafeteria_Analysis_Report.md
├── forecast.py
├── requirements.txt
├── eda_analysis.py
├── forecast_results.csv
└── cafeteria_forecast_trend.png

> Additional files will be added as the analysis progresses.




---

📦 Dataset

The original SQL dataset contains cafeteria order information across multiple branches and counters.

The dataset is approximately 1.3 GB in size and is therefore processed locally using MySQL.

The raw SQL dataset is not included in this repository due to its large file size.


---

🧹 Data Processing

The project performs the following preprocessing steps:

Connect to the local MySQL database

Identify the relevant cafeteria order table

Inspect the table structure and data types

Check for missing values

Check for duplicate records

Validate date and time fields

Validate order and branch identifiers

Aggregate order data according to the analysis requirements



---

🔎 Exploratory Data Analysis

The EDA analyzes:

Total number of orders

Number of branches

Orders by branch

Orders by date

Daily order trends

Weekly patterns

Peak ordering periods

Frequently ordered menu items

Sales/order relationships where applicable



---

📅 Demand Forecasting

For forecasting:

1. A suitable branch is selected from the available data.


2. Historical orders for that branch are extracted.


3. Orders are aggregated by date.


4. The resulting time series is analyzed.


5. A suitable forecasting method is selected.


6. The model generates a forecast for the next 7 days.


7. Forecast results are exported for reporting and visualization.




---

📊 Reported Results

The current analysis report provides the following reported results:

Metric	Reported Result

Peak Lunch Window	12:00 PM – 2:00 PM
Peak Evening Window	5:00 PM – 7:00 PM
Top Categories	Beverages & Snacks
Category Contribution	Over 65% of daily transactions
Highest Performing Branch	Branch_A
Reported Branch Difference	14.5% vs Branch_B and Branch_C


> These figures are reported in the current analysis document and should be validated against the source database during the final analysis stage.




---

🔮 Next 7 Days Demand Forecast

The current report provides the following baseline rolling-trend forecast:

Date	Estimated Orders

2026-10-02	44
2026-10-03	48
2026-10-04	35
2026-10-05	52
2026-10-06	50
2026-10-07	47
2026-10-08	49


Forecast Summary

The reported forecast ranges from 35 to 52 estimated orders per day.

Highest projected demand: 52 orders on October 5, 2026

Lowest projected demand: 35 orders on October 4, 2026

Forecast period: October 2–8, 2026



---

📈 Forecast Visualization

7-Day Cafeteria Demand Forecast

The visualization shows the reported baseline forecast for the next seven days.


---

📋 Forecast Data

The forecast results can also be stored in:

forecast_results.csv

Expected structure:

Date	Forecasted Orders

2026-10-02	44
2026-10-03	48
2026-10-04	35
2026-10-05	52
2026-10-06	50
2026-10-07	47
2026-10-08	49



---

🚧 Project Status

Work in Progress

Completed

[x] GitHub repository created

[x] Initial project structure prepared

[x] Project workflow defined

[x] MySQL environment setup

[x] Initial exploratory analysis

[x] Branch profiling

[x] Baseline demand forecasting

[x] Forecast visualization


In Progress

[ ] Complete database validation

[ ] Database optimization

[ ] Automated ETL scripts

[ ] Model tuning

# Cafeteria Order Analytics & Demand Forecasting

A data analytics and demand forecasting project developed as part of the Kanishka Software Pvt. Ltd. Internship Evaluation Challenge.

The project focuses on analyzing cafeteria order data across multiple branches and counters, identifying operational patterns, and forecasting order demand for the next 7 days for a selected branch.

---

📌 Project Objective

The main objectives of this project are:

- Import and process cafeteria order data
- Clean and prepare the dataset for analysis
- Perform Exploratory Data Analysis (EDA)
- Analyze branch-wise order patterns
- Identify peak ordering periods
- Analyze menu/item performance
- Select a branch for demand forecasting
- Forecast the next 7 days of orders
- Generate meaningful business insights and recommendations

---

🛠️ Technologies Used

| Technology | Purpose |
| :--- | :--- |
| Python | Data analysis and forecasting |
| Pandas | Data manipulation and preprocessing |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| MySQL | SQL data storage and querying |
| Scikit-learn | Machine learning utilities |
| Statsmodels | Time-series analysis |

---

🔄 Project Workflow

---

📊 Analysis Areas

1. Data Cleaning

The dataset will be checked for:

- Missing values
- Duplicate records
- Invalid dates
- Incorrect data types
- Invalid or inconsistent values

2. Exploratory Data Analysis

The analysis will explore:

- Total order volume
- Branch-wise order distribution
- Daily and weekly order trends
- Peak operating periods
- Menu/item performance
- Sales and order patterns

3. Branch Analysis

Branches will be compared using metrics such as:

- Total orders
- Average daily orders
- Order frequency
- Peak-period activity

4. Demand Forecasting

One branch will be selected based on the available dataset.

The selected branch's historical order data will be aggregated by date and used to generate a 7-day order forecast.

The forecasting approach will be selected based on the characteristics and quality of the available data.

---

📈 Visualizations

The project will include visualizations such as:

- Daily order trend
- Branch-wise order distribution
- Peak-period analysis
- Top menu/item analysis
- Actual vs. forecasted orders

---

💡 Business Insights

The final analysis will provide data-supported insights related to:

- High-demand branches
- Peak ordering periods
- Frequently ordered items
- Changes in order volume
- Operational planning opportunities
