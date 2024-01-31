import sqlite3

# Creates employee table
CREATE_EMPLOYEES_TABLE = "CREATE TABLE IF NOT EXISTS employees (eid INTEGER PRIMARY KEY, efname TEXT, elname TEXT);"
# Manipulate employee table
INSERT_EMPLOYEE = "INSERT INTO employees (efname, elname) VALUES (?, ?);"
READ_EMPLOYEE_LIST = "SELECT eid, elname FROM employees;"
UPDATE_EMPLOYEE_DATA = "UPDATE employees SET efname = ?, elname = ? WHERE eid =?;"
DELETE_EMPLOYEE = "DELETE FROM employees WHERE eid = ?"

# Create customer
CREATE_CUSTOMERS_TABLE = "CREATE TABLE IF NOT EXISTS customers (cid INTEGER PRIMARY KEY, cfname TEXT, clname TEXT);"
# Manipulate customer table
INSERT_CUSTOMER = "INSERT INTO customers (cfname, clname, idesc, sqty, stotal) VALUES (?, ?, ?, ?);"
# TRIGGER_SALE = "CREATE TRIGGER IF NOT EXISTS newsale AFTER INSERT ON sales " \
#                "BEGIN " \
#                "INSERT INTO customer (idesc, sqty, stotal) VALUES (idesc, sqty, stotal, UPDATE);" \
#                "END;"
READ_CUSTOMER_LIST = "SELECT cfname, clname FROM customers;"
UPDATE_CUSTOMER_DATA = "UPDATE customers SET cfname = ?, clname = ? idesc = ?, sqty = ?, stotal = ? WHERE cid=?;"
DELETE_CUSTOMER = "DELETE FROM customers WHERE cid = ?;"

# Create sales table
CREATE_SALES_TABLE = "CREATE TABLE IF NOT EXISTS sales (sid INTEGER PRIMARY KEY, " \
                     "sqty INTEGER, stotal INTEGER, cid INTEGER);"
# Manipulate sales table
INSERT_SALE = "INSERT INTO sales (cid, sqty, stotal) VALUES (?, ?, ?);"
READ_SALES_LIST = "SELECT stotal FROM sales;"
UPDATE_SALES_DATA = "UPDATE sales SET sqty = ?, stotal = ? WHERE sid =?;"
DELETE_SALE = "DELETE FROM sales WHERE sid = ?"

# Create inventory table
CREATE_INVENTORY_TABLE = "CREATE TABLE IF NOT EXISTS inventory (iid INTEGER PRIMARY KEY, idesc TEXT, iprice INTEGER);"
# Manipulate inventory table
INSERT_INVENTORY_ITEM = "INSERT INTO inventory (idesc, iprice) VALUES (?, ?);"
READ_INVENTORY = "SELECT idesc, iprice FROM inventory;"
UPDATE_INVENTORY_DATA = "UPDATE inventory SET idesc = ?, iprice = ? WHERE iid =?;"
DELETE_INVENTORY_ITEM = "DELETE FROM inventory WHERE iid = ?;"


def connect():
    return sqlite3.connect("database.db")


# Functions for creating tables
def create_tables(connection):
    with connection:
        connection.execute(CREATE_EMPLOYEES_TABLE)
        connection.execute(CREATE_CUSTOMERS_TABLE)
        connection.execute(CREATE_SALES_TABLE)
        connection.execute(CREATE_INVENTORY_TABLE)


# Functions for adding data to tables
def add_employee(connection, efname, elname):
    with connection:
        connection.execute(INSERT_EMPLOYEE, (efname, elname))


def add_customer(connection, cfname, clname):
    with connection:
        connection.execute(INSERT_CUSTOMER, (cfname, clname))


def add_sale(connection, cid, sqty, stotal):
    with connection:
        connection.execute(INSERT_SALE, (cid, sqty, stotal))


# def add_sale_to_customer_table(connection, idesc, sqty, stotal):
#     with connection:
#         connection.execute(TRIGGER_SALE, (idesc, sqty, stotal))


def add_inventory(connection, idesc, iprice):
    with connection:
        connection.execute(INSERT_INVENTORY_ITEM, (idesc, iprice))


# Functions for reading data from all tables
def lookup_employees(connection):
    with connection:
        return connection.execute(READ_EMPLOYEE_LIST).fetchall()


def lookup_customers(connection):
    with connection:
        return connection.execute(READ_CUSTOMER_LIST).fetchall()


def lookup_sales(connection):
    with connection:
        return connection.execute(READ_SALES_LIST).fetchall()


def lookup_inventory(connection):
    with connection:
        return connection.execute(READ_INVENTORY).fetchall()


# Functions to modify data in tables
def update_employees(connection, eid, efname, elname):
    with connection:
        return connection.execute(UPDATE_EMPLOYEE_DATA, (eid, efname, elname))


def update_customers(connection, cid, cfname, clname):
    with connection:
        return connection.execute(UPDATE_CUSTOMER_DATA, (cid, clname, cfname))


def update_sales(connection, sid, sqty, stotal):
    with connection:
        return connection.execute(UPDATE_SALES_DATA, (sid, sqty, stotal))


def update_inventory(connection, iid, idesc, iprice):
    with connection:
        return connection.execute(UPDATE_INVENTORY_DATA, (iid, idesc, iprice))


# Functions to delete data in tables
def delete_employees(connection, eid):
    with connection:
        return connection.execute(DELETE_EMPLOYEE, eid)


def delete_customer(connection, cid):
    with connection:
        return connection.execute(DELETE_CUSTOMER, cid)


def delete_sale(connection, sid):
    with connection:
        return connection.execute(DELETE_SALE, sid)


def delete_inventory_item(connection, iid):
    with connection:
        return connection.execute(DELETE_INVENTORY_ITEM, iid)


connect()

connect().commit()

connect().close()
