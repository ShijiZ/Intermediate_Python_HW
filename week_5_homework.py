import logging

def mylogging(func):
    ''' Create a function that execute func, but add a logging
     entry to a log file everytime the function is called. '''
    def wrapper(*args, **kwargs):
        ''' Add a logging entry, which include the name of func
         and both positional and keyword arguments passed to func,
         to a log file. Then execute func.
        '''
        logging.debug("Function called: {}; Positional arguments: {}; Keyword arguments: {}"
        .format(func.__name__, args, kwargs))
        result = func(*args, **kwargs)
        return result
    return wrapper


class Person:
    ''' The Person class
    
    Parameters
    ----------
    name : str
        the name of the person
    
    weight : float, int
        the weight of the person
    '''
    
    def __init__(self, name, height, weight):
        ''' Initialize the person object with the name, height and weight of this person. '''
        self.name = name
        self.height = height
        self.weight = weight
    
    @property
    def BMI(self):
        ''' Return the Body Mass Index (BMI) of this person. '''
        return self.weight/(self.height)**2


class LinearModel:
    ''' The Linear Model class 
    
    Parameters
    ----------
    m : int, float
        the slope of the linear model
    
    b : int, float
        the intercept of the linear model
    '''

    def __init__(self, m, b):
        ''' Initialize the linear model object with the slope m and intercept b. '''
        self.m = m
        self.b = b
    
    def predict(self, x):
        ''' Return the prediction of output y given input x'''
        y = self.m*x + self.b
        return y
