bills =[]

import random

class Customer:
    def __init__(self):
        self.name   = ""
        self.number = ""
        self.adress = ""
        self.id     = ""

class Car:
    def __init__(self):
        self.branch     = ""
        self.model      = ""
        self.colour     = ""
        self.id         = ""
        self.max_speed  = 0
        self.kilometers = ""

    def start(self):
        print(f"car with serial number {self.id} started")

    def stop(self):
        print(f"car with serial number {self.id} stopped")
    
    def driven(self, km:int):
        print(f"car with serial number {self.id} moved")
        self.kilometers = self.kilometers + km

    def driven_current(self):
        print(str(self.driven))

class Bill:
    def __init__(self):
        self.car        = ""
        self.customer   = ""
        self.price      = ""
        self.bill_number= 0

def sell_car(customer_parameter:Customer, car_parameter:Car, price_parameter:int) -> bool:
    bill            = Bill()
    bill.car        = car_parameter
    bill.customer   = customer_parameter
    bill.price      = price_parameter
    bill.bill_number= random.randint(1000,10000) 
    
    try:
        bills.append(bill) 
        
    except Exception as ex:
        print(ex.message)
        print("Car wasn't sold")
        return False
    else:
        print("Car is sold")
        return True

def show_sold_cars():
    template = "Index: {}, Customer id: {}, Customer Name: {}, Car Serial Number: {}, Car Branch/Model: {}/{}, Car Price: {}"
    index=0
    for bill in bills:
        print(template.format(index, bill.bill_number, bill.customer.id, bill.customer.name, bill.car.id, bill.car.branch, bill.car.model, bill.price))
        index += 1
        print("----------------------------------------------------------------------------------")

def cancel_bill(bill_index:int):
    bill_which_will_be_canceled = bills[bill_index]
    print("Bill number which will be canceled", str(bill_which_will_be_canceled.bill_number))
    bills.pop(bill_index)
    options = input("bills will be canceled, are you sure? yes (press 'e'), no (press any key and enter)")
    if options==("e") or options==("E"):
        bills.pop(bill_index)
        print("Bill was canceled")

def show_options():
    print("""
    Get lists, press     (1)
    Sell car, press      (2)
    Cancel sold, press   (3)
    Quit press           (4)         
    """)

while True:
    show_options()
    options = input(":")

    if options =="1":
        show_sold_cars()
    elif options == "2":
        car             = Car()
        car.id          = input("please enter car id")
        car.branch      = "Ford"
        car.model       = "Focus"

        customer        = Customer()
        customer.id     = input("please enter your customer id")
        customer.name   = "cem"
        customer.number = "555444"
        bill_price      = int(input("please enter the price: "))

        result= sell_car(customer,car,bill_price)
        if result:
            pass
        else:
            pass
    
    elif options=="3":
        show_sold_cars()
        index_number_of_canceled_bill = int(input("please enter index number of canceled bill : "))
        cancel_bill(index_number_of_canceled_bill)

    elif options == "4":
        break
    else:
        print("Not found")





