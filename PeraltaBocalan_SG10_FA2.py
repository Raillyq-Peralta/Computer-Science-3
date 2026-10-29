# Raillyq Lairdswill S. Peralta | Rachel Bocalan
# 9-Lithium | 10-29-26

# PATIENT CLASS
class Patient:
    # CONSTRUCTOR
    def __init__(self, name, bill_amount):
        self.__name = name
        self.__bill_amount = bill_amount

    # METHODS
    def calculate_bill(self):
        return self.__new_bill_amount

    # GETTERS AND SETTERS
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def bill_amount(self):
        return self.__bill_amount

    @bill_amount.setter
    def bill_amount(self, new_bill_amount):
        self.__new_bill_amount = new_bill_amount

    @property
    def new_bill_amount(self):
        self.__new_bill_amount = self.__bill_amount
        return self.__new_bill_amount
    
# SENIOR PATIENT CLASS
class SeniorPatient(Patient):
    # METHODS
    def calculate_bill(self, bill_amount):
        discount = bill_amount * .20
        self.__new_bill_amount = bill_amount - discount
        return self.__new_bill_amount

# PHILHEALTH PATIENT CLASS
class PhilHealthPatient(Patient):
    # METHODS
    def calculate_bill(self, bill_amount):
            discount = bill_amount * .15
            self.__new_bill_amount = bill_amount - discount
            return self.__new_bill_amount

# OBJECTS
regular_patient = Patient("Juan Dela Cruz", 15000)
senior_patient = SeniorPatient("Maria Santos", 15000)
philhealth_patient = PhilHealthPatient("Pedro Reyes", 15000)

# OUTPUT
print("Hospital Billing System")
print("-----------------------")
print(f"Patient Name: {regular_patient.name}")
print(f"Original Bill: ₱{regular_patient.bill_amount:,.2f}")
print(f"Final Bill: ₱{regular_patient.new_bill_amount:,.2f}")

print(f"\nPatient Name: {senior_patient.name}")
print(f"Original Bill: ₱{senior_patient.bill_amount:,.2f}")
print(f"Final Bill: ₱{senior_patient.calculate_bill(senior_patient.bill_amount):,.2f}")

print(f"\nPatient Name: {philhealth_patient.name}")
print(f"Original Bill: ₱{philhealth_patient.bill_amount:,.2f}")
print(f"Final Bill: ₱{philhealth_patient.calculate_bill(philhealth_patient.bill_amount):,.2f}")