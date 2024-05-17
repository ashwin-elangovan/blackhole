class Customer:
    def __init__(self, name):
        self.name = name
        self.questions_asked = 0

    def ask_question(self):
        if self.questions_asked < 1:
            self.questions_asked += 1
            return True
        else:
            return False

class Vendor:
    def __init__(self, name):
        self.name = name
        self.questions_answered = 0

    def answer_question(self):
        if self.questions_answered < 5:
            self.questions_answered += 1
            return True
        else:
            return False

class QuestionSystem:
    def __init__(self):
        self.customers = []
        self.vendors = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def add_vendor(self, vendor):
        self.vendors.append(vendor)

    def ask_question(self, customer, vendor):
        if customer.ask_question() and vendor.answer_question():
            print(f"{customer.name} asked a question to {vendor.name}")
        else:
            print("Cannot ask/question limit exceeded")

# Example usage
system = QuestionSystem()

customer1 = Customer("John")
customer2 = Customer("Jane")

vendor1 = Vendor("Vendor 1")
vendor2 = Vendor("Vendor 2")

system.add_customer(customer1)
system.add_customer(customer2)

system.add_vendor(vendor1)
system.add_vendor(vendor2)

system.ask_question(customer1, vendor1)
system.ask_question(customer1, vendor1)
system.ask_question(customer2, vendor2)
system.ask_question(customer2, vendor2)
system.ask_question(customer2, vendor2)
system.ask_question(customer2, vendor2)
system.ask_question(customer2, vendor2)
