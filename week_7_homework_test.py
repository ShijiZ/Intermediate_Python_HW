import week_7_homework as w7h
import numpy as np

# Problem 1
list1 = [1, 2, 3, 4, 5, 6]
list2 = [1, 6, 10, 11]
is_in = w7h.list_is_in(list1, list2)
print(is_in)

# Problem 2
input_array = \
    np.array([[-0.47752694,  2.10771366, 0.59367963],
              [-0.99518782, -0.56534531, 0.01539558],
              [ 0.44353958,  1.31930398, 2.42232459]])

normalized_array = w7h.mean_normalize(input_array)
print(normalized_array)

# Problem 3
filepath = 'test.csv'

temp = w7h.temperature_model(filepath)
print(temp.mean_normalize())