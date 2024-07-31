import numpy 

def double_list(size):
    inital_list = list(range(size))
    return [2 * i for i in inital_list]

def double_array(size):
    initial_array = numpy.arange(size)
    return 2 * initial_array

double_list(1_00_00)
double_array(1_00_00)