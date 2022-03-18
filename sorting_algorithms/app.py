### Bubble Sort (n^2) ###
def bubble_sort(nums):
    # copy of the list
    nums = list(nums)

    for _ in range(len(nums) - 1):  # ignores the last element
        # ignores the last element to allow comparison of the last 2
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:  # we compare
                # we swap
                nums[i], nums[i+1] = nums[i+1], nums[i]
    return nums


### Insertion Sort ###
def insertion_sort(nums):
    nums = list(nums)

    for i in range(nums):
        drop = nums.pop(i)
        j = i-1

        while j >= 0 and nums[j] > drop:
            j -= 1
            nums.insert(j+1, drop)
    return nums


### DIVIDE and CONQUER ###

# the merge algorithm
def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2
    left = nums[:mid]
    right = nums[mid:]

    sort_left, sort_right = merge_sort(left), merge_sort(right)

    def merge(num1, num2):
        merged = []

        i, j = 0, 0

        while i < len(num1) and j < len(num2):
            # compare and append
            if num1[i] <= num2[j]:
                merged.append(num1[i])
                i += 1
            else:
                merged.append(num2[j])
                j += 1

        # the remaining of each
        num1_tail = num1[i:]
        num2_tail = num2[j:]

        return merged + num1_tail + num2_tail

    # combination of the sorted array using the sort function
    sorted = merge(sort_left, sort_right)

    return sorted


print(merge_sort([4, 2, 6, 3, 4, 6, 2, 1]))
