import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import mysql.connector
from getpass import getpass

# ============================================================
# DEEP CAFETERIA ORDER ANALYSIS
# ============================================================

print("\n==============================================")
print("     CAFETERIA DEEP ANALYTICS")
print("==============================================\n")

# ------------------------------------------------------------
# 1. MYSQL CONNECTION
# ------------------------------------------------------------

password = getpass("Enter MySQL password: ")

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password=password,
    database="cafeteria_db"
)

print("✓ MySQL connected successfully")

# ------------------------------------------------------------
# 2. LOAD DATA
# ------------------------------------------------------------

query = """
SELECT
    id,
    order_number,
    user_id,
    order_status,
    order_date,
    branch_id,
    grand_total,
    mode_of_transaction
FROM orders
WHERE order_date IS NOT NULL
"""

df = pd.read_sql(query, conn)

conn.close()

print(f"✓ Orders loaded: {len(df):,}")

# ------------------------------------------------------------
# 3. DATA CLEANING
# ------------------------------------------------------------

df["order_date"] = pd.to_datetime(
    df["order_date"],
    errors="coerce"
)

df["grand_total"] = pd.to_numeric(
    df["grand_total"],
    errors="coerce"
)

df["branch_id"] = df["branch_id"].astype("string")

df["payment_method"] = (
    df["mode_of_transaction"]
    .fillna("Unknown")
    .astype(str)
    .str.strip()
    .str.lower()
)

df["payment_method"] = df["payment_method"].replace({
    "upi": "UPI",
    "paytm": "Paytm",
    "cca": "CCA",
    "qr": "QR",
    "cash": "Cash",
    "card": "Card",
    "": "Unknown",
    "nan": "Unknown"
})

df = df.dropna(
    subset=["order_date", "grand_total"]
)

# Time columns
df["date"] = df["order_date"].dt.date
df["hour"] = df["order_date"].dt.hour
df["weekday"] = df["order_date"].dt.day_name()
df["month"] = df["order_date"].dt.to_period("M").astype(str)

# ------------------------------------------------------------
# 4. OUTPUT FOLDER
# ------------------------------------------------------------

os.makedirs("outputs", exist_ok=True)

# ------------------------------------------------------------
# 5. BASIC DATA QUALITY ANALYSIS
# ------------------------------------------------------------

print("\n==============================================")
print("DATA QUALITY")
print("==============================================")

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())

print("\nDuplicate order numbers:")
print(df["order_number"].duplicated().sum())

print("\nOrder status:")
print(df["order_status"].value_counts(dropna=False))

# ------------------------------------------------------------
# 6. KPI SUMMARY
# ------------------------------------------------------------

total_orders = len(df)
total_revenue = df["grand_total"].sum()
average_order_value = df["grand_total"].mean()

unique_customers = df["user_id"].nunique()
unique_branches = df["branch_id"].nunique()

minimum_order = df["grand_total"].min()
maximum_order = df["grand_total"].max()
median_order = df["grand_total"].median()

print("\n==============================================")
print("KEY PERFORMANCE INDICATORS")
print("==============================================")

print(f"Total Orders        : {total_orders:,}")
print(f"Total Revenue       : ₹{total_revenue:,.2f}")
print(f"Average Order Value : ₹{average_order_value:,.2f}")
print(f"Unique Customers    : {unique_customers:,}")
print(f"Branches            : {unique_branches}")
print(f"Minimum Order       : ₹{minimum_order:,.2f}")
print(f"Maximum Order       : ₹{maximum_order:,.2f}")
print(f"Median Order Value  : ₹{median_order:,.2f}")

# ------------------------------------------------------------
# 7. BRANCH ANALYSIS
# ------------------------------------------------------------

branch_analysis = (
    df.groupby("branch_id")
    .agg(
        orders=("id", "count"),
        revenue=("grand_total", "sum"),
        average_order_value=("grand_total", "mean")
    )
    .sort_values("revenue", ascending=False)
)

branch_analysis["revenue_share_%"] = (
    branch_analysis["revenue"]
    / total_revenue
    * 100
)

print("\n==============================================")
print("BRANCH ANALYSIS")
print("==============================================")

print(branch_analysis.round(2))

branch_analysis.to_csv(
    "branch_analysis.csv"
)

