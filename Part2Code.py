import random,time
import matplotlib.pyplot as plt
#q3
def findKlargest(arr,K):
    klar=[]
    while K>0:
        max= arr[0]
        for i in range(len(arr)):
            if arr[i] not in klar:
                
                if arr[i]>max:
                    max=arr[i]
            else:
                continue
        klar.append(max)
        K-=1
    return klar
def possibleAct(timings):
    
    pass

def mergedIntervals(intervals):
    
    interval=[]
    for i in range(len(intervals)):
        #converting list of tuples to list of lists since tuples are immutable objects
        interval.append(list(intervals[i]))
    #sorting based on start values:
    for i in range(len(interval)-1):
        for j in range(len(interval)-i-1):
            if interval[j][0] > interval[j+1][0]:
                temp=interval[j]
                interval[j]=interval[j+1]
                interval[j+1]=temp
    sortedInt=interval
    print(sortedInt)
    
    i=0
    while i<len(interval)-1:
        if interval[i+1][0]<=interval[i][1]:
            if interval[i+1][1]>interval[i][1]:
                interval[i+1]=interval[i][0],interval[i+1][1]
                #print(interval[i])
                interval.remove(interval[i])
                i+=1
            else:
                #print(interval[i])
                interval.remove(interval[i+1])
                i+=1
        # else:
        #     if interval[i+1][1]<=interval[i][0]:
    return interval      
def MergedIntervals(intervals):
    interval = [list(interval) for interval in intervals]  # Convert tuples to lists
    # Sorting based on start values
    for i in range(len(interval)-1):
        for j in range(len(interval)-i-1):
            if interval[j][0] > interval[j+1][0]:
                interval[j], interval[j+1] = interval[j+1], interval[j]  # Swap intervals
    
    print("Sorted Intervals:", interval)
    
    i = 0
    while i < len(interval) - 1:
        if interval[i+1][0] <= interval[i][1]:  # Check for overlap
            interval[i][1] = max(interval[i][1], interval[i+1][1])  # Merge intervals
            interval.pop(i+1)  # Remove the next interval
        else:
            i += 1  # Move to the next interval
    
    return interval
def sortArrays(arr1,arr2):
    arrUpdated=[]
    k=0
    i=0
    j=0
    while i < len(arr1)-1 and j < len(arr2)-1:
        if arr1[i]<arr2[j]:
            arrUpdated[k]=arr1[i]
            i+=1
            k+=1
        else:
            arrUpdated[k]=arr2[j]
            j+=1
            k+=1
    while i or j < len(arr1)-1 or len(arr2)-1:       
        if i<len(arr1):
            arrUpdated[k]=arr1[i]
            i+=1
            k+=1
        else:
            arrUpdated[k]=arr2[j]
            j+=1
            k+=1
    return arrUpdated
        
def SortArrays(arr1, arr2):
    arrUpdated = []  # Initialize the result array
    i = 0
    j = 0
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            arrUpdated.append(arr1[i])  # Append element from arr1 to arrUpdated
            i += 1
        else:
            arrUpdated.append(arr2[j])  # Append element from arr2 to arrUpdated
            j += 1
    
    # Append remaining elements from arr1 or arr2 (if any)
    while i < len(arr1):
        arrUpdated.append(arr1[i])
        i += 1
    
    while j < len(arr2):
        arrUpdated.append(arr2[j])
        j += 1
    
    return arrUpdated    

def findMaxAct(acts):
    posActs=[]
    print(acts)
    #sorting based on finishing time.
    for i in range(len(acts)-1):
        for j in range(len(acts)-1):
            if acts[j][1]>acts[j+1][1]:
                temp=acts[j]
                acts[j]=acts[j+1]
                acts[j+1]=temp
    posActs.append(acts[0])
    posActs=[x for x in posActs]
    k=0# to keep track of the posActs array that may not get updated for every iteration through the acts array
    for i in range(1,len(acts)):
        if (acts[i][0]>posActs[k][1]):
            print(acts[i][0], posActs[k][1])
            posActs.append(acts[i])
            k+=1
        else:
            continue
    return posActs,len(posActs)


def sortBubble(arr):
    start_time = time.time()
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    end_time = time.time()
    return arr, end_time - start_time

# Selection Sort
def sortSelection(arr):
    start_time = time.time()
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    end_time = time.time()
    return arr, end_time - start_time

# Insertion Sort
def sortInsertion(arr):
    start_time = time.time()
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    end_time = time.time()
    return arr, end_time - start_time

