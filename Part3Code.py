import Part1Code
def pairWithGivenSum(arr,sum):
    results=[]
    for i in range(len(arr)):
        for j in range(len(arr)):
            if (arr[i]+arr[j]==sum and j!=i):
                results.append((arr[i],arr[j]))
    if results==[]:
        return "No pair found."  
    else:
        return results

def maxProduct(arr):
    #since the mult. of a neg and pos. no. doesnt give a max product, we sort the negative numbers
    #in ascending order and positive numbers in descending order and take the first 2 elem of both the 
    #arrays and find the product, then return whichever is greater.
    pos=[]
    neg=[]
    for i in arr:
        if i>0 or i==0:
            pos.append(i)
        else:
            neg.append(i)
    #sorting
    for i in range(len(pos)-1):
        for j in range(len(pos)-1):
            if (pos[j]<pos[j+1]):
                temp=pos[j]
                pos[j]=pos[j+1]
                pos[j+1]=temp
    for i in range(len(neg)-1):
        for j in range(len(neg)-1):
            if (neg[j]>neg[j+1]):
                temp=neg[j]
                neg[j]=neg[j+1]
                neg[j+1]=temp
    #print(pos, neg)
    if len(pos)>1:
        pmax=pos[0]*pos[1]
        if len(neg)<2:
            return pmax
    if len(neg)>1:
        nmax=neg[0]*neg[1]
        if len(pos)<2:
            return nmax
    if pmax>nmax:
        return pmax
    else: 
        return nmax
def sortArr(arr):
    swapped=False
    for i in range(len(arr)-1):
        swapped = True
        for j in range(len(arr)-1):
            if swapped==True:
                if arr[j]>arr[j+1]:
                    temp= arr[j]
                    arr[j]=arr[j+1]
                    arr[j+1]=temp
                swapped = False
            
        
    return arr
def binSeperate(arr):
    seg=[]
    count1=0
    for i in arr:
        if i==0:
            seg.append(i)
        elif i==1:
            count1+=1
        else:
            continue
    while count1!=0:
        seg.append(1)
        count1-=1
    return seg

def inversionCount(arr):
    inversions=[]
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
                if arr[i]>arr[j]:
                    inversions.append((arr[i],arr[j]))
    return inversions,len(inversions)

def pairWithGivenSum2(arr,sum):
    results=[]
    for i in range(len(arr)):
        for j in range(len(arr)):
            if (arr[i]+arr[j]==sum ):
                results.append((arr[i],arr[j]))
    if results==[]:
        return "No pair found."  
    else:
        return "yes"     

   
def pairWithGivenSumAprch2(arr,sum):
    Sarr=sorted(arr) #nlogn
    
    results=[]
    for i in range(len(arr)):
        c1=Sarr[i]
        c2=abs(sum-c1)
        #search if c2 exists in the array 
        pos=Part1Code.binSearch(c2,0,len(arr)-1,Sarr)[0]
        if pos>=0:
            results.append((c1,Sarr[pos]))
            
            return results,"Yes"
        else:
            continue
    return "No pair found"                        

def main():
    #q1
    nums= input("enter the numbers( seperated by space) to find the pair that sums to the target : ").split()
    nums = [int(x) for x in nums]
    #print(nums)
    target= int(input("enter the target sum:"))
    print(pairWithGivenSum(nums,target))

    #q2
    arrMax= input("Enter the array elemenets with both positive and negative elements( seperated by space) to find the max product").split()
    arrMax= [int(x) for x in arrMax]
    print("The maximum product is :",maxProduct(arrMax))
    
    #q3
    #Sort the array in linear time when only 2 elements are swapped 
    arrS= input("Enter the array to be sorted seperated by space (with only 2 elements swappen out of order):").split()
    arrS= [int(x) for x in arrS]
    print("Sorted array :", sortArr(arrS))
    #q4
    binArr= input("Enter the binary array to be segregated: ").split()
    binArr=[int(x) for x in binArr]
    
    print("The segregated array is : ", binSeperate(binArr))
    
    #q5
    nums= input("enter the numbers( seperated by space) to find their inversion pairs : ").split()
    nums = [int(x) for x in nums]

    print("The Inversions found are ",inversionCount(nums)[0], "and the no. of inversions is :",inversionCount(nums)[1])
    #q6 a)
    nums= input("enter the numbers( seperated by space) to find the pair that sums to the target : ").split()
    nums = [int(x) for x in nums]
    #print(nums)
    target= int(input("enter the target sum:"))
    print("The answer to whether a pair exists to give the desired sum is : ",pairWithGivenSum2(nums,target))
    #b)
    print("Using approach 2 (traversing the array and finding the 2nd element through binary search) the answer to whether the pair exists or not is :",pairWithGivenSumAprch2(nums,target))
if __name__=="__main__":
    main()
