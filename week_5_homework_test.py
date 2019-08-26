import week_5_homework as w5h
import logging
logging.basicConfig(filename='week5_homework.log', level=logging.DEBUG)

# Problem 1
@w5h.mylogging
def add_2(x):
    '''Add 2 to x'''
    return x + 2

print(add_2(5))

# Problem 2
person = w5h.Person(name='Joe', height=2, weight=80)
print(person.BMI)

# Problem 3
my_model = w5h.LinearModel(m=1, b=0)
y = my_model.predict(2)
assert y==2
print(y)