import mysql.connector
from mysql.connector import Error
from tkinter import messagebox

con = None
cur = None

class Database:
    try:
        def __init__(self):
            self.con = mysql.connector.connect(host="localhost", user="root", password="raj295", database="management")
            self.cur = self.con.cursor()
            self.con.is_connected()
            print(f"Information of Server: {self.con.get_server_info()}")
    except Error as e:
            messagebox.showwarning("Connection Error", f"Error due to:{e}")
    else:
        def Insert(self, query, value):
            try:
                self.cur.execute(query, value)
                self.con.commit()
                self.con.close()
                self.cur.close()
            except Error as e:
                messagebox.showwarning("Error", f"Adding error due to {e}")
            finally:
                if self.cur:
                    self.cur.close()
                if self.con:
                    self.con.close()

        def Update(self, query, value):
            try:
                self.cur.execute(query, value)
                self.con.commit()
            except Error as e:
                messagebox.showwarning("Error", f"Updating error due to {e}")
            finally:
                if self.cur:
                    self.cur.close()
                if self.con:
                    self.con.close()

        def Delete(self, query, value):
            try:
                self.cur.execute(query, value)
                self.con.commit()
            except Error as e:
                messagebox.showwarning("Error", f"Deleting error due to {e}")
            finally:
                if self.cur:
                    self.cur.close()
                if self.con:
                    self.con.close()

        def Select_Many(self, query, value):
            try:
                self.cur.execute(query, value)
                self.records = self.cur.fetchmany(1)
                self.con.commit()
                return self.records
            except Error as e:
                messagebox.showerror("Error", f"Selecting many Error due to {e}")
            finally:
                if self.cur:
                    self.cur.close()
                if self.con:
                    self.con.close()

        def Select_All(self, query):
            try:
                self.cur.execute(query)
                self.records = self.cur.fetchall()
                self.con.commit()
                return self.records
            except Error as e:
                messagebox.showerror("Error", f"Selecting all Error due to {e}")
            finally:
                if self.cur:
                    self.cur.close()
                if self.con:
                    self.con.close()