from tkinter import *
from tkinter import messagebox
import pymysql
import mysql.connector
from tkinter import filedialog
from Display import Display


class Profile:
    def __init__(self, window):
        self.edit_details_frame = None
        self.delete_frame = None
        self.user_detail_frame = None
        self.window = window

    def showEdit(self):
        self.user_detail_frame.place_forget()
        self.edit_details_frame.place(x=50, y=50)

    def showAccountInfo(self):
        # edit_img_frame.place(x=30, y=100)
        self.delete_frame.place_forget()
        self.edit_details_frame.place_forget()
        self.user_detail_frame.place(x=50, y=50)

    def showDelete(self):
        self.user_detail_frame.place_forget()
        self.delete_frame.place(x=50, y=50)

    @staticmethod
    def editAccount(username, email, address, phone):
        if username == "" or email == '' or address == '' or phone == '':
            messagebox.showerror("Error", "All fields are required")
        else:
            editroot = Tk()
            edit = Display(editroot)
            edit.edit_details(username, email, address, phone)
            editroot.mainloop()

    @staticmethod
    def deleteAccount(smg, passwo, copass):
        mydb = mysql.connector.connect(host="localhost", user="root", password="root", db="Car_Rental_Service")
        db_cursor = mydb.cursor()
        try:
            Queryall = 'Select Username from customer_details'
            db_cursor.execute(Queryall)
            all_details = db_cursor.fetchall()
            dlist = []
            for g in all_details:
                for h in g:
                    dlist.append(h)
            if smg in dlist:
                Queryp = f"Select Customer_Password from Customer_Details where Username='{smg}'"
                db_cursor.execute(Queryp)
                passwords = db_cursor.fetchall()
                if passwo == copass:
                    for i in passwords:
                        for j in i:
                            if j == passwo:
                                Queryd = f"Delete from Customer_Details where Username='{smg}'"
                                db_cursor.execute(Queryd)
                                mydb.commit()
                                mydb.close()
                                messagebox.showinfo("Completed", f"The Account of {smg} has been \ndeleted")
                            else:
                                messagebox.showerror("Password error", "The Password is wrong")
                else:
                    messagebox.showerror("Password error", "Both Passwords does not match")
            else:
                raise mysql.connector.errors.ProgrammingError()
        except mysql.connector.errors.ProgrammingError:
            messagebox.showerror("Username error", "The Username you entered is wrong")

    def openImage(self):
        mydb = pymysql.connect(
            user="root",
            password="root",
            host="localhost",
            database='car_rental_service'
        )
        cursor = mydb.cursor()
        query1 = 'select * from login'
        cursor.execute(query1)
        fetch = cursor.fetchone()
        global op_img
        self.window.filename = filedialog.askopenfilename(initialdir="\Downloads\sbv", title="Select File",
                                                          filetypes=(("jpg files", "*.jpg"), ("All files", "*.*")))
        # with open(self.window.filename, 'rb') as file:
        #     binaryData = file.read()
        # query2 = f'update customer_details set avatar={binaryData} where Username="{fetch[0]}"'
        # cursor.execute(query2)

    def Profile_frame(self):
        mydb = pymysql.connect(
            user="root",
            password="root",
            host="localhost",
            database='car_rental_service'
        )
        cursor = mydb.cursor()
        q = "select Username from login"
        fetch = []
        cursor.execute(q)
        loginuser = cursor.fetchall()
        for i in loginuser:
            for j in i:
                fetch.append(j)
        for h in fetch:
            Queryuser = f'select Customer_name from customer_details where Username="{h}"'
            cursor.execute(Queryuser)
            fetchuser = cursor.fetchone()
            Queryemail = f'select Customer_EMail from customer_details where Username="{h}"'
            cursor.execute(Queryemail)
            fetchemail = cursor.fetchone()
            Queryaddress = f'select Customer_Address from customer_details where Username="{h}"'
            cursor.execute(Queryaddress)
            fetchaddress = cursor.fetchone()
            Queryphone = f'select Customer_phone from customer_details where Username="{h}"'
            cursor.execute(Queryphone)
            fetchphone = cursor.fetchone()
            disp_frame1 = Frame(self.window, width=800, height=100)
            disp_frame1.config(background='#F3EFE0')
            disp_frame1.pack()

            disp_frame2 = Frame(self.window, width=800, height=500)
            disp_frame2.config(background="#850000", relief='groove')
            disp_frame2.place(x=0, y=0)

            self.user_detail_frame = Frame(self.window, width=700, height=400)
            self.user_detail_frame.place(x=50, y=50)

            account_label = Label(self.user_detail_frame, text="Account Details", font=("telegrafico", 30),
                                  border=0)
            account_label.place(x=180, y=10)

            btn2 = Button(self.user_detail_frame, text="Edit Details", border=5, width=12, command=self.showEdit,
                          foreground='#B20600', font=("telegrafico", 15), relief=FLAT)
            btn2.place(x=50, y=320)

            btn3 = Button(self.user_detail_frame, text="Delete Account", border=5, width=14,
                          command=self.showDelete, relief=FLAT,
                          foreground='#B20600', font=("telegrafico", 15))
            btn3.place(x=470, y=320)

            img_frame = Frame(self.user_detail_frame, width=200, height=200, background='grey')
            img_frame.place(x=30, y=100)

            # global imgm
            # img = Image.open("Resources/avatar.png")
            # resize = img.resize((300, 200))
            # imgm = ImageTk.PhotoImage(resize)
            # carpic = Text(img_frame)
            # carpic.place(x=0, y=0)
            # carpic.image_create(INSERT, image=imgm)
            # carpic.image = imgm

            # img_query = f'select avatar from customer_details where Username="{h}"'
            # cursor.execute(img_query)
            # avatar = cursor.fetchone()
            # avatar_label = Label(img_frame, image=avatar[0])
            # avatar_label.pack()

            for user in fetchuser:
                user_name = Label(self.user_detail_frame, text=f"{user}", font=("telegrafico", 25))
                user_name.place(x=250, y=110)

            for email in fetchemail:
                user_email = Label(self.user_detail_frame, text=f"{email}", font=("Arial Bold", 15))
                user_email.place(x=255, y=150)

            for phone in fetchphone:
                user_phone = Label(self.user_detail_frame, text=f"{phone}", font=("Times New Roman", 15))
                user_phone.place(x=255, y=180)

            for address in fetchaddress:
                user_address = Label(self.user_detail_frame, text=f"{address}", font=("Times New Roman", 15))
                user_address.place(x=255, y=210)

            self.edit_details_frame = Frame(self.window, width=700, height=400)

            edit_label = Label(self.edit_details_frame, text="Edit Details", font=("telegrafico", 30), border=0)
            edit_label.place(x=220, y=10)

            Label(self.edit_details_frame, text="Enter new Name  ", font=("telegrafico", 15)).place(x=50,y=100)
            e1 = Entry(self.edit_details_frame, width=25, font=("Times New Roman", 15))
            e1.place(x=400, y=100)
            Label(self.edit_details_frame, text="Enter new Email-Id  ", font=("telegrafico", 15)).place(x=50, y=150)
            e2 = Entry(self.edit_details_frame, width=25, font=("Times New Roman", 15))
            e2.place(x=400, y=150)
            Label(self.edit_details_frame, text="Enter new Address  ", font=("telegrafico", 15)).place(x=50, y=200)
            e3 = Entry(self.edit_details_frame, width=25, font=("Times New Roman", 15))
            e3.place(x=400, y=200)
            Label(self.edit_details_frame, text="Enter new phone number ", font=("telegrafico", 15)).place(
                x=50, y=250)
            e4 = Entry(self.edit_details_frame, width=25, font=("Times New Roman", 15))
            e4.place(x=400, y=250)

            btn1 = Button(self.edit_details_frame, width=8, text="Cancel", border=5, command=self.showAccountInfo,
                          foreground='#B20600', font=("telegrafico", 15), relief=FLAT)
            btn1.place(x=380, y=300)

            btn2 = Button(self.edit_details_frame, width=10, text="Save Details", border=5, foreground='#B20600',
                          command=lambda: self.editAccount(e1.get(), e2.get(), e3.get(), e4.get())
                          , font=("telegrafico", 15), relief=FLAT)
            btn2.place(x=520, y=300)

            btn3 = Button(self.edit_details_frame, text="Change Image", border=5, command=self.openImage,
                          foreground='#B20600', font=("telegrafico", 15), relief=FLAT)
            btn3.place(x=70, y=300)

            # window 2

            self.delete_frame = Frame(self.window, width=700, height=400)
            # delete_frame.pack()

            delete_label = Label(self.delete_frame, text="Delete Account", font=("telegrafico", 30), border=0)
            delete_label.place(x=180, y=10)

            Label(self.delete_frame, text="Enter your Username  ", font=("telegrafico", 15)).place(x=100, y=100)
            d1 = Entry(self.delete_frame, width=25, font=("Times New Roman", 15))
            d1.place(x=400, y=100)
            Label(self.delete_frame, text="Enter your password  ", font=("telegrafico", 15)).place(x=100, y=150)
            d2 = Entry(self.delete_frame, width=25, font=("Times New Roman", 15))
            d2.place(x=400, y=150)
            Label(self.delete_frame, text="Confirm your password  ", font=("telegrafico", 15)).place(x=100,
                                                                                                         y=200)
            d3 = Entry(self.delete_frame, width=25, font=("Times New Roman", 15))
            d3.place(x=400, y=200)

            btn1 = Button(self.delete_frame, width=10, text="Cancel", border=5, command=self.showAccountInfo,
                          foreground='#B20600', font=("telegrafico", 15), relief=FLAT)
            btn1.place(x=200, y=330)

            btn2 = Button(self.delete_frame, width=10, text="Confirm", border=5, foreground='#B20600',
                          command=lambda: self.deleteAccount(d1.get(), d2.get(), d3.get())
                          , font=("telegrafico", 15), relief=FLAT)
            btn2.place(x=450, y=330)
