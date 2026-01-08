-- =========================================================
-- Query 1: Monthly Sales Drill-Down Analysis
-- Business Scenario:
-- "The CEO wants to see sales performance broken down by time
-- periods. Start with yearly total, then quarterly, then monthly
-- sales for 2024."
-- Demonstrates: Drill-down from Year → Quarter → Month
-- =========================================================

SELECT
    d.year,
    d.quarter,
    d.month_name,
    SUM(f.total_amount) AS total_sales,
    SUM(f.quantity_sold) AS total_quantity
FROM fact_sales f
JOIN dim_date d
    ON f.date_key = d.date_key
WHERE d.year = 2024
GROUP BY
    d.year,
    d.quarter,
    d.month,
    d.month_name
ORDER BY
    d.year,
    d.quarter,
    d.month;


-- ================================…