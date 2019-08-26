# Problem 1
class Vehicle:
    '''A class to represent a vehicle
    
    Parameters
    ----------
    weight : flot, int
        the weight of the vehicle
    
    horsepower : float, int
        the horsepower of the vehicle
    '''
    def __init__(self, weight, horsepower):
        self.weight = weight
        self.horsepower = horsepower

    def drive(self):
        print('Now driving...')

    def stop(self):
        print('Now stopping...')
            
class Car(Vehicle):
    '''A class to represent a car
    
    Parameters
    ----------
    weight : float, int
        the weight of the car
    
    horsepower : float, int
        the horsepower of the car

    wheel : int
        the number of wheels of the car
    '''
    def __init__(self, weight, horsepower, wheel=4):
        self.wheel = wheel
        super().__init__(weight, horsepower)
        
class Motorcycle(Vehicle):
    '''A class to represent a motorcycle
    
    Parameters
    ----------
    weight : float, int
        the weight of the motorcycle
    
    horsepower : float, int
        the horsepower of the motorcycle
    
    wheel : int
        the number of wheels of the motorcycle
    '''
    def __init__(self, weight, horsepower, wheel=2):
        self.wheel = wheel
        super().__init__(weight, horsepower)
    
    def wheelie(self):
        print("Now wheelieing...")
        
class Truck(Vehicle):
    '''A class to represent a truck
    
    Parameters
    ----------
    weight : float, int
        the weight of the truck
    
    horsepower : float, int
        the horsepower of the truck
    
    wheel : int
        the number of wheels of the truck
    '''
    def __init__(self, weight, horsepower, wheel=6):
        self.wheel = wheel
        super().__init__(weight, horsepower)
    
    def dump(self):
        print("Now dumping...")


# Problem 2
class NumericList(list):
    '''A class that behaves just like a list with an additional method product()'''
    def product(self):
        '''Return the product of items in the list'''
        product = 1
        for i in self:
            product = product * i
        return product


# Problem 3
from datetime import datetime

class Customer:
    '''
    A class to model customers

    Parameters
    ----------
    customer_number : int, str
        the numerical customer id

    customer_info_filepath : str
        the filepath to the customer info file

    purchases_filepath : str
        the filepath to the purchases file
    '''
    def __init__(self, customer_number, customer_info_filepath,
                 purchases_filepath):
        self.customer_number = str(customer_number)
        self.customer_info_filepath = customer_info_filepath
        self.purchases_filepath = purchases_filepath
        self.purchases = {}

    def _load_customer_info(self):
        '''Load the data from the customer info file for this customer'''
        with open(self.customer_info_filepath, 'r') as read_file:
            for line in read_file:
                line_splits = line.strip().split(',')
                if line_splits[0] == self.customer_number:
                    self.name = line_splits[1]
                    self.age = line_splits[2]
                    self.state = line_splits[3]
                    break

    def _load_purchases(self):
        '''Load the purchases data from the purchases file, for this customer
        '''
        with open(self.purchases_filepath, 'r') as read_file:
            for line in read_file:
                line_splits = line.strip().split(',')
                if line_splits[0] == self.customer_number:
                    purchase_date = datetime.strptime(line_splits[1],
                                                      "%Y-%m-%d %H:%M:%S")
                    self.purchases[purchase_date] = line_splits[2]

    def load_data(self):
        '''Load all the customers data'''
        self._load_customer_info()
        self._load_purchases()

    def get_last_purchase(self):
        '''return the most recent purchase made by the customer'''
        return self.purchases[max(self.purchases.keys())]
    
    def get_first_purchase(self):
        '''return the first purchase made by the customer'''
        return self.purchases[min(self.purchases.keys())]

    def get_num_purchases(self):
        '''return the number of purchases the customer has made

        Note: If more than one purchases identified, only record the latest one'''
        return len(self.purchases)
    
    def get_sum_of_purchases(self):
        '''return the sum of all the purchases the customer as made
        
        Note: If more than one purchases identified, only record the latest one'''
        sum = 0
        for i in self.purchases.values():
            sum += float(i)
        return sum
