# %%
import matplotlib.pyplot as plt
import seaborn as sns

# Optional: nicer default style
sns.set_style("whitegrid")
%matplotlib inline
import pandas as pd


# %% [markdown]
# ### Connect to PostgreSQL

# %%

import pandas as pd
from sqlalchemy import create_engine

# PostgreSQL connection
engine = create_engine("postgresql+psycopg2://postgres:new_password@localhost:5432/Superstore_db")


# %% [markdown]
# ### Load Tables from PostgreSQL

# %%
# Fact table
fact_sales = pd.read_sql("SELECT * FROM fact_sales;", engine)

# Dimension tables
dim_customer = pd.read_sql("SELECT * FROM dim_customer;", engine)
dim_product = pd.read_sql("SELECT * FROM dim_product;", engine)
dim_region = pd.read_sql("SELECT * FROM dim_region;", engine)
dim_date = pd.read_sql("SELECT * FROM dim_date;", engine)
# Merge fact table with dimension tables
# Merge dimensions to create full dataset for analytics & visualization
df = fact_sales \
    .merge(dim_customer, on="customer_id", how="left") \
    .merge(dim_product, on="product_id", how="left") \
    .merge(dim_region, on="region_id", how="left") \
    .merge(dim_date, left_on="order_date", right_on="date", how="left")


# %%
# Check for nulls
print(df.isna().sum())

# Quick overview
print(df.head())
print(df.info())


# %%
top_customers = df.groupby('customer_id')['sales'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(12,6))
sns.barplot(x=top_customers.values, y=top_customers.index, palette="viridis")
plt.title("Top 10 Customers by Sales")
plt.xlabel("Sales")
plt.ylabel("Customer ID")
plt.show()


# %%
#the aboove graph shows the top 10 customers based on their total sales, 
# with customer IDs on the y-axis and sales amounts on the x-axis.

# %% [markdown]
# ### Product Performance
# 
# #### Which products generate the highest revenue?

