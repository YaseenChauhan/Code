def findTriplets(arr, ize, sum): 
    arr.sort() 
    for i in range(0, size-2): 
      
        left = i + 1 
         
        right = size-1 
        while (left < right): 
          
            if( arr[i] + arr[left] + arr[right] == sum):
                return True
              
            elif (arr[i] + arr[left] + arr[right] < sum): 
                left += 1
            else:
                right -= 1
  
    return False
    
arr = [5, 4, 10, 7, 1, 9] 
target_sum = 13
size = len(arr) 
  
print(findTriplets(arr, size, target_sum)) 
