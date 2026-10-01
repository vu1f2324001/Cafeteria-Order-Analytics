### Observation

Branches 1 and 2 account for the majority of recorded revenue, contributing approximately 94.65% combined revenue.

Branch 2 recorded the highest order volume and revenue, while Branch 1 recorded a higher average order value.

---

# ⏰ Hourly Order Analysis

Hourly analysis was performed to identify high-demand ordering periods.

| Hour | Orders |
|---|---:|
| 19:00 | 3,746 |
| 18:00 | 3,571 |
| 22:00 | 2,127 |
| 23:00 | 1,846 |
| 02:00 | 1,302 |

### Orders by Hour

![Orders by Hour](outputs/orders_by_hour.png)

### Revenue by Hour

![Revenue by Hour](outputs/revenue_by_hour.png)

### Observation

The highest order volume was recorded at **19:00**, with 3,746 orders, followed by 18:00 with 3,571 orders.

The evening period shows the strongest recorded ordering activity in the two-day dataset.

---

# 💳 Payment Method Analysis

Payment methods were normalized into standard categories before analysis.

| Payment Method | Orders | Revenue | AOV | Revenue Share |
|---|---:|---:|---:|---:|
| Paytm | 10,109 | ₹6,05,197.70 | ₹59.87 | 38.27% |
| UPI | 5,591 | ₹4,36,978.00 | ₹78.16 | 27.64% |
| CCA | 2,823 | ₹1,94,752.00 | ₹68.99 | 12.32% |
| QR | 2,353 | ₹1,14,031.00 | ₹48.46 | 7.21% |
| Cash | 2,062 | ₹1,08,379.00 | ₹52.56 | 6.85% |
| Card | 1,210 | ₹1,02,551.00 | ₹84.75 | 6.49% |
| Unknown | 296 | ₹19,297.50 | ₹65.19 | 1.22% |

### Payment Revenue

![Payment Revenue](outputs/payment_revenue.png)

### Observation

Paytm generated the highest recorded revenue share at 38.27%, followed by UPI at 27.64%.

Card transactions had the highest average order value among the listed payment methods at ₹84.75.

---

# 📅 Daily Performance

| Date | Orders | Revenue | AOV |
|---|---:|---:|---:|
| 2024-04-01 | 12,168 | ₹7,45,170.20 | ₹61.24 |
| 2024-04-02 | 12,276 | ₹8,36,016.00 | ₹68.10 |

### Daily Orders

![Daily Orders](outputs/daily_orders.png)

### Daily Revenue

![Daily Revenue](outputs/daily_revenue.png)

### Observation

Between the two recorded days:

- Orders increased by approximately **0.89%**
- Revenue increased by approximately **12.19%**
- Average order value increased by approximately **11.20%**

Because the dataset covers only two days, these changes should not be interpreted as a long-term trend.

---

# 🔮 Demand Forecasting

A simple baseline forecasting approach was used because the available analysis dataset contains only two days of transaction history.

The baseline daily demand was calculated using the average number of daily orders:

**Average Daily Orders = 12,222 orders/day**

This value was used as a simple reference baseline for future demand estimation.

### Demand Forecast

![Demand Forecast](outputs/demand_forecast.png)

> **Important:** This is a baseline forecast, not a production-ready machine-learning prediction. A reliable seasonal forecast would require several weeks or months of historical data.

---

# 💡 Business Insights

Based on the analyzed data:

1. **Branch 2** recorded the highest order volume and revenue.
2. **Branches 1 and 2** generated approximately 94.65% of total recorded revenue.
3. **19:00** was the highest-volume ordering hour.
4. Evening hours showed strong ordering activity.
5. **Paytm** generated the largest revenue share among payment methods.
6. **UPI** recorded a higher AOV than Paytm.
7. **435 orders (1.78%)** had a grand total of ₹0 and were retained after data-quality investigation.
8. Repeated order-number values were flagged rather than automatically deleted because record-level differences were observed.
9. The two-day dataset limits long-term seasonality and forecasting conclusions.

---

# 🛠️ Technology Stack

- **Python 3.x**
- **Pandas** – Data cleaning and analysis
- **NumPy** – Numerical operations
- **Matplotlib** – Data visualization
- **MySQL 8.0** – Data storage and SQL analysis
- **Git & GitHub** – Version control and project hosting

---

# 🔄 Project Workflow

```text
Raw Transaction Data
        ↓
MySQL Database
        ↓
Data Extraction
        ↓
Data Cleaning
        ↓
Data Quality Checks
        ↓
Exploratory Data Analysis
        ↓
KPI Calculation
        ↓
Visualization
        ↓
Demand Baseline
        ↓
Business Insights
