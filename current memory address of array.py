from array import *
a_num=array('i', [1, 3, 4, 6, 5, 7, 8])
print("Original array : "+str(a_num))
print("current buffer memory  and length of array"+str(a_num.buffer_info()))
print("The size of the memory buffer in bytes"+str(a_num.buffer_info()[1]*a_num.itemsize))