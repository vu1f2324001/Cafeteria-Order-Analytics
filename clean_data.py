import pandas as pd
import mysql.connector

# -----------------------------
# 1. Connect to MySQL
# -----------------------------
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password=input("Enter MySQL password: "),
    database="cafeteria_db"
)

# -----------------------------
# 2. Load required order data
# -----------------------------
query = """
SELECT
    id,
    order_number,
    user_id,
    order_status,
    order_date,
    branch_id,
    sub_total,
    tax_amount,
    discount_amount,
    mode_of_transaction,
    grand_total,
    reward_amount,
    is_refunded,
    order_cancel_reason
FROM orders
"""

df = pd.read_sql(query, conn)

conn.close()

print("\nOriginal rows:", len(df))

# -----------------------------
# 3. Normalize payment method
# -----------------------------
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

# -----------------------------
# 4. Flag zero-value orders
# -----------------------------
df["zero_value_order"] = df["grand_total"].fillna(0).eq(0)

# -----------------------------
# 5. Flag repeated order numbers
# -----------------------------
df["duplicate_order_number"] = (
    df["order_number"]
    .duplicated(keep=False)
)

# -----------------------------
# 6. Flag negative orders
# -----------------------------
df["negative_value_order"] = (
    df["grand_total"].fillna(0) < 0
)

# -----------------------------
# 7. Convert date
# -----------------------------
df["order_date"] = pd.to_datetime(df["order_date"])

# -----------------------------
# 8. Save cleaned dataset
# -----------------------------
df.to_csv("cleaned_orders.csv", index=False)

# -----------------------------
# 9. Data Quality Summary
# -----------------------------
summary = {
    "Original Orders": len(df),
    "Zero Value Orders": int(df["zero_value_order"].sum()),
    "Negative Value Orders": int(df["negative_value_order"].sum()),
    "Repeated Order Numbers": int(df["duplicate_order_number"].sum()),
    "Unique Branches": df["branch_id"].nunique(),
    "Unique Customers": df["user_id"].nunique(),
    "Total Revenue": df["grand_total"].sum(),
    "Average Order Value": df["grand_total"].mean()
}

summary_df = pd.DataFrame(
    summary.items(),
    columns=["Metric", "Value"]
)

summary_df.to_csv("data_quality_summary.csv", index=False)

# -----------------------------
# 10. Print results
# -----------------------------
print("\n===== DATA CLEANING COMPLETE =====")
print("Original Orders          :", len(df))
print("Zero Value Orders        :", df["zero_value_order"].sum())
print("Negative Value Orders    :", df["negative_value_order"].sum())
print("Repeated Order Numbers   :", df["duplicate_order_number"].sum())
print("Unique Branches          :", df["branch_id"].nunique())
print("Unique Customers         :", df["user_id"].nunique())

print("\nFiles created:")
print("1. cleaned_orders.csv")
print("2. data_quality_summary.csv")