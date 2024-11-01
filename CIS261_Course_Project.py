
#// Name: Marcus Bracken
#// Course: CIS261 Object Oriented Computer Programming I
#: Lab: Course Project Phase 2: Using Lists and Dictionaries to Store and Retrieve Data

from datetime import datetime

def get_employee_name():

    return input("Enter employee name (or 'End' to finish): ").strip()

def get_dates():

    while True:
        try:
            from_date = input("Enter from date (mm/dd/yyyy): ").strip()
            to_date = input("Enter to date (mm/dd/yyyy): ").strip()
            # Validate date format
            datetime.strptime(from_date, "%m/%d/%Y")
            datetime.strptime(to_date, "%m/%d/%Y")
            return from_date, to_date
        except ValueError:
            print("Invalid date format. Please enter dates in mm/dd/yyyy format.")

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

def main():

    totals = {
        'total_employees': 0,
        'total_hours': 0,
        'total_gross': 0,
        'total_tax': 0,
        'total_net': 0
    }
    employee_records = []

    while True:
        name = get_employee_name()
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

        totals['total_employees'] += 1
        totals['total_hours'] += hours
        totals['total_gross'] += gross_pay
        totals['total_tax'] += income_tax
        totals['total_net'] += net_pay


    display_totals(totals)

if __name__ == "__main__":
    main()

