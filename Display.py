from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector
from datetime import datetime
from tkcalendar import Calendar
from PIL import ImageTk, Image
import pymysql

today = datetime.now()  # date and time
month1 = today.strftime("%B")  # month in words


def hide(logineyeimage, loginpasswordentry, logineyebutton):
    logineyeimage.config(file='Resources/closeye.png')
    loginpasswordentry.config(show='*')
    logineyebutton.config(command=lambda: show(logineyeimage, loginpasswordentry, logineyebutton))


def show(logineyeimage, loginpasswordentry, logineyebutton):
    logineyeimage.config(file='Resources/openeye.png')
    loginpasswordentry.config(show="")
    logineyebutton.config(command=lambda: hide(logineyeimage, loginpasswordentry, logineyebutton))


class Display:
    def __init__(self, root):
        self.second_frame = None
        self.frame2 = None
        self.properloc2 = None
        self.loc_list2 = None
        self.loc_list = None
        self.properloc = None
        self.main_loc = None
        self.locate = None
        self.v = None
        self.current = None
        self.proceed = None
        self.near = None
        self.pick = None
        self.drop = None
        self.pick_date = None
        self.drop_date = None
        self.root = root
        self.pdate = None
        self.ddate = None
        self.frame = None
        self.cal = None
        self.frame1 = None
        self.registerFrame = None
        self.logineyeButton = None
        self.logineyeImage = None
        self.signupPasswordEntry = None
        self.signupAddressEntry = None
        self.signupPhoneEntry = None
        self.signupEmailEntry = None
        self.signupnameEntry = None
        self.signupUsernameEntry = None
        self.signupConfirmEntry = None
        self.resetFrame = None
        self.resetConfirmEntry = None
        self.resetPasswordEntry = None
        self.resetUsernameEntry = None
        self.signinFrame = None
        self.loginUsernameEntry = None
        self.loginPasswordEntry = None
        self.window = None

    @staticmethod
    def edit_details(name, email, address, phone):
        mydb = mysql.connector.connect(host="localhost", user="root", password="root", db="Car_Rental_Service")
        db_cursor = mydb.cursor()
        q = "select Username from login"
        fetch = []
        db_cursor.execute(q)
        loginuser = db_cursor.fetchall()
        for i in loginuser:
            for j in i:
                fetch.append(j)
        for h in fetch:
            print(type(h))
            Queryuser = f'Update customer_details set Customer_name="{name}" where Username="{h}"'
            db_cursor.execute(Queryuser)
            Queryemail = f'Update customer_details set Customer_EMail="{email}" where Username="{h}"'
            db_cursor.execute(Queryemail)
            Queryaddress = f'Update customer_details set Customer_Address="{address}" where Username="{h}"'
            db_cursor.execute(Queryaddress)
            Queryphone = f'Update customer_details set Customer_phone="{phone}" where Username="{h}"'
            db_cursor.execute(Queryphone)
            mydb.commit()
            mydb.close()

    def Top_frame(self, second_frame):
        Company_name = Canvas(second_frame, width=1920, height=600, highlightthickness=0)
        Company_name.pack()

        global bg
        bg = ImageTk.PhotoImage(file="Resources/Trial.png")
        Company_name.pack(fill="both", expand=True)
        Company_name.create_image(0, 0, image=bg, anchor="nw")
        Company_name.image = bg

    @staticmethod
    def middle_frame(second_frame):
        midframe = Frame(second_frame, height=1600)
        midframe.pack(fill=BOTH, expand=1)

        global image
        img = Image.open("Resources/24-7company-service.png")
        resize = img.resize((800, 200))
        image = ImageTk.PhotoImage(resize)
        img_label = Label(midframe, image=image)
        img_label.place(x=150, y=150)
        text = Label(midframe, text="Do you need help?\nWe are there for you 24/7.",
                     font=('Times new roman', 23))
        text.place(x=1000, y=210)

        global image1
        img = Image.open("Resources/car-cleaning-covid-1.png")
        resize = img.resize((466, 313))
        image1 = ImageTk.PhotoImage(resize)
        img_label = Label(midframe, image=image1)
        img_label.place(x=700, y=470)
        text = Label(midframe, text="Every car goes through\nchecks and sanitation\nbefore it reaches you.",
                     font=('Times new roman', 23))
        text.place(x=300, y=530)

        global image3
        img = Image.open("Resources/Tata-Safari-White-Gold-Side.png")
        resize = img.resize((1300, 850))
        image3 = ImageTk.PhotoImage(resize)
        img_label = Label(midframe, image=image3, height=1000)
        img_label.place(x=-250, y=800)
        text = Label(midframe, text="Our cars are always in Top\ncondition.\nRent it and experience it yourself",
                     font=('Times new roman', 23))
        text.place(x=1060, y=1250)

    def get_pdate(self, up):
        self.pick_date.delete(0, END)
        self.pick_date.insert(0, self.cal.get_date())
        self.frame1.destroy()
        up.destroy()

    def get_ddate(self, up):
        self.drop_date.delete(0, END)
        self.drop_date.insert(0, self.cal.get_date())
        self.frame2.destroy()
        up.destroy()

    def pdate_pick(self):
        self.frame1 = Frame(self.root, background='#B20600')
        self.frame1.place(x=550, y=377)
        self.cal = Calendar(self.frame1)
        self.cal.grid(row=1, column=4, columnspan=2)
        cal_button = Button(self.frame1, text="Select", height=11, command=lambda: self.get_pdate(up1), bg="#B20600",
                            fg="#F3EFE0", relief=FLAT)
        cal_button.grid(row=1, column=0)
        up1 = Button(self.frame, text="^", command=lambda: self.up4(up1), relief=FLAT)
        up1.place(x=685, y=6, height=21)

    def ddate_pick(self):
        self.frame2 = Frame(self.root, background='#B20600')
        self.frame2.place(x=1232, y=377)
        self.cal = Calendar(self.frame2)
        self.cal.grid(row=1, column=4, columnspan=2)
        cal_button = Button(self.frame2, text="Select", height=11, command=lambda: self.get_ddate(up1), bg="#B20600",
                            fg="#F3EFE0", relief=FLAT)
        cal_button.grid(row=1, column=0)
        up1 = Button(self.frame, text="^", command=lambda: self.up5(up1), relief=FLAT)
        up1.place(x=1138, y=6, height=21)

    def insertion(self):
        if self.pick_date.get() == '' or self.pick.get() == '' or self.drop_date.get() == '' or self.drop.get() == '':
            messagebox.showwarning('Entry Error', 'All fields are required')
        elif self.pick_date.get() == 'Pickup Date' or self.pick.get() == 'Pickup Location':
            messagebox.showwarning('Entry Error', 'All fields are required')
        elif self.drop_date.get() == 'Dropoff Date' or self.drop.get() == 'Dropoff Location':
            messagebox.showwarning('Entry Error', 'All fields are required')
        elif self.current.get() == 'Thiruvananthapuram' or self.current.get() == 'Kollam' \
                or self.current.get() == 'Kochi' or self.current.get() == 'Kozhikode' \
                or self.current.get() == 'Kannur' or self.current.get() == 'Alapuzha':
            try:
                con = pymysql.connect(
                    user="root",
                    password="root",
                    host="localhost",
                    database='car_rental_service'
                )
                cursor = con.cursor()
            except:
                messagebox.showerror('DB Error', 'DB connectivity issue, please try again later.')
                return
            query = 'select * from login'
            cursor.execute(query)
            row = cursor.fetchone()
            if row is None:
                messagebox.showerror('Login Error', 'Not logged in yet')
            else:
                Query = "insert into temp_booking(Month_of_Booking, Date_of_Booking, Time_of_Booking, " \
                        "Pickup_Date, Pickup_Location, Dropoff_Date, Dropoff_location, Username) " \
                        "values(%s,%s,%s,%s,%s,%s,%s,%s)"
                values = (
                    month1, today.date(), today.time(), self.pick_date.get(), self.pick.get(), self.drop_date.get(),
                    self.drop.get(), row[0])
                cursor.execute(Query, values)
                con.commit()
                con.close()
        else:
            messagebox.showwarning('Entry Error', 'Unfortunately we do not have service here')

    def currentclick(self, *args):
        if self.current.get() == "Current Location":
            self.current.delete(0, END)

    def pickupclick(self, *args):
        if self.pick.get() == "Pickup Location":
            self.pick.delete(0, END)

    def dropoffclick(self, *args):
        if self.drop.get() == "Dropoff Location":
            self.drop.delete(0, END)

    def select_pickup(self):
        if self.current.get() == "Thiruvananthapuram" or self.current.get() == 'Kollam' \
                or self.current.get() == 'Kochi' or self.current.get() == 'Alapuzha' \
                or self.current.get() == 'Kozhikode' or self.current.get() == 'Kannur':
            try:
                mydb = pymysql.connect(
                    host='localhost',
                    user='root',
                    password='root',
                    db='car_rental_service'
                )
            except:
                messagebox.showerror('DB Error', 'DB connectivity issue, please try again later.')
                return
            cursor = mydb.cursor()
            # pickup selection
            pQuery = f'select PD_locations from locations where Current_Location="{self.current.get()}"'
            cursor.execute(pQuery)
            up1 = Button(self.frame, text="^", command=lambda: self.up2(up1), relief=FLAT)
            up1.place(x=477, y=6, height=21)
            location_list = cursor.fetchall()
            self.properloc = Frame(self.root)
            self.properloc.place(x=380, y=377)
            main_label = Label(self.properloc, text='Select location', font='telegrafico 16', bg='#B20600',
                               foreground='white', width=32,
                               height=3)
            main_label.pack()
            self.loc_list = []
            for i in location_list:
                for j in i:
                    self.loc_list.append(j)

            for h in range(len(self.loc_list)):
                loc = Button(self.properloc, text=f'{self.loc_list[h]}', width=36, height=2, relief=FLAT,
                             font="telegrafico 14",
                             command=lambda h=h: self.properpick_click(h, up1))
                loc.pack()
        else:
            messagebox.showwarning('Entry Error', 'Please select a City')

    def select_dropoff(self):
        if self.current.get() == "Thiruvananthapuram" or self.current.get() == 'Kollam' \
                or self.current.get() == 'Kochi' or self.current.get() == 'Alapuzha' \
                or self.current.get() == 'Kozhikode' or self.current.get() == 'Kannur':
            try:
                mydb = pymysql.connect(
                    host='localhost',
                    user='root',
                    password='root',
                    db='car_rental_service'
                )
            except:
                messagebox.showerror('DB Error', 'DB connectivity issue, please try again later.')
                return
            cursor = mydb.cursor()
            # pickup selection
            pQuery = f'select PD_locations from locations'
            cursor.execute(pQuery)
            up1 = Button(self.frame, text="^", command=lambda: self.up3(up1), relief=FLAT)
            up1.place(x=931, y=6, height=21)
            location_list = cursor.fetchall()
            self.properloc2 = Frame(self.root)
            self.properloc2.place(x=605, y=10)

            main_label = Label(self.properloc2, text='Select location', font='telegrafico 16', bg='#B20600',
                               foreground='white', width=35,
                               height=3)
            main_label.pack()
            self.loc_list2 = []
            for i in location_list:
                for j in i:
                    self.loc_list2.append(j)
            for h in range(len(self.loc_list2)):
                loc = Button(self.properloc2, text=f'{self.loc_list2[h]}', width=40, height=2, relief=FLAT,
                             font="telegrafico 12",
                             command=lambda h=h: self.properdrop_click(h, up1))
                loc.pack()
        else:
            messagebox.showwarning('Entry Error', 'Please select a City')

    def properpick_click(self, i, up):
        self.pick.delete(0, END)
        self.pick.insert(0, self.loc_list[i])
        up.destroy()
        self.properloc.destroy()

    def properdrop_click(self, i, up):
        self.drop.delete(0, END)
        self.drop.insert(0, self.loc_list2[i])
        up.destroy()
        self.properloc2.destroy()

    def pick_current(self):
        up1 = Button(self.frame, text="^", command=lambda: self.up(up1), relief=FLAT)
        up1.place(x=230, y=6, height=21)
        self.main_loc = ["Thiruvananthapuram", "Kollam", "Kozhikode", "Kannur", "Kochi", "Alapuzha"]
        self.locate = Frame(self.root, bg='#B20600')
        self.locate.place(x=135, y=377)
        main_label = Label(self.locate, text='Select City', font='telegrafico 16', bg='#B20600', foreground='white',
                           height=3)
        main_label.pack()

        for i in range(len(self.main_loc)):
            loc = Button(self.locate, text=f'{self.main_loc[i]}', width=21, height=2, relief=FLAT,
                         font="telegrafico 14",
                         command=lambda i=i: self.current_click(i, up1))
            # Using the i=i trick causes your function to store the current value of i at the time your lambda is defined
            loc.pack()

    def up(self, up1):
        self.locate.destroy()
        up1.destroy()

    def up2(self, up1):
        self.properloc.destroy()
        up1.destroy()

    def up3(self, up1):
        self.properloc2.destroy()
        up1.destroy()

    def up4(self, up1):
        self.frame1.destroy()
        up1.destroy()

    def up5(self, up1):
        self.frame2.destroy()
        up1.destroy()

    def current_click(self, i, up):
        self.current.delete(0, END)
        self.current.insert(0, self.main_loc[i])
        up.destroy()
        self.locate.destroy()

    def frame_build(self, second_frame):
        self.frame = Frame(second_frame, bg="#B20600")
        self.frame.place(x=130, y=350)

        self.current = Entry(self.frame, width=24, font='Telegrafico 18')
        self.current.grid(row=0, column=0, padx=4, pady=4)
        self.current.insert(0, "Current Location")
        self.current.bind('<Button-1>', self.currentclick)

        self.v = Button(self.frame, text="V", command=self.pick_current, relief=FLAT)
        self.v.place(x=230, y=6, height=21)

        self.pick = Entry(self.frame, width=24, font='Telegrafico 18')
        self.pick.grid(row=0, column=2, pady=4)
        self.pick.insert(0, "Pickup Location")
        self.pick.bind('<Button-1>', self.pickupclick)

        self.v = Button(self.frame, text="V", command=self.select_pickup, relief=FLAT)
        self.v.place(x=477, y=6, height=21)

        self.pick_date = Entry(self.frame, width=20, font='Telegrafico 18')
        self.pick_date.grid(row=0, column=3, padx=2, pady=4)
        self.pick_date.insert(0, "Pickup Date")

        self.v = Button(self.frame, text="V", command=self.pdate_pick, relief=FLAT)
        self.v.place(x=685, y=6, height=21)

        self.drop = Entry(self.frame, width=24, font='Telegrafico 18')
        self.drop.grid(row=0, column=5, padx=2, pady=4)
        self.drop.insert(0, "Dropoff Location")
        self.drop.bind('<Button-1>', self.dropoffclick)

        self.v = Button(self.frame, text="V", command=self.select_dropoff, relief=FLAT)
        self.v.place(x=931, y=6, height=21)

        self.drop_date = Entry(self.frame, width=20, font='Telegrafico 18')
        self.drop_date.grid(row=0, column=6, pady=4)
        self.drop_date.insert(0, "Dropoff Date")

        self.v = Button(self.frame, text="V", command=self.ddate_pick, relief=FLAT)
        self.v.place(x=1138, y=6, height=21)

        self.proceed = Button(self.frame, text="Confirm", command=self.insertion)
        self.proceed.grid(row=0, column=8, padx=3, pady=4)

        label = Label(second_frame, text="Car For Hire - Don't Commit", font="Telegrafico 30 bold")
        label.place(x=130, y=300)

    def back(self):
        self.signinFrame.tkraise()

    def change_password(self):
        if self.resetUsernameEntry.get() == '' or self.resetPasswordEntry.get() == '' or \
                self.resetConfirmEntry.get() == '':
            messagebox.showerror('Incomplete Fields', 'All fields are required.')
        elif self.resetPasswordEntry.get() != self.resetConfirmEntry.get():
            messagebox.showerror('Password Mismatch', 'Password and confirmation mismatch.')
        else:
            con = pymysql.connect(
                user="root",
                password="root",
                host="localhost", database='car_rental_service'
            )
            cursor = con.cursor()
            query = 'select * from Customer_details where Username=%s'
            cursor.execute(query, (self.resetUsernameEntry.get()))
            row = cursor.fetchone()
            if row is None:
                messagebox.showerror('Reset Failed', 'Reset failed, incorrect username.')
            else:
                query = 'update Customer_details set Customer_Password=%s where Username=%s'
                cursor.execute(query, (self.resetPasswordEntry.get(), self.resetUsernameEntry.get()))
                con.commit()
                con.close()
                messagebox.showinfo('Done!', f'Password for {self.resetUsernameEntry.get()}'f' was reset successfully')
                self.signinFrame.tkraise()

    def forgot_password(self, window):
        self.resetpage(window)

    def register_page(self, window):
        self.registerpage(window)

    def login_user(self, window):
        if self.loginUsernameEntry.get() == '' or self.loginPasswordEntry.get() == '':
            messagebox.showerror('Error', 'All field are required.')
        else:
            try:
                con = pymysql.connect(
                    user="root",
                    password="root",
                    host="localhost",
                    database='car_rental_service'
                )
                cursor = con.cursor()
            except:
                messagebox.showerror('DB Error', 'DB connectivity issue, please try again later.')
                return
            query = 'select * from Customer_details where Username=%s and Customer_Password=%s'
            cursor.execute(query, (self.loginUsernameEntry.get(), self.loginPasswordEntry.get()))
            row = cursor.fetchone()
            if row is None:
                messagebox.showerror('Login Error', 'Invalid Credentials.')
            else:
                query = 'select * from login'
                cursor.execute(query)
                row2 = cursor.fetchone()
                if row2 is not None:
                    messagebox.showerror('Login Error', 'Already Logged in.')
                    window.destroy()
                else:
                    messagebox.showinfo('Welcome', 'Successfully logged in to the server!')
                    ins = 'insert into login(Username, Password) values(%s, %s)'
                    values = (self.loginUsernameEntry.get(), self.loginPasswordEntry.get())
                    cursor.execute(ins, values)
                    con.commit()
                    con.close()
                    window.destroy()

    def clear_signup(self):
        self.signupEmailEntry.delete(0, END)
        self.signupUsernameEntry.delete(0, END)
        self.signupPasswordEntry.delete(0, END)
        self.signupConfirmEntry.delete(0, END)

    def save_db(self):
        if self.signupEmailEntry.get() == '' or self.signupUsernameEntry.get() == '' or self.signupPasswordEntry.get() \
                == '' or self.signupConfirmEntry.get() == '':
            messagebox.showerror('Error', 'All fields are required!')
        elif self.signupPasswordEntry.get() != self.signupConfirmEntry.get():
            messagebox.showerror('Password Mismatch', 'Your passwords don\'t match!')
        else:
            try:
                con = pymysql.connect(
                    user="root",
                    password="root",
                    host="localhost"
                )
                cursor = con.cursor()
            except:
                messagebox.showerror('DB ERROR', 'DB connectivity issue, please try again later.')
                return

            try:
                query = "create database car_rental_service"
                cursor.execute(query)
            except:
                try:
                    cursor.execute('use car_rental_service')
                    query = "CREATE table Customer_Details(Customer_ID int AUTO_INCREMENT primary key, " \
                            "Customer_name varchar(30), Username varchar(20), Customer_phone varchar(20), " \
                            "Customer_EMail varchar(30), Customer_Address varchar(40), Customer_Password varchar(20))"
                    cursor.execute(query)
                except:
                    try:
                        cursor.execute('use car_rental_service')

                        query = 'select * from Customer_details where Username=%s'
                        cursor.execute(query, (self.signupUsernameEntry.get()))

                        row = cursor.fetchone()
                        if row is not None:
                            messagebox.showerror('Duplicate Username', 'Username already exists. Try something else.')
                        else:
                            query = 'insert into Customer_Details(Customer_name, Username, Customer_phone,  ' \
                                    'Customer_EMail, Customer_Address, Customer_Password) values (%s,%s,%s,%s,%s,%s)'
                            cursor.execute(query,
                                           (self.signupnameEntry.get(), self.signupUsernameEntry.get(),
                                            self.signupPhoneEntry.get(),
                                            self.signupEmailEntry.get(), self.signupAddressEntry.get(),
                                            self.signupPasswordEntry.get()))
                            con.commit()
                            con.close()
                            messagebox.showinfo('Done!', 'Registration successful')
                            self.clear_signup()
                            self.signinFrame.tkraise()
                    except:
                        messagebox.showerror('DB ERROR', 'DB connectivity issue, please try again later.')
                        return

    def usernameClick(self, *args):
        if self.loginUsernameEntry.get() == "Username":
            self.loginUsernameEntry.delete(0, 'end')

    def passwordClick(self, *args):
        if self.loginPasswordEntry.get() == "Password":
            self.loginPasswordEntry.delete(0, END)

    def Login_profile(self, window):
        self.signinFrame = Frame(window, height=window.winfo_screenheight(),
                                 width=window.winfo_screenwidth())
        self.signinFrame.place(x=0, y=0)

        global bgPhoto
        bgPhoto = ImageTk.PhotoImage(file="Resources/bg2.png", master=self.signinFrame)
        bgLabel = Label(self.signinFrame, image=bgPhoto)
        bgLabel.place(x=0, y=0)

        loginHeading = Label(self.signinFrame, text='USER LOGIN', font=('Times New Roman', 23), bg="white",
                             fg='#B20600')
        loginHeading.place(x=590, y=120)

        self.loginUsernameEntry = Entry(self.signinFrame, width=25, font=('Times New Roman', 11),
                                        insertbackground='#B20600', bd=0, fg='#B20600', bg='white')
        self.loginUsernameEntry.place(x=580, y=200)
        self.loginUsernameEntry.insert(0, 'Username')
        self.loginUsernameEntry.bind("<Button-1>", self.usernameClick)

        Frame(self.signinFrame, width=240, height=2, bg='#B20600').place(x=580, y=222)

        self.loginPasswordEntry = Entry(self.signinFrame, width=25,
                                        insertbackground='#B20600', font=('Times New Roman', 11), bd=0,
                                        fg='#B20600',
                                        bg='white')
        self.loginPasswordEntry.config(show='*')
        self.loginPasswordEntry.place(x=580, y=260)
        self.loginPasswordEntry.insert(0, 'Password')

        self.loginPasswordEntry.bind("<Button-1>", self.passwordClick)
        Frame(self.signinFrame, width=240, height=2, bg='#B20600').place(x=580, y=282)
        global logineyeImage
        logineyeImage = PhotoImage(file='Resources/closeye.png', master=self.signinFrame)
        self.logineyeButton = Button(self.signinFrame, image=logineyeImage, bd=0, bg='white',
                                     activebackground='white',
                                     cursor='hand2',
                                     command=lambda: show(logineyeImage, self.loginPasswordEntry, self.logineyeButton))
        self.logineyeButton.place(x=800, y=255)

        loginForgotButton = Button(self.signinFrame, text="Forgot Password?", bd=0, bg='white',
                                   activebackground='white', activeforeground='#B20600', cursor='hand2',
                                   font=('Times New Roman', 9), fg='#B20600',
                                   command=lambda: self.forgot_password(window))
        loginForgotButton.place(x=715, y=295)

        loginButton = Button(self.signinFrame, text='Login', font=('Times New Roman', 14), fg='#F3EFE0',
                             bg='#B20600', activebackground='black',
                             activeforeground='goldenrod1', cursor='hand2', bd=0,
                             width=19, command=lambda: self.login_user(window))
        loginButton.place(x=578, y=350)

        loginOrLabel = Label(self.signinFrame, text='--------- OR ---------',
                             font=('Times New Roman', 16), bg='white', fg='#B20600')
        loginOrLabel.place(x=593, y=400)

        loginRegisterButton = Button(self.signinFrame, text='Register', font=('Times New Roman', 14), fg='black',
                                     bg='goldenrod1', activebackground='black',
                                     activeforeground='#F3EFE0', cursor='hand2', bd=0,
                                     width=19, command=lambda: self.register_page(window))
        loginRegisterButton.place(x=578, y=450)

    def registerpage(self, window):
        # REGISTER PAGE

        self.registerFrame = Frame(window, height=window.winfo_screenheight(),
                                   width=window.winfo_screenwidth(),
                                   bg='#F3EFE0')
        self.registerFrame.place(x=575, y=40)

        # bgLabel = Label(registerFrame,image=bgPhoto)
        # bgLabel.place(x=0, y=0)

        signupHeading = Label(self.registerFrame, text='Create an Account',
                              font=('Times New Roman', 18, 'bold'), bg="#F3EFE0",
                              fg='#B20600', bd=0)
        signupHeading.grid(row=0, column=0, padx=30)

        signupnameLabel = Label(self.registerFrame, text='Name',
                                font=('Times New Roman', 10,), bg="#F3EFE0",
                                fg='#B20600', bd=0)
        signupnameLabel.grid(row=1, column=0, sticky='w', padx=25, pady=25)
        self.signupnameEntry = Entry(self.registerFrame, width=25, font=('Times New Roman', 10,),
                                     bg='#F3EFE0', insertbackground='#B20600',
                                     fg='#B20600', bd=0)
        self.signupnameEntry.grid(row=1, column=0, sticky='sw', padx=25)
        Frame(self.registerFrame, width=250, height=2, bg='#B20600').grid(row=2, column=0, sticky='n')

        signupUsernameLabel = Label(self.registerFrame, text='Username',
                                    font=('Times New Roman', 10,), bg="#F3EFE0",
                                    fg='#B20600', bd=0)
        signupUsernameLabel.grid(row=2, column=0, sticky='w', padx=25, pady=25)
        self.signupUsernameEntry = Entry(self.registerFrame, width=25, font=('Times New Roman', 10,),
                                         bg='#F3EFE0', insertbackground='#B20600',
                                         fg='#B20600', bd=0)
        self.signupUsernameEntry.grid(row=2, column=0, sticky='sw', padx=25)
        Frame(self.registerFrame, width=250, height=2, bg='#B20600').grid(row=3, column=0, sticky='n')

        signupPhoneLabel = Label(self.registerFrame, text='Phone',
                                 font=('Times New Roman', 10,), bg="#F3EFE0",
                                 fg='#B20600', bd=0)
        signupPhoneLabel.grid(row=3, column=0, sticky='w', padx=25, pady=25)
        self.signupPhoneEntry = Entry(self.registerFrame, width=25, font=('Times New Roman', 10,),
                                      bg='#F3EFE0',
                                      insertbackground='#B20600', fg='#B20600', bd=0)
        self.signupPhoneEntry.grid(row=3, column=0, sticky='sw', padx=25)
        Frame(self.registerFrame, width=250, height=2, bg='#B20600').grid(row=4,
                                                                          column=0, sticky='n')

        signupEmailLabel = Label(self.registerFrame, text='Email',
                                 font=('Times New Roman', 10,), bg="#F3EFE0",
                                 fg='#B20600', bd=0)
        signupEmailLabel.grid(row=4, column=0, sticky='w', padx=25, pady=25)
        self.signupEmailEntry = Entry(self.registerFrame, width=25, font=('Times New Roman', 10,),
                                      bg='#F3EFE0',
                                      insertbackground='#B20600', fg='#B20600', bd=0)
        self.signupEmailEntry.grid(row=4, column=0, sticky='sw', padx=25)
        Frame(self.registerFrame, width=250, height=2, bg='#B20600').grid(row=5,
                                                                          column=0, sticky='n')

        signupAddressLabel = Label(self.registerFrame, text='Address',
                                   font=('Times New Roman', 10,), bg="#F3EFE0",
                                   fg='#B20600', bd=0)
        signupAddressLabel.grid(row=5, column=0, sticky='w', padx=25, pady=25)
        self.signupAddressEntry = Entry(self.registerFrame, width=25, font=('Times New Roman', 10,),
                                        bg='#F3EFE0',
                                        insertbackground='#B20600', fg='#B20600', bd=0)
        self.signupAddressEntry.grid(row=5, column=0, sticky='sw', padx=25)
        Frame(self.registerFrame, width=250, height=2, bg='#B20600').grid(row=6, column=0, sticky='n')

        signupPasswordLabel = Label(self.registerFrame, text='Password',
                                    font=('Times New Roman', 10,), bg="#F3EFE0",
                                    fg='#B20600', bd=0)
        signupPasswordLabel.grid(row=6, column=0, sticky='w', padx=25, pady=25)
        self.signupPasswordEntry = Entry(self.registerFrame, width=25,
                                         insertbackground='#B20600', font=('Times New Roman', 10,),
                                         bg='#F3EFE0', fg='#B20600', bd=0)
        self.signupPasswordEntry.grid(row=6, column=0, sticky='sw', padx=25)
        Frame(self.registerFrame, width=250, height=2, bg='#B20600').grid(row=7, column=0, sticky='n')

        signupConfirmLabel = Label(self.registerFrame, text='Confirm Password',
                                   font=('Times New Roman', 10,), bg="#F3EFE0",
                                   fg='#B20600', bd=0)
        signupConfirmLabel.grid(row=8, column=0, sticky='w', padx=25, pady=25)
        self.signupConfirmEntry = Entry(self.registerFrame, width=25, font=('Times New Roman', 10,),
                                        bg='#F3EFE0', fg='#B20600',
                                        insertbackground='#B20600', bd=0)
        self.signupConfirmEntry.grid(row=8, column=0, sticky='sw', padx=25)
        Frame(self.registerFrame, width=250, height=2, bg='#B20600').grid(row=9, column=0, sticky='n')

        signupButton = Button(self.registerFrame, text='Sign up', font=('Times New Roman', 14), fg='#F3EFE0',
                              bg='#B20600', activebackground='black',
                              activeforeground='goldenrod1', cursor='hand2', bd=0,
                              width=19, command=self.save_db)
        signupButton.grid(row=9, column=0, pady=10)

        signinButton = Button(self.registerFrame, text="Already have an account? Sign in.", bd=0, bg='goldenrod1',
                              activebackground='black', activeforeground='#F3EFE0', cursor='hand2',
                              font=('Times New Roman', 9), fg='black', command=lambda: self.signinFrame.tkraise())
        signinButton.grid(row=10, column=0)

        # FORGOT PASSWORD PAGE

    def resetpage(self, window):
        self.resetFrame = Frame(window, height=window.winfo_screenheight(), width=window.winfo_screenwidth(),
                                bg='#F3EFE0')
        self.resetFrame.place(x=575, y=122)

        # bgLabel = Label(registerFrame,image=bgPhoto)
        # bgLabel.place(x=0, y=0)

        resetHeading = Label(self.resetFrame, text='Reset Password',
                             font=('Times New Roman', 20, 'bold'), bg="#F3EFE0",
                             fg='#B20600', bd=0)
        resetHeading.grid(row=0, column=0, padx=30)

        resetUsernameLabel = Label(self.resetFrame, text='Username',
                                   font=('Times New Roman', 10,), bg="#F3EFE0",
                                   fg='#B20600', bd=0)
        resetUsernameLabel.grid(row=1, column=0, sticky='w', padx=25, pady=25)
        self.resetUsernameEntry = Entry(self.resetFrame, width=25, font=('Times New Roman', 10,),
                                        insertbackground='#B20600',
                                        bg='#F3EFE0', fg='#B20600', bd=0)
        self.resetUsernameEntry.grid(row=1, column=0, sticky='sw', padx=25)
        Frame(self.resetFrame, width=250, height=2, bg='#B20600').grid(row=3, column=0, sticky='n')

        resetPasswordLabel = Label(self.resetFrame, text='Password',
                                   font=('Times New Roman', 10,), bg="#F3EFE0",
                                   fg='#B20600', bd=0)
        resetPasswordLabel.grid(row=4, column=0, sticky='w', padx=25, pady=25)
        self.resetPasswordEntry = Entry(self.resetFrame, width=25, font=('Times New Roman', 10,),
                                        insertbackground='#B20600',
                                        bg='#F3EFE0', fg='#B20600', bd=0)
        self.resetPasswordEntry.grid(row=4, column=0, sticky='sw', padx=25)
        Frame(self.resetFrame, width=250, height=2, bg='#B20600').grid(row=6, column=0, sticky='n')

        resetConfirmLabel = Label(self.resetFrame, text='Confirm Password',
                                  font=('Times New Roman', 10,), bg="#F3EFE0",
                                  fg='#B20600', bd=0)
        resetConfirmLabel.grid(row=7, column=0, sticky='w', padx=25, pady=25)
        self.resetConfirmEntry = Entry(self.resetFrame, width=25, font=('Times New Roman', 10,),
                                       insertbackground='#B20600',
                                       bg='#F3EFE0', fg='#B20600', bd=0)
        self.resetConfirmEntry.grid(row=7, column=0, sticky='sw', padx=25)
        Frame(self.resetFrame, width=250, height=2, bg='#B20600').grid(row=9, column=0, sticky='n')

        backButton = Button(self.resetFrame, text='Go Back', font=('Times New Roman', 14), fg='black',
                            bg='goldenrod1', activebackground='black',
                            activeforeground='#F3EFE0', cursor='hand2', bd=0,
                            width=19, command=self.back)
        backButton.grid(row=11, column=0, pady=10)

        resetButton = Button(self.resetFrame, text='Update Password', font=('Times New Roman', 14), fg='#F3EFE0',
                             bg='#B20600', activebackground='black',
                             activeforeground='goldenrod1', cursor='hand2', bd=0,
                             width=19, command=self.change_password)  # Note that you pass the callback without
        resetButton.grid(row=10, column=0, pady=20)  # parentheses () within the command option. Otherwise, the callback
        # would be called as soon as the program runs
