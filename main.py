import random
from dataPrep import *
from auto_ELM import *

# Read Data from csv
#
# Files in Datasets:
#   int_test.csv
#   char_test.csv
#   endl_test.csv
#   shuffle_test.csv
#   olivettifaces.csv

raw_data = read_data('Datasets\shuffle_test.csv')

# Print raw data
#print_data(data,'s')
print("Raw data size")
print_data_size(raw_data)

# Transpose Data
rotated_data = transpose_data(raw_data)

print("Rotated data size")
print_data_size(rotated_data)

# Normilaize Data
norm_data = scale_data(rotated_data,255,0,1,0)

# Label Sorted data
labeled_data = label_data(norm_data,3)

# Print labeled data
#print_data(labeled_data,'f')

# Shuffle data
random.shuffle(labeled_data)

# Split in to trainning and testing data

[TR, TS] = split_data(labeled_data,0.5)

# Print divider
print("---------------------------------------------------")

# Print Trainning data
print("Trainning data size")
print_data_size(TR)
#print_data(TR,'f')

# Print testing data
print("Testing data size")
print_data_size(TS)
#print_data(TS,'f')

# Print divider
print("---------------------------------------------------")

C1=2^2; # you can set as 2^{-20} to 2^{20}
target_dimension=200;  # the desired dimension what you want
loop=10;  #  number of loop in each learning step, it could eqaul 2 to 10, but not too many differences.

[train_time_x,test_accuracy2_x,Training_x,Testing_x] = auto_ELM(TR,TS,1,target_dimension,'sine',C1,loop,0)


