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

Recommendations will be based only on patterns observed in the dataset.

---

📂 Project Structure
Additional files will be added as the analysis progresses.

---

📦 Dataset

The original SQL dataset contains cafeteria order information across multiple branches and counters.

The dataset is approximately 1.3 GB in size and is therefore processed locally using MySQL.

The raw SQL dataset is not included in this repository due to its large file size.

---

🧹 Data Processing

The project will perform the following preprocessing steps:

1. Connect to the local MySQL database.
2. Identify the relevant cafeteria order table.
3. Inspect the table structure and data types.
4. Check for missing values.
5. Check for duplicate records.
6. Validate date and time fields.
7. Validate order and branch identifiers.
8. Aggregate order data according to the analysis requirements.

---

🔎 Exploratory Data Analysis

The EDA will analyze:

- Total number of orders
- Number of branches
- Orders by branch
- Orders by date
- Daily order trends
- Weekly patterns
- Peak ordering periods
- Frequently ordered menu items
- Sales/order relationships where applicable

All insights reported in the final analysis will be derived from the actual dataset.

---

📅 Demand Forecasting

For forecasting:

1. A suitable branch will be selected from the available data.
2. Historical orders for that branch will be extracted.
3. Orders will be aggregated by date.
4. The resulting time series will be analyzed.
5. A suitable forecasting method will be selected.
6. The model will generate a forecast for the next 7 days.
7. Forecast results will be saved for reporting and visualization.

The forecasting model will be selected based on the available data and observed time-series characteristics.

---

📊 Forecast Output

The final project will generate:

- Selected branch
- Historical daily order volume
- Forecast dates
- Forecasted order counts
- Forecast visualization
- Forecast evaluation metrics where applicable

Example output structure:

| Date | Forecasted Orders |
| :--- | :--- |
| YYYY-MM-DD | -- |
| YYYY-MM-DD | -- |
| YYYY-MM-DD | -- |
| YYYY-MM-DD | -- |
| YYYY-MM-DD | -- |
| YYYY-MM-DD | -- |
| YYYY-MM-DD | -- |

Actual values will be generated from the dataset after completing the analysis.

---

📈 Visualizations

The project will generate visualizations such as:

Daily Order Trend
Shows how order volume changes over time.

Branch-wise Orders
Compares order volume across branches.

Menu / Item Analysis
Identifies frequently ordered items.

Forecast Trend
Shows historical orders together with the 7-day forecast.

---

💡 Business Insights & Recommendations

The final report will provide data-supported recommendations related to:

- Branch-level demand
- Staffing requirements
- Inventory planning
- Peak-period preparation
- Frequently ordered items
- Demand fluctuations
- Operational planning

Recommendations will be based only on patterns observed in the actual dataset.

---

🚧 Project Status

Work in Progress

Completed

- [x] GitHub repository created
- [x] Initial project structure prepared
- [x] Project workflow defined
- [x] MySQL environment setup

In Progress

- [ ] Complete SQL data import
- [ ] Database inspection
- [ ] Data cleaning
- [ ] Exploratory Data Analysis
- [ ] Branch analysis
- [ ] Time-based analysis
- [ ] Menu/item analysis
- [ ] Branch selection
- [ ] Forecasting model
- [ ] Forecast evaluation
- [ ] Visualizations
- [ ] Business insights
- [ ] Final report

---

▶️️ Installation

Clone the repository:

```bash
git clone [https://github.com/vu1f2324001/Cafeteria-Order-Analytics.git](https://github.com/vu1f2324001/Cafeteria-Order-Analytics.git)
cd Cafeteria-Order-Analytics
pip install -r requirements.txt
MySQL Database
      ↓
SQL Data Inspection
      ↓
Python + Pandas
      ↓
Data Cleaning
      ↓
EDA
      ↓
Branch Analysis
      ↓
Time-Series Aggregation
      ↓
Forecasting
      ↓
Visualization
      ↓
Business Insights
      ↓
Final Report