# ------------------------------------------------------------
# 8. CHART — REVENUE BY BRANCH
# ------------------------------------------------------------

plt.figure(figsize=(9, 6))

sns.barplot(
    x=branch_analysis.index.astype(str),
    y=branch_analysis["revenue"]
)

plt.title("Revenue by Branch")
plt.xlabel("Branch")
plt.ylabel("Revenue (₹)")
plt.tight_layout()

plt.savefig(
    "outputs/01_revenue_by_branch.png",
    dpi=200
)

plt.close()

# ------------------------------------------------------------
# 9. CHART — ORDERS BY BRANCH
# ------------------------------------------------------------

plt.figure(figsize=(9, 6))

sns.barplot(
    x=branch_analysis.index.astype(str),
    y=branch_analysis["orders"]
)

plt.title("Orders by Branch")
plt.xlabel("Branch")
plt.ylabel("Number of Orders")
plt.tight_layout()

plt.savefig(
    "outputs/02_orders_by_branch.png",
    dpi=200
)

plt.close()

# ------------------------------------------------------------
# 10. CHART — BRANCH AOV
# ------------------------------------------------------------

plt.figure(figsize=(9, 6))

sns.barplot(
    x=branch_analysis.index.astype(str),
    y=branch_analysis["average_order_value"]
)

plt.title("Average Order Value by Branch")
plt.xlabel("Branch")
plt.ylabel("Average Order Value (₹)")
plt.tight_layout()

plt.savefig(
    "outputs/03_branch_aov.png",
    dpi=200
)

plt.close()

# ------------------------------------------------------------
# 11. HOURLY ANALYSIS
# ------------------------------------------------------------

hourly_analysis = (
    df.groupby("hour")
    .agg(
        orders=("id", "count"),
        revenue=("grand_total", "sum")
    )
    .sort_index()
)

print("\n==============================================")
print("HOURLY ANALYSIS")
print("==============================================")

print(hourly_analysis)

peak_hour = hourly_analysis["orders"].idxmax()
peak_hour_orders = hourly_analysis["orders"].max()

print(
    f"\nPeak order hour: {peak_hour}:00 "
    f"with {peak_hour_orders:,} orders"
)

hourly_analysis.to_csv(
    "hourly_analysis.csv"
)

# ------------------------------------------------------------
# 12. CHART — ORDERS BY HOUR
# ------------------------------------------------------------

plt.figure(figsize=(12, 6))

sns.lineplot(
    x=hourly_analysis.index,
    y=hourly_analysis["orders"],
    marker="o"
)

plt.title("Orders by Hour of Day")
plt.xlabel("Hour")
plt.ylabel("Number of Orders")
plt.xticks(range(24))
plt.grid(True, alpha=0.3)

plt.tight_layout()

plt.savefig(
    "outputs/04_orders_by_hour.png",
    dpi=200
)

plt.close()

# ------------------------------------------------------------
# 13. CHART — REVENUE BY HOUR
# ------------------------------------------------------------

plt.figure(figsize=(12, 6))

sns.lineplot(
    x=hourly_analysis.index,
    y=hourly_analysis["revenue"],
    marker="o"
)

plt.title("Revenue by Hour of Day")
plt.xlabel("Hour")
plt.ylabel("Revenue (₹)")
plt.xticks(range(24))
plt.grid(True, alpha=0.3)

plt.tight_layout()

plt.savefig(
    "outputs/05_revenue_by_hour.png",
    dpi=200
)

plt.close()

# ------------------------------------------------------------
# 14. DAILY ANALYSIS
# ------------------------------------------------------------

daily_analysis = (
    df.groupby("date")
    .agg(
        orders=("id", "count"),
        revenue=("grand_total", "sum"),
        average_order_value=("grand_total", "mean")
    )
)

daily_analysis.index = pd.to_datetime(
    daily_analysis.index
)

print("\n==============================================")
print("DAILY ANALYSIS")
print("==============================================")

print(daily_analysis.round(2))

daily_analysis.to_csv(
    "daily_analysis.csv"
)

# ------------------------------------------------------------
# 15. DAILY ORDERS CHART
# ------------------------------------------------------------

plt.figure(figsize=(10, 6))

