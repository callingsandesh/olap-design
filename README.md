
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


# I created `fact_product` after creating it dimentions tables like `dim_uom` , `dim_brand`,`dim_category`,`dim_status`.
> `schema\create_dim_brand.sql`
```
CREATE TABLE dim_brand(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);


```
> `schema\create_dim_category.sql`
```
CREATE TABLE dim_category(
	id SERIAL PRIMARY KEY,
	name VARCHAR(255)
);
```

> `schema\create_dim_status.sql`
```
CREATE TABLE dim_status(
 id SERIAL PRIMARY KEY,
 type VARCHAR(255)
);
```

> `schema\create_dim_uom`
``CREATE TABLE dim_uom(
    id SERIAL PRIMARY KEY,
    type VARCHAR(255)
);`
```

> `schema\create_fact_product.sql`
```
CREATE TABLE fact_product(
	product_id INTEGER PRIMARY KEY,
	product_name VARCHAR(255),
	description TEXT,
	price FLOAT,
	mrp FLOAT,
	pieces_per_case FLOAT,
	weight_per_piece FLOAT,
	uom_id INTEGER,
	brand_id INTEGER,
	category_id INTEGER,
	tax_percent INTEGER,
	product_status_id INTEGER,
	created_by VARCHAR(255),
	created_date TIMESTAMP,
	updated_by VARCHAR(255),
	updated_date TIMESTAMP,
	
	CONSTRAINT fk_fact_product_dim_uom
	FOREIGN KEY(uom_id) REFERENCES dim_uom(id),
	CONSTRAINT fk_fact_product_dim_brand
	FOREIGN KEY(brand_id) REFERENCES dim_brand(id),
	CONSTRAINT fk_fact_product_dim_category
	FOREIGN KEY(category_id) REFERENCES dim_category(id),
	CONSTRAINT fk_fact_product_dim_status
	FOREIGN KEY(product_status_id) REFERENCES dim_status(id)
);
```
# I populated the above dimention table first and then the `fact_product` using the following query on the pipeline.

```
INSERT INTO dim_brand(name)
SELECT DISTINCT brand
FROM product_dump
```

```
INSERT INTO dim_category(name)
SELECT DISTINCT category
FROM product_dump
```

```
INSERT INTO dim_status(type)
SELECT DISTINCT active
FROM product_dump
```

```
INSERT INTO dim_uom(type)
SELECT DISTINCT uom
FROM product_dump
```

```
INSERT INTO fact_product
SELECT 
	product_id,
	product_name,
	description,
	price,
	mrp,
	pieces_per_case,
	weight_per_piece,
	dim_uom.id AS uom_id,
	dim_brand.id AS brand_id,
	dim_category.id AS category_id,
	tax_percent,
	dim_status.id AS product_status_id,
	created_by,
	created_date,
	updated_by,
	updated_date
FROM product_dump
INNER JOIN dim_uom
	ON product_dump.uom = dim_uom.type
INNER JOIN dim_brand
	ON product_dump.brand = dim_brand.name
INNER JOIN dim_category
	ON product_dump.category = dim_category.name
INNER JOIN dim_status
	ON product_dump.active = dim_status.type
```

After all the facts and dimention table of product was created , I made the `fact_sales_product` using the following query
> `schema\create_fact_sales_product.sql`

```
CREATE TABLE fact_sales_product(
	id SERIAL PRIMARY KEY,
	date DATE,
	product_id INTEGER,
	total_quantity FLOAT,
	price FLOAT,
	total_gross_price FLOAT,
	total_discount_amt FLOAT,
	total_customers SMALLINT,
	total_tax_amount FLOAT,
	total_new_bill_amount FLOAT,

	CONSTRAINT fk_fact_sales_product
	FOREIGN KEY(product_id) REFERENCES fact_product(product_id)
);
```
So, to insert the data into the above table, I did some preprocessing on the dump tables ,extracted out the necessary data and populated with it using the pipeline.

