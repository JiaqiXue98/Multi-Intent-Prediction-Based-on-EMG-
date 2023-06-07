
# Jiaqi Xue 
import pandas as pd 
import numpy as np
import os

def read_data(data_path, split = "train"):
    """ Read data """

    # Fixed params
    n_channels=14
    n_class = 3
    n_steps = 300 #64
    overlap= 280

    rawdata=np.loadtxt(data_path)
    #array=rawdata.as_matrix()
    array=rawdata
    #print(len(array))
    
    num=((len(array)-n_steps)//(n_steps-overlap))+1
    #print("num",num)

    labels_r1=np.zeros((num,1))
    labels_r2=np.zeros((num,1))
    labels_c=np.zeros((num,1))
    #print(len(labels_r1))

    for i in range(num):
        labels_r1[i][0] =array[n_steps-1+i*(n_steps-overlap)][n_channels]
    for i in range(num):
        labels_r2[i][0] =array[n_steps-1+i*(n_steps-overlap)][n_channels+1]    
    for i in range(num):
        labels_c[i][0] =array[n_steps-1+i*(n_steps-overlap)][n_channels+2]     
    #print("len(labels)",len(labels))
    #print("len(labels[0])",len(labels[0]))        


    print("len(labels_r1)",len(labels_r1))
    print("(labels_r1[0])",labels_r1[0])
    print("(labels_c[0])",labels_c[0])    

    X = np.zeros((len(labels_r1), n_steps, n_channels))#three dimensional array  len(labels)
    #print(array)
    #i_ch = 0
    for j in range(num):

        start=j*n_steps-j*overlap
        X[j,...] = array[start:start+n_steps,0:n_channels] #error


    return X, labels_r1,labels_r2,labels_c
