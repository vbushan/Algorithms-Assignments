# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 22:50:35 2020

@author: Vamsi
"""

import sys
sys . setrecursionlimit ( 50000 )

import resource
resource . setrlimit ( resource . RLIMIT_STACK , ( resource . RLIM_INFINITY , resource . RLIM_INFINITY ) )

import random
import time


def partition_rqs(arr,low,high):
  pivot=arr[high]
  i=low-1

  for j in range (low,high):
    if arr[j]<pivot:
      i+=1
      arr[i],arr[j]=arr[j],arr[i]
  
  arr[i+1],arr[high]=arr[high],arr[i+1]

  return i+1



def qsort(arr,low,high):
  #print('Before random swap',arr)
  if low<high:
    rpivot=random.randrange(low,high)
    arr[high],arr[rpivot]=arr[rpivot],arr[high]
    #print('After random swap',arr)
    pindex=partition_rqs(arr,low,high)
    #print('After partition',arr)
    qsort(arr,low,pindex-1)
    qsort(arr,pindex+1,high)
   

def dqs(arr,low,high):
  if low<high:
    if high-low>=2:
      random_index=random.sample(list(range(low,high)),2)
      arr[low],arr[random_index[0]]=arr[random_index[0]],arr[low]
      arr[high],arr[random_index[1]]=arr[random_index[1]],arr[high]
       
    lp,rp=partition_dqs(arr,low,high)
    dqs(arr,low,lp-1)
    dqs(arr,lp+1,rp-1)
    dqs(arr,rp+1,high)
    
    

def partition_dqs(arr,low,high):
    if arr[low]>arr[high]:
        arr[low],arr[high]=arr[high],arr[low]
    
    j=low+1
    g=high-1
    k=low+1
    p=arr[low]
    q=arr[high]
    while(k<=g):
        if arr[k]<p:
            arr[k],arr[j]=arr[j],arr[k]
            j+=1
        
        elif(arr[k]>=q):
            while (arr[g]>q and k<g):
                g-=1
            arr[k],arr[g]=arr[g],arr[k]
            g-=1
            if arr[k]<p:
                arr[k],arr[j]=arr[j],arr[k]
                j+=1
        k+=1
    j-=1
    g+=1
    
    arr[low],arr[j]=arr[j],arr[low]
    arr[high],arr[g]=arr[g],arr[high]
    
    return j,g


def ins_sort(arr):
    x=list(arr)
    count=0
    ins_start_time=time.time()
    
    for i in range(1,len(x)):
        pivot=x[i]
        j=i-1
        
        while(j>=0) and pivot<x[j]:
            #if pivot>x[j]:
            #    break
            x[j+1],x[j]=x[j],x[j+1]
            j-=1
            count+=1
        
        count+=1
    ins_end_time=time.time()
    
    return (ins_end_time-ins_start_time,count,x)


#The below function generates a list with length equal to the size parameter, and elements of the list are random numbers between (1,size)
def generate_inputs(size):
    return [random.randint(1,size) for k in range(0,size)]

#The below function swaps two elements in the input list at random.
def swap_inputs(arr):
    indexes=list(range(len(arr)))
    swap_indexes=[]
    for i in range(0,50):
        swap_indexes=random.sample(indexes,2)
        arr[swap_indexes[0]],arr[swap_indexes[1]]=arr[swap_indexes[1]],arr[swap_indexes[0]]
    
    return arr


#The function below generates the first plot.
def part_1():
  #Plot 1
    
  #Generate Inputs for Plot 1
  input_sizes=[i*5000 for i in range(1,7)]


  ins_avg_time=[]
  qs_avg_time=[]
  dqs_avg_time=[]

  for i in input_sizes:
    #input for insertion sort
    input_1=generate_inputs(i)
    input_2=generate_inputs(i)
    input_3=generate_inputs(i)
    
    #input for random pivot quick sort
    qs_input_1=list(input_1)
    qs_input_2=list(input_2)
    qs_input_3=list(input_3)

    #input for random dual pivot quick sort
    dqs_input_1=list(input_1)
    dqs_input_2=list(input_2)
    dqs_input_3=list(input_3)

    
    ins_avg_time.append((ins_sort(input_1)[0]+ins_sort(input_2)[0]+ins_sort(input_3)[0])/3)
    
    #Quick sort average time for one input size
    qs_time=0
    start_time=time.time()
    qsort(qs_input_1,0,len(qs_input_1)-1)
    end_time=time.time()
    if qs_input_1!=sorted(input_1):
        print('Wrong code') 
    qs_time+=(end_time-start_time)

    start_time=time.time()
    qsort(qs_input_2,0,len(qs_input_2)-1)
    end_time=time.time()
    
    if qs_input_2!=sorted(input_2):
        print('Wrong code')
    
    qs_time+=(end_time-start_time)

    start_time=time.time()
    qsort(qs_input_3,0,len(qs_input_3)-1)
    end_time=time.time()
    
    


    if qs_input_3!=sorted(input_3):
        print('Wrong code')
    
    qs_time+=(end_time-start_time)
    
    qs_avg_time.append(qs_time/3)

    #Dual pivot Quick sort average time for one input size
    dqs_time=0
    start_time=time.time()
    dqs(dqs_input_1,0,len(dqs_input_1)-1)
    end_time=time.time()
    if dqs_input_1!=sorted(input_1):
        print('Wrong code') 
    dqs_time+=(end_time-start_time)

    start_time=time.time()
    dqs(dqs_input_2,0,len(dqs_input_2)-1)
    end_time=time.time()
    
    if dqs_input_2!=sorted(input_2):
        print('Wrong code')
    
    dqs_time+=(end_time-start_time)

    start_time=time.time()
    dqs(dqs_input_3,0,len(dqs_input_3)-1)
    end_time=time.time()
    
    dqs_time+=(end_time-start_time)


    if dqs_input_3!=sorted(input_3):
        print('Wrong code')
    dqs_avg_time.append(dqs_time/3)

  print(ins_avg_time)
  print(qs_avg_time)
  print(dqs_avg_time)

  from matplotlib import pyplot as plt
  fig = plt.figure(figsize=(15, 15))
  plt.plot(input_sizes,ins_avg_time,label='Insertion sort')
  plt.plot(input_sizes,qs_avg_time,label='Quick Sort')
  plt.plot(input_sizes,dqs_avg_time,label='Dual pivot Quick Sort')
  plt.ylabel('Running time')
  plt.xlabel('Input size')
  plt.title('Plot 1')
  fig.savefig('plot1.png', dpi=fig.dpi)

  plt.legend()

part_1()

def part_2():
  #Plot 2
    
  #Generate Inputs for Plot 2
  input_sizes=[i*5000 for i in range(1,7)]


  ins_avg_time=[]
  qs_avg_time=[]
  dqs_avg_time=[]

  for i in input_sizes:
    #input for insertion sort
    input_1=sorted(generate_inputs(i))
    input_2=sorted(generate_inputs(i))
    input_3=sorted(generate_inputs(i))
    
    #input for random pivot quick sort
    qs_input_1=list(input_1)
    qs_input_2=list(input_2)
    qs_input_3=list(input_3)

    #input for random dual pivot quick sort
    dqs_input_1=list(input_1)
    dqs_input_2=list(input_2)
    dqs_input_3=list(input_3)

    
    ins_avg_time.append((ins_sort(input_1)[0]+ins_sort(input_2)[0]+ins_sort(input_3)[0])/3)
    
    #Quick sort average time for one input size
    qs_time=0
    start_time=time.time()
    qsort(qs_input_1,0,len(qs_input_1)-1)
    end_time=time.time()
    if qs_input_1!=sorted(input_1):
        print('Wrong code') 
    qs_time+=(end_time-start_time)

    start_time=time.time()
    qsort(qs_input_2,0,len(qs_input_2)-1)
    end_time=time.time()
    
    if qs_input_2!=sorted(input_2):
        print('Wrong code')
    
    qs_time+=(end_time-start_time)

    start_time=time.time()
    qsort(qs_input_3,0,len(qs_input_3)-1)
    end_time=time.time()
    
    


    if qs_input_3!=sorted(input_3):
        print('Wrong code')
    
    qs_time+=(end_time-start_time)
    
    qs_avg_time.append(qs_time/3)

    #Dual pivot Quick sort average time for one input size
    dqs_time=0
    start_time=time.time()
    dqs(dqs_input_1,0,len(dqs_input_1)-1)
    end_time=time.time()
    if dqs_input_1!=sorted(input_1):
        print('Wrong code') 
    dqs_time+=(end_time-start_time)

    start_time=time.time()
    dqs(dqs_input_2,0,len(dqs_input_2)-1)
    end_time=time.time()
    
    if dqs_input_2!=sorted(input_2):
        print('Wrong code')
    
    dqs_time+=(end_time-start_time)

    start_time=time.time()
    dqs(dqs_input_3,0,len(dqs_input_3)-1)
    end_time=time.time()
    
    dqs_time+=(end_time-start_time)


    if dqs_input_3!=sorted(input_3):
        print('Wrong code')
    dqs_avg_time.append(dqs_time/3)

  print(ins_avg_time)
  print(qs_avg_time)
  print(dqs_avg_time)

  from matplotlib import pyplot as plt
  fig = plt.figure(figsize=(15, 15))
  plt.plot(input_sizes,ins_avg_time,label='Insertion sort')
  plt.plot(input_sizes,qs_avg_time,label='Quick Sort')
  plt.plot(input_sizes,dqs_avg_time,label='Dual pivot Quick Sort')
  plt.ylabel('Running time')
  plt.xlabel('Input size')
  plt.title('Plot 2')
  fig.savefig('plot2.png', dpi=fig.dpi)

  plt.legend()

part_2()
#The function below generates the third plot.
def part_3():
  #Plot 1
    
  #Generate Inputs for Plot 3
  input_sizes=[i*5000 for i in range(1,7)]


  ins_avg_time=[]
  qs_avg_time=[]
  dqs_avg_time=[]

  for i in input_sizes:
    #input for insertion sort
    input_1=sorted(generate_inputs(i),reverse=True)
    input_2=sorted(generate_inputs(i),reverse=True)
    input_3=sorted(generate_inputs(i),reverse=True)
    
    #input for random pivot quick sort
    qs_input_1=list(input_1)
    qs_input_2=list(input_2)
    qs_input_3=list(input_3)

    #input for random dual pivot quick sort
    dqs_input_1=list(input_1)
    dqs_input_2=list(input_2)
    dqs_input_3=list(input_3)

    
    ins_avg_time.append((ins_sort(input_1)[0]+ins_sort(input_2)[0]+ins_sort(input_3)[0])/3)
    
    #Quick sort average time for one input size
    qs_time=0
    start_time=time.time()
    qsort(qs_input_1,0,len(qs_input_1)-1)
    end_time=time.time()
    if qs_input_1!=sorted(input_1):
        print('Wrong code') 
    qs_time+=(end_time-start_time)

    start_time=time.time()
    qsort(qs_input_2,0,len(qs_input_2)-1)
    end_time=time.time()
    
    if qs_input_2!=sorted(input_2):
        print('Wrong code')
    
    qs_time+=(end_time-start_time)

    start_time=time.time()
    qsort(qs_input_3,0,len(qs_input_3)-1)
    end_time=time.time()
    
    


    if qs_input_3!=sorted(input_3):
        print('Wrong code')
    
    qs_time+=(end_time-start_time)
    
    qs_avg_time.append(qs_time/3)

    #Dual pivot Quick sort average time for one input size
    dqs_time=0
    start_time=time.time()
    dqs(dqs_input_1,0,len(dqs_input_1)-1)
    end_time=time.time()
    if dqs_input_1!=sorted(input_1):
        print('Wrong code') 
    dqs_time+=(end_time-start_time)

    start_time=time.time()
    dqs(dqs_input_2,0,len(dqs_input_2)-1)
    end_time=time.time()
    
    if dqs_input_2!=sorted(input_2):
        print('Wrong code')
    
    dqs_time+=(end_time-start_time)

    start_time=time.time()
    dqs(dqs_input_3,0,len(dqs_input_3)-1)
    end_time=time.time()
    
    dqs_time+=(end_time-start_time)


    if dqs_input_3!=sorted(input_3):
        print('Wrong code')
    dqs_avg_time.append(dqs_time/3)

  print(ins_avg_time)
  print(qs_avg_time)
  print(dqs_avg_time)

  from matplotlib import pyplot as plt
  fig = plt.figure(figsize=(15, 15))
  plt.plot(input_sizes,ins_avg_time,label='Insertion sort')
  plt.plot(input_sizes,qs_avg_time,label='Quick Sort')
  plt.plot(input_sizes,dqs_avg_time,label='Dual pivot Quick Sort')
  plt.ylabel('Running time')
  plt.xlabel('Input size')
  plt.title('Plot 3')
  fig.savefig('plot3.png', dpi=fig.dpi)

  plt.legend()

part_3()

#The function below generates the fourth plot.
def part_4():






  #Plot 4
    
  #Generate Inputs for Plot 4
  input_sizes=[i*5000 for i in range(1,7)]

  ins_avg_time=[]
  qs_avg_time=[]
  dqs_avg_time=[]

  
  for i in input_sizes:
    input_1=swap_inputs(sorted(generate_inputs(i)))
    input_2=swap_inputs(sorted(generate_inputs(i)))
    input_3=swap_inputs(sorted(generate_inputs(i)))
    ins_avg_time.append((ins_sort(input_1)[0]+ins_sort(input_2)[0]+ins_sort(input_3)[0])/3)
    

    #input for random pivot quick sort
    qs_input_1=list(input_1)
    qs_input_2=list(input_2)
    qs_input_3=list(input_3)

    #input for random dual pivot quick sort
    dqs_input_1=list(input_1)
    dqs_input_2=list(input_2)
    dqs_input_3=list(input_3)

    
    #ins_avg_time.append((ins_sort(input_1)[0]+ins_sort(input_2)[0]+ins_sort(input_3)[0])/3)
    
    #Quick sort average time for one input size
    qs_time=0
    start_time=time.time()
    qsort(qs_input_1,0,len(qs_input_1)-1)
    end_time=time.time()
    if qs_input_1!=sorted(input_1):
        print('Wrong code') 
    qs_time+=(end_time-start_time)

    start_time=time.time()
    qsort(qs_input_2,0,len(qs_input_2)-1)
    end_time=time.time()
    
    if qs_input_2!=sorted(input_2):
        print('Wrong code')
    
    qs_time+=(end_time-start_time)

    start_time=time.time()
    qsort(qs_input_3,0,len(qs_input_3)-1)
    end_time=time.time()
    
    


    if qs_input_3!=sorted(input_3):
        print('Wrong code')
    
    qs_time+=(end_time-start_time)
    
    qs_avg_time.append(qs_time/3)

    #Dual pivot Quick sort average time for one input size
    dqs_time=0
    start_time=time.time()
    dqs(dqs_input_1,0,len(dqs_input_1)-1)
    end_time=time.time()
    if dqs_input_1!=sorted(input_1):
        print('Wrong code') 
    dqs_time+=(end_time-start_time)

    start_time=time.time()
    dqs(dqs_input_2,0,len(dqs_input_2)-1)
    end_time=time.time()
    
    if dqs_input_2!=sorted(input_2):
        print('Wrong code')
    
    dqs_time+=(end_time-start_time)

    start_time=time.time()
    dqs(dqs_input_3,0,len(dqs_input_3)-1)
    end_time=time.time()
    
    dqs_time+=(end_time-start_time)


    if dqs_input_3!=sorted(input_3):
        print('Wrong code')
    dqs_avg_time.append(dqs_time/3)

  print(ins_avg_time)
  print(qs_avg_time)
  print(dqs_avg_time)

  from matplotlib import pyplot as plt
  fig = plt.figure(figsize=(15, 15))
  plt.plot(input_sizes,ins_avg_time,label='Insertion sort')
  plt.plot(input_sizes,qs_avg_time,label='Quick Sort')
  plt.plot(input_sizes,dqs_avg_time,label='Dual pivot Quick Sort')
  plt.ylabel('Running time')
  plt.xlabel('Input size')
  plt.title('Plot 4')
  fig.savefig('plot4.png', dpi=fig.dpi)

  plt.legend()


part_4()

#The function below generates the fifth plot.
def part_5():
  #Plot 5
    
  #Generate Inputs for Plot 1
  input_sizes=[i*5000 for i in range(1,7)]


  ins_avg_time=[]
  qs_avg_time=[]
  dqs_avg_time=[]

  for i in input_sizes:
    #input for insertion sort
    input_1=[random.randint(0,i)]*i
    input_2=[random.randint(0,i)]*i
    input_3=[random.randint(0,i)]*i
    
    #input for random pivot quick sort
    qs_input_1=list(input_1)
    qs_input_2=list(input_2)
    qs_input_3=list(input_3)

    #input for random dual pivot quick sort
    dqs_input_1=list(input_1)
    dqs_input_2=list(input_2)
    dqs_input_3=list(input_3)

    
    ins_avg_time.append((ins_sort(input_1)[0]+ins_sort(input_2)[0]+ins_sort(input_3)[0])/3)
    
    #Quick sort average time for one input size
    qs_time=0
    start_time=time.time()
    qsort(qs_input_1,0,len(qs_input_1)-1)
    end_time=time.time()
    if qs_input_1!=sorted(input_1):
        print('Wrong code') 
    qs_time+=(end_time-start_time)

    start_time=time.time()
    qsort(qs_input_2,0,len(qs_input_2)-1)
    end_time=time.time()
    
    if qs_input_2!=sorted(input_2):
        print('Wrong code')
    
    qs_time+=(end_time-start_time)

    start_time=time.time()
    qsort(qs_input_3,0,len(qs_input_3)-1)
    end_time=time.time()
    
    


    if qs_input_3!=sorted(input_3):
        print('Wrong code')
    
    qs_time+=(end_time-start_time)
    
    qs_avg_time.append(qs_time/3)

    #Dual pivot Quick sort average time for one input size
    dqs_time=0
    start_time=time.time()
    dqs(dqs_input_1,0,len(dqs_input_1)-1)
    end_time=time.time()
    if dqs_input_1!=sorted(input_1):
        print('Wrong code') 
    dqs_time+=(end_time-start_time)

    start_time=time.time()
    dqs(dqs_input_2,0,len(dqs_input_2)-1)
    end_time=time.time()
    
    if dqs_input_2!=sorted(input_2):
        print('Wrong code')
    
    dqs_time+=(end_time-start_time)

    start_time=time.time()
    dqs(dqs_input_3,0,len(dqs_input_3)-1)
    end_time=time.time()
    
    dqs_time+=(end_time-start_time)


    if dqs_input_3!=sorted(input_3):
        print('Wrong code')
    dqs_avg_time.append(dqs_time/3)

  print(ins_avg_time)
  print(qs_avg_time)
  print(dqs_avg_time)

  from matplotlib import pyplot as plt
  fig = plt.figure(figsize=(15, 15))
  plt.plot(input_sizes,ins_avg_time,label='Insertion sort')
  plt.plot(input_sizes,qs_avg_time,label='Quick Sort')
  plt.plot(input_sizes,dqs_avg_time,label='Dual pivot Quick Sort')
  plt.ylabel('Running time')
  plt.xlabel('Input size')
  plt.title('Plot 5')
  fig.savefig('plot5.png', dpi=fig.dpi)

  plt.legend()

part_5()

#The function below is the implementation of Part 6 of the assignment.
def part_6():
  ins_time=[]
  qs_time=[]
  dqs_time=[]

  for i in range(0,100000):
    input_array=generate_inputs(50)
    
    ins_input=list(input_array)
    ins_time.append(ins_sort(ins_input)[0])

    qs_input=list(input_array)
    qs_start=time.time()
    qsort(qs_input,0,len(qs_input)-1)
    qs_end=time.time()
    if qs_input!=sorted(input_array):
      print('Wrong implementation')
    qs_time.append(qs_end-qs_start)

    dqs_input=list(input_array)
    dqs_start=time.time()
    dqs(dqs_input,0,len(dqs_input)-1)
    dqs_end=time.time()

    if dqs_input!=sorted(input_array):
      print('Wrong implementation')
    dqs_time.append(dqs_end-dqs_start)

  
  print('Average time of insertion sort',sum(ins_time)/len(ins_time))
  print('Average time of quick sort',sum(qs_time)/len(qs_time))
  print('Average time of dual pivot quick sort',sum(dqs_time)/len(dqs_time))


part_6()