# Merge Sort
def sortMerge(arr):
    start_time = time.time()
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        sortMerge(L)
        sortMerge(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    end_time = time.time()
    return arr, end_time - start_time

# Quick Sort

def sortQuick(arr):
    start_time = time.time()
    if len(arr) <= 1:
        return arr, time.time() - start_time
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    sorted_left, _ = sortQuick(left)
    sorted_right, _ = sortQuick(right)
    end_time = time.time()
    return sorted_left + middle + sorted_right, end_time - start_time


# Bucket Sort
def sortBucket(arr):
    start_time = time.time()
    max_val = max(arr)
    bucket = [0] * (max_val + 1)
    for i in arr:
        bucket[i] += 1
    sorted_arr = []
    for i in range(len(bucket)):
        for j in range(bucket[i]):
            sorted_arr.append(i)
    end_time = time.time()
    return sorted_arr, end_time - start_time

# Radix Sort
def sortRadix(arr):
    start_time = time.time()
    max_digit = len(str(max(arr)))
    for digit in range(max_digit):
        buckets = [[] for _ in range(10)]
        for num in arr:
            buckets[(num // 10**digit) % 10].append(num)
        arr = [num for bucket in buckets for num in bucket]
    end_time = time.time()
    return arr, end_time - start_time

# Heap Sort
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def sortHeap(arr):
    start_time = time.time()
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    end_time = time.time()
    return arr, end_time - start_time

    
def main():
    #Generate 1000 integer random numbers between 1 and 10000. Compare the sorting
# algorithms learnt in the class using the same set of numbers generated. Plot the time taken
# for them to complete the process.
    # Generate 1000 random numbers between 1 and 10000
    random_numbers = [random.randint(1, 10000) for _ in range(1000)]

    # Comparing sorting algorithms
    results = {
        'Bubble Sort': sortBubble(random_numbers)[1],
        'Selection Sort': sortSelection(random_numbers)[1],
        'Insertion Sort': sortInsertion(random_numbers)[1],
        'Merge Sort': sortMerge(random_numbers)[1],
        'Quick Sort': sortQuick(random_numbers)[1],
        'Bucket Sort': sortBucket(random_numbers)[1],
        'Radix Sort': sortRadix(random_numbers)[1],
        'Heap Sort': sortHeap(random_numbers)[1]
    }
        
    import matplotlib.pyplot as plt

    plt.bar(results.keys(), results.values())
    plt.xlabel('Algorithm')
    plt.ylabel('Time taken (s)')
    plt.title('Comparison of Sorting Algorithms')
    plt.show()      

    #q3
    arrForKlarg=[]
    for i in range(1,1001):
        arrForKlarg.append(random.randint(100,9000))
        
    k= int(input("enter the no. of largest elements you want to find from the array: "))
    print(findKlargest(arrForKlarg,k))
    #q4
    #inputing the start and end time
    startT=list(input("Enter the starting times of the activity: "))
    endT = list(input("Enter the ending times of the activity: "))
    actT=list(zip(startT,endT))
    print("The maximum possible activities are : ",possibleAct(actT))
    #q5
    startInT=list(input("Enter the starting point of the interval: "))
    endInT = list(input("Enter the ending point of the interval: "))
    combInT=list(zip(startInT,endInT))
    print("The merged intervals are : ",MergedIntervals(combInT))
    #q2
    listOfSortedArr = []
    n = int(input("Enter the number of arrays: "))
    for i in range(n):
        arr = input("Enter the sorted array (space-separated integers): ").split()
        arr = [int(x) for x in arr]  # Convert strings to integers
        listOfSortedArr.append(arr)
    
    newArr = listOfSortedArr[0]
    for i in range(1, n):
        newArr = SortArrays(newArr, listOfSortedArr[i])
    
    print("The fully sorted array is:", newArr)
    
    #q4
    n = int(input("Enter the number of activities: "))
    activities = []

    for i in range(n):
        # Prompt the user to enter a tuple
        act = input(f"Enter timings of  {i+1}st activity (in the format 'x, y'): ")
        
        # Split the input by comma and convert the values to integers
        acts = tuple(map(int, act.split(',')))
        
        # Append the tuple to the list
        activities.append(acts)
    maxAct=findMaxAct(activities)
    print("The activities that can be performed are : ",maxAct[0]," which is a total of ",maxAct[1] ,"activities")
    
        
if __name__=="__main__":
    main()