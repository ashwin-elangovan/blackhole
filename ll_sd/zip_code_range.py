class ZipCodeRange:
    def __init__(self, start_zip_code, end_zip_code):
        self.start_zip_code = start_zip_code
        self.end_zip_code = end_zip_code

    def is_zip_code_in_range(self, zip_code):
        return self.start_zip_code <= zip_code <= self.end_zip_code

class Product:
    def __init__(self, name, zip_code_range):
        self.name = name
        self.zip_code_range = zip_code_range

    def is_zip_code_allowed(self, zip_code):
        return self.zip_code_range.is_zip_code_in_range(zip_code)

class Customer:
    def __init__(self, name, zip_code):
        self.name = name
        self.zip_code = zip_code

def can_deliver_product(product, customer):
    return product.is_zip_code_allowed(customer.zip_code)

# Example usage
product1 = Product("Product A", ZipCodeRange(10000, 19999))
product2 = Product("Product B", ZipCodeRange(20000, 29999))

customer1 = Customer("John", 15000)
customer2 = Customer("Jane", 25000)

print(f"Can deliver Product A to {customer1.name}? {can_deliver_product(product1, customer1)}")
print(f"Can deliver Product A to {customer2.name}? {can_deliver_product(product1, customer2)}")
print(f"Can deliver Product B to {customer1.name}? {can_deliver_product(product2, customer1)}")
print(f"Can deliver Product B to {customer2.name}? {can_deliver_product(product2, customer2)}")
