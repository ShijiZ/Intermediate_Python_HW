import week_3_homework as w3h
import os

# Problem 1
result = w3h.all_the_kwags(my_kwags='this', second_kwag='that', some_number=1)
print(result)

# Problem 2
for n in w3h.almost_fibonacci(10):
    print(n)

# Problem 3
aesopa10_path = os.path.join(os.getcwd(), '../aesopa10.txt')
for word in w3h.first_word_of_each_line(aesopa10_path):
    print(word)
