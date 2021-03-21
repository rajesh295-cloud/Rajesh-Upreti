from tkinter import *
from User_Register_page import *
import tkinter.messagebox
__all__ = ["Admin_for_Employee_Details"]

class Log_in_Form:
    def __init__(self, window):
        self.wn = window
        self.wn.geometry("500x400")
        self.wn.title('Login')
        self.wn.config(bg='lime')

        # =======================lbl Heading

        self.lb_heading = Label(self.wn, text="Log in System", bg="Red", fg="black", font=("arial", 20, "bold"))
        self.lb_heading.place(x=0, y=0, relwidth=1)

        # frame================f

        self.frame1 = Frame(self.wn, bg='green')
        self.frame1.place(x=50, y=100)

        # label  username===================

        self.lb_username = Label(self.frame1, text="Username:", font=("arial", 15, "bold"), fg="blue", bg='yellow')
        self.lb_username.grid(row=0, column=0, padx=10, pady=10)

        # Entry Username Box =====================

        self.ent_username = Entry(self.frame1, font=("arial", "16", "bold"))
        self.ent_username.grid(row=0, column=1, padx=10, pady=10)

        #  Label Password===============

        self.lb_password = Label(self.frame1, text="Password:", font=("arial", 15, "bold"), fg="blue", bg='yellow')
        self.lb_password.grid(row=1, column=0, padx=10, pady=10)

        # Entry Password===============

        self.ent_password = Entry(self.frame1, show="*", font=('arial', '16', 'bold'))
        self.ent_password.grid(row=1, column=1, padx=10, pady=10)

        # button.......

        self.btn_login = Button(self.wn, text='Login', fg='black', font=('arial', 16, 'bold'),
                                command=self.btn_login_click)
        self.btn_login.place(x=200, y=210)

        self.btn_reset = Button(self.wn, text='Reset', fg='black', font=('arial', 16, 'bold'),
                                command=self.reset_btn_click)
        self.btn_reset.place(x=280, y=210)

        self.btn_signup = Button(self.wn, text='Sign Up', bg='yellow', fg='red', font=('arial', 15, 'bold italic'),
                                 bd=6, command=self.btn_signup_click)

        self.btn_signup.place(x=330, y=270)

        self.lb_clk = Label(self.wn, text="If you don't have account please", bg='#000080', font=("arial", 15, "bold"),
                            fg="white")
        self.lb_clk.place(x=10, y=270)

    def btn_signup_click(self):
        user_window = Tk()
        User_Form(user_window)

    def load(self):
        le = os.path.getsize("C:\\Users\\rajes\\python assignment\\sem 1 assignment\\form.txt")

        if le > 0:
            f = open("form.txt", "rb+")
            ld = pickle.load(f)
            f.close()

            for i, j in ld.items():
                if i == self.ent_username.get() or j == self.ent_password.get():
                    for p in j:
                        if (self.ent_password.get()) == p:
                            tkinter.messagebox.showinfo("Welcome", "Login Successful")
                            self.wel()
            else:
                tkinter.messagebox.showerror("Sign Up First", "Wrong Password or Username")
                f.close()
        else:
            tkinter.messagebox.showerror("Sign Up First", "Register First")

    def btn_login_click(self):
        self.load()

    def wel(self):
        self.wn.destroy()
        import Admin_for_Employee_Details
        # Admin_for_Employee_Details.Employee()

    def reset_btn_click(self):
        self.ent_username.delete('0', 'end')
        self.ent_password.delete('0', 'end')


window = Tk()
Log_in_Form(window)
window.mainloop()