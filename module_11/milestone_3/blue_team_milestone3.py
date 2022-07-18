
from platform import python_branch
import mysql.connector
from mysql.connector import errorcode

mydb = {
    "host": '127.0.0.1',
    "user": 'root',
    "password": 'D@tabase4585',  # replace with your own password
    # make sure to have an existing database of this name to store CHAR(20)o
    "database": 'bacchus_winery',
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**mydb)

    print("\n Database user {} connected to MySQL on host {} with database {}".format(
        mydb['user'], mydb['host'], mydb['database']))

    input("\n Press any key to continue...")
    print("\n")

    # Creating a cursor object using the cursor method
    cursor = db.cursor()

    # Drop all tables if they exist - ONLY USE THIS FOR TESTING, 
    # you need to drop the tables every time you run the script. 
    # FOR THE FIRST RUN COMMENT THIS OUT every run after they should be left in
    cursor.execute("DROP TABLE IF EXISTS COMPANY;")
    cursor.execute("DROP TABLE IF EXISTS EMPLOYEE;")
    cursor.execute("DROP TABLE IF EXISTS HOURS_WORKED;")
    cursor.execute("DROP TABLE IF EXISTS PRODUCTS;")
    cursor.execute("DROP TABLE IF EXISTS DISTRIBUTOR_ORDERS;")
    cursor.execute("DROP TABLE IF EXISTS DISTRIBUTOR;")
    cursor.execute("DROP TABLE IF EXISTS SUPPLIES;")
    cursor.execute("DROP TABLE IF EXISTS SUPPLY_ORDERS;")
    cursor.execute("DROP TABLE IF EXISTS SUPPLIER;")
    

    # Creating all tables
    cursor.execute("CREATE TABLE COMPANY (COMPANY_NAME CHAR(20))")

    cursor.execute("CREATE TABLE EMPLOYEE (EMPLOYEE_ID int, FIRST_NAME CHAR(20), LAST_NAME CHAR(20),JOB_TITLE CHAR(20))")

    cursor.execute("CREATE TABLE HOURS_WORKED (EMPLOYEE_ID int, Q1 int, Q2 int, Q3 int, Q4 int)")

    cursor.execute("CREATE TABLE PRODUCTS (PRODUCT_ID int, PRODUCT_NAME char(20), AMOUNT_IN_INVENTORY int, AMOUNT_SOLD int, PRICE float)")

    cursor.execute('''CREATE TABLE DISTRIBUTOR_ORDERS (DISTRIBUTOR_ORDER_NUMBER int, DISTRIBUTOR_ID int, PRODUCT_ID int,AMOUNT_BOUGHT int, TOTAL_PRICE float, TRACKING_NUMBER CHAR(20), ORDER_DATE date, SHIP_DATE date)''')

    cursor.execute("CREATE TABLE DISTRIBUTOR (DISTRIBUTOR_ID int, DISTRIBUTOR_NAME CHAR(20))")

    cursor.execute("CREATE TABLE SUPPLIES (SUPPLY_ID int, SUPPLY_NAME char(20), AMOUNT_ON_HAND int)")

    cursor.execute('''CREATE TABLE SUPPLY_ORDERS (SUPPLY_ORDER_NUMBER int,  SUPPLIER_ID int, SUPPLY_ID int, AMOUNT_ORDERED int, TOTAL_COST float, SUPPLY_ORDER_DATE date,  SUPPLY_SHIP_DATE date, EXPECTED_DELIVERY_DATE date, ACTUAL_DELIVERY_DATE date)''')

    cursor.execute("CREATE TABLE SUPPLIER (SUPPLIER_ID int,  SUPPLIER_NAME CHAR(20))")

    # Inserting data INTO the COMPANY table
    sql = "INSERT INTO COMPANY (COMPANY_NAME) VALUES (%s)"
    val = ('Bacchus Winery')
    cursor.execute(sql, (val,))

    # Inserting data INTO the EMPLOYEE table
    sql = "INSERT INTO EMPLOYEE (EMPLOYEE_ID, FIRST_NAME, LAST_NAME, JOB_TITLE) VALUES (%s, %s, %s, %s)"
    val = [
        (1001, "Stan", "Bacchus", "Owner"),
        (1002, "Davis", "Bacchus", "Owner"),
        (1003, "Janet", "Collins", "Finances/Payroll"),
        (1004,	"Roz",	"Murphy", "Marketing"),
        (1005,	"Bob",	"Ulrich", "Assistant to Roz"),
        (1006,	"Henry", "Doyle", "Manages Production"),
        (1007,	"Maria", "Costanza", "Manages Distribution")
    ]

    cursor.executemany(sql, val,)

    # Inserting data INTO the HOURS_WORKED table
    sql = "INSERT INTO HOURS_WORKED (EMPLOYEE_ID, Q1, Q2, Q3, Q4) VALUES (%s, %s, %s, %s, %s)"
    val = [
        (1001, 530, 460, 504, 512),
        (1002, 504, 488, 496, 504),
        (1003, 480, 500, 488, 494),
        (1004, 472, 504, 480, 494),
        (1005, 512, 504, 504, 488),
        (1006, 512, 480, 504, 512),
        (1007, 480, 500, 520, 504)
    ]

    cursor.executemany(sql, val,)

    # Inserting data INTO the PRODUCTS table
    sql = "INSERT INTO PRODUCTS (PRODUCT_ID, PRODUCT_NAME, AMOUNT_IN_INVENTORY, AMOUNT_SOLD, PRICE) VALUES (%s, %s, %s, %s, %s)"
    val = [
        (70001, "Merlot", 100, 10, 99.99),
        (70002, "Cabernet", 300, 30, 59.99),
        (70003, "Chablis", 200, 20, 67.99),
        (70004, "Chardonnay", 200, 20, 55.99)
    ]

    cursor.executemany(sql, val,)

    # Inserting data INTO the DISTRIBUTOR_ORDERS table
    sql = "INSERT INTO DISTRIBUTOR_ORDERS (DISTRIBUTOR_ORDER_NUMBER, DISTRIBUTOR_ID, PRODUCT_ID, AMOUNT_BOUGHT, TOTAL_PRICE, TRACKING_NUMBER, ORDER_DATE, SHIP_DATE) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = [
        (200101, 2001, 70001, 20, 1980, "2004001", "2022-01-01", "2022-01-03"),
        (200102, 2002, 70002, 20, 1180, "2004002", "2022-01-01", "2022-01-03"),
        (200103, 2003, 70003, 20, 1340, "2004003", "2022-01-01", "2022-01-03"),
        (200104, 2004, 70004, 20, 1100, "2004004", "2022-01-01", "2022-01-03")
    ]

    cursor.executemany(sql, val,)

    # Inserting data INTO the DISTRIBUTOR table
    sql = "INSERT INTO DISTRIBUTOR (DISTRIBUTOR_ID, DISTRIBUTOR_NAME) VALUES (%s, %s)"
    val = [
        (2001, "ABC Wines"),
        (2002, "Wine & Dine"),
        (2003, "Day Drinking"),
        (2004, "Live, Laugh, Wine")
    ]

    cursor.executemany(sql, val,)

    # Inserting data INTO the SUPPLIES table
    sql = "INSERT INTO SUPPLIES (SUPPLY_ID, SUPPLY_NAME, AMOUNT_ON_HAND) VALUES (%s, %s, %s)"
    val = [
        (90001, "Bottles", 21),
        (90002, "Corks", 29),
        (90003, "Labels", 90),
        (90004, "Boxes", 86),
        (90005, "Vats", 101),
        (90006, "Tubing", 49)
    ]

    cursor.executemany(sql, val,)

    # Inserting data INTO the SUPPLY_ORDERS table
    sql = "INSERT INTO SUPPLY_ORDERS (SUPPLY_ORDER_NUMBER, SUPPLIER_ID, SUPPLY_ID, AMOUNT_ORDERED, TOTAL_COST, SUPPLY_ORDER_DATE, SUPPLY_SHIP_DATE, EXPECTED_DELIVERY_DATE, ACTUAL_DELIVERY_DATE) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = [
        (300101, 3001, 90001, 23, 2500, "2022-02-01",
         "2022-02-03", "2022-02-05", "2022-02-05"),
        (300102, 3001, 90002, 39, 2500, "2022-02-01",
         "2022-02-03", "2022-02-05", "2022-02-05"),

        (300103, 3002, 90003, 29, 2500, "2022-02-02",
         "2022-02-04", "2022-02-06", "2022-02-06"),
        (300104, 3002, 90004, 45, 2500, "2022-02-02",
         "2022-02-04", "2022-02-06", "2022-02-06"),

        (300105, 3003, 90005, 90, 2500, "2022-02-03",
         "2022-02-05", "2022-02-07", "2022-02-09"),
        (300106, 3003, 90006, 58, 2500, "2022-02-03",
         "2022-02-05", "2022-02-07", "2022-02-09")
    ]

    cursor.executemany(sql, val,)

    # Inserting data INTO the Supplier table
    sql = "INSERT INTO SUPPLIER (SUPPLIER_ID, SUPPLIER_NAME) VALUES (%s, %s)"
    val = [
        (3001, "B&C"),
        (3002, "L&B"),
        (3003, "V&T")
    ]

    cursor.executemany(sql, val,)

    # Showing the tables
    cursor.execute("SHOW TABLES")
    result = cursor.fetchall()
    for x in result:
        print(str(x).strip("()").replace("\'","").replace(",",""))
    
    # execute your query
    cursor.execute("SELECT * FROM COMPANY;")
    # fetch all the matching rows
    result = cursor.fetchall()
    # loop through the rows
    print("\n-- DISPLAYING COMPANY RECORDS --")
    for row in result:
        print("\nCompany Name: {}".format(row[0]))

    # execute your query
    cursor.execute("SELECT * FROM EMPLOYEE;")
    # fetch all the matching rows
    result = cursor.fetchall()
    # loop through the rows
    print("\n-- DISPLAYING EMPLOYEE RECORDS --")
    for row in result:
        print("\nEmployee ID: {}\nFirst Name: {}\nLast Name: {}\nJob Title: {}".format(row[0], row[1], row[2], row[3]))
    
    # execute your query
    cursor.execute("SELECT * FROM HOURS_WORKED;")
    # fetch all the matching rows
    result = cursor.fetchall()
    # loop through the rows
    print("\n-- DISPLAYING HOURS WORKED RECORDS --")
    for row in result:
        print("\nEmployee ID: {}\nQ1: {}\nQ2: {}\nQ3: {}\nQ4: {}".format(row[0], row[1], row[2], row[3], row[4]))

    # execute your query
    cursor.execute("SELECT * FROM DISTRIBUTOR;")
    # fetch all the matching rows
    result = cursor.fetchall()
    # loop through the rows
    print("\n-- DISPLAYING DISTRIBUTOR RECORDS --")
    for row in result:
        print("\nDistributor ID: {}\nDistributor Name: {}".format(row[0], row[1]))

    # execute your query
    cursor.execute("SELECT * FROM DISTRIBUTOR_ORDERS;")
    # fetch all the matching rows
    result = cursor.fetchall()
    # loop through the rows
    print("\n--DISPLAYING DISTRIBUTOR ORDER RECORDS --")
    for row in result:
        print("\nDistributor Order #: {}\nDistributor ID: {}\nProduct ID: {}\nAmount Bought: {}\nOrder Total: {}\nTracking #: {}\nOrder Date: {}\nShip Date: {}".format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))

    # execute your query
    cursor.execute("SELECT * FROM PRODUCTS;")
    # fetch all the matching rows
    result = cursor.fetchall()
    # loop through the rows
    print("\n-- DISPLAYING PRODUCT RECORDS --")
    for row in result:
        print("\nProduct ID: {}\nProduct Name: {}\nAmount in Inventory: {}\nAmount Sold: {}\nPrice: {}".format(row[0], row[1], row[2], row[3], row[4]))

    # execute your query
    cursor.execute("SELECT * FROM SUPPLIES;")
    # fetch all the matching rows
    result = cursor.fetchall()
    # loop through the rows
    print("\n-- DISPLAYING SUPPLY RECORDS --")
    for row in result:
        print("\nSupply ID: {}\nSupply Name: {}\nAmount on Hand: {}".format(row[0], row[1], row[2]))

    # execute your query
    cursor.execute("SELECT * FROM SUPPLY_ORDERS;")
    # fetch all the matching rows
    result = cursor.fetchall()
    # loop through the rows
    print("\n-- DISPLAYING SUPPLY ORDER RECORDS --")
    for row in result:
        print("\nSupply Order Number: {}\nSupplier ID: {}\nSupply ID: {}\nAmount Ordered: {}\nTotal Cost: {}\nSupply Order Date: {}\nSupply Ship Date: {}\nExpected Delivery Date: {}\nActual Delivery Date: {}".format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))

    # execute your query
    cursor.execute("SELECT * FROM SUPPLIER;")
    # fetch all the matching rows
    result = cursor.fetchall()
    # loop through the rows
    print("\n-- DISPLAYING SUPPLIER RECORDS --")
    for row in result:
        print("\nSupplier ID: {}\nSupplier Name: {}".format(row[0], row[1]))

    print("\n\n-- DISPLAYING REPORTS --")
    # Creating a cursor object using the cursor method
    cursor = db.cursor()

    # Executing a SQL query to get the order number, expected delivery date, and the actual delivery date
    cursor.execute(
        "SELECT SUPPLY_ORDER_NUMBER, EXPECTED_DELIVERY_DATE, ACTUAL_DELIVERY_DATE FROM SUPPLY_ORDERS")

    # Storing the results of the query in a variable
    delivery_Dates = cursor.fetchall()

    print("\n-- Expected vs. Actual Delivery Date --")

    # Looping through the results of the query
    for row in delivery_Dates:
        print("Supply Order Number:           {}".format(row[0]))
        print("Expected Delivery Date:        {}".format(row[1]))
        print("Actual Delivery Date:          {}".format(row[2]))
        print("\n")

    # Select the distributor name, wine name, and the amount of wine sold
    cursor.execute('''SELECT DISTRIBUTOR.DISTRIBUTOR_NAME, PRODUCTS.PRODUCT_NAME, DISTRIBUTOR_ORDERS.AMOUNT_BOUGHT 
                   FROM PRODUCTS INNER JOIN DISTRIBUTOR_ORDERS ON PRODUCTS.PRODUCT_ID = DISTRIBUTOR_ORDERS.PRODUCT_ID INNER JOIN 
                   DISTRIBUTOR ON DISTRIBUTOR_ORDERS.DISTRIBUTOR_ID = DISTRIBUTOR.DISTRIBUTOR_ID''')

    # Storing the results of the query in a variable
    wine_sold = cursor.fetchall()

    print("-- Wines Sold --")

    # Looping through the results of the query
    for row in wine_sold:
        print("Distributor:          {}".format(row[0]))
        print("Wine:                 {}".format(row[1]))
        print("Amount Sold:          {}".format(row[2]))
        print("\n")

    # select the employee name and the numbers of hours worked per quarter
    cursor.execute('''SELECT EMPLOYEE.FIRST_NAME, EMPLOYEE.LAST_NAME, HOURS_WORKED.Q1, HOURS_WORKED.Q2, HOURS_WORKED.Q3, HOURS_WORKED.Q4
                   FROM EMPLOYEE INNER JOIN HOURS_WORKED ON EMPLOYEE.EMPLOYEE_ID = HOURS_WORKED.EMPLOYEE_ID''')

    # Storing the results of the query in a variable
    hours_worked = cursor.fetchall()

    print("-- Hours Worked --")

    # Looping through the results of the query
    for row in hours_worked:
        print("Employee:        {}".format(row[0]) + " " + row[1])
        print("Q1:              {}".format(row[2]) + " hours")
        print("Q2:              {}".format(row[3]) + " hours")
        print("Q3:              {}".format(row[4]) + " hours")
        print("Q4:              {}".format(row[5]) + " hours")
        print("\n")


except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("\n Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("\n Database does not exist")
    else:
        print(err)

finally:
    db.commit
    db.close()
    print("\n Database connection closed")