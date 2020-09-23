

def best_share_sort(a:list,b:list)->list:
    
    #The time complexity of the following algorithm is O(nlog(n)), as I have used the in-built sorting function of python.
    #The space complexity of the following algorithm is O(n) as I am maintaining a array of differences between Alice's and Bob's happiness quotient for each item in the list. 
    #No extra space is consumed for sorting, as it's done in-place.
    
    diff=[i-j for i,j in zip(a,b)]
    diff=[(i,diff[i]) for i in range(len(diff))]
    diff.sort(key=lambda tup:tup[1], reverse=True)
    
    return [diff[i][0] for i in range(0,len(diff)//2)]
    


def best_share_dp(a:list,b:list)->list:
    
    #The time complexity of the following algorithm is O(n^2). There are two nested for-loops which help in traversing and updating a (n+1,n/2+1) matrix.
    #The space complexity of the following algorithm is O(n^3) as at every index in the (n+1,n/2+1) matrix 
    #the algorithm tries to store the maximum happiness that can be achieved after processing the elements and also the items that were assigned to Alice that resulted in the sum at that Index.  

    dp=[[0]*(len(a)//2+1) for i in range(len(a)+1)]
    for i in range(len(dp)):
        dp[i][0]=(sum(b[:i]),[])
    
    for i in range(1,len(dp)):
        for j in range(1,len(dp[i])):
            if j==i:
                dp[i][j]=(sum(a[:i]),list(range(i)))
            
            elif j<i:
                temp_var=[(dp[i-1][j-1][0]+a[i-1],dp[i-1][j-1][1]+[i-1]),(dp[i-1][j][0]+b[i-1],dp[i-1][j][1])]
                dp[i][j]=max(temp_var,key= lambda tup:tup[0])
    
            
    return dp[len(dp)-1][len(dp[0])-1][1] 

#The following method includes all the test cases that were mentioned in the document.
def test_1():
    #Case 1
    a=[2,1]
    b=[1,2]
    
    sort_result=best_share_sort(a,b)
    dp_result=best_share_dp(a,b)
    
    sort_sum=sum([a[i] for i in sort_result])
    dp_sum=sum([a[i] for i in dp_result])
    
    if(sort_sum!=dp_sum):
        return "Test Case Failed"
    
    #Case 2
    a=[10,20,30,40]
    b=[8,18,25,35]
    
    sort_result=best_share_sort(a,b)
    dp_result=best_share_dp(a,b)
    
    sort_sum=sum([a[i] for i in sort_result])
    dp_sum=sum([a[i] for i in dp_result])
    
    if(sort_sum!=dp_sum):
        return "Test Case Failed"
    
    #Case 3
    a=[10]*4
    b=[7,9,11,13]
    
    sort_result=best_share_sort(a,b)
    dp_result=best_share_dp(a,b)
    
    sort_sum=sum([a[i] for i in sort_result])
    dp_sum=sum([a[i] for i in dp_result])
    
    if(sort_sum!=dp_sum):
        return "Test Case Failed"
    
    return "Test Cases Passed!"

print(test_1())

#The following method checks the validatiy of our algorithm for different input sizes.
def test_2():
    size_array=[i*10 for i in range(1,11)]
    for i in size_array:
        a=list(range(1,i,1))
        b=a[::-1]
        
        sort_result=best_share_sort(a,b)
        dp_result=best_share_dp(a,b)
    
        sort_sum=sum([a[i] for i in sort_result])
        dp_sum=sum([a[i] for i in dp_result])
    
        if(sort_sum!=dp_sum):
            return "Test Case Failed"
        
    return "Test Cases Passed!"

print(test_2())

#The following method checks the validatiy of our algorithm for empty Lists
def test_3():
  a=[]
  b=[]
  sort_result=best_share_sort(a,b)
  dp_result=best_share_dp(a,b)
    
  sort_sum=sum([a[i] for i in sort_result])
  dp_sum=sum([a[i] for i in dp_result])
    
  if(sort_sum!=dp_sum):
    return "Test Cases Failed"
  
  return "Test Cases Passed!"

print(test_3())

#The following method checks the validatiy of our algorithm for lists with identical elements
def test_4():
  for i in range(10):
    a=[i]*10
    b=a[::-1]
    sort_result=best_share_sort(a,b)
    dp_result=best_share_dp(a,b)
    
    sort_sum=sum([a[i] for i in sort_result])
    dp_sum=sum([a[i] for i in dp_result])
    
    if(sort_sum!=dp_sum):
      return "Test Cases Failed"
  
  return "Test Cases Passed!"

print(test_4())

# The following method checks the validatiy of our algorithm for large input arrays with large elements
import random
def test_5():
  size_arr=[5*i for i in range(50,501,50)]

  for i in size_arr:
    a=[random.randint(1,i) for j in range(i)]
    b=a[::-1]

    sort_result=best_share_sort(a,b)
    dp_result=best_share_dp(a,b)
    
    sort_sum=sum([a[i] for i in sort_result])
    dp_sum=sum([a[i] for i in dp_result])
    
    if(sort_sum!=dp_sum):
      return "Test Case Failed"
        
  return "Test Cases Passed!"
#print(test_5())

#The following function checks if there's any randomness in the algorithm by checking if the output is same in multiple iterations.
def test_6():
    a=[random.randint(100,5000) for i in range(100)]
    b=a[::-1]
    sort_result=best_share_sort(a,b)
    dp_result=best_share_dp(a,b)
    
    sort_sum=sum([a[i] for i in sort_result])
    dp_sum=sum([a[i] for i in dp_result])
    
    if(sort_sum!=dp_sum):
      return "Test Case Failed"
    
    initial_solution=sort_sum  # Initial solution which is the sum of happiness of Alice after receiving n/2 items.    
    for i in range(100):
        sort_result=best_share_sort(a,b)
        dp_result=best_share_dp(a,b)
    
        sort_sum=sum([a[i] for i in sort_result])
        dp_sum=sum([a[i] for i in dp_result])
    
        if(sort_sum!=dp_sum):
            return "Test Case Failed"
        if(sort_sum!=initial_solution):
            return "Algorithm didn't generate the same output in subsequent iterations"
        
    return "Test Cases Passed!"

print(test_6())