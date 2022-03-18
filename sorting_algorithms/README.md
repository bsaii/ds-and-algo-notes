### The divide and conquer is efficient and has the time complexity of O(n log n).

When to use
- when sorting an array
- when you want to merge two sorted arrays
- ???


Here's a step-by-step description for merge sort:

1. If the input list is empty or contains just one element, it is already sorted. Return it.
2. If not, divide the list of numbers into two roughly equal parts.
3. Sort each part recursively using the merge sort algorithm. You'll get back two sorted lists.
4. Merge the two sorted lists to get a single sorted list; The merge function is written by repeatedly comparing one element of each array, and copy the smaller one into a new array


### Code for merge sort

```
def merge_sort(nums):
    # Terminating condition (list of 0 or 1 elements)
    if len(nums) <= 1:
        return nums
    
    # Get the midpoint
    mid = len(nums) // 2
    
    # Split the list into two halves
    left = nums[:mid]
    right = nums[mid:]
    
    # Solve the problem for each half recursively
    left_sorted, right_sorted = merge_sort(left), merge_sort(right)
    
    # Combine the results of the two halves
    sorted_nums =  merge(left_sorted, right_sorted)
    
    return sorted_nums
```
    

### Code for merge

```
def merge(nums1, nums2):    
    # List to store the results 
    merged = []
    
    # Indices for iteration
    i, j = 0, 0
    
    # Loop over the two lists
    while i < len(nums1) and j < len(nums2):        
        
        # Include the smaller element in the result and move to next element
        if nums1[i] <= nums2[j]:
            merged.append(nums1[i])
            i += 1 
        else:
            merged.append(nums2[j])
            j += 1
    
    # Get the remaining parts
    nums1_tail = nums1[i:]
    nums2_tail = nums2[j:]
    
    # Return the final merged array
    return merged + nums1_tail + nums2_tail
```
    
    
### Other sorting algorithms
  - bubble sort
  - insertion sort
  - Quick sort
    
