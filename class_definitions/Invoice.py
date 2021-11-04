"""
Program: Invoice.py
Author: Andy Volesky
Last date modified: 11/03/2021
The purpose of this program:

Write an Invoice class with the following data members, which are identified as required or optional in the constructor.
invoice_id - required
customer_id - required
last_name - required
first_name - required
phone_number - required
address - required
items_with_price - dictionary, optional
Methods:
constructor that sets all required items as listed above and uses appropriate default values for optional
built-ins (str() and repr())
add_item() that adds an item to items_with_price dictionary (Recall: what is the dictionary function to add?)
create_invoice() that prints each item and price, then a total with tax calculated

"""

class Invoice:
    """Invoice Class"""
    # Constructor
    def __init__(self, invid, custid, addy, lname, fname, phnum, item={}):
        self.invoice_id = invid
        self.customer_id = custid
        self.last_name = lname
        self.first_name = fname
        self.phone_number = phnum
        self.address = addy
        self.item_with_price = item

    def __str__(self):
        return self.customer_id + ": " + self.last_name + ", " + self.first_name + " Phone: " + self.phone_number + " Address: " + self.address

    def __repr__(self):
        return 'Customer({},{},{},{},{})'.format(self.customer_id, self.last_name, self.first_name, self.phone_number, self.address)

    def set_invoice_id(self, invid):
        self.invoice_id = invid

    def set_customer_id(self, custid):
        self.customer_id = custid

    def set_last_name(self, lname):
        self.last_name = lname

    def set_first_name(self, fname):
        self.first_name = fname

    def phone_number(self, phnum):
        self.phone_number = phnum

    def set_address(self, addy):
        self.address = addy

    def set_item_with_price(self, item):
        self.item_with_price = item

    def add_item(self, item_key):
        self.item_with_price.update(item_key)

    def create_invoice(self):
        total = 0
        for each in self.item_with_price:
            print(str(each) + "....." + str(self.item_with_price[each]))
            total += self.item_with_price[each]
        print("Tax....." +"{:.2f}".format(total*.06))
        print("Total....." + "{:.2f}".format(total*1.06))

# Driver code
invoice = Invoice(1, 123, '1313 Disneyland Dr, Anaheim, CA 92802' ,'Mouse', 'Minnie', '555-867-5309')
invoice.add_item({'iPad': 799.99})
invoice.add_item({'Surface': 999.99})
invoice.create_invoice()