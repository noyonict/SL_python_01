
def sum_(num_1, num_2):
    return num_1 + num_2


def sub_(a, b):
    return a - b


def mul_(num1, num2):   # 8943 * 334    # 7 * 7
    return num1 * num2


def div_(num1, num2):
    return num1 / num2


def user_input(i):   # recursive function   78b 78
    try:
        return int(input(f'Number {i}: '))  # 89o
    except Exception as e:
        print('Please enter a valid number')
        return user_input(i)

#
# def user_input(i):
#     while True:
#         try:
#             num = int(input(f'Number {i}: '))  # 89o, 89m, 67
#             return num
#         except Exception as e:
#             print('Please enter a valid number')


if __name__ == '__main__':
    user_num1 = user_input(1)
    user_num2 = user_input(2)


    while True:
        print('1 - sum \n2 - sub \n3 - mul \n4 - div')

        user_choice = input('What do you want?: ')
        if user_choice == '1':
            print(f"{user_num1} + {user_num2} = {sum_(user_num1, user_num2)}")

        elif user_choice == '2':
            print('{} - {} = {}'.format(user_num1, user_num2, sub_(user_num1, user_num2)))

        elif user_choice == '3':
            print(user_num1, 'x', user_num2, '=', mul_(user_num1, user_num2))

        elif user_choice == '4':
            print(str(user_num1) + ' % ' + str(user_num2) + ' = ' + str(div_(user_num1, user_num2)))

        else:
            print('Please choose between (1-4)')
            continue

        continue_ = input('Do you want to do it again? (y/n): ')
        if continue_.lower() == 'n':
            print('Thank you! See you soon!')
            break
        print('*' * 40)




