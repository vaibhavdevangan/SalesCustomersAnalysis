### 🧾 Superstore Sales Analytics & Data Warehouse Project
##### 🔍 Project Summary

This project implements an end-to-end sales analytics system using a data warehouse approach on a retail Superstore dataset.
The focus is on data modeling, ETL engineering, analytical querying, and business-driven insights, closely resembling how analytics systems are built in real organizations.

The workflow starts from raw transactional data, transforms it into a star schema, loads it into PostgreSQL, and performs SQL + Python-based analysis and visualization to extract actionable insights.

##### 🎯 Project Goals

Design a scalable star schema for sales analytics

Perform clean, repeatable ETL pipelines using Python

Store analytics-ready data in PostgreSQL

Enable fast SQL analysis and business reporting

Generate meaningful insights through visualizations

Build a strong data engineering + analytics portfolio project

##### 📦 Dataset Description

The dataset represents retail transactions containing:

Order lifecycle details (order date, ship date)

Customer segmentation

Product hierarchy

Geographic information

Sales and profitability metrics

Core Metrics

Sales

Profit

Quantity

Discount

Business Dimensions

Customer

Product

Region

Date

##### 🏗️ Data Warehouse Design

The system follows a Star Schema, optimized for analytical workloads.

Fact Table

fact_sales

Stores transactional measures:

sales

profit

quantity

discount

References all dimension tables via foreign keys

Dimension Tables

dim_customer → customer identity & segmentation

dim_product → product, category, sub-category

dim_region → country, region, state, city

dim_date → calendar attributes for time analysis

This structure supports fast aggregations, time-series analysis, and BI integration.

🔄 ETL & Data Processing Workflow
1️⃣ Raw Data Exploration

Loaded CSV data into Pandas

Identified fact vs dimension attributes

Validated data quality and null patterns

2️⃣ Database & Environment Setup

PostgreSQL database creation

Python–PostgreSQL integration using SQLAlchemy

Version-controlled development using Git

3️⃣ Schema Creation

Designed tables with:

Proper data types

Primary keys

Foreign key constraints

Ensured referential integrity

4️⃣ Dimension Loading

Deduplicated records

Ensured idempotent inserts

Loaded clean, consistent dimension data

5️⃣ Date Dimension Engineering

Generated derived attributes:

year, month, day, quarter

day name

Handled missing dates safely

Ensured full coverage for fact records

6️⃣ Fact Table Loading

Mapped natural keys to dimension keys

Validated zero orphan records

Verified row counts and constraints

##### 📊 Analytical & Visualization Layer

Analysis was performed using SQL and Python.

Key Insights Extracted

Top revenue-generating customers

Most profitable products and categories

Impact of discounts on profit

Monthly and quarterly sales trends

Regional sales vs profit comparison

Identification of loss-making patterns

Visualization Tools

Matplotlib

Seaborn

Pandas

Charts were designed with a business-first mindset, focusing on:

Clarity

Interpretability

Decision relevance

##### 💡 Business Findings (Highlights)

High discounts strongly correlate with negative profit

Revenue is concentrated among a small customer segment

Some high-sales products are consistently unprofitable

Seasonal trends significantly impact sales volume

Regional performance varies strongly in profitability, not just sales

##### 🧠 Skills Demonstrated

Data Warehousing & Dimensional Modeling

SQL (joins, aggregations, analytical queries)

Python ETL pipelines

PostgreSQL optimization mindset

Data visualization for business insights

Git-based project structuring

##### 🛠️ Tech Stack

Database: PostgreSQL

Language: Python

Libraries: Pandas, SQLAlchemy, Matplotlib, Seaborn

Environment: Jupyter Notebook, VS Code

Version Control: Git & GitHub