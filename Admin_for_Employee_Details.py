from tkinter import *
from tkinter import ttk
from Module_Class.Employee_Details import *
from tkinter import messagebox
from Database.Database_Connectivity_Employee_Details import *

__all__ = ["Module_Class","Database"]

class Employee:

    def __init__(self, *args, **kwargs):

        # ================ All Variables ========== #
        self.ID_no_var = StringVar()
        self.Name_var = StringVar()
        self.Gender_var = StringVar()
        self.Email_var = StringVar()
        self.Contact_var = StringVar()
        self.D_O_B_var = StringVar()
        self.Department_var = StringVar()
        self.Position_var = StringVar()

        self.Search_by = StringVar()
        self.Search_txt = StringVar()

        self.wn7 = window
        self.wn7.geometry("1920x800")
        self.wn7.title("Employee Management System")
        self.wn7.configure(bg="yellow")
        self.wn7.configure()
        # ========================Top label========================= #
        self.wn7.top_label = Label(self.wn7, text="Employee Management System", relief="groove", font="Cambria 38 bold",
                                   bg="white", bd=10, fg="deeppink", pady=2)
        self.wn7.top_label.pack(side=TOP, fill=X)
        # ============================ Main Frame ================== #
        self.manage_frame = Frame(self.wn7, bd=4, relief="ridge", bg="aqua")
        self.manage_frame.place(x=20, y=100, width=520, height=750)

        self.lbl_title = Label(self.manage_frame, text="Registration", fg="red", bg="aqua",
                               font="Cambria 32 bold")
        self.lbl_title.grid(row=0, columnspan=2, padx=20, pady=0)

        self.lbl_ID_no = Label(self.manage_frame, text="ID No", fg="magenta", bg="aqua", font="Cambria 18 bold")
        self.lbl_ID_no.grid(row=1, column=0, padx=50, pady=10, sticky="w")

        self.txt_ID_no = Entry(self.manage_frame, textvariable=self.ID_no_var, font="Arial 16 bold", relief="groove",
                               bd=10)
        self.txt_ID_no.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        self.lbl_name = Label(self.manage_frame, text="Name", fg="magenta", bg="aqua", font="Cambria 18 bold")
        self.lbl_name.grid(row=2, column=0, padx=50, pady=10, sticky="w")

        self.txt_name = Entry(self.manage_frame, textvariable=self.Name_var, font="Arial 16 bold", relief="groove",
                              bd=10)
        self.txt_name.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        self.lbl_gender = Label(self.manage_frame, text="Gender", fg="magenta", bg="aqua", font="Cambria 18 bold")
        self.lbl_gender.grid(row=3, column=0, padx=50, pady=10, sticky="w")

        self.Combo_gender = ttk.Combobox(self.manage_frame, textvariable=self.Gender_var, font="Arial 16 bold",
                                         state="readonly", width=20)
        self.Combo_gender['values'] = ["Male", "Female", "Others"]
        self.Combo_gender.grid(row=3, column=1, padx=10, pady=10, sticky="w")

        self.lbl_email = Label(self.manage_frame, text="Email", fg="magenta", bg="aqua", font="Cambria 18 bold")
        self.lbl_email.grid(row=4, column=0, padx=50, pady=10, sticky="w")

        self.txt_email = Entry(self.manage_frame, textvariable=self.Email_var, font="Arial 16 bold",
                               relief="groove",
                               bd=10)
        self.txt_email.grid(row=4, column=1, padx=10, pady=10, sticky="w")

        self.lbl_contact = Label(self.manage_frame, text="Contact", fg="magenta", bg="aqua", font="Cambria 18 bold")
        self.lbl_contact.grid(row=5, column=0, padx=50, pady=10, sticky="w")

        self.txt_contact = Entry(self.manage_frame, textvariable=self.Contact_var, font="Arial 16 bold",
                                 relief="groove", bd=10)
        self.txt_contact.grid(row=5, column=1, padx=10, pady=10, sticky="w")

        self.lbl_DOB = Label(self.manage_frame, text="D.O.B", fg="magenta", bg="aqua", font="Cambria 18 bold")
        self.lbl_DOB.grid(row=6, column=0, padx=50, pady=10, sticky="w")

        self.txt_DOB = Entry(self.manage_frame, textvariable=self.D_O_B_var, font="Arial 16 bold", relief="groove",
                             bd=10)
        self.txt_DOB.grid(row=6, column=1, padx=10, pady=10, sticky="w")

        self.department = Label(self.manage_frame, text="Department", fg="magenta", bg="aqua", font="Cambria 18 bold")
        self.department.grid(row=7, column=0, padx=15, pady=10, sticky="w")

        self.department_combobox = ttk.Combobox(self.manage_frame, textvariable=self.Department_var,
                                                font="Arial 19 bold", state="readonly")
        self.department_combobox['values'] = ["Network", "Hardware", "Software", "Security", "IT", "Account",
                                              "CustomerService", "Managing"]

        self.department_combobox.grid(row=7, column=1, padx=10, pady=10, sticky="w")

        self.lbl_position = Label(self.manage_frame, text="Position", fg="magenta", bg="aqua", font="Cambria 18 bold")
        self.lbl_position.grid(row=8, column=0, padx=40, pady=10, sticky="w")

        self.combo_position = ttk.Combobox(self.manage_frame, textvariable=self.Position_var, font="Arial 19 bold",
                                           state="readonly")
        self.combo_position['values'] = ["Manager", "Director", "Supervisor", "Hacker", "Accountant", "Servant"]

        self.combo_position.grid(row=8, column=1, padx=10, pady=10, sticky="w")

        self.lbl_Address = Label(self.manage_frame, text="Address", fg="magenta", bg="aqua", font="Cambria 18 bold")
        self.lbl_Address.grid(row=9, column=0, padx=40, pady=10, sticky="w")

        self.txt_address = Text(self.manage_frame, font="Arial 16 bold", width=20, height=1, bd=10)
        self.txt_address.grid(row=9, column=1, padx=10, pady=5, sticky="w")

        # =================== Button Frame ================================= #
        self.btn_frame = Frame(self.manage_frame, bd=4, relief="ridge", bg="cyan")
        self.btn_frame.place(x=8, y=620, width=527, height=130)

        self.insert_btn = Button(self.btn_frame, text="Add", font="Arial 12 bold", bd=10, width=6, height=2,
                                 fg="white",
                                 bg="deeppink", command=self.Insert_Database)
        self.insert_btn.grid(row=0, column=0, padx=15, pady=0)

        self.update_btn = Button(self.btn_frame, text="Change", font="Arial 12 bold", bd=10, width=6, height=2,
                                 fg="white", bg="deeppink", command=self.Update_data)
        self.update_btn.grid(row=0, column=1, padx=15, pady=0)

        self.delete_btn = Button(self.btn_frame, text="Delete", font="Arial 12 bold", bd=10, width=6, height=2,
                                 fg="white", bg="deeppink", command=self.Delete_data)
        self.delete_btn.grid(row=0, column=2, padx=15, pady=0)

        self.clear_btn = Button(self.btn_frame, text="Clear", font="Arial 12 bold", bd=10, width=6, height=2,
                                fg="white",
                                bg="deeppink", command=self.Clear_data)
        self.clear_btn.grid(row=0, column=3, padx=15, pady=0)

        # ============================== Details Frame ======================= #
        self.detail_frame = Frame(self.wn7, bd=4, relief="ridge", bg="lime")
        self.detail_frame.place(x=550, y=100, width=1050, height=690)

        # self.back_btn = Button(self.detail_frame, text="Back", font="Cambria 18 bold", bd=7, width=8, bg="dodgerblue",
        #                        fg="white", command=self.Search_text_separate)
        # self.back_btn.grid(row=0, column=0, padx=10, pady=10)

        self.lbl_search = Label(self.detail_frame, text="Search By:", bg="lime", fg="Magenta",
                                font="Cambria 20 bold")
        self.lbl_search.grid(row=0, column=1, padx=0)

        self.Combo_search = ttk.Combobox(self.detail_frame, textvariable=self.Search_by, font="Cambria 12 bold",
                                         state="readonly", width=10)
        self.Combo_search["values"] = ["ID_No"]
        self.Combo_search.grid(row=0, column=2, padx=10, pady=5)

        self.Search_txt1 = Entry(self.detail_frame, font="Cambria 14 bold", relief="groove", bd=10, width=10,
                                 textvariable=self.Search_txt)
        self.Search_txt1.grid(row=0, column=3, padx=10, pady=10, sticky="w")

        self.show_btn = Button(self.detail_frame, text="Search", font="Cambria 18 bold", bd=7, width=8, bg="dodgerblue",
                               fg="white", command=self.Search_text_separate)
        self.show_btn.grid(row=0, column=4, padx=0, pady=0)

        self.search_btn = Button(self.detail_frame, text="Show All", font="Cambria 18 bold", bd=7, width=8,
                                 bg="dodgerblue", fg="white", command=self.Select_data)
        self.search_btn.grid(row=0, column=5, padx=10, pady=0)

        self.lbl_icon = Label(self.detail_frame, text="", bg="lime", fg="darkorange",
                              font="Cambria 38 bold")
        self.lbl_icon.grid(row=0, column=6, padx=7)

        self.table_frame = Frame(self.detail_frame, bd=4, relief="ridge", bg="lime")
        self.table_frame.place(x=0, y=80, width=995, height=650)

        self.Scrollbar_x = Scrollbar(self.table_frame, orient=HORIZONTAL)
        self.Scrollbar_y = Scrollbar(self.table_frame, orient=VERTICAL)
        self.Student_table = ttk.Treeview(self.table_frame, style="mystyle.Treeview",
                                          columns=["ID No", "Name", "Gender", "Email", "Contact", "D.O.B", "Department",
                                                   "Position", "Address"],
                                          xscrollcommand=self.Scrollbar_x.set, yscrollcommand=self.Scrollbar_y.set)
        self.Scrollbar_x.pack(side=BOTTOM, fill=X)
        self.Scrollbar_y.pack(side=RIGHT, fill=Y)

        self.Scrollbar_x.config(command=self.Student_table.xview)
        self.Scrollbar_y.config(command=self.Student_table.yview)

        self.style = ttk.Style()
        self.style.configure("mystyle.Treeview.Heading", font=("Arial bold", 10))
        self.style.configure("mystyle.Treeview", highlightthickness=1, bd=0, font=("Arial", 10))

        self.Student_table.heading("ID No", text="ID No")
        self.Student_table.heading("Name", text="Name")
        self.Student_table.heading("Gender", text="Gender")
        self.Student_table.heading("Email", text="Email")
        self.Student_table.heading("Contact", text="Contact")
        self.Student_table.heading("D.O.B", text="D.O.B")
        self.Student_table.heading("Department", text="Department")
        self.Student_table.heading("Position", text="Position")
        self.Student_table.heading("Address", text="Address")
        self.Student_table["show"] = "headings"

        self.Student_table.column("ID No", width=10)
        self.Student_table.column("Name", width=50)
        self.Student_table.column("Gender", width=50)
        self.Student_table.column("Email", width=50)
        self.Student_table.column("Contact", width=50)
        self.Student_table.column("D.O.B", width=50)
        self.Student_table.column("Department", width=50)
        self.Student_table.column("Position", width=50)
        self.Student_table.column("Address", width=50)

        self.Student_table.pack(fill=BOTH, expand=1)
        self.Student_table.bind("<ButtonRelease-1>", self.Get_Cursor)

        # ====================== Database object ===============================#

        self.obj_model_employee_details = Employee_Details(self.ID_no_var.get(),
                                                           self.Name_var.get(),
                                                           self.Gender_var.get(),
                                                           self.Email_var.get(),
                                                           self.Contact_var.get(),
                                                           self.D_O_B_var.get(),
                                                           self.Department_var.get(),
                                                           self.Position_var.get(),
                                                           self.txt_address.get("1.0", END))

    def Insert_Database(self):
        self.db_connect = Database()
        # ================= Model class employee details values send =================#
        self.obj_model_employee_details = Employee_Details(self.ID_no_var.get(),
                                                           self.Name_var.get(),
                                                           self.Gender_var.get(),
                                                           self.Email_var.get(),
                                                           self.Contact_var.get(),
                                                           self.D_O_B_var.get(),
                                                           self.Department_var.get(),
                                                           self.Position_var.get(),
                                                           self.txt_address.get("1.0", END))
        if len(self.txt_ID_no.get()) == 0:
            messagebox.showerror("Blank", "ID Must be Filled", parent=self.wn7)
        elif not self.txt_ID_no.get().isdigit():
            messagebox.showerror("Wrong", "ID cannot be String", parent=self.wn7)
        elif len(self.Name_var.get()) == 0:
            messagebox.showwarning("Blank", "Name Must be Filled", parent=self.wn7)
        elif self.Name_var.get().isdigit():
            messagebox.showerror("Wrong", "Name cannot be Integer", parent=self.wn7)
        elif len(self.Gender_var.get()) == 0:
            messagebox.showwarning("Blank", "Gender Must be Filled", parent=self.wn7)
        elif len(self.Email_var.get()) == 0:
            messagebox.showwarning("Blank", "Email Must be Filled", parent=self.wn7)
        elif len(self.Contact_var.get()) == 0:
            messagebox.showwarning("Blank", "Contact Must be Filled", parent=self.wn7)
        elif len(self.D_O_B_var.get()) == 0:
            messagebox.showwarning("Blank", "Date of Birth Must be Filled", parent=self.wn7)
        elif len(self.Department_var.get()) == 0:
            messagebox.showwarning("Blank", "Department Must be Filled", parent=self.wn7)
        elif len(self.Position_var.get()) == 0:
            messagebox.showwarning("Blank", "Position Must be Filled", parent=self.wn7)
        else:
            quory_add = 'insert into employee_details values(%s, %s, %s, %s, %s, %s, %s, %s, %s);'
            values_add = (int(self.obj_model_employee_details.get_id_no()),
                          self.obj_model_employee_details.get_name(),
                          self.obj_model_employee_details.get_gender(),
                          self.obj_model_employee_details.get_email(),
                          self.obj_model_employee_details.get_contact(),
                          self.obj_model_employee_details.get_date_of_birth(),
                          self.obj_model_employee_details.get_department(),
                          self.obj_model_employee_details.get_position(),
                          self.obj_model_employee_details.get_address())
            self.db_connect.Insert(quory_add, values_add)
            print("Inserted Successfully")
            messagebox.showinfo("Insert", "Inserted Successfully", parent=self.wn7)

    def Update_data(self):
        self.db_connect = Database()
        # ================= Model class employee details values send =================#
        self.obj_model_employee_details = Employee_Details(self.txt_ID_no.get(),
                                                           self.Name_var.get(),
                                                           self.Gender_var.get(),
                                                           self.Email_var.get(),
                                                           self.Contact_var.get(),
                                                           self.D_O_B_var.get(),
                                                           self.Department_var.get(),
                                                           self.Position_var.get(),
                                                           self.txt_address.get("1.0", END))
        if len(self.txt_ID_no.get()) == 0:
            messagebox.showerror("Blank", "ID Must be Filled", parent=self.wn7)
        elif not self.txt_ID_no.get().isdigit():
            messagebox.showerror("Wrong", "ID cannot be String", parent=self.wn7)
        elif len(self.Name_var.get()) == 0:
            messagebox.showwarning("Blank", "Name Must be Filled", parent=self.wn7)
        elif self.Name_var.get().isdigit():
            messagebox.showerror("Wrong", "Name cannot be Integer", parent=self.wn7)
        elif len(self.Gender_var.get()) == 0:
            messagebox.showwarning("Blank", "Gender Must be Filled", parent=self.wn7)
        elif len(self.Email_var.get()) == 0:
            messagebox.showwarning("Blank", "Email Must be Filled", parent=self.wn7)
        elif len(self.Contact_var.get()) == 0:
            messagebox.showwarning("Blank", "Contact Must be Filled", parent=self.wn7)
        elif len(self.D_O_B_var.get()) == 0:
            messagebox.showwarning("Blank", "Date of Birth Must be Filled", parent=self.wn7)
        elif len(self.Department_var.get()) == 0:
            messagebox.showwarning("Blank", "Department Must be Filled", parent=self.wn7)
        elif len(self.Position_var.get()) == 0:
            messagebox.showwarning("Blank", "Position Must be Filled", parent=self.wn7)
        else:
            quory_update = 'update employee_details set Name=%s,Gender=%s,Email=%s,Contact=%s,D_O_B=%s,Department=%s,' \
                           'Position=%s,Address=%s where ID_No=%s; '
            values_update = (
                self.obj_model_employee_details.get_name(),
                self.obj_model_employee_details.get_gender(),
                self.obj_model_employee_details.get_email(),
                self.obj_model_employee_details.get_contact(),
                self.obj_model_employee_details.get_date_of_birth(),
                self.obj_model_employee_details.get_department(),
                self.obj_model_employee_details.get_position(),
                self.obj_model_employee_details.get_address(),
                int(self.obj_model_employee_details.get_id_no()))

            self.db_connect.Update(quory_update, values_update)
            print("Updated Successfully")
            messagebox.showinfo("Update", "Updated Successfully", parent=self.wn7)
            self.Select_data()

    def Delete_data(self):

        if len(self.txt_ID_no.get()) == 0:
            messagebox.showerror("Blank", "ID Must be Filled")
        elif not self.txt_ID_no.get().isdigit():
            messagebox.showerror("Wrong", "ID cannot be String", parent=self.wn7)
        elif len(self.Name_var.get()) == 0:
            messagebox.showwarning("Blank", "Name Must be Filled", parent=self.wn7)
        elif self.Name_var.get().isdigit():
            messagebox.showerror("Wrong", "Name cannot be Integer", parent=self.wn7)
        elif len(self.Gender_var.get()) == 0:
            messagebox.showwarning("Blank", "Gender Must be Filled", parent=self.wn7)
        elif len(self.Email_var.get()) == 0:
            messagebox.showwarning("Blank", "Email Must be Filled", parent=self.wn7)
        elif len(self.Contact_var.get()) == 0:
            messagebox.showwarning("Blank", "Contact Must be Filled", parent=self.wn7)
        elif len(self.D_O_B_var.get()) == 0:
            messagebox.showwarning("Blank", "Date of Birth Must be Filled", parent=self.wn7)
        elif len(self.Department_var.get()) == 0:
            messagebox.showwarning("Blank", "Department Must be Filled", parent=self.wn7)
        elif len(self.Position_var.get()) == 0:
            messagebox.showwarning("Blank", "Position Must be Filled", parent=self.wn7)
        else:
            self.db_connect = Database()
            # ================= Model class employee details values send =================#
            self.obj_model_employee_details = Employee_Details(self.ID_no_var.get(),
                                                               self.Name_var.get(),
                                                               self.Gender_var.get(),
                                                               self.Email_var.get(),
                                                               self.Contact_var.get(),
                                                               self.D_O_B_var.get(),
                                                               self.Department_var.get(),
                                                               self.Position_var.get(),
                                                               self.txt_address.get("1.0", END))

            quory_delete = 'delete from employee_details where ID_No=%s;'
            values_delete = (int(self.obj_model_employee_details.get_id_no()),)
            self.db_connect.Delete(quory_delete, values_delete)
            print("Deleted Successfully")
            messagebox.showinfo("Delete", "Deleted Successfully", parent=self.wn7)
            self.Select_data()

    def Select_data(self):
        self.db_connect = Database()
        quory_select = 'select * from employee_details;'
        value_select = self.db_connect.Select_All(quory_select)
        print(f"Value Select is: {value_select}")
        if len(value_select) == 0:
            messagebox.showerror("Black", "No products Found\nPlease Add require Products ", parent=self.wn7)
        elif len(value_select) != 0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in value_select:
                self.Student_table.insert('', END, values=row)

    def Search_text_separate(self):
        self.db_connect = Database()
        quory_select = "select * from employee_details where ID_No=%s;"
        values_select = (self.Search_txt.get(),)
        value_select_tuple = self.db_connect.Select_Many(quory_select, values_select)
        lst = list(value_select_tuple)
        if len(lst) != 0:
            self.Student_table.delete(*self.Student_table.get_children())
            for i in lst:
                self.Student_table.insert("", END, values=i)
        elif self.Linear_Search(lst, self.Search_txt.get()) not in lst:
            messagebox.showerror("Error", "Given ID does not found")

    def Get_Cursor(self, *args):
        cursor_row = self.Student_table.focus()
        contents = self.Student_table.item(cursor_row)
        row = contents['values']
        self.ID_no_var.set(row[0])
        self.Name_var.set(row[1])
        self.Gender_var.set(row[2])
        self.Email_var.set(row[3])
        self.Contact_var.set(row[4])
        self.D_O_B_var.set(row[5])
        self.Department_var.set(row[6])
        self.Position_var.set(row[7])
        self.txt_address.delete("1.0", END)
        self.txt_address.insert(END, row[8])
        print(row)

    def Clear_data(self):
        self.ID_no_var.set("")
        self.Name_var.set("")
        self.Gender_var.set("")
        self.Email_var.set("")
        self.Contact_var.set("")
        self.D_O_B_var.set("")
        self.Department_var.set("")
        self.Position_var.set("")
        self.txt_address.delete("1.0", END)
        self.Student_table.delete(*self.Student_table.get_children())
        messagebox.showinfo("Clear", "Clear Text Successfully", parent=self.wn7)

    def Linear_Search(self, full_list, msg):
        for i in full_list:
            if msg == i:
                return i
            return True
        return False

window = Tk()
obj = Employee(window)
window.mainloop()