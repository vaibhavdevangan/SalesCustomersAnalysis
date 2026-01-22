# SalesCustomersAnalysis

# Superstore Analytics Project

## Project Overview
The **Superstore Analytics Project** is designed to perform a detailed analysis of retail sales data to gain insights into product performance, customer behavior, and regional trends. The project uses **PostgreSQL** as the database and **Python** for data analysis and visualization.

The goal is to build a structured database, ingest sales data, perform exploratory data analysis (EDA), and create meaningful visualizations and dashboards to assist business decisions.

---

## Dataset
The dataset used is a **Superstore sales dataset** containing information about orders, products, customers, regions, and sales transactions. Key columns include:

- `Order ID`, `Order Date`, `Order Priority`
- `Customer ID`, `Customer Name`
- `Product ID`, `Product Name`
- `City`, `State`, `Country`, `Region`
- `Sales`, `Quantity`, `Discount`, `Profit`

---

## Database Design

The dataset has been split into 4 normalized tables:

1. **Customers**
   - `Customer ID` (PK), `Customer Name`, `City`, `State`, `Country`, `Region`

2. **Products**
   - `Product ID` (PK), `Product Name`, `Category`, `Sub-Category`

3. **Orders**
   - `Order ID` + `Product ID` (Composite PK)
   - Foreign Keys: `Customer ID` → Customers, `Product ID` → Products
   - Columns: `Order Date`, `Order Priority`, `Sales`, `Quantity`, `Discount`, `Profit`

4. **Regions**
   - `Region` (PK), mapping of region to states and countries

---

## Environment Setup

- **Database:** PostgreSQL 17.x
- **Python Packages:**
  - `pandas` – for data manipulation
  - `sqlalchemy` – for database connection and ORM
  - `psycopg2` – PostgreSQL driver
  - `matplotlib` / `seaborn` – for visualization

---

## What Has Been Completed

1. Dataset exploration and understanding
2. Database schema design and table relationships
3. PostgreSQL installation and database creation
4. PostgreSQL configuration (`postgresql.conf` and `pg_hba.conf`) for local connections
5. Verified database connection through **psql CLI**
6. Setup Python environment with required packages
7. Attempted SQLAlchemy connection (pending TCP/IP connectivity fix)

---

## Pending Tasks

1. Fix **Python → PostgreSQL connection issue** (`Connection refused` on `127.0.0.1:5432`)
2. Load CSV dataset into PostgreSQL tables using Python
3. Clean and preprocess data (missing values, duplicates, foreign key consistency)
4. Perform **Exploratory Data Analysis (EDA)**
5. Execute SQL queries for business insights:
   - Top-selling products
   - Best customers and regions
   - Profit and sales trends
6. Build interactive dashboards (optional):
   - Using `Streamlit`, `Dash`, or visualization tools like Tableau

---

## Notes / Observations

- PostgreSQL must allow TCP/IP connections (`listen_addresses = '*'`) and authentication must be set in `pg_hba.conf`.
- Changes to configuration require a **restart of PostgreSQL service**.
- Connection issues are currently under investigation for Python/SQLAlchemy.

---

## References

- [SQLAlchemy Documentation](https://www.sqlalchemy.org/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [Python pandas Documentation](https://pandas.pydata.org/)
- Superstore Dataset source: public Kaggle datasets or provided CSV
