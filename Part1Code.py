import matplotlib.pyplot as plt
import random
import time
import math
import sys

sys.setrecursionlimit(1500)  # Set recursion limit higher
# increased the recursion limit using sys.setrecursionlimit() to allow deeper recursion without encountering 
# the "maximum recursion depth exceeded" error.
def firstNsumIter(num,sum):
    start = time.time()
    for i in range(1,num+1):
        sum=sum+i
    stop=time.time()
    TotTime=stop-start
    return sum,TotTime
    
def firstNsumRec(num,sum):
    start=time.time()
    if num==1:
        stop=time.time()
        totTime=stop-start
        return sum+1,totTime
    
    else:
        sum = sum + num
        return firstNsumRec(num-1,sum)
#q2
def linSearch(key, arr):
    t1 = time.time()
    for i in range(len(arr)):
        if key == arr[i]:
            t2 = time.time()
            return i + 1, t2 - t1
    return -1, None  # Return -1 if the key is not found

def binSearch(key, lb, ub, arr):
    t1 = time.time()
    while lb <= ub:
        mid = (lb + ub) // 2
        if key == arr[mid]:
            t2 = time.time()
            return mid, t2 - t1
        elif key < arr[mid]:
            ub = mid - 1
        else:
            lb = mid + 1
    return -1, None  # Return -1 if the key is not found

#iterative 
def stringRevIter(s):
    revString=""
    for i in s(-1,-1,-1):
        revString+=s
    return revString
#q4
#recursive
def StringRev(s,revS,i):
    if len(s)-i<0:#when index starts getting out of range
        return revS
    else:
        revS+=s[len(s)-i]
        i+=1
        return StringRev(s,revS,i)
#q5    
def IsPalin(s,revS,i):
    if len(s)-i<0:#when index starts getting out of range
        if revS==s:
            return "Yes, Its a palindrome"
        else:
            return "No, Its not a palindrome"
    else:
        revS+=s[len(s)-i]
        i+=1
        return IsPalin(s,revS,i)
    
    
 #q3
def StrToInt(numS,numI,i):
    
    if(len(numS)-i<0):
        return numI  
    else:
        print(math.pow(10,len(numS)-i))
        numI=numI+ int(numS[i]*int(math.pow(10,len(numS)-i)))
        return StrToInt(numS,numI,i+1)
def strToInt(digits):

  if not digits:  # Base case: empty string
    return 0

  # Extract the first digit and convert it to an integer
  first_digit = int(digits[0])

  # Recursively convert the remaining digits
  remaining_digits = digits[1:]

  # Combine the first digit with the converted remaining digits
  return first_digit * (10 ** (len(remaining_digits))) + strToInt(remaining_digits)

    
            
    
def main():
    #q1
    NumSum = int(input("enter the no. up to which the sum is to be calculated:"))
    print("Sum using iterative approach: ")
    print(firstNsumIter(NumSum,0))
    print("Sum using recursive approach : ")
    print(firstNsumRec(NumSum,0))
    Nvalues=[]
    results1=[]
    results2=[]
    for i in range(1,11):
        Nvalues.append(random.randint(1000,1500))
        sum1,timeIter=firstNsumIter(Nvalues[i-1],0)
        sum2,timeRec=firstNsumRec(Nvalues[i-1],0)
        results1.append(timeIter)
        results2.append(timeRec)
 
    plt.plot(Nvalues,results1,label="Iterative")
    plt.plot(Nvalues,results2, label="Recursive")
    plt.xlabel("N value")
    plt.ylabel("Time taken")
    plt.legend()
    plt.show()
    #q2
    arrForSearch = []
    for i in range(0, 10000):
        arrForSearch.append(random.randint(1, 1000))

    print("The randomly generated array:", arrForSearch)
    searchKey = []
    timelin = []
    timebin = []

    for i in range(5):
        searchKey.append(int(input("Enter the search key: ")))
        pos1, linTime = linSearch(searchKey[i], arrForSearch)
        pos2, binTime = binSearch(searchKey[i], 0, len(arrForSearch) - 1, arrForSearch)
        timelin.append(linTime)
        timebin.append(binTime)

    plt.plot(searchKey, timelin, label="LinearSearch")
    plt.plot(searchKey, timebin, label="BinarySearch")
    plt.xlabel("Search Key")
    plt.ylabel("Time taken")
    plt.legend()
    plt.show()
        
    #q4
    strToRev = input("Enter the string to be reversed:")
    print("Reversed String :" ,StringRev(strToRev,"",1))

    #q5
    strToCheckPal= input("Enter the string to be Checked if palindrome or not:")
    print("Reversed String :" ,IsPalin(strToCheckPal,"",1))
    
    
    #q3
    StrtoConv=input("enter the string to be converted to integer:")
    print("Integer form: ",strToInt(StrtoConv))
    
if __name__ == "__main__":
    main()
