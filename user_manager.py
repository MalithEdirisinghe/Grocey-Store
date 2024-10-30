def authenticate_user(users_data):
    username = input("Enter username: ")
    password = input("Enter password: ")
    for user in users_data:
        if user[0] == username and user[1] == password:
            return user[2]  # Return user role ('cashier' or 'manager')
    return None
