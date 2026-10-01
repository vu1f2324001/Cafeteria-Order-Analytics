import os
import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector
from getpass import getpass

# ============================================================
# 1. CONNECT TO MYSQL
# ============================================================

print("\nConnecting to MySQL...")

password = getpass("Enter MySQL password: ")

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password=password,
    database="cafeteria_db"
)

print("Connected successfully!")

# ============================================================
# 2. LOAD ORDER DATA
# ============================================================

query = """
SELECT
    id,
    order_date,
    branch_id,
    grand_total,
    mode_of_transaction,
    order_status
FROM orders
WHERE order_date IS NOT NULL
  AND grand_total IS NOT NULL
"""

df = pd.read_sql(query, conn)

conn.close()

print(f"\nTotal orders loaded: {len(df):,}")

# ============================================================
# 3. BASIC CLEANING
# ============================================================

df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
df["grand_total"] = pd.to_numeric(df["grand_total"], errors="coerce")

df = df.dropna(subset=["order_date", "grand_total"])

df["hour"] = df["order_date"].dt.hour
df["weekday"] = df["order_date"].dt.day_name()
df["date"] = df["order_date"].dt.date
df["month"] = df["order_date"].dt.to_period("M").astype(str)

# Create output folder
os.makedirs("outputs", exist_ok=True)

# ============================================================
# 4. CHART 1 — REVENUE BY BRANCH
# ============================================================

branch_revenue = (
    df.groupby("branch_id")["grand_total"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(9, 6))

branch_revenue.plot(kind="bar")

plt.title("Revenue by Branch")
plt.xlabel("Branch")
plt.ylabel("Revenue (₹)")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig(
    "outputs/revenue_by_branch.png",
    dpi=200,
    bbox_inches="tight"
)

plt.close()

print("✓ revenue_by_branch.png created")

# ============================================================
# 5. CHART 2 — ORDERS BY HOUR
# ============================================================

orders_by_hour = (
    df.groupby("hour")
    .size()
    .sort_index()
)

plt.figure(figsize=(10, 6))

orders_by_hour.plot(kind="bar")

plt.title("Orders by Hour of Day")
plt.xlabel("Hour")
plt.ylabel("Number of Orders")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig(
    "outputs/orders_by_hour.png",
    dpi=200,
    bbox_inches="tight"
)

plt.close()

print("✓ orders_by_hour.png created")

# ============================================================
# 6. CHART 3 — ORDERS BY WEEKDAY
# ============================================================

weekday_order = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

orders_by_weekday = (
    df.groupby("weekday")
    .size()
    .reindex(weekday_order)
    .dropna()
)

plt.figure(figsize=(10, 6))

orders_by_weekday.plot(kind="bar")

plt.title("Orders by Day of Week")
plt.xlabel("Day")
plt.ylabel("Number of Orders")
plt.xticks(rotation=30)
plt.tight_layout()

plt.savefig(
    "outputs/orders_by_weekday.png",
    dpi=200,
    bbox_inches="tight"
)

plt.close()

print("✓ orders_by_weekday.png created")

# ============================================================
# 7. CHART 4 — MONTHLY ORDERS BY BRANCH
# ============================================================

monthly_branch = (
    df.groupby(["month", "branch_id"])
    .size()
    .unstack(fill_value=0)
)

plt.figure(figsize=(11, 6))

monthly_branch.plot(kind="bar")

plt.title("Monthly Orders by Branch")
plt.xlabel("Month")
plt.ylabel("Number of Orders")
plt.xticks(rotation=30)

plt.tight_layout()

plt.savefig(
    "outputs/monthly_orders_by_branch.png",
    dpi=200,
    bbox_inches="tight"
)

plt.close()

print("✓ monthly_orders_by_branch.png created")

# ============================================================
# 8. DAILY ORDER DATA
# ============================================================

daily_orders = (
    df.groupby("date")
    .size()
    .reset_index(name="orders")
)

daily_orders["date"] = pd.to_datetime(daily_orders["date"])

daily_orders = daily_orders.sort_values("date")

# ============================================================
# 9. SIMPLE 7-DAY DEMAND FORECAST
# ============================================================

print("\nCreating demand forecast...")

# If enough historical days exist, use 7-day rolling average.
# With only 2 days of data, use available historical average.

historical_average = daily_orders["orders"].mean()

if len(daily_orders) >= 7:

    recent_average = (
        daily_orders["orders"]
        .tail(7)
        .mean()
    )

else:

    recent_average = historical_average


last_date = daily_orders["date"].max()

future_dates = pd.date_range(
    start=last_date + pd.Timedelta(days=1),
    periods=7,
    freq="D"
)

forecast = pd.DataFrame({
    "date": future_dates,
    "forecast_orders": [
        round(recent_average)
    ] * 7
})

# ============================================================
# 10. SAVE FORECAST CSV
# ============================================================

forecast.to_csv(
    "forecast_results.csv",
    index=False
)

print("✓ forecast_results.csv created")

# ============================================================
# 11. FORECAST CHART
# ============================================================

plt.figure(figsize=(11, 6))

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

plt.title("Cafeteria Order Demand Forecast")
plt.xlabel("Date")
plt.ylabel("Number of Orders")

plt.legend()

plt.xticks(rotation=30)

plt.tight_layout()

plt.savefig(
    "outputs/cafeteria_forecast_trend.png",
    dpi=200,
    bbox_inches="tight"
)

plt.close()

print("✓ cafeteria_forecast_trend.png created")

# ============================================================
# 12. FINAL SUMMARY
# ============================================================

print("\n========================================")
print("       CHART GENERATION COMPLETE")
print("========================================")

print(f"Orders analyzed : {len(df):,}")
print(f"Total revenue   : ₹{df['grand_total'].sum():,.2f}")
print(f"Average order   : ₹{df['grand_total'].mean():,.2f}")

print("\nGenerated files:")

print("outputs/revenue_by_branch.png")
print("outputs/orders_by_hour.png")
print("outputs/orders_by_weekday.png")
print("outputs/monthly_orders_by_branch.png")
print("outputs/cafeteria_forecast_trend.png")
print("forecast_results.csv")

print("\nDone! ✓")