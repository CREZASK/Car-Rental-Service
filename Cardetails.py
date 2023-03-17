from tkinter import *
from tkinter import ttk, Button, messagebox
import pymysql
from PIL import Image, ImageTk
from datetime import datetime


class Cardet:
    def __init__(self, root, car_frame, second_frame):
        self.new_canvas = None
        self.third_frame = None
        self.car_frame1 = None
        self.te = None
        self.alldet = None
        self.spec_frame = None
        self.booking_frame = None
        self.Days = None
        self.Ddate = None
        self.Ploc = None
        self.Pdate = None
        self.Dloc = None
        self.image_frame = None
        self.img = None
        self.button_frame = None
        self.second_frame = None
        self.main_frame1 = None
        self.root = root
        self.car_frame = car_frame
        self.second_frame = second_frame

    # Calculating the days of rent
    def Calculate_days(self):
        d1 = datetime.strptime(self.Pdate[0], "%m/%d/%y")
        d2 = datetime.strptime(self.Ddate[0], "%m/%d/%y")
        self.Days = d2 - d1

    def SeeBooking(self):
        mydb = pymysql.connect(
            user="root",
            host="localhost",
            password="2510triblaz",
            database="car_rental_service"
        )
        db_cursor = mydb.cursor()
        TempQpd = "Select Pickup_Date from temp_booking"
        db_cursor.execute(TempQpd)
        self.Pdate = db_cursor.fetchone()
        TempQpl = "Select Pickup_Location from temp_booking"
        db_cursor.execute(TempQpl)
        self.Ploc = db_cursor.fetchone()
        TempQdd = "Select Dropoff_Date from temp_booking"
        db_cursor.execute(TempQdd)
        self.Ddate = db_cursor.fetchone()
        TempQdl = "Select Dropoff_location from temp_booking"
        db_cursor.execute(TempQdl)
        self.Dloc = db_cursor.fetchone()

        self.booking_frame = Frame(self.second_frame, bg='#343434')
        self.booking_frame.place(x=10, y=20)

        # booking info panel on left top corner
        # First Column
        pickup = Label(self.booking_frame, text="Pickup", fg="#F4F4F4", bg='#343434',
                       font='telegrafico 18')
        pickup.grid(row=0, column=0)
        Pllabel = Label(self.booking_frame, text=f"{self.Ploc[0]}", fg="#8C0909", bg='#F4F4F4', width=12, height=5,
                        font='telegrafico 20')
        Pllabel.grid(row=1, column=0, padx=5, pady=5)
        Pickdate = Label(self.booking_frame, text="From", fg="#F4F4F4", bg='#343434',
                         font='telegrafico 18')
        Pickdate.grid(row=2, column=0)
        Pdlabel = Label(self.booking_frame, text=f"{self.Pdate[0]}", fg="#8C0909", bg='#F4F4F4', width=6, height=3,
                        font='telegrafico 24')
        Pdlabel.grid(row=3, column=0, padx=3, pady=3)

        to = Label(self.booking_frame, text='To', fg="#F4F4F4", bg='#343434', font='telegrafico 15')
        to.grid(row=1, column=1)
        to = Label(self.booking_frame, text='To', fg="#F4F4F4", bg='#343434', font='telegrafico 15')
        to.grid(row=3, column=1)
        # Second Column
        pickup = Label(self.booking_frame, text="Dropoff", fg="#F4F4F4", bg='#343434',
                       font='telegrafico 18')
        pickup.grid(row=0, column=2)
        Dllabel = Label(self.booking_frame, text=f"{self.Dloc[0]}", fg="#8C0909", bg='#F4F4F4', width=12, height=5,
                        font='telegrafico 20')
        Dllabel.grid(row=1, column=2, padx=5, pady=5)
        Dropdate = Label(self.booking_frame, text="Until", fg="#F4F4F4", bg='#343434',
                         font='telegrafico 18')
        Dropdate.grid(row=2, column=2)
        Ddlabel = Label(self.booking_frame, text=f"{self.Ddate[0]}", fg="#8C0909", bg='#F4F4F4', width=6, height=3,
                        font='telegrafico 24')
        Ddlabel.grid(row=3, column=2, padx=5, pady=5)
        self.Calculate_days()
        self.te = Frame(self.second_frame, bg='#343434')
        self.te.place(x=10, y=280, width=473, height=100)
        days = Label(self.te, text=f'{self.Days.days}', fg="#F4F4F4", bg='#343434',
                     font='telegrafico 34')
        days.place(x=350, y=28)
        daystext = Label(self.te, text=f'Days of Rent:', fg="#F4F4F4", bg='#343434',
                         font='telegrafico 30')
        daystext.place(x=70, y=30)

    def Car_click(self, j):
        try:
            mydb = pymysql.connect(
                host='localhost',
                user='root',
                password='2510triblaz',
                db='car_rental_service'
            )
        except:
            messagebox.showerror('DB Error', 'DB connectivity issue, please try again later.')
            return
        cursor = mydb.cursor()

        self.new_canvas = Frame(self.root)
        self.new_canvas.place(x=0, y=150, width=1537)
        newlab = Label(self.new_canvas)
        newlab.pack(side=LEFT, pady=295)
        self.car_frame1 = Frame(self.new_canvas)
        self.car_frame1.pack(side=LEFT, fill=BOTH, expand=1)
        car_canvas1 = Canvas(self.car_frame1)
        car_canvas1.pack(side=LEFT, fill=BOTH, expand=1)

        v = ttk.Scrollbar(self.car_frame1, orient=VERTICAL, command=car_canvas1.yview)
        v.pack(side=LEFT, fill=Y)

        car_canvas1.configure(yscrollcommand=v.set)
        car_canvas1.bind('<Configure>', lambda e: car_canvas1.configure(scrollregion=car_canvas1.bbox("all")))

        self.third_frame = Frame(car_canvas1)

        car_canvas1.create_window((0, 0), window=self.third_frame, anchor="nw")

        bill_frame = Frame(self.third_frame)
        bill_frame.pack()

        bill_label = Label(bill_frame, height=65, width=250)
        bill_label.pack()

        if len(self.Ploc[0]) > 20:
            x = self.Ploc[0][:19]
            y = self.Ploc[0][19:]
            Pllabel = Label(bill_frame, text=f"{x}\n{y}", fg="#8C0909", font='telegrafico 20', justify=LEFT)
            Pllabel.place(x=780, y=140)
        else:
            Pllabel = Label(bill_frame, text=f"{self.Ploc[0]}", fg="#8C0909", font='telegrafico 20')
            Pllabel.place(x=780, y=140)

        Pickdate = Label(bill_frame, text="Booked", fg="black", font='telegrafico 24')
        Pickdate.place(x=650, y=100)
        Pickdate = Label(bill_frame, text="Pickup:\nFrom", fg="#343434", font='telegrafico 20', justify=LEFT)
        Pickdate.place(x=650, y=140)
        Pickdate = Label(bill_frame, text="On:", fg="#343434", font='telegrafico 20')
        Pickdate.place(x=650, y=190)
        Pdlabel = Label(bill_frame, text=f"{self.Pdate[0]}", fg="#8C0909", font=('Arial bold', 15))
        Pdlabel.place(x=780, y=190)

        if len(self.Dloc[0]) > 20:
            a = self.Dloc[0][:19]
            b = self.Dloc[0][19:]
            Dllabel = Label(bill_frame, text=f"{a}\n{b}", fg="#8C0909", font='telegrafico 20')
            Dllabel.place(x=780, y=280)
        else:
            Dllabel = Label(bill_frame, text=f"{self.Dloc[0]}", fg="#8C0909", font='telegrafico 20')
            Dllabel.place(x=780, y=280)
        Pickdate = Label(bill_frame, text="Booked", fg="black", font='telegrafico 24')
        Pickdate.place(x=650, y=250)
        Pickdate = Label(bill_frame, text="Dropoff:\nAt", fg="#343434", font='telegrafico 20', justify=LEFT)
        Pickdate.place(x=650, y=280)
        Pickdate = Label(bill_frame, text="On:", fg="#343434", font='telegrafico 20')
        Pickdate.place(x=650, y=330)
        Ddlabel = Label(bill_frame, text=f"{self.Ddate[0]}", fg="#8C0909", font=('Arial bold', 15))
        Ddlabel.place(x=780, y=330)

        Confirm = Button(bill_frame, text='Confirm', font='telegrafico 18', foreground='#F3EFE0',
                         command=self.confirm, background='#850000', relief=FLAT)
        Confirm.place(x=1260, y=400)

        back = Button(bill_frame, text='Go Back', font='telegrafico 18', foreground='#F3EFE0',
                      command=lambda: self.back(self.car_frame1), background='#850000', relief=FLAT)
        back.place(x=1180, y=450)

        Pickdate = Label(bill_frame, text="Incase you need a different Car", fg="#343434", font='telegrafico 11')
        Pickdate.place(x=1115, y=490)

        Cancel = Button(bill_frame, text='Cancel', font='telegrafico 18', foreground='white',
                        command=self.cancel, background='#343434', relief=FLAT)
        Cancel.place(x=1100, y=400)

        carimages = []
        global carimg
        img = Image.open(self.alldet[j][7])
        resize = img.resize((500, 350))
        carimg = ImageTk.PhotoImage(resize)
        carpic = Text(bill_frame, width=60, height=20, relief=FLAT, bg='#850000')
        carpic.place(x=100, y=90)
        carpic.image_create(INSERT, image=carimg)
        carpic.image = imgm
        carimages.append(imgm)

        labelcar = Label(bill_frame, text=f"{self.alldet[j][1]} {self.alldet[j][0]}", fg='black',
                         font='telegrafico 34')
        labelcar.place(x=100, y=420)

        Bill = Frame(bill_frame)
        Bill.place(x=1100, y=60)
        billlabel = Label(Bill, text='BILL', font='telegrafico 28')
        billlabel.pack(pady=20)

        # Price Calculation
        p = int(self.alldet[j][6])
        Price4d = p * self.Days.days
        GST = Price4d * 0.18
        Total = Price4d + GST

        Price = Label(Bill, text=f'Price/day:          \t   ₹{self.alldet[j][6]}/-', font='telegrafico 14',
                      justify=LEFT)
        Price.pack(pady=20)
        Price = Label(bill_frame, text=f'Price for {self.Days.days} days:             ₹{Price4d}/-',
                      font='telegrafico 14', justify=LEFT)
        Price.place(x=1100, y=200)
        Price = Label(bill_frame, text=f'GST(18%):CGST(9%)\n\t   SGST(9%):             ₹{GST}/-',
                      font='telegrafico 14', justify=LEFT)
        Price.place(x=1100, y=250)
        Price = Label(bill_frame, text=f'Total:       \t\t    ₹{Total}/-',
                      font='telegrafico 14', justify=LEFT)
        Price.place(x=1100, y=320)
        line = Frame(bill_frame, bg='red', height=2, width=280)
        line.place(x=1100, y=130)
        line = Frame(bill_frame, bg='red', height=2, width=280)
        line.place(x=1100, y=290)

        # Specifications
        specq = f'select * from specifications where Car_name="{self.alldet[j][0]}"'
        cursor.execute(specq)
        car_specs = cursor.fetchone()
        car_specs = list(car_specs)

        self.spec_frame = Frame(bill_frame, bg="#CACACA")
        self.spec_frame.place(x=100, y=470, height=400, width=485)

        line = Frame(self.spec_frame, bg='black', height=2, width=450)
        line.place(x=20, y=35)
        specifications = Label(self.spec_frame, text='Specifications', font='telegrafico 20', fg="#8C0909",
                               bg="#CACACA",
                               justify=LEFT)
        specifications.place(x=20, y=40)
        line = Frame(self.spec_frame, bg='black', height=2, width=450)
        line.place(x=20, y=70)

        specifications = Label(self.spec_frame, text=f'Type :{car_specs[1]}', font='telegrafico 14', fg="#414141",
                               bg="#CACACA",
                               justify=LEFT)
        specifications.place(x=20, y=100)
        specifications = Label(self.spec_frame, text=f'Colour:{car_specs[2]}', font='telegrafico 14', fg="#414141",
                               bg="#CACACA",
                               justify=LEFT)
        specifications.place(x=20, y=130)
        specifications = Label(self.spec_frame, text=f'Transmission:{car_specs[3]}', font='telegrafico 14', fg="#414141",
                               bg="#CACACA",
                               justify=LEFT)
        specifications.place(x=20, y=160)
        specifications = Label(self.spec_frame, text=f'Fuel Type:{car_specs[4]}', font='telegrafico 14', fg="#414141",
                               bg="#CACACA",
                               justify=LEFT)
        specifications.place(x=20, y=190)
        specifications = Label(self.spec_frame, text=f'Mileage:{car_specs[5]}', font='telegrafico 14', fg="#414141",
                               bg="#CACACA",
                               justify=LEFT)
        specifications.place(x=20, y=220)

        specifications = Label(self.spec_frame, text=f'Seats:{car_specs[6]}', font='telegrafico 14', fg="#414141",
                               bg="#CACACA",
                               justify=LEFT)
        specifications.place(x=20, y=250)
        specifications = Label(self.spec_frame, text=f'AC:{car_specs[7]}', font='telegrafico 14', fg="#414141",
                               bg="#CACACA",
                               justify=LEFT)
        specifications.place(x=20, y=280)
        specifications = Label(self.spec_frame, text=f'Infotainment:{car_specs[8]}', font='telegrafico 14', fg="#414141",
                               bg="#CACACA",
                               justify=LEFT)
        specifications.place(x=20, y=310)
        specifications = Label(self.spec_frame, text=f'Fog Lamps:{car_specs[9]}', font='telegrafico 14', fg="#414141",
                               bg="#CACACA",
                               justify=LEFT)
        specifications.place(x=20, y=340)

        username = 'select * from login'
        cursor.execute(username)
        user = cursor.fetchone()
        q = f"update temp_booking set Car_name=%s, Cost=%s where Username=%s"
        cursor.execute(q, (f'{self.alldet[j][0]}', f'{Total}', f'{user[0]}'))
        mydb.commit()


        # instruction_panel
        instruction = Label(bill_frame, text='Instructions to User', font=('telegrafico', 34),
                            fg="#8C0909")
        instruction.place(x=650, y=540)
        line = Frame(bill_frame, bg='black', height=2, width=800)
        line.place(x=650, y=580)
        text = Label(bill_frame, text="Clicking on confirm will redirect you to a new page where you must "
                                      "choose a suitable payment method. Within 20", font=('Times new roman', 13))
        text.place(x=650, y=600)
        text = Label(bill_frame, text="minutes of payment you will receive a call from one of our "
                                      "employees. During which you may choose to have the ",
                     font=('Times new roman', 13))
        text.place(x=650, y=630)
        text = Label(bill_frame, text="car delivered or pick it up yourself. ",
                     font=('Times new roman', 13))
        text.place(x=650, y=660)
        text = Label(bill_frame, text="If you had chosen the offline payment method, you may pay the cash "
                                      "either during the delivery of the car of your",
                     font=('Times new roman', 13))
        text.place(x=650, y=700)
        text = Label(bill_frame, text="choice or when you come to pick it up.",
                     font=('Times new roman', 13))
        text.place(x=650, y=730)
        text = Label(bill_frame, text="In Case of any emergencies during your travels you may contact us through "
                                      "the Helpline number or the phone number", font=('Times new roman', 13))
        text.place(x=650, y=770)
        text = Label(bill_frame, text="that is provided in the website. Please be free to reach out as we will be "
                                      "available 24/7 at your service.",
                     font=('Times new roman', 13))
        text.place(x=650, y=800)
        text = Label(bill_frame, text="For additional information you may reach out through the E-mail, phone or "
                                      "visit us directly at the address provided.",
                     font=('Times new roman', 13))
        text.place(x=650, y=830)

    def front(self):
        self.carbutton()
        self.SeeBooking()

    def carbutton(self):
        try:
            mydb = pymysql.connect(
                host='localhost',
                user='root',
                password='2510triblaz',
                db='car_rental_service'
            )
        except:
            messagebox.showerror('DB Error', 'DB connectivity issue, please try again later.')
            return
        cursor = mydb.cursor()

        self.button_frame = Frame(self.second_frame)
        self.button_frame.pack(padx=590)

        query = 'select * from car_details'
        cursor.execute(query)
        self.alldet = cursor.fetchall()
        self.alldet = list(self.alldet)
        for i in range(len(self.alldet)):
            self.alldet[i] = list(self.alldet[i])

        carimages = []
        for j in range(len(self.alldet)):
            carframe = Frame(self.button_frame, bg='#850000')
            carframe.pack()
            car_button = Button(carframe, height=12, width=150, relief=FLAT, bg='#F4F4F4', activebackground='#F4F4F4',
                                command=lambda j=j: self.Car_click(j))
            car_button.pack(pady=1)
            Label(carframe,
                  text=f"{self.alldet[j][1]}\n{self.alldet[j][0]}", bg='#F4F4F4',
                  foreground='#810000', font="telegrafico 28", justify=LEFT,
                  relief=FLAT).place(x=350, y=40)
            Label(carframe,
                  text=f"Type: {self.alldet[j][2]}\n\nTransmission: {self.alldet[j][3]}\n\nFuel: "
                       f"{self.alldet[j][5]}\n\n{self.alldet[j][4]}",
                  foreground='#434242', font="telegrafico 14", width=25, bg='#F4F4F4',
                  relief=FLAT, justify=LEFT).place(x=640, y=40)
            Label(carframe,
                  text=f"Price: {self.alldet[j][6]}/day",
                  foreground='#03002C', font="telegrafico 20", width=15, bg='#F4F4F4',
                  relief=FLAT, justify=LEFT).place(x=320, y=120)

            global imgm
            img = Image.open(self.alldet[j][7])
            resize = img.resize((300, 200))
            imgm = ImageTk.PhotoImage(resize)
            carpic = Text(carframe, width=37, relief=FLAT, bg='#850000')
            carpic.place(x=0, y=0)
            carpic.image_create(INSERT, image=imgm)
            carpic.image = imgm
            carimages.append(imgm)

    @staticmethod
    def confirm():
        try:
            mydb = pymysql.connect(
                host='localhost',
                user='root',
                password='2510triblaz',
                db='car_rental_service'
            )
        except:
            messagebox.showerror('DB Error', 'DB connectivity issue, please try again later.')
            return
        cursor = mydb.cursor()
        try:
            q = 'select * from temp_booking'
            cursor.execute(q)
            row = cursor.fetchone()

            # Insert into the main Booking table
            Query = "insert into booking_details(Month_of_Booking, Date_of_Booking, Time_of_Booking, " \
                    "Pickup_Date, Pickup_Location, Dropoff_Date, Dropoff_location, Username, Car_name, Cost) " \
                    "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(Query, row)

            # Empty the temporary table
            delete = 'delete from temp_booking'
            cursor.execute(delete)

            mydb.commit()
            mydb.close()
            messagebox.showinfo('Success', 'Your Wagen is En Route')

        except:
            messagebox.showerror('Booking Error', 'You have cancelled your booking already, please return Home to '
                                                  'restart the process')

    def back(self, car_frame1):
        try:
            mydb = pymysql.connect(
                host='localhost',
                user='root',
                password='2510triblaz',
                db='car_rental_service'
            )
        except:
            messagebox.showerror('DB Error', 'DB connectivity issue, please try again later.')
            return
        cursor = mydb.cursor()
        q = 'select * from temp_booking'
        cursor.execute(q)
        row = cursor.fetchone()
        if row is None:
            messagebox.showerror('Booking Error', 'You have cancelled your booking already, please return Home to '
                                                  'restart the process')
        else:
            self.new_canvas.destroy()

    @staticmethod
    def cancel():
        try:
            mydb = pymysql.connect(
                host='localhost',
                user='root',
                password='2510triblaz',
                db='car_rental_service'
            )
        except:
            messagebox.showerror('DB Error', 'DB connectivity issue, please try again later.')
            return
        cursor = mydb.cursor()
        delete = 'delete from temp_booking'
        cursor.execute(delete)

        mydb.commit()
        mydb.close()
