import numpy as np

def findConsecutive(value, nparray):
    indices = []
    start = -1
    end = -1
    for i, element in enumerate(nparray):
        if element == value and start == -1:
            start = i
        elif element == value:
            end = i
        
        #have reached an element different than value or have reached the end --> have a set of indices to add to solution
        if (element!= value or nparray.size <= i + 1) and start != -1:
            indices.append([start,end])
            start = -1
            end = -1

    return indices


#data_index = np.array([0,0,0,0,0,1,1,1,1,1,0,0,0,0,0])
data_index = np. concatenate((np.zeros(np.random.randint(2,5)),np.ones(np.random.randint(2,5)))*np.random.randint(1,50))
print('array: ')
print(data_index)

print('answer: ')
print(findConsecutive(0, data_index))