-- Top 10 Customers by Sales

SELECT f.customer_id, SUM(f.sales) AS total_sales
FROM fact_sales f
GROUP BY f.customer_id
ORDER BY total_sales DESC
LIMIT 10;


--Top 10 Products by Profit
SELECT p.product_name, SUM(f.profit) AS total_profit
FROM fact_sales f
JOIN dim_product p ON f.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_profit DESC
LIMIT 10;


--Sales Trend by Month
SELECT d.year, d.month, SUM(f.sales) AS monthly_sales
FROM fact_sales f
JOIN dim_date d ON f.order_date = d.date
GROUP BY d.year, d.month
ORDER BY d.year, d.month;


--Region-wise Profit
SELECT r.region, SUM(f.profit) AS total_profit
FROM fact_sales f
JOIN dim_region r ON f.region_id = r.region_id
GROUP BY r.region
ORDER BY total_profit DESC;

--10 products with the highest total sales.
SELECT p.product_name, SUM(f.sales) AS total_sales
FROM fact_sales f
JOIN dim_product p ON f.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_sales DESC
LIMIT 10;

--10 customers contributing the most profit.
SELECT c.customer_id, c.segment, SUM(f.profit) AS total_profit
FROM fact_sales f
JOIN dim_customer c ON f.customer_id = c.customer_id
GROUP BY c.customer_id, c.segment
ORDER BY total_profit DESC
LIMIT 10;

--which products are generating the highest revenue:
SELECT p.product_id, p.product_name, p.category, p.sub_category, SUM(f.sales) AS total_sales
FROM fact_sales f
JOIN dim_product p ON f.product_id = p.product_id
GROUP BY p.product_id, p.product_name, p.category, p.sub_category
ORDER BY total_sales DESC
LIMIT 10;


--which products are most profitable:
SELECT p.product_id, p.product_name, p.category, p.sub_category, SUM(f.profit) AS total_profit
FROM fact_sales f
JOIN dim_product p ON f.product_id = p.product_id
GROUP BY p.product_id, p.product_name, p.category, p.sub_category
ORDER BY total_profit DESC
LIMIT 10;

--Monthly sales trend:
SELECT d.year, d.month, SUM(f.sales) AS total_sales, SUM(f.profit) AS total_profit
FROM fact_sales f
JOIN dim_date d ON f.order_date = d.date
GROUP BY d.year, d.month
ORDER BY d.year, d.month;



--Quarterly performance:
SELECT d.year, d.quarter, SUM(f.sales) AS total_sales, SUM(f.profit) AS total_profit
FROM fact_sales f
JOIN dim_date d ON f.order_date = d.date
GROUP BY d.year, d.quarter
ORDER BY d.year, d.quarter;


-- >> Total Sales and Profit by Customer Segment
-- Problem: Identify which customer segments (Consumer, Corporate, Home Office) are contributing most to sales and profit
SELECT c.segment, SUM(f.sales) AS total_sales, SUM(f.profit) AS total_profit
FROM fact_sales f
JOIN dim_customer c ON f.customer_id = c.customer_id
GROUP BY c.segment
ORDER BY total_sales DESC;


--  Sales and Profit by Region and State
-- Problem: Determine sales and profit contribution at regional and state level
SELECT r.region, r.state, SUM(f.sales) AS total_sales, SUM(f.profit) AS total_profit
FROM fact_sales f
JOIN dim_region r ON f.region_id = r.region_id
GROUP BY r.region, r.state
ORDER BY total_sales DESC;


--  City-Level Sales and Profit
-- Problem: Find top cities driving sales and profit
SELECT r.city, SUM(f.sales) AS total_sales, SUM(f.profit) AS total_profit
FROM fact_sales f
JOIN dim_region r ON f.region_id = r.region_id
GROUP BY r.city
ORDER BY total_sales DESC
LIMIT 20;


--  Average Discount vs. Profit by Product Category
-- Problem: Check if high discounts lead to higher or lower profitability by category
SELECT p.category, AVG(f.discount) AS avg_discount, SUM(f.profit) AS total_profit
FROM fact_sales f
JOIN dim_product p ON f.product_id = p.product_id
GROUP BY p.category
ORDER BY total_profit DESC;


--  Top Products with Highest Discount Given
-- Problem: Identify products where maximum discount was offered
SELECT p.product_name, MAX(f.discount) AS max_discount, SUM(f.sales) AS total_sales
FROM fact_sales f
JOIN dim_product p ON f.product_id = p.product_id
GROUP BY p.product_name
ORDER BY max_discount DESC
LIMIT 10;


--  Time-Based Discount Analysis
-- Problem: Analyze if higher discounts were given in specific months and its impact on profit
SELECT d.year, d.month, AVG(f.discount) AS avg_discount, SUM(f.profit) AS total_profit
FROM fact_sales f
JOIN dim_date d ON f.order_date = d.date
GROUP BY d.year, d.month
ORDER BY d.year, d.month;


--  Sales Distribution by Day of Week
-- Problem: Find which days of the week have highest sales
SELECT d.day_name, SUM(f.sales) AS total_sales, SUM(f.profit) AS total_profit
FROM fact_sales f
JOIN dim_date d ON f.order_date = d.date
GROUP BY d.day_name
ORDER BY total_sales DESC;


--  Repeat Customers Analysis
-- Problem: Identify number of repeat orders per customer
SELECT f.customer_id, COUNT(DISTINCT f.order_id) AS total_orders, SUM(f.sales) AS total_sales
FROM fact_sales f
GROUP BY f.customer_id
ORDER BY total_orders DESC
LIMIT 20;


--  Sales vs. Profit Correlation by Category
-- Problem: Compare total sales and profit per category to identify low-profit high-sales products
SELECT p.category, SUM(f.sales) AS total_sales, SUM(f.profit) AS total_profit
FROM fact_sales f
JOIN dim_product p ON f.product_id = p.product_id
GROUP BY p.category
ORDER BY total_sales DESC;


--  Sales Contribution by Top 20 Customers
-- Problem: Find which 20 customers contribute highest revenue
SELECT f.customer_id, SUM(f.sales) AS total_sales, SUM(f.profit) AS total_profit
FROM fact_sales f
GROUP BY f.customer_id
ORDER BY total_sales DESC
LIMIT 20;



\d dim_customer;

