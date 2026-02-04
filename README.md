## 📊 Superstore Sales Analytics & Data Warehouse Project
### 📌 Project Overview

The Superstore Sales Analytics Project focuses on designing and implementing a Sales Data Warehouse using the Superstore retail dataset.

The objective is to:

Transform raw transactional CSV data into a structured star schema

Perform clean ETL (Extract, Transform, Load) using Python

Store analytics-ready data in PostgreSQL

Enable efficient SQL analysis, reporting, and BI integration

This project simulates a real-world data engineering workflow, from raw data to analytics-ready storage.

🗂 Dataset

The dataset used is a Superstore sales dataset containing information related to:

Orders and shipping details

Customers and segments

Products and categories

Geographic regions

Sales performance metrics

Key Columns Include:

Order ID, Order Date, Ship Date, Order Priority

Customer ID, Customer Name, Segment

Product ID, Product Name, Category, Sub-Category

Country, Region, State, City

Sales, Profit, Quantity, Discount

🛠 Tech Stack

Python (Pandas, SQLAlchemy)

PostgreSQL

Jupyter Notebook

VS Code

GitHub

Optional (future):

Power BI / Tableau

Streamlit / Dash

Apache Airflow

🗂 Database Design (Star Schema)

The data warehouse follows a Star Schema consisting of:

Dimension Tables

dim_customer – customer details

dim_product – product information

dim_region – geographical hierarchy

dim_date – time-based attributes

Fact Table

fact_sales – transactional sales metrics

This design supports fast aggregations and analytical queries.

🚀 Project Workflow (Step-by-Step)
✅ STEP 1: Raw Data Understanding

Loaded the Superstore CSV file into a Pandas DataFrame

Analyzed columns related to:

Customers

Products

Geography

Dates

Sales metrics

Objective: Identify dimension vs fact attributes.

✅ STEP 2: Environment & Database Setup

Installed and configured PostgreSQL

Created database: Superstore_db

Verified database access via:

psql CLI

SQLAlchemy engine from Python

Set up Python environment with required libraries

✅ STEP 3: Schema Design & Table Creation

Designed star schema tables with:

Proper data types

Primary keys

Foreign key constraints

Created tables in PostgreSQL:

dim_customer

dim_product

dim_region

dim_date

fact_sales

✅ STEP 4: Customer Dimension (dim_customer)

Purpose: Store unique customer records.

Actions:

Extracted customer-related columns

Removed duplicates using customer_id

Loaded 793 unique customers

Ensured idempotent inserts (safe re-runs)

✅ STEP 5: Product Dimension (dim_product)

Purpose: Store unique product details.

Actions:

Extracted:

product_id

product_name

category

sub_category

Removed duplicates

Loaded 1862 unique products

✅ STEP 6: Region Dimension (dim_region)

Purpose: Store geographical hierarchy.

Actions:

Extracted:

country

region

state

city

Cleaned and deduplicated data

Loaded region records while maintaining consistency

✅ STEP 7: Date Dimension (dim_date)

Purpose: Enable time-based analysis.

Columns:

date

day

month

year

quarter

day_name

Actions:

Converted raw date strings into proper date format

Handled missing and invalid date values

Generated derived date attributes

Enforced uniqueness on date column

Successfully loaded all valid dates

✅ STEP 8: Fact Table Preparation (fact_sales)

Purpose: Store transactional metrics.

Contains:

Foreign keys:

customer_id

product_id

region_id

date_id

Measures:

sales

profit

quantity

discount

Actions:

Joined fact data with dimension tables to fetch surrogate keys

Validated no NULL foreign keys

Ensured referential integrity

✅ STEP 9: Fact Table Loading

Inserted cleaned data into fact_sales

Verified row counts

Confirmed all foreign key relationships

🔍 Final Verification

Checked row counts across all tables

Verified primary and foreign key constraints

Ensured schema consistency and analytical readiness

📈 What This Project Enables

Fast analytical SQL queries

Sales and profit trend analysis

Customer and product performance insights

BI dashboard integration

Hands-on experience with data warehousing concepts

📌 Future Enhancements

Add indexes for performance optimization

Create analytical SQL views

Perform Exploratory Data Analysis (EDA)

Build dashboards using Power BI / Tableau

Automate ETL pipelines using Apache Airflow

📚 References

PostgreSQL Documentation

SQLAlchemy Documentation

Pandas Documentation

Superstore Dataset (public datasets)