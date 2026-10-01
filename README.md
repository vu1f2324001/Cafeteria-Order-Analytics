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

- **SQL Dataset**
- └── **Data Import**
- └── **Data Cleaning & Validation**
- └── **Exploratory Data Analysis (EDA)**
  - ├── Branch Analysis
  - └── Time-Based Analysis
- └── **Menu / Item Analysis**
- └── **Select Target Branch**
- └── **Daily Order Aggregation**
- └── **7-Day Demand Forecasting**
- └── **Business Insights & Recommendations**
- └── **Final Report**

---

## 📊 Analysis Areas

### 1. Data Cleaning
The dataset will be checked for:
- Missing values
- Duplicate records
- Invalid dates
- Incorrect data types
- Invalid or inconsistent values

### 2. Exploratory Data Analysis
The analysis will explore:
- Total order volume
- Branch-wise order distribution
- Daily and weekly order trends
- Peak operating periods
- Menu/item performance
- Sales and order patterns

### 3. Branch Analysis
Branches will be compared using metrics such as:
- Total orders
- Average daily orders
- Order frequency
- Peak-period activity

### 4. Demand Forecasting
One branch will be selected based on the available dataset. The selected branch's historical order data will be aggregated by date and used to generate a 7-day order forecast. The forecasting approach will be selected based on the characteristics and quality of the available data.

---

## 📈 Visualizations

The project includes visualizations such as:
- **Daily Order Trend:** Shows how order volume changes over time.
- **Branch-wise Orders:** Compares order volume across branches.
- **Peak-Period Analysis:** Identifies customer rush windows.
- **Top Menu/Item Analysis:** Identifies frequently ordered items.
- **Actual vs. Forecasted Orders:** Shows historical orders together with the 7-day forecast.
- **7-Day Demand Forecast:** Visual representation of predicted daily volume.

---

## 💡 Business Insights & Recommendations

The current analysis report identifies the following operational insights:

- **Dynamic Shift Staffing:** Increase counter and kitchen support during the reported 12:00 PM – 2:00 PM peak lunch window.
- **Inventory Stock Pre-allocation:** Pre-batch high-selling items before 11:30 AM to reduce potential stock-outs during peak operating hours.
- **Branch-Level Allocation:** The current report identifies Branch_A as the highest-performing branch during the reported rush intervals.

---

## 📂 Project Structure

- **Cafeteria-Order-Analytics/**
  - `README.md`
  - `Cafeteria_Analysis_Report.md`
  - `forecast.py`
  - `requirements.txt`
  - `eda_analysis.py`
  - `forecast_results.csv`
  - `cafeteria_forecast_trend.png`

> Additional files will be added as the analysis progresses.

---

## 📦 Dataset

The original SQL dataset contains cafeteria order information across multiple branches and counters.

The dataset is approximately **1.3 GB** in size and is therefore processed locally using MySQL. The raw SQL dataset is not included in this repository due to its large file size.

---

## 🧹 Data Processing

The project performs the following preprocessing steps:

1. Connect to the local MySQL database.
2. Identify the relevant cafeteria order table.
3. Inspect the table structure and data types.
4. Check for missing values.
5. Check for duplicate records.
6. Validate date and time fields.
7. Validate order and branch identifiers.
8. Aggregate order data according to the analysis requirements.

---

## 🔎 Exploratory Data Analysis

The EDA analyzes:

- Total number of orders
- Number of branches
- Orders by branch
- Orders by date
- Daily order trends
- Weekly patterns
- Peak ordering periods
- Frequently ordered menu items
- Sales/order relationships where applicable

---

## 📅 Demand Forecasting

For forecasting:

1. A suitable branch is selected from the available data.
2. Historical orders for that branch are extracted.
3. Orders are aggregated by date.
4. The resulting time series is analyzed.
5. A suitable forecasting method is selected.
6. The model generates a forecast for the next 7 days.
7. Forecast results are exported for reporting and visualization.

---

## 📊 Reported Results

| Metric | Reported Result |
| :--- | :--- |
| **Peak Lunch Window** | 12:00 PM – 2:00 PM |
| **Peak Evening Window** | 5:00 PM – 7:00 PM |
| **Top Categories** | Beverages & Snacks |
| **Category Contribution** | Over 65% of daily transactions |
| **Highest Performing Branch** | Branch_A |
| **Reported Branch Difference** | 14.5% vs Branch_B and Branch_C |

> These figures are reported in the current analysis document and should be validated against the source database during the final analysis stage.

---

## 🔮 Next 7 Days Demand Forecast

The current report provides the following baseline rolling-trend forecast[span_4](start_span)[span_4](end_span):

| Date | Estimated Orders |
| :---: | :---: |
| 2026-10-02 | 44 |
| 2026-10-03 | 48 |
| 2026-10-04 | 35 |
| 2026-10-05 | 52 |
| 2026-10-06 | 50 |
| 2026-10-07 | 47 |
| 2026-10-08 | 49 |

### Forecast Summary
- The reported forecast ranges from **35 to 52 estimated orders per day**[span_5](start_span)[span_5](end_span)[span_6](start_span)[span_6](end_span).
- **Highest projected demand:** 52 orders on October 5, 2026[span_7](start_span)[span_7](end_span)[span_8](start_span)[span_8](end_span)
- **Lowest projected demand:** 35 orders on October 4, 2026[span_9](start_span)[span_9](end_span)[span_10](start_span)[span_10](end_span)
- **Forecast period:** October 2–8, 2026[span_11](start_span)[span_11](end_span)[span_12](start_span)[span_12](end_span)

---

## 📈 Forecast Visualization

![Cafeteria - Next 7 Days Demand Forecast](cafeteria_forecast_trend.png)

The visualization shows the reported baseline forecast for the next seven days[span_13](start_span)[span_13](end_span)[span_14](start_span)[span_14](end_span).

---

## 📋 Forecast Data

The forecast results are stored in `forecast_results.csv`[span_15](start_span)[span_15](end_span):

| Date | Forecasted Orders |
| :---: | :---: |
| 2026-10-02 | 44 |
| 2026-10-03 | 48 |
| 2026-10-04 | 35 |
| 2026-10-05 | 52 |
| 2026-10-06 | 50 |
| 2026-10-07 | 47 |
| 2026-10-08 | 49 |

---

## 🚧 Project Status

**Work in Progress**

### Completed
- [x] GitHub repository created
- [x] Initial project structure prepared
- [x] Project workflow defined
- [x] MySQL environment setup
- [x] Initial exploratory analysis
- [x] Branch profiling
- [x] Baseline demand forecasting
- [x] Forecast visualization

### In Progress
- [ ] Complete database validation
- [ ] Database optimization
- [ ] Automated ETL scripts
- [ ] Model tuning

---

## ▶️ Installation & Setup

Clone the repository:
```bash
git clone [https://github.com/vu1f2324001/Cafeteria-Order-Analytics.git](https://github.com/vu1f2324001/Cafeteria-Order-Analytics.git)
cd Cafeteria-Order-Analytics
pip install -r requirements.txt
