# E-Commerce Sales Analytics

SQL-based analysis of a small e-commerce database, covering revenue tracking, customer segmentation, and product performance using Python, SQLAlchemy, and MySQL.

> **Note:** This project uses a practice database with synthetic customer and order data created for SQL learning purposes. Customer names and transaction values are not real.

## Schema

The database (`E-Commerce Analytics System`) contains four tables:

- **Customers** — customer records (id, first/last name, phone — phone is the only nullable field)
- **Orders** — order records linked to customers
- **Products** — product catalog
- **Order_Items** — line items linking orders to products, with quantity and purchase price


## What this does

- **Data quality checks**: null-value audit and duplicate-row checks across all four tables
- **Revenue per order**: total revenue calculated from `Order_Items` and joined back to `Orders`
- **Revenue and order count per customer**: aggregated via join across Customers → Orders → Order_Items
- **Revenue and quantity sold per product**
- **Monthly revenue trend**: running total of revenue by month using a window function
- **Top 5 customers by revenue** (`RANK()` window function)
- **Top 5 products by revenue**
- **Above-average customers**: customers whose total revenue exceeds the average across all customers (correlated subquery)
- **Customer segmentation**: customers bucketed into HIGH / MEDIUM / LOW tiers by total revenue (CASE statement)

## Tech stack

Python, SQLAlchemy, PyMySQL, Pandas, Matplotlib, Seaborn, python-dotenv

## Setup

```bash
pip install -r requirements.txt
```

Create a `.env` file (not committed — see `.gitignore`) with:
