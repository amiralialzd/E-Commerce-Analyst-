# E-Commerce Sales Analysis (SQL + Python)

## Project Overview

This project analyzes a small e-commerce database using **SQL and Python**.
The goal was to practice combining database querying, data analysis, and data visualization in a single workflow.

The project connects a **MySQL database to Python**, loads the tables into **pandas DataFrames**, performs analysis using **SQL queries**, and visualizes results using **Matplotlib / Seaborn**.

This was my **first project integrating SQL, Python, and visualization** in one pipeline.

---

## Technologies Used

* **MySQL** – database design and queries
* **Python**
* **Pandas** – data manipulation
* **SQLAlchemy** – database connection
* **Matplotlib / Seaborn** – visualization
* **dotenv** – environment variable management

---

## Database Structure

The project uses a simple **e-commerce schema** with four tables:

* **Customers** – customer information
* **Orders** – order records
* **Order_Items** – products included in each order
* **Products** – product catalog

Relationships between tables were created using **foreign keys**.

---

## Project Workflow

### 1. Database Connection

* Connected MySQL to Python using SQLAlchemy.
* Loaded all tables into pandas DataFrames.

### 2. Data Verification

* Checked for null values.
* Checked for duplicate rows.
* Verified relationships between tables.

### 3. Data Analysis

Using SQL queries, the project calculated:

* Total revenue per customer
* Total number of orders per customer
* Product revenue and quantity sold
* Monthly revenue trends
* Customer rankings based on revenue

### 4. Visualization

The results were visualized using Python:

* **Line chart** – revenue trend over time
* **Bar chart** – product revenue comparison
* **Pie chart** – revenue distribution by customer

---

## Key Insights

**Top Customers**

* John Doe
* Jane Smith
* Alice Brown

**Highest Revenue Period**

* 2026-02-28 generated the highest revenue in the dataset.

**Customer Revenue Segments**

| Customer       | Revenue | Category |
| -------------- | ------- | -------- |
| John Doe       | 1830    | High     |
| Jane Smith     | 1780    | High     |
| Alice Brown    | 1180    | Medium   |
| Liam Williams  | 1130    | Medium   |
| Olivia Johnson | 200     | Low      |

---

## Example Visualizations

The project includes charts showing:

* revenue trends
* product performance
* customer spending distribution

---

## What I Learned

Through this project I practiced:

* Designing a relational database
* Writing analytical SQL queries
* Using **window functions** for ranking
* Integrating **SQL with Python**
* Creating basic data visualizations

---

## Future Improvements

Possible improvements for this project:

* Larger and more realistic dataset
* Additional business metrics (average order value, customer lifetime value)
* More advanced visualizations
* Deeper revenue analysis

---

## Author

Amirali Alizadeh
