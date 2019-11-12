
class Student:
    def __init__(self, name, institute, email, phone):
        self.name = name
        self.institute = institute
        self.email = email
        self.phone = phone

    def __str__(self):
        return self.name

    def show_info(self):
        print('*' * 50)
        print('Name:', self.name)
        print('Institute:', self.institute)
        print('Email:', self.email)
        print('Phone:', self.phone)
        print()

    def change_phone(self, new_number):
        self.phone = new_number

    def change_email(self, new_email):
        self.email = new_email


salman = Student('Salman', 'DPI', 'salman@gmail.com', '01928493916')
abdullah = Student('Abdullah', 'DPI', 'salman@gmail.com', '01928493916')

salman.show_info()
abdullah.show_info()
abdullah.change_phone('01775748710')
abdullah.show_info()
salman.change_email('salman145122@bsdi-bd.org')
salman.show_info()




