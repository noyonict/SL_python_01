def is_student_id_exist(s_id):
    with open('student_db.txt', 'r') as f:
        info = f.read()
        for i in info.split('\n'):
            if i:
                old_s_id = i.split(',')[0]
                if s_id == old_s_id:
                    return True
    return False


def add_student():
    s_id = input('Enter student ID*: ')
    if s_id and is_student_id_exist(s_id):
        print('Student ID {} already taken!'.format(s_id))
        add_student()
        return False
    name = input('Enter student name*: ')
    email = input('Enter student email: ')
    phone = input('Enter student phone*: ')
    if s_id and name and phone:
        with open('student_db.txt', 'a') as f:
            f.write(s_id + ',' + name + ',' + email + ',' + phone + '\n')
        print('New student added successfully!')
    else:
        print('Student ID or Name or Phone Should not be blank!')


def edit_student():
    given_s_id = input('Enter the student id which you want to edit: ')
    with open('student_db.txt', 'r') as f:
        info = f.read()
        is_exist = False
        with open('student_db.txt', 'w') as fw:
            for i in info.split('\n'):
                if i:
                    s_id, name, email, phone = i.split(',')
                    if given_s_id == s_id:
                        is_exist = True
                        print('1 - Name')
                        print('2 - Email')
                        print('3 - Phone')
                        choice = int(input('what you want to edit?'))
                        if choice == 1:
                            name = input('Enter a new student name: ')
                        elif choice == 2:
                            email = input('Enter a new student email: ')
                        elif choice ==  3:
                            phone = input('Enter a new student phone: ')
                        print(given_s_id, 'is edited!')
                    fw.write(s_id + ',' + name + ',' + email + ',' + phone + '\n')
        if not is_exist:
            print('Student ID {} not exist!'.format(given_s_id))


def view_student():
    with open('student_db.txt', 'r') as f:
        info = f.read()
        for i in info.split('\n'):
            # print(i)
            if i:
                s_id, name, email, phone = i.split(',')
                print('*' * 40)
                print('Student ID:', s_id)
                print('Student Name:', name)
                print('Student E-mail:', email)
                print('Student Phone:', phone)
                print('*' * 40)


def delete_student():
    given_s_id = input('Enter the student id which you want to delete: ')
    with open('student_db.txt', 'r') as f:
        info = f.read()
        with open('student_db.txt', 'w') as fw:
            for i in info.split('\n'):
                # print(i)
                if i:
                    s_id, name, email, phone = i.split(',')
                    if given_s_id == s_id:
                        print(given_s_id, 'is deleted!')
                        continue
                    else:
                        fw.write(s_id + ',' + name + ',' + email + ',' + phone + '\n')


def user_choice():
    print('1 - Add New Student')
    print('2 - View All Student')
    print('3 - Edit a Student')
    print('4 - Delete a Student')
    return int(input('Enter your choice: '))


def main():
    while True:
        u_choice = user_choice()
        if u_choice == 1:
            add_student()
        elif u_choice == 2:
            view_student()
        elif u_choice == 3:
            edit_student()
        elif u_choice == 4:
            delete_student()
        again = input('Do you want to do it again? (y/n): ')
        if again == 'n' or again == 'N':
            print('Thank you! See you soon!')
            break


if __name__ == '__main__':
    main()

