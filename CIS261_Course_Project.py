
#// Name: Marcus Bracken
#// Course: CIS261 Object Oriented Computer Programming I
#: Lab: Course Project Phase 4: Add Basic Security to the Application

from datetime import datetime


class Login:
    def __init__(self, user_id, password, authorization):
        self.user_id = user_id
        self.password = password
        self.authorization = authorization


def store_user_info(filename="user_data.txt"):
    user_ids = set()
    try:
        with open(filename, 'r') as file:
            for line in file:
                user_id, _, _ = line.strip().split('|')
                user_ids.add(user_id)
    except FileNotFoundError:
        pass

    with open(filename, 'a') as file:
        while True:
            user_id = input("Enter User ID (or type 'End' to finish): ").strip()
            if user_id.lower() == 'end':
                break
            if user_id in user_ids:
                print("User ID already exists. Try another.")
                continue

            password = input("Enter Password: ").strip()
            authorization = input("Enter Authorization Code (Admin/User): ").strip()
            if authorization not in ["Admin", "User"]:
                print("Invalid authorization code. Try again.")
                continue

            file.write(f"{user_id}|{password}|{authorization}\n")
            user_ids.add(user_id)
            print("User information stored successfully.")


def display_user_data(filename="user_data.txt"):
    try:
        with open(filename, 'r') as file:
            print("\nStored User Data:")
            for line in file:
                user_id, password, authorization = line.strip().split('|')
                print(f"User ID: {user_id}, Password: {password}, Authorization: {authorization}")
    except FileNotFoundError:
        print("No user data found.")


def login_user(filename="user_data.txt"):
    user_data = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                user_id, password, authorization = line.strip().split('|')
                user_data[user_id] = (password, authorization)
    except FileNotFoundError:
        print("No user data found.")
        return None

    user_id = input("Enter User ID: ").strip()
    if user_id not in user_data:
        print("User ID not found.")
        return None

    password = input("Enter Password: ").strip()
    stored_password, authorization = user_data[user_id]
    if password != stored_password:
        print("Incorrect password.")
        return None

    print(f"Login successful. Authorization: {authorization}")
    return Login(user_id, password, authorization)


def get_dates():
    while True:
        try:
            from_date = input("Enter from date (mm/dd/yyyy): ").strip()
            to_date = input("Enter to date (mm/dd/yyyy): ").strip()
            datetime.strptime(from_date, "%m/%d/%Y")
            datetime.strptime(to_date, "%m/%d/%Y")
            return from_date, to_date
        except ValueError:
            print("Invalid date format. Please enter dates in mm/dd/yyyy format.")


def main():
    while True:
        print("\nOptions:")
        print("1. Store User Information")
        print("2. Display User Data")
        print("3. Login and Perform Operations")
        print("4. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            store_user_info()
        elif choice == '2':
            display_user_data()
        elif choice == '3':
            user = login_user()
            if user:
                if user.authorization == "Admin":
                    print("Access granted to enter and display data.")
                    # Allow admin to access the payroll system
                    payroll_operations()
                elif user.authorization == "User":
                    print("Access granted to display data only.")
                    display_user_data()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Try again.")


def payroll_operations():
    totals = {
        'total_employees': 0,
        'total_hours': 0,
        'total_gross': 0,
        'total_tax': 0,
        'total_net': 0
    }
    employee_records = []

    while True:
        name = input("Enter employee name (or 'End' to finish): ").strip()
        if name.lower() == 'end':
            break

        from_date, to_date = get_dates()
        hours = get_float_input("Enter total hours worked: ")
        rate = get_float_input("Enter hourly rate: ")
        tax_rate = get_float_input("Enter income tax rate (as a decimal): ")

        gross_pay, income_tax, net_pay = calculate_pay(hours, rate, tax_rate)

        employee_data = {
            'from_date': from_date,
            'to_date': to_date,
            'name': name,
            'hours': hours,
            'rate': rate,
            'gross_pay': gross_pay,
            'tax_rate': tax_rate,
            'income_tax': income_tax,
            'net_pay': net_pay
        }
        employee_records.append(employee_data)

        display_employee_payroll(employee_data)
        write_employee_to_file(employee_data)

        totals['total_employees'] += 1
        totals['total_hours'] += hours
        totals['total_gross'] += gross_pay
        totals['total_tax'] += income_tax
        totals['total_net'] += net_pay

    display_totals(totals)


def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt).strip())
        except ValueError:
            print("Please enter a valid number.")


def calculate_pay(hours, rate, tax_rate):
    gross_pay = hours * rate
    income_tax = gross_pay * tax_rate
    net_pay = gross_pay - income_tax
    return gross_pay, income_tax, net_pay


def display_employee_payroll(employee_data):
    print(f"\nEmployee Name: {employee_data['name']}")
    print(f"From Date: {employee_data['from_date']}")
    print(f"To Date: {employee_data['to_date']}")
    print(f"Hours Worked: {employee_data['hours']}")
    print(f"Hourly Rate: {employee_data['rate']}")
    print(f"Gross Pay: {employee_data['gross_pay']}")
    print(f"Income Tax Rate: {employee_data['tax_rate']}")
    print(f"Income Tax: {employee_data['income_tax']}")
    print(f"Net Pay: {employee_data['net_pay']}")


def display_totals(total_data):
    print("\nPayroll Summary:")
    print(f"Total Number of Employees: {total_data['total_employees']}")
    print(f"Total Hours Worked: {total_data['total_hours']}")
    print(f"Total Gross Pay: {total_data['total_gross']}")
    print(f"Total Income Taxes: {total_data['total_tax']}")
    print(f"Total Net Pay: {total_data['total_net']}")


def write_employee_to_file(employee_data, filename="employee_data.txt"):
    with open(filename, 'a') as file:
        record = f"{employee_data['from_date']}|{employee_data['to_date']}|{employee_data['name']}|{employee_data['hours']}|{employee_data['rate']}|{employee_data['tax_rate']}\n"
        file.write(record)


if __name__ == "__main__":
    main()
