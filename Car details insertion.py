import mysql.connector
from tkinter import *
from Display import Display

mydb = mysql.connector.connect(host="localhost", user="root", password="2510triblaz", db="Car_Rental_Service")
db_cursor = mydb.cursor()

root = Tk()




class Car:
    def __init__(self):
        self.price = None
        self.car_name = None
        self.car_brand = None
        self.car_transmission = None
        self.car_type = None
        self.car_AC = None
        self.fuel_type = None
        self.proceed = None

    def insertion(self):
        Query = "insert into car_details(Car_name, Car_brand, Car_Type, Car_transmission,  " \
                "Car_AC, Fuel_type, Price) values(%s,%s,%s,%s,%s,%s,%s)"
        values = (self.car_name.get(), self.car_brand.get(), self.car_type.get(), self.car_transmission.get(),
                  self.car_AC.get(), self.fuel_type.get(), self.price.get())
        db_cursor.execute(Query, values)
        mydb.commit()

    def frame_build(self):
        frame = Frame(root, bg="#B20600")
        frame.place(x=70, y=350)
        self.car_name = Entry(frame, width=30)
        self.car_name.grid(padx=4, pady=4)
        self.car_name.insert(0, "Car Name")

        self.car_brand = Entry(frame, width=30)
        self.car_brand.grid(row=0, column=2, padx=2, pady=4)
        self.car_brand.insert(0, "Car Brand")

        self.car_type = Entry(frame, width=30)
        self.car_type.grid(row=0, column=3, padx=2, pady=4)
        self.car_type.insert(0, "Car Type")

        self.car_transmission = Entry(frame, width=30)
        self.car_transmission.grid(row=0, column=4, padx=2, pady=4)
        self.car_transmission.insert(0, "Car Transmission")

        self.car_AC = Entry(frame, width=30)
        self.car_AC.grid(row=0, column=5, padx=2, pady=4)
        self.car_AC.insert(0, "AC/Non-AC")

        self.fuel_type = Entry(frame, width=30)
        self.fuel_type.grid(row=0, column=6, padx=2, pady=4)
        self.fuel_type.insert(0, "Fuel type")

        self.price = Entry(frame, width=30)
        self.price.grid(row=0, column=7, padx=2, pady=4)
        self.price.insert(0, "Price/day")

        self.proceed = Button(frame, text="Proceed", command=self.insertion)
        self.proceed.grid(row=0, column=8, padx=2, pady=4)



ins = Car()
ins.frame_build()

Style = Display(root)
Style.Top_frame()
#Style.middle_frame()

root.mainloop()