sns.barplot(
    x=daily_analysis.index.strftime("%Y-%m-%d"),
    y=daily_analysis["orders"]
)

plt.title("Daily Orders")
plt.xlabel("Date")
plt.ylabel("Orders")
plt.xticks(rotation=30)

plt.tight_layout()

plt.savefig(
    "outputs/06_daily_orders.png",
    dpi=200
)

plt.close()

# ------------------------------------------------------------
# 16. DAILY REVENUE CHART
# ------------------------------------------------------------

plt.figure(figsize=(10, 6))

sns.barplot(
    x=daily_analysis.index.strftime("%Y-%m-%d"),
    y=daily_analysis["revenue"]
)

plt.title("Daily Revenue")
plt.xlabel("Date")
plt.ylabel("Revenue (₹)")
plt.xticks(rotation=30)

plt.tight_layout()

plt.savefig(
    "outputs/07_daily_revenue.png",
    dpi=200
)

plt.close()

# ------------------------------------------------------------
# 17. PAYMENT ANALYSIS
# ------------------------------------------------------------

payment_analysis = (
    df.groupby("payment_method")
    .agg(
        orders=("id", "count"),
        revenue=("grand_total", "sum"),
        average_order_value=("grand_total", "mean")
    )
    .sort_values("revenue", ascending=False)
)

payment_analysis["revenue_share_%"] = (
    payment_analysis["revenue"]
    / total_revenue
    * 100
)

print("\n==============================================")
print("PAYMENT METHOD ANALYSIS")
print("==============================================")

print(payment_analysis.round(2))

payment_analysis.to_csv(
    "payment_analysis.csv"
)

# ------------------------------------------------------------
# 18. PAYMENT REVENUE CHART
# ------------------------------------------------------------

plt.figure(figsize=(11, 6))

sns.barplot(
    x=payment_analysis.index,
    y=payment_analysis["revenue"]
)

plt.title("Revenue by Payment Method")
plt.xlabel("Payment Method")
plt.ylabel("Revenue (₹)")
plt.xticks(rotation=30)

plt.tight_layout()

plt.savefig(
    "outputs/08_payment_revenue.png",
    dpi=200
)

plt.close()

# ------------------------------------------------------------
# 19. PAYMENT ORDER COUNT CHART
# ------------------------------------------------------------

plt.figure(figsize=(11, 6))

sns.barplot(
    x=payment_analysis.index,
    y=payment_analysis["orders"]
)

plt.title("Orders by Payment Method")
plt.xlabel("Payment Method")
plt.ylabel("Number of Orders")
plt.xticks(rotation=30)

plt.tight_layout()

plt.savefig(
    "outputs/09_payment_orders.png",
    dpi=200
)

plt.close()

# ------------------------------------------------------------
# 20. ORDER VALUE DISTRIBUTION
# ------------------------------------------------------------

plt.figure(figsize=(10, 6))

sns.histplot(
    df["grand_total"],
    bins=40,
    kde=True
)

plt.title("Order Value Distribution")
plt.xlabel("Order Value (₹)")
plt.ylabel("Number of Orders")

plt.tight_layout()

plt.savefig(
    "outputs/10_order_value_distribution.png",
    dpi=200
)

plt.close()

# ------------------------------------------------------------
# 21. WEEKDAY ANALYSIS
# ------------------------------------------------------------

weekday_order = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

weekday_analysis = (
    df.groupby("weekday")
    .size()
    .reindex(weekday_order)
    .dropna()
)

print("\n==============================================")
print("WEEKDAY ANALYSIS")
print("==============================================")

print(weekday_analysis)

plt.figure(figsize=(10, 6))

sns.barplot(
    x=weekday_analysis.index,
    y=weekday_analysis.values
)

plt.title("Orders by Day of Week")
plt.xlabel("Day")
plt.ylabel("Number of Orders")
plt.xticks(rotation=30)

plt.tight_layout()

plt.savefig(
    "outputs/11_orders_by_weekday.png",
    dpi=200
)

plt.close()

# ------------------------------------------------------------
# 22. BRANCH × HOUR ANALYSIS
# ------------------------------------------------------------

branch_hour = (
    df.groupby(["hour", "branch_id"])
    .size()
    .unstack(fill_value=0)
)

