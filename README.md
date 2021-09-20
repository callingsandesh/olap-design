
# Requirement identification
- To find out the trends among the customers.
- To analyze their sales to invest more on product that are selling fast.
- To analyze their sales to invest more on product that are producing high profits.
- To analyze the sales to remove the potential products that are not doing so good.

# Potential area of analysis
- products
- sales
- customer
- location
- product brand
- product categoty

# The list of entities proposed are:
1. dim_uom
	* id
	* type
2. dim_brand
3. dim_category
4. dim_status
5. fact_product
6. fact_sales_product
7. dim_customer
8. fact_sales


 
# Proposed ER diagram of the warehouse



# Firstly I created different tables to dump the flat files datas.
>`schema\create_table_customer_dump.sql`

```
CREATE TABLE customer_dump(
    customer_id INTEGER PRIMARY KEY,
    user_name VARCHAR(255),
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    country VARCHAR(255),
    town VARCHAR(255),
    active CHAR
);
```
Then dumped the file using the SQL command ,`INSERT INTO customer_dump VALUES(%s,%s,%s,%s,%s,%s,%s)` using the pipeline.

> `schema\create_table_product_dump.sql`
```
CREATE TABLE product_dump(
	product_id VARCHAR(255) PRIMARY KEY,
	product_name VARCHAR(255),
	description VARCHAR(255),
	price VARCHAR(255),
	mrp VARCHAR(255),
	pieces_per_case VARCHAR(255),
	weight_per_piece VARCHAR(255),
	uom VARCHAR(255),
	brand VARCHAR(255),
	category VARCHAR(255),
	tax_percent VARCHAR(255),
	active VARCHAR(255),
	created_by VARCHAR(255),
	created_date VARCHAR(255),
	updated_by VARCHAR(255),
	updated_date VARCHAR(255)
)
```
Then dumped the file using the SQL command ,`INSERT INTO product_dump VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);` using the pipeline.

> `schema\create_table_sales_dump.sql`
```
CREATE TABLE sales_dump(
	id INTEGER PRIMARY KEY,
	transaction_id VARCHAR(255),
	bill_no VARCHAR(255),
	bill_date VARCHAR(255),
	bill_location VARCHAR(255),
	customer_id INTEGER,
	product_id INTEGER,
	qty VARCHAR(255),
	uom VARCHAR(255),
	price VARCHAR(255),
	gross_price VARCHAR(255),
	tax_pc VARCHAR(255),
	tax_amount VARCHAR(255),
	discount_pc VARCHAR(255),
	discount_amt VARCHAR(255),
	net_bill_amt VARCHAR(255),
	created_by VARCHAR(255),
	updated_by VARCHAR(255),
	created_date VARCHAR(255),
	updated_date VARCHAR(255)
);
```
Then dumped the file using the SQL command ,`INSERT INTO sales_dump VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);` using the pipeline.

After dumping all of the files , i had the closer look at the datas and the proper requirement analysis of it
