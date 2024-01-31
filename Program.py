import database

MAIN_MENU = """--- Larry’s Sartorial Shoppe ---

Choose an option:
1) Add Employee
2) View Employees
3) Modify Employees
4) Delete Employee

5) Add Customer
6) View Customers
7) Modify Customers
8) Delete Customer

9) Add Sale
10) View Sales
11) Modify Sales
12) Delete Sale

13) Add Inventory Item
14) View Inventory
15) Modify Inventory
16) Delete Inventory Item

17) View Sales & Inventory

18) Exit

Your Selection:"""


def menu():
    connection = database.connect()
    database.create_tables(connection)

    # Loop for menu function and run program
    while (user_input := input(MAIN_MENU)) != "18":

        # Add employee to database
        if user_input == "1":
            efname = input("Enter first employee name: ")
            elname = input("Enter employee last name: ")
            database.add_employee(connection, efname, elname)
            print("Employee has been added to database")

        # View all employees
        elif user_input == "2":
            employees = database.lookup_employees(connection)

            for employee_list in employees:
                print(employee_list)

        # Modify employee data
        elif user_input == "3":
            eid = input("Enter employee id: ")
            efname = input("Change first name to: ")
            elname = input("Change last name to: ")
            database.update_employees(connection, eid, efname, elname)
            print("Employee data has been updated")

        # Delete employee
        elif user_input == "4":
            delete_employee_now = input("Enter employee id: ")

            database.delete_employees(connection, eid=delete_employee_now)
            print("Employee deleted from database")

        # Add customer to database
        elif user_input == "5":
            cfname = input("Enter customer first name: ")
            clname = input("Enter customer last name: ")
            database.add_customer(connection, cfname, clname)
            print("Customer has been added to database")

        # View all customers
        elif user_input == "6":
            customers = database.lookup_customers(connection)

            for customer_list in customers:
                print(customer_list)

        # Modify customer data
        elif user_input == "7":
            cid = input("Enter customer id: ")
            cfname = input("Change first name to: ")
            clname = input("Change last name to: ")
            database.update_customers(connection, cfname, cfname, clname)
            print("Customer information has been updated")

        # Delete customer data
        elif user_input == "8":
            delete_customer_now = input("Enter customer id: ")

            database.delete_customer(connection, cid=delete_customer_now)
            print("Customer has been deleted from database")

        # Add sale to database and customer table
        elif user_input == "9":
            customer_id = input("Enter customer ID: ")
            item = input("Enter item purchased: ")
            sale_qty = input("Enter sale quantity: ")
            sale_total = float(input('Enter sale price: '))
            print("Receipt For Sale: ",
                  "Customer ID" + " " + customer_id + " " + "has purchased" + " " + sale_qty + " " + "of" + " "
                  + item + " " + "for", sale_total)
            database.add_sale(connection, cid=customer_id, sqty=sale_qty, stotal=sale_total)
            # database.add_sale_to_customer_table(connection, idesc=item, sqty=sale_qty, stotal=sale_total)

        # View all sales
        elif user_input == "10":
            sales = database.lookup_sales(connection)

            for sales_list in sales:
                print(sales_list)

        # Modify sales data
        elif user_input == "11":
            modify_sale = input("Enter sale id:")
            sale_qty = input("Enter sale quantity: ")
            sale_total = float(input('Enter sale price: '))
            print("Sale has been updated")
            database.update_sales(connection, sid=modify_sale, sqty=sale_qty, stotal=sale_total)

        # Delete sale data
        elif user_input == "12":
            delete_sale_now = input("Enter sale id: ")

            database.delete_sale(connection, sid=delete_sale_now)
            print("Sale has been deleted from database")

        # Add inventory to database
        elif user_input == "13":
            idesc = input("Enter inventory description: ")
            iprice = float(input('Enter item price: '))
            database.add_inventory(connection, idesc, iprice)
            print("Item added to inventory")

        # View all inventory items
        elif user_input == "14":
            inventory = database.lookup_inventory(connection)

            for inventory_list in inventory:
                print(inventory_list)

        # Modify inventory data
        elif user_input == "15":
            iid = input("Enter inventory id:")
            idesc = input("Change item description: ")
            iprice = float(input("Change item price: "))
            database.update_inventory(connection, iid, idesc, iprice)
            print("Inventory updated")

        # Delete inventory data
        elif user_input == "16":
            delete_inventory_item_now = input("Enter inventory id: ")

            database.delete_inventory_item(connection, iid=delete_inventory_item_now)
            print("Inventory item deleted from database")

        elif user_input == "17":
            inventory = database.lookup_inventory(connection)
            sales = database.lookup_sales(connection)

            transactions = inventory + sales

            for inventory_sales_list in transactions:
                print("Transactions", inventory_sales_list)


# Start program
menu()
