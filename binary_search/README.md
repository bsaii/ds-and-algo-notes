### Binary Search O(log n)

Here's how binary search can be applied to our problem:

1. Find the middle element of the list.
2. If it matches queried number, return the middle position as the answer.
3. If it is less than the queried number, then search the first half of the list
4. If it is greater than the queried number, then search the second half of the list
5. If no more elements remain, return -1.


## Code for binary search

```
def locate_card(cards, query):
  low, high = 0, len(cards) - 1

# a loop
  while low <= high:
    # the index of the middle number
    mid = (low + high) // 2
    mid_num = cards[mid] # the middle number

    # printing the numbers
    print('low_num:', cards[low], 'high_num:', cards[high], 'mid_num:', mid_num, 'query:', query)

    if mid_num == query:
      return mid
    elif query > mid_num:
      high = mid - 1 # search the left
    elif query < mid_num:
      low = mid + 1 # search the right
  
  # anything else
  return -1
  ```
