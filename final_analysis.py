import pandas as pd
import matplotlib.pyplot as plt
import os

# ============================================================
# 1. LOAD CLEANED DATA
# ============================================================

df = pd.read_csv("cleaned_orders.csv")

df["order_date"] = pd.to_datetime(df["order_date"])

# Create output folder
os.makedirs("outputs", exist_ok=True)

# Extract useful date/time fields
df["date"] = df["order_date"].dt.date
df["hour"] = df["order_date"].dt.hour
df["weekday"] = df["order_date"].dt.day_name()

# ============================================================
# 2. BASIC KPI SUMMARY
# ============================================================

total_orders = len(df)
total_revenue = df["grand_total"].sum()
aov = df["grand_total"].mean()
branches = df["branch_id"].nunique()
customers = df["user_id"].nunique()
zero_orders = df["zero_value_order"].sum()

kpi = pd.DataFrame({
    "Metric": [
        "Total Orders",
        "Total Revenue",
        "Average Order Value",
        "Branches",
        "Unique Customers",
        "Zero Value Orders"
    ],
    "Value": [
        total_orders,
        total_revenue,
        aov,
        branches,
        customers,
        zero_orders
    ]
})

kpi.to_csv("outputs/kpi_summary.csv", index=False)

# ============================================================
# 3. BRANCH ANALYSIS
# ============================================================

branch = (
    df.groupby("branch_id")
    .agg(
        orders=("id", "count"),
        revenue=("grand_total", "sum")
    )
    .reset_index()
)

branch["aov"] = branch["revenue"] / branch["orders"]
branch["revenue_share"] = (
    branch["revenue"] / total_revenue * 100
)

branch.to_csv("outputs/branch_analysis.csv", index=False)

# Revenue by Branch
plt.figure(figsize=(8, 5))
plt.bar(
    branch["branch_id"].astype(str),
    branch["revenue"]
)
plt.title("Revenue by Branch")
plt.xlabel("Branch")
plt.ylabel("Revenue (₹)")
plt.tight_layout()
plt.savefig("outputs/revenue_by_branch.png", dpi=200)
plt.close()

# Orders by Branch
plt.figure(figsize=(8, 5))
plt.bar(
    branch["branch_id"].astype(str),
    branch["orders"]
)
plt.title("Orders by Branch")
plt.xlabel("Branch")
plt.ylabel("Number of Orders")
plt.tight_layout()
plt.savefig("outputs/orders_by_branch.png", dpi=200)
plt.close()

# ============================================================
# 4. HOURLY DEMAND ANALYSIS
# ============================================================

hourly = (
    df.groupby("hour")
    .agg(
        orders=("id", "count"),
        revenue=("grand_total", "sum")
    )
    .reset_index()
)

hourly.to_csv("outputs/hourly_analysis.csv", index=False)

# Orders by Hour
plt.figure(figsize=(10, 5))
plt.plot(
    hourly["hour"],
    hourly["orders"],
    marker="o"
)
plt.title("Orders by Hour")
plt.xlabel("Hour of Day")
plt.ylabel("Number of Orders")
plt.xticks(range(24))
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("outputs/orders_by_hour.png", dpi=200)
plt.close()

# Revenue by Hour
plt.figure(figsize=(10, 5))
plt.plot(
    hourly["hour"],
    hourly["revenue"],
    marker="o"
)
plt.title("Revenue by Hour")
plt.xlabel("Hour of Day")
plt.ylabel("Revenue (₹)")
plt.xticks(range(24))
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("outputs/revenue_by_hour.png", dpi=200)
plt.close()

# ============================================================
# 5. DAILY ANALYSIS
# ============================================================

daily = (
    df.groupby("date")
    .agg(
        orders=("id", "count"),
        revenue=("grand_total", "sum")
    )
    .reset_index()
)

daily["aov"] = daily["revenue"] / daily["orders"]

daily.to_csv("outputs/daily_analysis.csv", index=False)

# Daily Orders
plt.figure(figsize=(8, 5))
plt.bar(
    daily["date"].astype(str),
    daily["orders"]
)
plt.title("Daily Orders")
plt.xlabel("Date")
plt.ylabel("Orders")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("outputs/daily_orders.png", dpi=200)
plt.close()

# Daily Revenue
plt.figure(figsize=(8, 5))
plt.bar(
    daily["date"].astype(str),
    daily["revenue"]
)
plt.title("Daily Revenue")
plt.xlabel("Date")
plt.ylabel("Revenue (₹)")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("outputs/daily_revenue.png", dpi=200)
plt.close()

