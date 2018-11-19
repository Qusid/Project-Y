import time
from dataPrep import *
from scipy.linalg import orth

def hello_world():
    print("Hello, World")

# makeshift struct
class data_struct:
    P = []
    T = []

def auto_ELM(train_data, test_data, Elm_Type, NumberofHiddenNeurons, ActivationFunction,C,kkkk,type):

# Input:
# train_data - training data set
# test_data - testing data set
# Elm_Type - 1 for classification only
# NumberofHiddenNeurons - desired dimensional target
# ActivationFunction - Type of activation function:
# 'sig'
# for Sigmoidal function
# 'sin' for Sine function
#
# kkkk - Number of internal loop(normally set 2).
# type - activation usage.
# Output:
# TrainingTime - Time(seconds) spent on training ELM
# TestingAccuracy - Testing accuracy:
# RMSE for reconstruction error


# Authors: YIMIN YANG, Q.M.Jonathan Wu, and YAONAN WANG
# DATE: APRIL 2017
# The current version is still not optimized

# Macro definition
    REGRESSION=0
    fdafe=0

# Load training dataset
    T = []
    for i in range(len(train_data)):
        T.append(train_data[i].pop(0))
    OrgT = T
    P = train_data
    del train_data # Release raw training data array

# Load testing dataset

    TV = data_struct()
    for i in range(len(test_data)):
        TV.T.append(test_data[i].pop(0))
    OrgTT = TV.T
    TV.P = test_data
    del test_data # Release raw testing data array

    #print(len(P))
    #print(len(TV.P))
    #print(len(TV.P[0]))

    NumberofTrainingData = len(P)
    print(NumberofTrainingData)

    NumberofTestingData = len(TV.P)
    NumberofInputNeurons = len(P[0])

    if Elm_Type != REGRESSION:
        # Preprocessing the data of classification
        sorted_target = TV.T + T
        sorted_target.sort()
        # Find and save in 'label' class label from training and testing data sets

        label = zeros(1,1)
        label[0] = sorted_target[0]

        #label = []
        #label.append(sorted_target[0])# index starts at 0 in python and 1 in matlab

        j = 0 # index starts at 0 in python and 1 in matlab
        for i in range(1,NumberofTrainingData + NumberofTestingData):
            if sorted_target[i] != label[j]:
                j = j + 1
                label.append(sorted_target[i])
        number_class = j
        NumberofOutputNeurons = number_class

        # print(sorted_target)
        # print(label)


        # Processing the targets of training
        temp_T = zeros(NumberofOutputNeurons,NumberofTrainingData)

        print("Temp Target")
        print_data_size(temp_T)

        for i in range(NumberofTrainingData):
            for j in range(number_class):
                if label[j] == T[i]:
                    break
            temp_T[j][i] = 1

        #print(temp_T)

        #TV.T = array_times_const(temp_T,2,-1) #T = (temp_T*2-1)

    # end if of Elm_Type
    start_time_train = time.time()
    # Need to add timer

    # useless test. always count = 1
    #-------------------------------------------
    # Calculate weights & biases
    for j in range(0,kkkk):
        if j == 1:
            count = 1;
        else:
            count = 1
    #-------------------------------------------


    #Random generate input weights InputWeight(w_i) and biases BiasofHiddenNeurons(b_i) of hidden neurons
    for nxh in range(count):
        if j == 1:

            BiasofHiddenNeurons1 = rand_list(NumberofHiddenNeurons)
            BiasofHiddenNeurons1 = orth(BiasofHiddenNeurons1)
            #print(BiasofHiddenNeurons1)

            BiasofHiddenNeurons1 = orth(BiasofHiddenNeurons1)
            BBP = BiasofHiddenNeurons1

            InputWeight = rand_list(NumberofHiddenNeurons,NumberofInputNeurons)#*2-1


    # Placeholders to be fixed when I get there
    train_time = 1
    test_accuracy = 2
    Training = 3
    Testing = 4

    TrainingTime = 1
    TestingAccuracy = 2
    Training = 3
    Testing = 4
    return  [TrainingTime, TestingAccuracy, Training, Testing]

def zeros(x,y):
    array = []
    for i in range(x):
        array.append([])
        for j in range(y):
            array[i].append(0)
    return array

def array_times_const(array, proctuct, term):
    output = []
    for i in range(len(array)):
        output.append([])
        for j in range(len(array[0])):
            output[i][j] = array[i][j] * proctuct + term
    return output
import random

def rand_list(array_size):
    array = []
    for i in range(array_size):
        array.append(random.random())
    return array

def orth (matrix):
    return matrix
