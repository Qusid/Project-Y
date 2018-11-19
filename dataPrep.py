import csv
import sys

def read_data(file_name):
    _out_data = []
    i = 0
    f = open(file_name, 'r')
    with f:
        reader = csv.reader(f)
        for row in reader:
            _out_data.append([])
            for c in row:
                _out_data[i].append(c)
            i = i + 1
    return _out_data


def scale_data(in_data,input_high,input_low,output_high,output_low):
    out_data = []
    for i in range(len(in_data)):
        out_data.append([])
        for j in range(len(in_data[i])):
            out_data[i].append(((int(in_data[i][j]) - input_low) / (input_high - input_low)) * (output_high - output_low) + output_low)
    return out_data


def print_data(in_data,data_type):
    for row in range(len(in_data)):
        for col in range(len(in_data[row])):

            if data_type ==  'f':

                sys.stdout.write("Float")
                sys.stdout.write("%1.04f" % (in_data[row][col]))
                #print("%1.04f" % (in_data[row][col]), end = '')
            elif data_type ==  'i':
                sys.stdout.write("Int")
                #print("%i" % int(in_data[row][col]), end=' ')
            elif data_type == 'c':
                sys.stdout.write("Char")
                #print("%c" % (in_data[row][col]), end=' ')
            elif data_type == 's':
                sys.stdout.write("String")
                #print("%03s" % (in_data[row][col]), end=' ')
            else:
                sys.stdout.write(in_data[row][col])
                #print(in_data[row][col], end=' ')
        sys.stdout.write("\n")
        #print('')

def print_data_size(in_data):
    row_size  = len(in_data)
    col_size = len(in_data[0])
    print("%i x %i"% (row_size,col_size))

def transpose_data(in_data):
    return [*zip(*in_data)]

def label_data(_in_data,categories):
    for i in range(len(_in_data)):
        _in_data[i].insert(0, int(i / categories))
    return _in_data

def split_data(_all_data,_ratio):
    _training_data = []
    _testing_data = []
    _train_size = int(float(len(_all_data)) * _ratio)
    _test_size = int(float(len(_all_data)) * (1 - _ratio))
    for i in range(_train_size):
        _training_data.append(_all_data[i])
    for i in range(_test_size):
        _testing_data.append(_all_data[i + _train_size])
    return [_training_data,_testing_data]