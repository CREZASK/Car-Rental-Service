from tkinter import *
from tkinter import ttk, messagebox
import pymysql
from Display import Display
from Cardetails import Cardet
from Profile import Profile


class CRService:
    def __init__(self):
        self.third_frame = None
        self.car_frame1 = None
        self.car_frame = None
        self.main_canvas = None
        self.main_frame = None
        self.second_frame = None
        self.root = None

    # Creating root
    def create_root(self):
        self.root = Tk()
        self.root.geometry("1920x1080")
        self.root.title("Car Rental")
        self.root.iconbitmap("Resources/Crezask logo frame (256).ico")
        self.root.attributes('-fullscreen', True)

        # Top Frame
        Company2_name = Canvas(self.root, height=150, width=1920, bg='#850000', highlightthickness=0)
        Company2_name.pack(side=TOP)

        home_f = Frame(Company2_name, width=100, height=40)
        home_f.place(x=30, y=90)

        home = Button(home_f, text="HOME", background='#850000', foreground='#F3EFE0', command=self.Home, relief=FLAT,
                      font=('telegrafico', 26))
        home.pack(side=LEFT)
        profile = Button(home_f, text="PROFILE", background='#850000', foreground='#F3EFE0', command=self.Profile,
                         relief=FLAT, font=('telegrafico', 26))
        profile.pack(side=LEFT)
        login = Button(home_f, text="LOGIN", background='#850000', foreground='#F3EFE0', command=self.Login,
                       relief=FLAT, font=('telegrafico', 26))
        login.pack(side=LEFT)
        home = Button(home_f, text="LOGOUT", background='#850000', foreground='#F3EFE0',
                      command=self.logout, font=('telegrafico', 26),
                      relief=FLAT)
        home.pack(side=LEFT)
        exitframe = Frame(Company2_name, width=100, height=40)
        exitframe.place(x=1500, y=0)
        Exit = Button(exitframe, text="X", background='#850000', foreground='#F3EFE0', activebackground='#850000',
                      activeforeground='#F3EFE0', command=self.exit_root, font=('telegrafico', 20),
                      relief=FLAT)
        Exit.pack(side=RIGHT)

    def Bottom_frame(self):
        style = ttk.Style()
        style.configure("Contact_info.TFrame", background='#222222')

        Contact_info = ttk.Frame(self.root, width=1920, height=100, style="Contact_info.TFrame")
        Contact_info.pack(side=BOTTOM)
        Helpline = Label(Contact_info, text='Helpline\n📞 1800 5203 520', font=('Times new Roman', 14), fg='white',
                         bg='#222222', justify=LEFT)
        Helpline.place(x=20, y=28)

        whatsapp = Label(Contact_info, text='Whatsapp\n📞 9851236544', font=('Times new Roman', 14), fg='white',
                         bg='#222222', justify=LEFT)
        whatsapp.place(x=1390, y=28)

        symbols = Label(Contact_info, text='Instagram', font=('Times new Roman', 14), fg='white',
                        bg='#222222', justify=LEFT)
        symbols.place(x=550, y=38)
        symbols = Label(Contact_info, text='Facebook', font=('Times new Roman', 14), fg='white',
                        bg='#222222', justify=LEFT)
        symbols.place(x=650, y=38)
        symbols = Label(Contact_info, text='Linked In', font=('Times new Roman', 14), fg='white',
                        bg='#222222', justify=LEFT)
        symbols.place(x=750, y=38)
        symbols = Label(Contact_info, text='YouTube', font=('Times new Roman', 14), fg='white',
                        bg='#222222', justify=LEFT)
        symbols.place(x=850, y=38)
        symbols = Label(Contact_info, text='Twitter', font=('Times new Roman', 14), fg='white',
                        bg='#222222', justify=LEFT)
        symbols.place(x=950, y=38)

    # Creating a Main Page with scrollbar
    def Main_page(self):
        self.main_frame = Frame(self.root, highlightthickness=0)
        self.main_frame.pack(side=TOP, fill=BOTH, expand=1)
        self.main_canvas = Canvas(self.main_frame)
        self.main_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        v = ttk.Scrollbar(self.main_frame, orient=VERTICAL, command=self.main_canvas.yview)
        v.pack(side=RIGHT, fill=Y)

        self.main_canvas.configure(yscrollcommand=v.set)
        self.main_canvas.bind('<Configure>',
                              lambda e: self.main_canvas.configure(scrollregion=self.main_canvas.bbox("all")))

        self.second_frame = Frame(self.main_canvas, highlightthickness=0)

        self.main_canvas.create_window((0, 0), window=self.second_frame, anchor="nw")

    def from_display(self):
        Style = Display(self.root)
        Style.Top_frame(self.second_frame)
        Style.middle_frame(self.second_frame)
        Style.frame_build(self.second_frame)

    def ending(self):
        self.root.mainloop()

    def Home(self):
        try:
            mydb = pymysql.connect(
                user="root",
                password="root",
                host="localhost",
                database='car_rental_service'
            )
        except:
            messagebox.showerror('DB Error', 'DB connectivity issue, please try again later.')
            return
        dbcursor = mydb.cursor()
        delete = "DELETE FROM temp_booking"
        dbcursor.execute(delete)
        mydb.commit()
        mydb.close()
        self.car_frame.destroy()
        self.main_frame.destroy()
        self.Main_page()
        self.from_display()
        self.main_buttons()
        self.ending()

    def proceed(self):
        try:
            mydb = pymysql.connect(
                user="root",
                password="root",
                host="localhost",
                database='car_rental_service'
            )
            cursor = mydb.cursor()
        except:
            messagebox.showerror('DB Error', 'DB connectivity issue, please try again later.')
            return
        query = 'select * from temp_booking'
        cursor.execute(query)
        row = cursor.fetchone()
        if row is None:
            messagebox.showerror('Error', 'Please confirm your booking')
        else:
            self.main_frame.destroy()

            self.car_frame = Frame(self.root)
            self.car_frame.pack(side=LEFT, fill=BOTH, expand=1)
            car_canvas = Canvas(self.car_frame)
            car_canvas.pack(side=LEFT, fill=BOTH, expand=1)

            v = ttk.Scrollbar(self.car_frame, orient=VERTICAL, command=car_canvas.yview)
            v.pack(side=LEFT, fill=Y)

            car_canvas.configure(yscrollcommand=v.set)
            car_canvas.bind('<Configure>', lambda e: car_canvas.configure(scrollregion=car_canvas.bbox("all")))

            self.second_frame = Frame(car_canvas)

            car_canvas.create_window((0, 0), window=self.second_frame, anchor="nw")

            Car = Cardet(self.root, self.car_frame, self.second_frame)
            Car.front()

    @staticmethod
    def Profile():
        try:
            mydb = pymysql.connect(
                user="root",
                password="root",
                host="localhost",
                database='car_rental_service'
            )
            cursor = mydb.cursor()
        except:
            messagebox.showerror('DB Error', 'DB connectivity issue, please try again later.')
            return
        query = 'select * from login'
        cursor.execute(query)
        row = cursor.fetchone()
        if row is None:
            messagebox.showerror('Login Error', 'Not logged in yet')
        else:
            window = Tk()

            window.geometry("800x500")
            window.resizable(False, False)
            window.title("Account Details")

            profile = Profile(window)
            profile.Profile_frame()

            window.mainloop()

    @staticmethod
    def Login():
        try:
            con = pymysql.connect(
                user="root",
                password="root",
                host="localhost",
                database='car_rental_service'
            )
        except:
            messagebox.showerror('DB Error', 'DB connectivity issue, please try again later.')
            return
        window = Tk()
        window.geometry('990x660')
        window.resizable(False, False)
        window.title('Sign In')

        login = Display(window)
        login.Login_profile(window)

        window.mainloop()

    @staticmethod
    def logout():
        try:
            mydb = pymysql.connect(
                user="root",
                password="root",
                host="localhost",
                database='car_rental_service'
            )
            cursor = mydb.cursor()
        except:
            messagebox.showerror('DB Error', 'DB connectivity issue, please try again later.')
            return
        query = 'select * from login'
        cursor.execute(query)
        row = cursor.fetchone()
        if row is None:
            messagebox.showerror('Logout Error', 'Not logged in yet')
        else:
            cursor = mydb.cursor()
            delQuery = "Delete from login"
            cursor.execute(delQuery)
            mydb.commit()
            mydb.close()
            messagebox.showinfo('Done', 'Logout Successful')

    def exit_root(self):
        try:
            mydb = pymysql.connect(
                user="root",
                password="root",
                host="localhost",
                database='car_rental_service'
            )
            cursor = mydb.cursor()
        except:
            messagebox.showerror('DB Error', 'DB connectivity issue, please try again later.')
            return
        deleteq = 'delete from temp_booking'
        cursor.execute(deleteq)
        mydb.commit()
        mydb.close()
        self.root.destroy()

    def main_buttons(self):
        loginframe = Frame(self.second_frame, bg='#B20600')
        loginframe.place(x=1345, y=350)
        proceed = Button(loginframe, text="Proceed", command=self.proceed)
        proceed.pack(pady=4, padx=2)


New_page = CRService()
New_page.create_root()
New_page.Main_page()
New_page.from_display()
New_page.main_buttons()
New_page.Bottom_frame()
New_page.ending()
