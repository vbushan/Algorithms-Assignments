# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 17:17:49 2020

@author: Vamsi
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 18:26:49 2020

@author: Vamsi
"""
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 18:14:12 2020

@author: Vamsi
"""

import random

import time

#Implementation of Insertion Sort
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

#Implementation of Bubble Sort
def optimized_bubble_sort(x):
    arr=list(x)
    count=0
    bbs_start_time=time.time()
    for i in range(len(arr)):
        count1=0
        for j in range(1,len(arr)):
            if arr[j-1]>arr[j]:
                arr[j-1],arr[j]=arr[j],arr[j-1]
                count1+=1
            count+=1
        if count1==0:
            break
    bbs_end_time=time.time()

    
    return (bbs_end_time-bbs_start_time,count,arr)

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
  bbs_avg_time=[]
  for i in input_sizes:
    input_1=generate_inputs(i)
    input_2=generate_inputs(i)
    input_3=generate_inputs(i)
    ins_avg_time.append((ins_sort(input_1)[0]+ins_sort(input_2)[0]+ins_sort(input_3)[0])/3)
    bbs_avg_time.append((optimized_bubble_sort(input_1)[0]+optimized_bubble_sort(input_2)[0]+optimized_bubble_sort(input_3)[0])/3)



  print(ins_avg_time)
  print(bbs_avg_time)

  from matplotlib import pyplot as plt
  fig = plt.figure(figsize=(15, 15))
  plt.plot(input_sizes,ins_avg_time,label='Insertion sort')
  plt.plot(input_sizes,bbs_avg_time,label='Bubble sort')
  plt.ylabel('Running time')
  plt.xlabel('Input size')
  plt.title('Plot 1')
  fig.savefig('plot1.png', dpi=fig.dpi)

  plt.legend()

part_1()

#The function below generates the second plot.
def part_2():
  #Plot 2
    
  #Generate Inputs for Plot 2
  input_sizes=[i*5000 for i in range(1,7)]

  ins_avg_time=[]
  bbs_avg_time=[]
  for i in input_sizes:
    input_1=sorted(generate_inputs(i))
    input_2=sorted(generate_inputs(i))
    input_3=sorted(generate_inputs(i))
    ins_avg_time.append((ins_sort(input_1)[0]+ins_sort(input_2)[0]+ins_sort(input_3)[0])/3)
    bbs_avg_time.append((optimized_bubble_sort(input_1)[0]+optimized_bubble_sort(input_2)[0]+optimized_bubble_sort(input_3)[0])/3)



  print(ins_avg_time)
  print(bbs_avg_time)

  from matplotlib import pyplot as plt
  fig = plt.figure(figsize=(15, 15))
  plt.plot(input_sizes,ins_avg_time,label='Insertion sort')
  plt.plot(input_sizes,bbs_avg_time,label='Bubble sort')
  plt.ylabel('Running time')
  plt.xlabel('Input size')
  plt.title('Plot 2')
  plt.legend()
  fig.savefig('plot2.png', dpi=fig.dpi)
part_2()

#The function below generates the third plot.
def part_3():
  #Plot 3
    
  #Generate Inputs for Plot 3
  input_sizes=[i*5000 for i in range(1,7)]

  ins_avg_time=[]
  bbs_avg_time=[]
  for i in input_sizes:
    input_1=sorted(generate_inputs(i),reverse=True)
    input_2=sorted(generate_inputs(i),reverse=True)
    input_3=sorted(generate_inputs(i),reverse=True)
    ins_avg_time.append((ins_sort(input_1)[0]+ins_sort(input_2)[0]+ins_sort(input_3)[0])/3)
    bbs_avg_time.append((optimized_bubble_sort(input_1)[0]+optimized_bubble_sort(input_2)[0]+optimized_bubble_sort(input_3)[0])/3)



  print(ins_avg_time)
  print(bbs_avg_time)

  from matplotlib import pyplot as plt
  fig = plt.figure(figsize=(15, 15))

  plt.plot(input_sizes,ins_avg_time,label='Insertion sort')
  plt.plot(input_sizes,bbs_avg_time,label='Bubble sort')
  plt.ylabel('Running time')
  plt.xlabel('Input size')
  plt.title('Plot 3')

  plt.legend()
  fig.savefig('plot3.png', dpi=fig.dpi)
part_3()


#The function below generates the fourth plot.
def part_4():






  #Plot 4
    
  #Generate Inputs for Plot 4
  input_sizes=[i*5000 for i in range(1,7)]

  ins_avg_time=[]
  bbs_avg_time=[]
  for i in input_sizes:
    input_1=swap_inputs(sorted(generate_inputs(i)))
    input_2=swap_inputs(sorted(generate_inputs(i)))
    input_3=swap_inputs(sorted(generate_inputs(i)))
    ins_avg_time.append((ins_sort(input_1)[0]+ins_sort(input_2)[0]+ins_sort(input_3)[0])/3)
    bbs_avg_time.append((optimized_bubble_sort(input_1)[0]+optimized_bubble_sort(input_2)[0]+optimized_bubble_sort(input_3)[0])/3)



  print(ins_avg_time)
  print(bbs_avg_time)

  from matplotlib import pyplot as plt
  fig = plt.figure(figsize=(15, 15))
  plt.plot(input_sizes,ins_avg_time,label='Insertion sort')
  plt.plot(input_sizes,bbs_avg_time,label='Bubble sort')
  plt.ylabel('Running time')
  plt.xlabel('Input size')
  plt.title('Plot 4')
  plt.legend()
  fig.savefig('plot4.png', dpi=fig.dpi)


part_4()


#The function below generates 100000 arrays/lists with size 50, and compares the average sorting time of insertion 
#and bubble sort algorithms for these inputs.
def part_5():
  ins_time=[]
  bbs_time=[]


  #Generate Inputs for Part 5
  for i in range(0,100000):
 
    
    inp_list=generate_inputs(50)
    ins_sample_time, ins_sorted_array=ins_sort(inp_list)[0],ins_sort(inp_list)[2]
    bbs_sample_time, bbs_sorted_array=optimized_bubble_sort(inp_list)[0],optimized_bubble_sort(inp_list)[2]
    
    if ins_sorted_array==bbs_sorted_array==sorted(inp_list):
    
      ins_time.append(ins_sample_time)
      bbs_time.append(bbs_sample_time)
    else:
      print('Algorithm not working')
      print('Insertion Sort',ins_sorted_array)
      print('Bubble Sort',bbs_sorted_array)
      print('Default Sort',sorted(inp_list))
      
      break
    

  print('Average time of insertion sort', sum(ins_time)/len(ins_time))
  print('Average time of bubble sort with check', sum(bbs_time)/len(bbs_time))

part_5()  