plt.figure(figsize=(13, 7))

sns.heatmap(
    branch_hour.T,
    annot=False,
    cmap="YlGnBu"
)

plt.title("Branch-wise Demand by Hour")
plt.xlabel("Hour")
plt.ylabel("Branch")

plt.tight_layout()

plt.savefig(
    "outputs/12_branch_hour_heatmap.png",
    dpi=200
)

plt.close()

# ------------------------------------------------------------
# 23. ORDER STATUS ANALYSIS
# ------------------------------------------------------------

status_analysis = (
    df["order_status"]
    .value_counts(dropna=False)
    .sort_index()
)

print("\n==============================================")
print("ORDER STATUS ANALYSIS")
print("==============================================")

print(status_analysis)

plt.figure(figsize=(9, 6))

sns.barplot(
    x=status_analysis.index.astype(str),
    y=status_analysis.values
)

plt.title("Order Status Distribution")
plt.xlabel("Order Status")
plt.ylabel("Number of Orders")

plt.tight_layout()

plt.savefig(
    "outputs/13_order_status.png",
    dpi=200
)

plt.close()

# ------------------------------------------------------------
# 24. FORECAST
# ------------------------------------------------------------

print("\n==============================================")
print("DEMAND FORECAST")
print("==============================================")

daily_orders = (
    df.groupby("date")
    .size()
    .reset_index(name="orders")
)

daily_orders["date"] = pd.to_datetime(
    daily_orders["date"]
)

daily_orders = daily_orders.sort_values("date")

if len(daily_orders) >= 7:

    forecast_value = (
        daily_orders["orders"]
        .tail(7)
        .mean()
    )

else:

    forecast_value = (
        daily_orders["orders"]
        .mean()
    )

last_date = daily_orders["date"].max()

future_dates = pd.date_range(
    start=last_date + pd.Timedelta(days=1),
    periods=7,
    freq="D"
)

forecast = pd.DataFrame({
    "date": future_dates,
    "forecast_orders": [
        round(forecast_value)
    ] * 7
})

print(forecast)

forecast.to_csv(
    "forecast_results.csv",
    index=False
)

# Forecast chart

plt.figure(figsize=(12, 6))

plt.plot(
    daily_orders["date"],
    daily_orders["orders"],
    marker="o",
    label="Historical Orders"
)

plt.plot(
    forecast["date"],
    forecast["forecast_orders"],
    marker="o",
    linestyle="--",
    label="7-Day Forecast"
)

plt.title("Cafeteria Demand Forecast")
plt.xlabel("Date")
plt.ylabel("Number of Orders")
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()

plt.savefig(
    "outputs/14_demand_forecast.png",
    dpi=200
)

plt.close()

# ------------------------------------------------------------
# 25. MASTER SUMMARY
# ------------------------------------------------------------

summary = pd.DataFrame({
    "Metric": [
        "Total Orders",
        "Total Revenue",
        "Average Order Value",
        "Median Order Value",
        "Minimum Order Value",
        "Maximum Order Value",
        "Unique Customers",
        "Unique Branches",
        "Peak Order Hour",
        "Peak Hour Orders",
        "Analysis Start Date",
        "Analysis End Date"
    ],
    "Value": [
        total_orders,
        total_revenue,
        average_order_value,
        median_order,
        minimum_order,
        maximum_order,
        unique_customers,
        unique_branches,
        peak_hour,
        peak_hour_orders,
        df["order_date"].min(),
        df["order_date"].max()
    ]
})

summary.to_csv(
    "analytics_summary.csv",
    index=False
)

# ------------------------------------------------------------
# 26. FINAL OUTPUT
# ------------------------------------------------------------

print("\n==============================================")
print("       DEEP ANALYSIS COMPLETE ✓")
print("==============================================")

print("\nGenerated charts:")

for file in sorted(os.listdir("outputs")):
    if file.endswith(".png"):
        print("✓", file)

print("\nGenerated analysis files:")

print("✓ analytics_summary.csv")
print("✓ branch_analysis.csv")
print("✓ hourly_analysis.csv")
print("✓ daily_analysis.csv")
print("✓ payment_analysis.csv")
print("✓ forecast_results.csv")

print("\n==============================================")
print("All analysis completed successfully!")
print("==============================================")