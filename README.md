\# Cafeteria Order Analytics \& Demand Forecasting



!\[Python](https://img.shields.io/badge/Python-3.x-blue)

!\[MySQL](https://img.shields.io/badge/MySQL-8.0-orange)

!\[Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-green)

!\[Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-yellow)

!\[Status](https://img.shields.io/badge/Project-Completed-success)



\## 📌 Project Overview



\*\*Cafeteria Order Analytics \& Demand Forecasting\*\* is a data analytics project developed as part of the \*\*Kanishka Software Pvt. Ltd. Internship Evaluation Challenge\*\*.



The project analyzes cafeteria order transaction data using \*\*MySQL and Python\*\* to identify sales patterns, branch performance, payment behavior, peak ordering hours, data-quality issues, and baseline future demand.



The analysis follows a complete data workflow:



\*\*Raw Data → Data Cleaning → Exploratory Data Analysis → Visualization → Demand Forecasting → Business Insights\*\*



\---



\## 👩‍💻 Author



\*\*Akshada Valkunde\*\*



Computer Engineering  

Padmabhushan Vasantdada Patil Pratishthan's College of Engineering \& Visual Arts (PVPPCOE)



GitHub: \[@vu1f2324001](https://github.com/vu1f2324001)



\---



\# 🎯 Objectives



\- Analyze cafeteria order transaction data

\- Measure overall revenue and order performance

\- Compare branch-wise sales and order volumes

\- Identify peak ordering hours

\- Analyze payment methods

\- Detect and document data-quality issues

\- Analyze zero-value transactions

\- Create visual dashboards/charts

\- Generate a simple baseline demand forecast

\- Derive actionable business insights



\---



\# 📊 Dataset Summary



The current analysis dataset contains:



| Metric | Value |

|---|---:|

| Total Orders | \*\*24,444\*\* |

| Total Revenue | \*\*₹15,81,186.20\*\* |

| Average Order Value | \*\*₹64.69\*\* |

| Branches | \*\*3\*\* |

| Unique Customers | \*\*6,661\*\* |

| Zero-Value Orders | \*\*435\*\* |

| Negative-Value Orders | \*\*0\*\* |

| Analysis Period | \*\*1 Apr 2024 – 2 Apr 2024\*\* |



> \*\*Note:\*\* The currently analyzed dataset covers two calendar days. Therefore, weekday and forecasting insights are treated as limited/baseline analysis rather than long-term seasonal predictions.



\---



\# 🧹 Data Cleaning \& Quality Checks



The raw order data was reviewed before performing analytics.



\### Checks performed



\- Missing/unknown payment method handling

\- Payment method normalization

\- Zero-value transaction detection

\- Negative-value transaction detection

\- Repeated order-number identification

\- Date/time conversion

\- Branch and customer uniqueness checks



\### Zero-Value Transactions



There were \*\*435 orders\*\* where `grand\_total = ₹0`.



These records were \*\*not deleted\*\*.



Further investigation showed:



\- 435/435 had positive subtotal values

\- 435/435 had positive reward amounts

\- 0 were marked as refunded

\- 0 had cancellation reasons

\- 0 had discounts recorded



Therefore, these records were retained and flagged as:



`zero\_value\_order = True`



This prevents potentially valid transactions from being incorrectly removed.



\### Repeated Order Numbers



Repeated `order\_number` values were identified.



However, detailed record-level inspection showed that repeated order numbers can correspond to separate transactions with differences in:



\- Date

\- Customer

\- Branch

\- Order value

\- Payment method



Therefore, repeated order numbers were \*\*flagged instead of deleted\*\*.



\---



\# 📈 Key Performance Indicators



\### Total Revenue



\*\*₹15,81,186.20\*\*



\### Total Orders



\*\*24,444\*\*



\### Average Order Value



\*\*₹64.69\*\*



\### Unique Customers



\*\*6,661\*\*



\### Branches



\*\*3\*\*



\---



\# 🏢 Branch Performance



The analysis compares branches based on order volume, revenue, and average order value.



| Branch | Orders | Revenue | AOV |

|---|---:|---:|---:|

| Branch 2 | 12,483 | ₹7,90,096.20 | ₹63.29 |

| Branch 1 | 10,326 | ₹7,06,472.00 | ₹68.42 |

| Branch 4 | 1,635 | ₹84,618.00 | ₹51.75 |



\### Revenue by Branch



!\[Revenue by Branch](outputs/revenue\_by\_branch.png)



\### Orders by Branch



!\[Orders by Branch](outputs/orders\_by\_branch.png)



\### Observation



Branches 1 and 2 account for the majority of recorded

