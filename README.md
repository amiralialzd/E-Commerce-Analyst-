# E-Commerce Sales Analytics

SQL-based analysis of a small e-commerce database, covering revenue tracking, customer segmentation, and product performance using Python, SQLAlchemy, and MySQL.

> **Note:** This project uses a practice database with synthetic customer and order data created for SQL learning purposes. Customer names and transaction values are not real.

## Schema

- **Customers** — customer records (id, first/last name, phone, email)
- **Orders** — order records linked to customers
- **Products** — product catalog
- **Order_Items** — line items linking orders to products, with quantity and purchase price

## What this does

- Data quality checks: null-value audit and duplicate-row checks
- Revenue per order, calculated from `Order_Items`
- Cumulative revenue over time (running total by date)
- Top 3–5 customers and products by revenue (window functions / ranking)
- Customers above average revenue (correlated subquery)
- Customer segmentation into HIGH / MEDIUM / LOW tiers by total revenue

## Tech stack

Python, SQLAlchemy, PyMySQL, Pandas, Matplotlib, Seaborn, python-dotenv

## Setup

```bash
pip install -r requirements.txt
```

Create a `.env` file (not committed) with:
```
DB_USER=your_mysql_username
DB_PASS=your_mysql_password
```

```bash
python main.py
```

## Results

**Top 3 customers by revenue:**

| Customer | Revenue |
|---|---|
| John Doe | 1830.0 |
| Jane Smith | 1780.0 |
| Alice Brown | 1180.0 |

**Top 5 products by revenue:**

| Product | Revenue |
|---|---|
| Laptop | 3000.0 |
| Smartphone | 2000.0 |
| Headphones | 600.0 |
| Keyboard | 320.0 |
| Mouse | 200.0 |

**Customer revenue segmentation:**

| Customer | Revenue | Category |
|---|---|---|
| John Doe | 1830 | HIGH |
| Jane Smith | 1780 | HIGH |
| Alice Brown | 1180 | MEDIUM |
| Liam Williams | 1130 | MEDIUM |
| Olivia Johnson | 200 | LOW |

See `Reports.md` for additional ad-hoc findings, and the `images/` folder for charts.

## Known limitations

- The per-product and per-customer summary tables built via `pd.concat(..., axis=1)` join by row position rather than by ID, which can misattribute revenue/quantity figures when row counts or ordering differ between the source tables. The dedicated ranking queries (top customers/products, segmentation) above are unaffected and reflect correct values.
- The product catalog contains some duplicate entries (same product inserted under a different ID); the duplicate check only flags fully identical rows, so it doesn't catch this case.
- The "Monthly Revenue" chart plots a cumulative running total rather than per-month figures.
