def fknapsack(arr,max_wt):
    #sort based on b/w ratio:
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j][0]//arr[j][1] <  arr[j+1][0]//arr[j+1][1]:
                #placing in descending order
                temp = arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
    
    max_bf=0
    i=0
    while max_wt >=0 and i<len(arr):
        proportion=1
        if max_wt-arr[i][1]>=0:
            max_wt-=arr[i][1]
            
        else:
            proportion=max_wt/arr[i][1]
            print(proportion)
            max_wt=0
        max_bf+=proportion*arr[i][0]
        print(max_bf)
        i+=1
    return max_bf
        


# MergeSort in Python
def mergeSort(array):
    if len(array) > 1:

        #  r is the point where the array is divided into two subarrays
        r = len(array)//2
        L = array[:r]
        M = array[r:]

        # Sort the two halves
        mergeSort(L)
        mergeSort(M)

        i = j = k = 0

        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1

        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1
    return array

# Print the array
def printList(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()


    

# Driver program
if __name__ == '__main__':
    arr1 = list(map(int,input("enter the array 1 elements  seperated by space.").split()))
    arr2 = list(map(int,input("enter the array 2 elements seperated by space.").split()))
    sort1 = mergeSort(arr1)
    sort2= mergeSort(arr2)
    sort= list(reversed(sort2))
    print(sort1, sort)
    sumOfProd=0
    for i in range(len(arr1)):
        sumOfProd+= sort1[i] * sort[i]
    print(sumOfProd)
    
    #Given an array of N integer, we have to maximize the sum of arr[i] * i, where i is the index
# of the element (i = 0, 1, 2, ..., N). We can rearrange the position of the integer in the array
# to maximize the sum
    arr3 = list(map(int,input("enter the array 1 elements  seperated by space.").split()))
    sort3= mergeSort(arr3)
    arrIdx= [ i for i in range(len(arr3))]
    sumOfPrd=0
    for i in range(len(arr3)):
        sumOfPrd+=arrIdx[i]*sort3[i]
    print(sumOfPrd)
   
       #get benefit-weight pairs
    n=int(input("enter the no. of pairs:"))
    bws=[]
    for i in range(n):
        bw=input("enter pair:")
        bwTuple= tuple(map(int,bw.split()))
        bws.append(bwTuple)
    wt=int(input("enter the max poss weight :"))
    print("Total weight possible :",fknapsack(bws,wt))
        
    
    #fractional knapsack
    
#     Solve the fractional knapsack problem for the given set of N items with benefit-weight
# pairs and sack capacity of W. Print the optimal solution
    # n = int(input("Enter the number of benefit-weight pairs: "))
    # bws = []

    # for i in range(n):
    #     # Prompt the user to enter a tuple
    #     bw = input(f"Enter timings of  {i+1}st benefit-weight (in the format 'x, y'): ")
    #     bw = bw,bw[i][0]//bw[i][1]
        
    #     # Split the input by comma and convert the values to integers
    #     bws = tuple(map(int, bw.split(',')))
        
    #     # Append the tuple to the list
    #     bws.append(bw)
    # print(bws)
    # sortPrc= mergeSort(bws)
    # optimalSoln=[0 for i in range(len(bws))]
    # maxBft=0
    