class Employee_Details:

    def __init__(self, id_no, name, gender, email, contact,  date_of_birth, department, position, address):
        self.__ID_No = id_no
        self.__Name = name
        self.__Gender = gender
        self.__Email = email
        self.__Contact = contact
        self.__Date_Of_Birth = date_of_birth
        self.__Department = department
        self.__Position = position
        self.__Address = address

    def set_id_no(self, id_no):
        self.__ID_No = id_no

    def get_id_no(self):
        return self.__ID_No

    def set_name(self, name):
        self.__Name = name

    def get_name(self):
        return self.__Name

    def set_gender(self, gender):
        self.__Gender = gender

    def get_gender(self):
        return self.__Gender

    def set_email(self, email):
        self.__Email = email

    def get_email(self):
        return self.__Email

    def set_contact(self, contact):
        self.__Contact = contact

    def get_contact(self):
        return self.__Contact

    def set_date_of_birth(self, date_of_birth):
        self.__Date_Of_Birth = date_of_birth

    def get_date_of_birth(self):
        return self.__Date_Of_Birth

    def set_department(self, department):
        self.__Department = department

    def get_department(self):
        return self.__Department

    def set_position(self, position):
        self.__Position = position

    def get_position(self):
        return self.__Position

    def set_address(self, address):
        self.__Address = address

    def get_address(self):
        return self.__Address