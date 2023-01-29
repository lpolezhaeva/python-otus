import json

from csv import DictReader
from lab2_test_data.files import BOOKS_FILE_PATH
from lab2_test_data.files import USERS_FILE_PATH


def read_books(file_name):
    result_list = []

    with open(file_name, newline='') as books_file:
        reader = DictReader(books_file)
        for row in reader:
            result_list.append(dict(row))

    return result_list


def read_users(file_name):
    with open(file_name) as users_file:
        users = json.loads(users_file.read())

    return users


def modify_books(books):
    new_books = []
    for i in range(len(books)):
        new_dict = {'title': books[i]['Title'], 'author': books[i]['Author'],
                    'pages': books[i]['Pages'], 'genre': books[i]['Genre']}
        new_books.append(new_dict)

    return new_books


def modify_users(users):
    new_users = []
    for i in range(len(users)):
        new_dict = {'name': users[i]['name'], 'gender': users[i]['gender'],
                    'address': users[i]['address'], 'age': users[i]['age']}
        new_users.append(new_dict)

    return new_users


def user_books_assignment(books, users):
    n_books = len(books)
    n_users = len(users)

    quotient = n_books // n_users
    remainder = n_books % n_users

    number_of_assigned_books = 0

    for i in range(n_users):
        number_of_books_for_current_user = quotient + (1 if i < remainder else 0)
        list_of_books_for_current_user = []
        for j in range(number_of_assigned_books, number_of_assigned_books + number_of_books_for_current_user - 1):
            list_of_books_for_current_user.append(books[j])
            number_of_assigned_books += 1
        users[i]['books'] = list_of_books_for_current_user
    return users


def save_result(users):
    with open("results.json", "w") as f:
        data = json.dumps(users, indent=4)
        f.write(data)


if __name__ == '__main__':
    books_ = modify_books(read_books(BOOKS_FILE_PATH))
    users_ = modify_users(read_users(USERS_FILE_PATH))
    save_result(user_books_assignment(books_, users_))

