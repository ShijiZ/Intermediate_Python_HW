import week_6_homework as w6h

# Problem 1
Corolla = w6h.Car(4, 4)
Corolla.drive()
Corolla.stop()
print("Wheels of car: ", Corolla.wheel) 

Harley = w6h.Motorcycle(2, 2)
Harley.drive()
Harley.stop()
Harley.wheelie()
print("Wheels of motorcycle: ", Harley.wheel) 

Tacoma = w6h.Truck(6, 6)
Tacoma.drive()
Tacoma.stop()
Tacoma.dump()
print("Wheels of truck: ", Tacoma.wheel)        

# Problem 2
my_list = w6h.NumericList((1, 2, 3))
print(my_list.product())

# Problem 3
customer_info_filepath = "/Users/shijizhao/Documents/UCI/Courses/Intermediate Python/Week6/customers.csv"
purchases_filepath = "/Users/shijizhao/Documents/UCI/Courses/Intermediate Python/Week6/purchases.csv"


customer_182764 = \
    w6h.Customer(customer_number=182764,
                       customer_info_filepath=customer_info_filepath,
                       purchases_filepath=purchases_filepath)

customer_182764.load_data()

print(customer_182764.name, customer_182764.age, customer_182764.state)
print(customer_182764.get_last_purchase())
print(customer_182764.get_first_purchase())
print(customer_182764.get_num_purchases())
print(customer_182764.get_sum_of_purchases())