# %%
top_products = (
    df.groupby("product_name")["sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

plt.figure(figsize=(8,5))
top_products.plot(kind="bar", color="red")
plt.title("Top 10 Products by Sales")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.xticks(rotation=45, ha="right")
plt.show()


# %%
# the above graph shows the top 10 products based on their total sales,
#  with product names on the x-axis and sales amounts on the y-axis.
# thus highlighting the best-selling products in the dataset whiich is canon printer.


# %% [markdown]
# ### Category-Level Analysis
# 
# ### Which categories drive the most sales?

# %%
category_sales = df.groupby("category")["sales"].sum()

plt.figure(figsize=(6,4))
category_sales.plot(kind="bar", color="green")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.show()


# %%
# the above grpah total sales for each product category,
#  with categories on the x-axis and sales amounts on the y-axis.
# thus showing that Furniture has the highest sales among the categories.
# and Technology has the lowest sales.

# %% [markdown]
# ### Regional Performance
# 
# #### Which regions are most profitable?

# %%
region_profit = df.groupby("region")["profit"].sum()

plt.figure(figsize=(6,4))
region_profit.plot(kind="bar", color="purple")
plt.title("Profit by Region")
plt.xlabel("Region")
plt.ylabel("Total Profit")
plt.show()


# %%
#from the above graph we can see that the region with the highest profit is the West region,
# while the region with the lowest profit is the South region.



# %% [markdown]
# ### Time-Series Trend (MOST IMPORTANT)
# 
# #### How do sales change over time?

# %%
monthly_sales = (
    df.groupby(["year", "month"])["sales"]
      .sum()
      .reset_index()
)

monthly_sales["year_month"] = (
    monthly_sales["year"].astype(str) + "-" +
    monthly_sales["month"].astype(str)
)

plt.figure(figsize=(12,5))
plt.plot(monthly_sales["year_month"], monthly_sales["sales"])
plt.title("Monthly Sales Trend")
plt.xlabel("Time")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.show()


# %%
# from the above graph we can observe the sales trend over the months,
# the sales is generally increasing over time with some seasonal fluctuations.

# %% [markdown]
# ### Top 10 Customers by Sales (Visualization)
# ### Business Question
# 
# ##### Which customers contribute the most to total sales?

# %%

top_customers = (
    df.groupby("customer_id")["sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

plt.figure(figsize=(10,5))
top_customers.plot(kind="bar", color="orange")
plt.title("Top 10 Customers by Sales")
plt.xlabel("Customer ID")
plt.ylabel("Total Sales")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()


# %% [markdown]
# 

# %%


# %%
# the above 

# %%
import pandas as pd 
query = """
SELECT discount, profit
FROM fact_sales
"""

df_discount_profit = pd.read_sql(query, engine)


# %%
df_discount_profit = df_discount_profit.dropna()
plt.figure(figsize=(10,6))
sns.scatterplot(data=df_discount_profit, x="discount", y="profit", alpha=0.6)
plt.title("Discount vs. Profit")

# %%
plt.figure(figsize=(8, 6))

plt.scatter(
    df_discount_profit["discount"],
    df_discount_profit["profit"],
    alpha=0.5
)

plt.xlabel("Discount")
plt.ylabel("Profit")
plt.title("Discount vs Profit")

plt.axhline(0)  # Profit = 0 reference line
plt.grid(True)

plt.show()


# %%
# the above graph shows that as discount increases, profit tends to decrease,
#  with many points showing negative profit at higher discount levels.

# %%
df_discount_profit["discount_level"] = pd.cut(
    df_discount_profit["discount"],
    bins=[-0.01, 0, 0.1, 0.2, 0.3, 0.5, 1.0],
    labels=["0%", "0–10%", "10–20%", "20–30%", "30–50%", "50%+"]
)
avg_profit_discount = (
    df_discount_profit
    .groupby("discount_level")["profit"]
    .mean()
)
plt.figure(figsize=(9,5))
avg_profit_discount.plot(kind="line", marker="o", color="red")
plt.axhline(0)
plt.xlabel("Discount Level")
plt.ylabel("Average Profit")
plt.title("Average Profit by Discount Level")
plt.tight_layout()
plt.show()


# %%
#from the above graph we can say that higher discount levels (especially above 30%) are associated with negative average profit,
# while lower discount levels (0–10%) tend to have positive average profit.
#

# %%
query = """
SELECT p.category, SUM(f.sales) AS total_sales, SUM(f.profit) AS total_profit
FROM fact_sales f
JOIN dim_product p ON f.product_id = p.product_id
GROUP BY p.category
"""

df_category = pd.read_sql(query, engine)
df_category


# %%
plt.figure(figsize=(7,5))

plt.bar(
    df_category["category"],
    df_category["total_profit"]
)

plt.axhline(0)
plt.xlabel("Category")
plt.ylabel("Total Profit")
plt.title("Total Profit by Product Category")
plt.grid(axis="y")
plt.show()


# %%
df_category.set_index("category")[["total_sales", "total_profit"]].plot(
    kind="bar",
    figsize=(8,5)
)
plt.title("Sales vs Profit by Category")
plt.ylabel("Amount")
plt.grid(axis="y")
plt.show()


# %%
# this graph compares total sales and total profit for each product category,

# we can conclude that while Technology has the highest sales, it does not have the highest profit compared to Furniture,
#     Furniture has the highest profit despite having lower sales than Technology, 
# and Office Supplies has the lowest profit among the categories.


# %% [markdown]
# ### Sales vs Profit by Region

# %%
fact_sales.columns

# %%

region_summary = fact_sales.groupby("region_id").agg(
    total_sales=("sales", "sum"),
    total_profit=("profit", "sum"),
    total_quantity=("quantity", "sum")
).reset_index()

plt.figure(figsize=(8,6))
plt.scatter(
    region_summary["total_sales"],
    region_summary["total_profit"],
    s=region_summary["total_quantity"]
)

for i, region in enumerate(region_summary["region_id"]):
    plt.text(
        region_summary["total_sales"][i],
        region_summary["total_profit"][i],
        region
    )

plt.xlabel("Total Sales")
plt.ylabel("Total Profit")
plt.title("Sales vs Profit by Region")
plt.axhline(0)
plt.show()



