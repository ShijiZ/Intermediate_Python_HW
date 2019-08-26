import week_4_homework as w4h
import os

# Problem 1
raise_to_5 = w4h.raise_to_power(5)
result = raise_to_5(5)
print(result)

# Problem 2
filepath_a = '/Users/shijizhao/Documents/UCI/Courses/Intermediate Python/Week4/HW/test_a.txt'
write_to_file_a = w4h.file_writer(filepath_a)
write_to_file_a('This is the text that will be written in test_a.txt')

filepath_b = '/Users/shijizhao/Documents/UCI/Courses/Intermediate Python/Week4/HW/test_b.txt'
write_to_file_b = w4h.file_writer(filepath_b)
write_to_file_b('This is the text that will be written in test_b.txt')

# Problem 3
aesopa10_path = os.path.join(os.getcwd(), '../Week3/aesopa10.txt')
lines_of_the_file = w4h.word_n_of_each_line(3)
for word in lines_of_the_file(aesopa10_path):
    print(word)