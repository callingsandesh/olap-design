## ETL weekend Assignemt

# >Firstly I created different tables to dump the data flat file datas.
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
