
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
	* id
	* name
3. dim_category
	* id
	* name
4. dim_status
	* id
	* type
5. fact_product
	* product_id
	* product_name
	* description
	* price
	* mrp
	* pieces_per_case
	* weight_per_pieces
	* uom_id
	* brand_id
	* category_id
	* tax_percent
	* product_status_id
	* created_by
	* created_date
	* updated_by
	* updated_date
6. fact_sales_product
	* id
	* date
	* product_id
	* total_quantity
	* price
	* total_gross_price
	* total_customers
	* total_tax_amount
	* totall_bill_amount
7. dim_customer
	* customer_id
	* user_name
	* first_name
	* last_name
	* country
	* town
	* active
8. fact_sales
	* id
	* client_sales_id
	* transaction_id
	* bill_no
	* bill_date
	* bill_location
	* customer_id
	* product_id
	* qty
	* uom_id
	* price
	* gross_price
	* tax_pc
	* tax_amt
	* discount_pc
	* discount_amt
	* net_bill_amt
	* created_by
	* updated_by
	* created_date
	* updated_date

 
# Proposed ER diagram of the warehouse

![Image ]()

After the logical modelling was purposed , I went to the physical implementation of it.

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


