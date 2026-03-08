import pandas as pd
from sqlalchemy import create_engine, column
import os
from dotenv import  load_dotenv
import seaborn as sns
from matplotlib import pyplot as plt

load_dotenv()


engine = create_engine(
        f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}@localhost/E-Commerce Analytics System"
)


query="select * from Customers"
df_Customers=pd.read_sql(query,engine)


query= """select * from Orders """
df_Orders=pd.read_sql(query,engine)


query= """select * from Products """
df_Products=pd.read_sql(query,engine)

query= """select * from Order_Items """
df_Order_Items=pd.read_sql(query,engine)

# print(f"customer table {df_Customers}"
#        f"\n-------------------------------\n"
#        f"Product table {df_Products}"
#        f"\n-------------------------------\n"
#        f"Order table {df_Orders}"
#        f"\n-------------------------------\n"
#        f"Order_Items table{df_Order_Items}")



tbales=[df_Customers,df_Products,df_Orders,df_Order_Items]
for i in tbales:
        print(i.isnull().sum())

print("\n------------------------------------\n")
#the only column can be null in Customers is phone_number others cannot be inserted with null values due to NOT NULL

#here we have checked if there is any null, which was zero

#there is no null values in Orders table therefore

#there is no null in order_Items

for i in tbales:
        print(i.duplicated().sum())

#no duplication in our dataframe





query="""select
 sum(oi.Quantity * oi.Purchase_Price) as TOTAL_REVENUE
 from Order_Items oi
 group by oi.Order_Id"""

Total_Revenue_Per_Order=pd.read_sql(query,engine)

# df_Orders.drop(columns="Total_price",inplace=True)
# we drop Total_price column because values were inserted manually so error possibility was high

df_Orders=pd.concat([df_Orders,Total_Revenue_Per_Order],axis=1)


# we add revenue per order by calculating so that error possibility is lower ( we have had already order_date in order table)

query="""
select 
sum(oi.Quantity* oi.Purchase_Price) as TOTAL_REVENUE ,
COUNT(Distinct(o.Id)) as TOTAL_ORDER
 FROM Customers c 
inner join Orders o 
on o.Customer_Id= c.Id
inner join Order_Items oi 
on oi.Order_Id=o.Id
GROUP BY c.Id, c.F_name , c.L_name;
"""
total_revenue_and_orders=pd.read_sql(query,engine)
df_Customers=pd.concat([df_Customers,total_revenue_and_orders],axis=1)
print(df_Customers.head())

#we have added total revenue and total order per Customer in our df


query="""SELECT sum(oi.Quantity * oi.Purchase_Price) as TOTAL_REVENUE,
SUM(oi.Quantity) AS TOTAL_QUANTITY_SOLD
From Products p
inner join Order_Items oi
on p.Id=oi.Product_Id
group by p.Id , p.P_name
"""

total_quan_sold_and_revenue=pd.read_sql(query,engine)
df_Products=pd.concat([df_Products,total_quan_sold_and_revenue],axis=1)
print(df_Products.head())

# we have added total_revenue and total_quantity_sold to Products df



query="""select 
Months, 
sum(total_revenue) over( order by Months asc) as REVENUE_PER_MONTH
from (select sum(oi.Quantity * oi.Purchase_Price) as total_revenue, DATE_FORMAT(o.Order_Date, '%%Y-%%m-%%d') as Months from Orders o
inner join Order_Items oi 
on o.Id=oi.Order_Id
group by o.Id
) as table_per_month
"""

monthly_trend=pd.read_sql(query,engine)
print(monthly_trend.head())

# tracking total_revenue per month in db way





query="""select 
FULL_NAME,
TOTAL_REVENUE,
RANK() OVER(ORDER BY TOTAL_REVENUE DESC ) AS REVENUE_RANK

FROM(
SELECT 
concat(F_name , " ", L_name) as FULL_NAME,
sum(oi.Quantity * oi.Purchase_Price) AS TOTAL_REVENUE 
 FROM Customers c 
 inner join Orders o 
 on c.Id= o.Customer_Id
 inner join Order_Items oi 
 on o.Id=oi.Order_Id
 group by c.Id 
 ) AS TABLE_CUSTOMER_REVENUE
 
 """


top_5_customers=pd.read_sql(query,engine)
print(top_5_customers)

#we identify top 5 customers based on their total_revenue

query="""
SELECT 
P_name ,
sum(oi.Purchase_Price * oi.Quantity) as TOTAL_REVENUE
from products p
inner join Order_Items oi
on p.Id= oi.Product_Id
group by p.P_name , p.Id 
order by TOTAL_REVENUE desc  limit 5 
"""


top_5_products= pd.read_sql(query,engine)
print(top_5_products)
#we identify top 5 Products  based on their total_revenue


query="""SELECT 
    FULL_NAME,
    TOTAL_REVENUE
FROM (
        SELECT 
            CONCAT(c.F_name, " ", c.L_name) AS FULL_NAME,
            SUM(oi.Quantity * oi.Purchase_Price) AS TOTAL_REVENUE
        FROM Customers c
        JOIN Orders o 
            ON c.Id = o.Customer_Id
        JOIN Order_Items oi 
            ON o.Id = oi.Order_Id
        GROUP BY c.Id
     ) AS customer_revenue
WHERE TOTAL_REVENUE > (
        SELECT AVG(TOTAL_REVENUE)
        FROM (
                SELECT 
                    SUM(oi.Quantity * oi.Purchase_Price) AS TOTAL_REVENUE
                FROM Customers c
                JOIN Orders o 
                    ON c.Id = o.Customer_Id
                JOIN Order_Items oi 
                    ON o.Id = oi.Order_Id
                GROUP BY c.Id
             ) AS avg_customer_revenue
)
ORDER BY TOTAL_REVENUE DESC; """


c_more_than_avg=pd.read_sql(query,engine)
print(c_more_than_avg)

#customers more than average


# plt.plot(monthly_trend["Months"],monthly_trend["REVENUE_PER_MONTH"],marker="o")
# plt.title("Monthly Revenue chart ")
# plt.xlabel("Months")
# plt.ylabel("Revenue per Month")
# plt.show()
# plt.close()

#Using bar plot to show revenue over each month

# sns.barplot(x=df_Products["P_name"],y=df_Products["TOTAL_REVENUE"])
# plt.title("Products Revenue chart ")
# plt.xlabel("Products Name")
# plt.ylabel("Revenue per Product")
# plt.show()
# plt.close()


#Using bar plot to show revenue for each product

query = """select concat(c.F_name , " " , c.L_name) as FULL_NAME ,SUM(oi.Quantity * oi.Purchase_Price) as TOTAL_REVENUE,
case 
when SUM(oi.Quantity * oi.Purchase_Price) >1501 THEN "HIGH"
WHEN SUM(oi.Quantity * oi.Purchase_Price) BETWEEN 1000 AND 1500 THEN "MEDIUM"
WHEN SUM(oi.Quantity * oi.Purchase_Price) <1000 THEN "LOW"
END AS CATEGORY
FROM Customers c 
inner join Orders o 
on c.Id = o.Customer_Id
inner join Order_Items oi
on oi.Order_Id=o.Id
GROUP BY c.Id, c.F_name,c.L_name"""

customer_category=pd.read_sql(query, engine)

# plt.pie(customer_category["TOTAL_REVENUE"],labels=customer_category["FULL_NAME"])
# plt.show()

#Using pie chart to visualize each customer total revenue