```
INSERT INTO fact_sales_product(date,product_id,total_quantity,price,total_gross_price,total_discount_amt,total_customers,total_tax_amount,total_new_bill_amount)
SELECT 
    CASE WHEN bill_date='2017-02-30 11:00:00' THEN DATE(TO_TIMESTAMP('2017-02-28 11:00:00','YYYY-MM-DD'))
	     ELSE DATE(TO_TIMESTAMP(bill_date,'YYYY-MM-DD'))
	     END AS date,
    product_id ,
	SUM(CAST(qty AS INT)) AS total_quantity,
	ROUND(AVG(CAST(price AS FLOAT))::NUMERIC,2) AS price, 
	ROUND(SUM(CAST(gross_price AS FLOAT))::NUMERIC,2) AS total_gross_price,
	SUM(CAST(discount_amt AS FLOAT)) AS total_discount_amt,
	COUNT(customer_id) AS total_customers,
	ROUND(sum(CAST(tax_amount AS FLOAT))::NUMERIC,2) AS total_tax_amount,
	ROUND(sum(CAST(net_bill_amt AS FLOAT))::NUMERIC,2) AS total_new_bill_amount
FROM sales_dump
GROUP BY date,product_id
ORDER BY date ASC , total_new_bill_amount DESC
```
I grouped by using date and product_id and  use the aggregate function to fectch the total numer of specific product sold on a specific date.


After the `fact_sale_product` table was populated , I did some query to analyse the data.

### SELECTING PRODUCT WITH HIGHEST SELLS ON EACH DAY BASIS
```
CREATE  OR REPLACE VIEW date_product_id_total_bill AS
SELECT 
*
FROM fact_sales_product

WHERE (date,total_new_bill_amount) IN (

SELECT date,MAX(total_new_bill_amount)
FROM fact_sales_product
GROUP BY date
)
ORDER BY date
```
`SELECT * FROM date_product_id_total_bill `

![Image ]()


> TOTAL SALES OF EACH PRODUCT ON DAILY BASIS
```
SELECT 
	e.product_id,
	p.product_name,
	e.avg_price,
	e.total_quantity as total_quantity_sold,
	e.total_sales,
	b.name as brand_name,
	c.name as category
FROM 
each_product_total_sale e
INNER JOIN fact_product p
	ON e.product_id = p.product_id
INNER JOIN dim_brand b
	ON p.brand_id = b.id
INNER JOIN dim_category c
	ON p.category_id = c.id
```

![Image ]()

### TOTAL PRODUCTS THAT ARE NOT SOLD YET
```
--TOTAL PRODUCTS THAT ARE NOT SOLD YET
SELECT 
	p.product_id,
	p.product_name,
	p.price,
	b.name as brand_name,
	c.name as category
FROM 
each_product_total_sale e
RIGHT JOIN fact_product p
	ON e.product_id = p.product_id
INNER JOIN dim_brand b
	ON p.brand_id = b.id
INNER JOIN dim_category c
	ON p.category_id = c.id
WHERE e.product_id IS NULL
```

![Image ]()



### TOTAL SALES BY BRAND
```
SELECT 
	
	ROUND(AVG(e.avg_price)::NUMERIC,2) AS avg_price,
	SUM(e.total_quantity) as total_quantity_sold,
	SUM(e.total_sales) as total_sales,
	b.name as brand_name
FROM 
each_product_total_sale e
INNER JOIN fact_product p
	ON e.product_id = p.product_id
INNER JOIN dim_brand b
	ON p.brand_id = b.id
GROUP BY brand_name
ORDER BY total_sales DESC
```
![Image ] ()

###TOTAL SALES BY CATEGORY
```
SELECT 
	ROUND(AVG(e.avg_price)::NUMERIC,2) AS avg_price ,
	SUM(e.total_quantity) as total_quantity_sold,
	SUM(e.total_sales) AS total_sales,
	c.name as category
FROM 
each_product_total_sale e
INNER JOIN fact_product p
	ON e.product_id = p.product_id
INNER JOIN dim_category c
	ON p.category_id = c.id
GROUP BY category
ORDER BY total_sales DESC
```


