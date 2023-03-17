import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="2510triblaz", db="Car_Rental_Service")
db_cursor = mydb.cursor()
# db_cursor.execute("CREATE table Car_Details(Car_ID int AUTO_INCREMENT primary key, Car_name varchar(30),  "
#                   "Car_brand varchar(20), Car_Type varchar(20), Car_transmission varchar(40), Car_AC varchar(20))")
# db_cursor.execute("CREATE table Customer_Details(Customer_ID int AUTO_INCREMENT primary key, "
#                   "Customer_name varchar(30), Username varchar(20), Customer_phone varchar(10), "
#                   "Customer_EMail varchar(30), Customer_Address varchar(40), Customer_Password varchar(20))")
# db_cursor.execute("CREATE table Employee_Details(Employee_ID int AUTO_INCREMENT primary key,  "
#                   "Employee_name varchar(30), Employee_phone varchar(10),"
#                   "Employee_EMail varchar(30), Employee_Address varchar(40), Employee_Password varchar(20))")
# db_cursor.execute("CREATE table Booking_Details(Booking_ID int AUTO_INCREMENT primary key, "
#                   "Month_of_Booking varchar(12), Date_of_Booking varchar(30), Time_of_Booking varchar(15), "
#                   "Pickup_Date varchar(10), Pickup_Location varchar(50), Dropoff_Date varchar(10),"
#                   " Dropoff_location varchar(50), Username varchar(30), Car_name varchar(20), Cost varchar(20))")
# db_cursor.execute("Create table Login(Username varchar(20), Password varchar(20))")
# db_cursor.execute(
#     "CREATE table temp_Booking(Month_of_Booking varchar(12), Date_of_Booking varchar(30), Time_of_Booking varchar(15), "
#     "Pickup_Date varchar(10), Pickup_Location varchar(50), Dropoff_Date varchar(10), Dropoff_location varchar(50)"
#     ", Username varchar(30), Car_name varchar(20), Cost varchar(20))")
# db_cursor.execute("create table locations(Current_Location varchar(50), PD_locations varchar(50))")

db_cursor.execute("create table specifications(Car_name varchar(20), type varchar(15), colour varchar(30), "
                  "transmission varchar(30), fuel varchar(30), mileage varchar(30), seats varchar(30)"
                  ", ac varchar(30), infotainment varchar(30), foglamps varchar(30))")

mydb.close()
