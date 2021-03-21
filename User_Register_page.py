from tkinter import *
import tkinter.messagebox
import pickle
import os

d = {}


class User_Form:
    def __init__(self, window):
        self.wn = window
        self.wn.title("Register User")
        self.wn.geometry("700x500")

        self.user_value = StringVar()
        self.pass_value = StringVar()
        self.add_value = StringVar()

        # heading-=============

        self.lb_heading = Label(self.wn, text="User Register Form:", bg="green", fg="white", font=("arial", 20, "bold"))
        self.lb_heading.grid(columnspan=2)

        # Label and entry============================
        self.lb_username = Label(self.wn, text="Username:", font=("arial", 15, "bold"), fg="blue")
        self.lb_username.grid(row=1, column=0, padx=10, pady=10)

        # Entry================

        self.ent_username = Entry(self.wn, font=("arial", 10, "bold"), fg="blue", textvariable=self.user_value)
        self.ent_username.grid(row=1, column=1, padx=10, pady=10)

        #  label Password=============================
        self.lb_Password = Label(self.wn, text="Password:", font=("arial", 15, "bold"), fg="blue")
        self.lb_Password.grid(row=2, column=0, padx=10, pady=10)

        # Entry Password ========================
        self.ent_Password = Entry(self.wn, show="*", font=("arial", 10, "bold"))
        self.ent_Password.grid(row=2, column=1, padx=10, pady=10)

        # label and entry for age...
        self.lb_age = Label(self.wn, text='Age:', font=('arial', 15, 'bold'), fg='blue')
        self.lb_age.grid(row=4, column=0, padx=10, pady=10)
        self.ent_age = Entry(self.wn, font=('arial', 15, 'bold'), fg='blue')
        self.ent_age.grid(row=4, column=1, padx=10, pady=10)

        #  label and entry for Phone Number:

        self.lb_phonenumber = Label(self.wn, text='Phone no:', font=('arial', 15, 'bold'), fg='blue')
        self.lb_phonenumber.grid(row=5, column=0, padx=10, pady=10)

        self.ent_phonenumber = Entry(self.wn, font=('arial', 15, 'bold'), fg='blue')
        self.ent_phonenumber.grid(row=5, column=1, padx=10, pady=10)

        # button..
        self.btn_submit = Button(self.wn, text='submit', font=('arial', 10, 'bold'), command=self.btn_submit_click)
        self.btn_submit.grid(row=6, column=0)

        self.btn_reset = Button(self.wn, text='reset', font=('arial', 10, 'bold'), command=self.reset_btn_click)
        self.btn_reset.grid(row=6, column=1)

    def btn_submit_click(self):
        self.insert()

    def insert(self):
        global d
        le = os.path.getsize("C:\\Users\\rajes\\python assignment\\sem 1 assignment\\form.txt")
        username = self.ent_username.get()
        password = self.ent_Password.get()
        age = self.ent_age.get()
        phone = self.ent_phonenumber.get()

        di = {username: [password, age, phone]}

        if le > 0:
            f = open("form.txt", "rb+")
            d = pickle.load(f)
            d.update(di)
            f.seek(0)
            pickle.dump(d, f)
            tkinter.messagebox.showinfo("success", "Data saved successfully")
            f.close()
            self.wn.destroy()

        else:
            f = open("form.txt", "wb")
            d.update(di)
            pickle.dump(d, f)
            tkinter.messagebox.showinfo("success", "Data saved successfully")
            f.close()
            self.wn.destroy()

    def reset_btn_click(self):
        self.ent_username.delete('0', 'end')
        self.ent_Password.delete('0', 'end')
        self.ent_age.delete('0', 'end')
