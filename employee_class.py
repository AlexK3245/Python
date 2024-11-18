# Creating and using a Employee SuperClass
# and a ProductionWorker subclass
# along with instantiating (making objects)

class Employee:
    # Employee is a Superclass of the ProductionWorker class
    def __init__(self, employee_name, employee_number):
        self.employee_name = employee_name
        self.employee_number = employee_number

    # Getters and setter for the Superclass

    def get_employee_name(self):
        return self.__employee_name

    def get_employee_number(self):
        return self.__employee_number

    def set_employee_name(self, value):
        self.__employee_name = value

    def set_employee_number(self, value):
        self.__employee_number = value

    def __str__(self):
        return f"Name: {self.employee_name} \nEmployee number: {self.employee_number}"


class ProductionWorker(Employee):
    # ProductionWorker is the subclass of Employee
    def __init__(self, employee_name, employee_number, shift_number, hourly_pay_rate):
        super().__init__(employee_name, employee_number)
        self.shift_number = shift_number
        self.hourly_pay_rate = hourly_pay_rate

    # Getters and Setter for the subclass

    def get_shift_number(self):
        return self.__shift_number

    def get_hourly_pay_rate(self):
        return self.__hourly_pay_rate

    def set_shift_number(self, value):
        self.__shift_number = value

    def set_hourly_pay_rate(self, value):
        self.__hourly_pay_rate = value

    def __str__(self):
        return f"{super().__str__()} \nShift: {self.hourly_pay_rate} \nPay rate: ${self.shift_number} \nBeing a production worker"


def main():
    # This is the main portion of the function where everything is executed
    print("\n")
    print("Enter the following details of the Employee")
    print("\n")
    employee_name = input("Enter Employee Name: ")
    employee_number = input("Enter Employee number: ")
    hourly_pay_rate = input("Enter Pay Rate: $")
    shift_number = input("Enter Shift Number: ")
    if shift_number == "2":
        shift_number = "Night"
    elif shift_number == "1":
        shift_number = "Day"
    print("\n")
    print("Details of Employee:")
    print("\n")
    Employee_2 = ProductionWorker(
        employee_name, employee_number, hourly_pay_rate, shift_number)
    print(Employee_2)


main()
