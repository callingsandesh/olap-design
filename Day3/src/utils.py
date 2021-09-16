import psycopg2
def connect_to_ecommerce_dump():
    return psycopg2.connect(user="postgres",
                                  password="admin",
                                  host="localhost",
                                  port="5432",
                                  database="ecommerce_dumb"
                                  )

def connect_to_sales_raw():
    return psycopg2.connect(user="postgres",
                                  password="admin",
                                  host="localhost",
                                  port="5432",
                                  database="sales_raw"
                                  )

def connect_to_sales_archive():
    return psycopg2.connect(user="postgres",
                                  password="admin",
                                  host="localhost",
                                  port="5432",
                                  database="sales_archive"
                                  )