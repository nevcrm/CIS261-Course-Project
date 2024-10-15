
#// Name: Marcus Bracken
#// Course: CIS261 Object Oriented Computer Programming I
#: Lab: Course Project Phase 1: Create and Call Functions with Parameters

def get_employee_name():
    return input("Enter employee name (or 'End' to finish): ")

def get_hours_worked():
    return float(input("Enter total hours worked "))

def get_hourly_rate():
    return float(input("Enter hourly rate: "))

def get_tax_rate():
    return float(input("Enter income tax rate (as a decinal): "))

def calculate_pay(hours, rate, tax_rate):
    gross_pay = hours * rate
    income_tax = gross_pay * tax_rate
    net_pay = gross_pay - income_tax
    return gross_pay, income_tax, net_pay

def display_employee_payroll(name, hours, rate, gross_pay, tax_rate, income_tax, net_pay):
    print(f"\nEmployee Name: {name}")
    print(f"Hours Worked: {hours}")
    print(f"Hourly Rate: {rate}")
    print(f"Gross Pay: {gross_pay}")
    print(f"Income Tax Rate: {tax_rate}")
    print(f"Income Tax: {income_tax}")
    print(f"Net Pay: {net_pay}")

def display_totals(total_employees, total_hours, total_gross, total_tax, total_net):
    print(f"\nTotal Number of Employees: {total_employees}")
    print(f"total Hours Worked: {total_hours}")
    print(f"Total Gross Pay: {total_gross}")
    print(f"Total Income Taxes: {total_tax}")
    print(f"Total Net Pay: {total_net}")

def main():
    total_employees = 0
    total_hours = 0
    total_gross = 0
    total_tax = 0
    total_net = 0
    
    while True:
        name = get_employee_name()
        if name.lower() == 'end':
            break

        hours = get_hours_worked()
        rate = get_hourly_rate()
        tax_rate = get_tax_rate()

        gross_pay, income_tax, net_pay = calculate_pay(hours, rate, tax_rate)

        display_employee_payroll(name, hours, rate, gross_pay, tax_rate, income_tax, net_pay)
        total_employees +=1
        total_hours += hours
        total_gross += gross_pay
        total_tax += income_tax
        total_net += net_pay

    display_totals(total_employees, total_hours, total_gross, total_tax, total_net)

if __name__ == "__main__":
    main()