# ============================================================
# 6. PAYMENT METHOD ANALYSIS
# ============================================================

payment = (
    df.groupby("payment_method")
    .agg(
        orders=("id", "count"),
        revenue=("grand_total", "sum")
    )
    .reset_index()
)

payment["aov"] = payment["revenue"] / payment["orders"]
payment["revenue_share"] = (
    payment["revenue"] / total_revenue * 100
)

payment.to_csv("outputs/payment_analysis.csv", index=False)

# Payment Revenue
plt.figure(figsize=(9, 5))
plt.bar(
    payment["payment_method"],
    payment["revenue"]
)
plt.title("Revenue by Payment Method")
plt.xlabel("Payment Method")
plt.ylabel("Revenue (₹)")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("outputs/payment_revenue.png", dpi=200)
plt.close()

# ============================================================
# 7. ORDER VALUE DISTRIBUTION
# ============================================================

plt.figure(figsize=(9, 5))
plt.hist(
    df["grand_total"],
    bins=30
)
plt.title("Order Value Distribution")
plt.xlabel("Order Value (₹)")
plt.ylabel("Number of Orders")
plt.tight_layout()
plt.savefig("outputs/order_value_distribution.png", dpi=200)
plt.close()

# ============================================================
# 8. ZERO-VALUE ORDER ANALYSIS
# ============================================================

zero = df[df["zero_value_order"] == True]

zero_summary = pd.DataFrame({
    "Metric": [
        "Zero Value Orders",
        "Percentage of Orders",
        "Positive Subtotal Orders",
        "Orders With Reward",
        "Refunded Orders",
        "Cancelled Orders"
    ],
    "Value": [
        len(zero),
        len(zero) / total_orders * 100,
        (zero["sub_total"] > 0).sum(),
        (zero["reward_amount"] > 0).sum(),
        (zero["is_refunded"] == 1).sum(),
        zero["order_cancel_reason"].notna().sum()
    ]
})

zero_summary.to_csv(
    "outputs/zero_value_analysis.csv",
    index=False
)

# ============================================================
# 9. TOP ORDER HOURS
# ============================================================

top_hours = hourly.sort_values(
    "orders",
    ascending=False
).head(5)

top_hours.to_csv(
    "outputs/top_order_hours.csv",
    index=False
)

# ============================================================
# 10. BASELINE DEMAND FORECAST
# ============================================================

# Because only two dates are available,
# use a simple average as a baseline forecast.

average_daily_orders = daily["orders"].mean()

future_dates = pd.date_range(
    start=daily["date"].max() + pd.Timedelta(days=1),
    periods=7,
    freq="D"
)

forecast = pd.DataFrame({
    "date": future_dates,
    "forecast_orders": round(average_daily_orders)
})

forecast.to_csv(
    "outputs/forecast_results.csv",
    index=False
)

plt.figure(figsize=(10, 5))

plt.plot(
    daily["date"].astype(str),
    daily["orders"],
    marker="o",
    label="Actual Orders"
)

plt.plot(
    forecast["date"].astype(str),
    forecast["forecast_orders"],
    marker="o",
    linestyle="--",
    label="Baseline Forecast"
)

plt.title("7-Day Baseline Demand Forecast")
plt.xlabel("Date")
plt.ylabel("Orders")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

plt.savefig(
    "outputs/demand_forecast.png",
    dpi=200
)

plt.close()

# ============================================================
# 11. PRINT FINAL RESULTS
# ============================================================

print("\n========================================")
print("      FINAL ANALYSIS COMPLETE")
print("========================================")

print(f"\nTotal Orders       : {total_orders:,}")
print(f"Total Revenue     : ₹{total_revenue:,.2f}")
print(f"Average Order     : ₹{aov:,.2f}")
print(f"Branches          : {branches}")
print(f"Customers         : {customers:,}")
print(f"Zero Value Orders : {zero_orders:,}")

print("\nTop Order Hours:")

for _, row in top_hours.iterrows():
    print(
        f"{int(row['hour']):02d}:00 "
        f"→ {int(row['orders']):,} orders"
    )

print("\nBaseline Daily Forecast:")
print(f"{round(average_daily_orders):,} orders/day")

print("\nCharts and CSV files saved inside:")
print("outputs/")