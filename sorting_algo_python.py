def bubble_sort(nums):
    """Bubble Sorting Algorithm"""
    # Iterations
    for index in range(len(nums)-1, 0, -1): 
        # Check each items in the list
        for j in range(index): 
            # Check if a > b
            if nums[j] > nums[j+1]:
                temp = nums[j] 

                 # Swapping the correct position
                nums[j],  nums[j+1] = nums[j+1], temp
        print(f"LOOP # {index + 1}: {nums}")

    return f"\nFINAL OUTPUT: {nums}"  # Final result
    
# num = [7, 6, 4, 3]
# print(bubble_sort(num))  # [3, 4, 6, 7]


def selection_sorting(nums): 
    """ Selection Sorting Algorithm """
    # Iteration
    for index in range(len(nums)):
        # loop for each index in nums list
        min_val = nums[index] # Minumum Value

        # Looping for the unsorted groups
        for item in nums[index:]:
            # Checking for the lowest value
            if min_val > item: 
                min_val =  item  # Modify the lowest value

        find_index = nums.index(min_val)  # Finding the index of min value 
        
        # Swapping the correct position
        nums[index], nums[find_index] = min_val,  nums[index]
        print(f"LOOP # {index + 1}: {nums}")  # Show Result of each loop
           
                
    return f"\nFINAL OUTPUT: {nums}"  # Final result


# num = [5, 3, 8, 6, 7, 2]
# print(selection_sorting(num)) # [2, 3, 5, 6, 7, 8]


def insertion_sorting(nums):
    """ Insertion Sorting Alogirthm"""
     # loop for each index in nums list
    for index in range(len(nums)):
        # Iterate list of items in nums by groups
        for item in nums[:index]:
            # Check if new value is less than item
            if item > nums[index]:
                find_index = nums.index(item)  # Finding the index of min value

                # Swapping the correct position
                nums[index], nums[find_index] = item, nums[index]

        print(f"LOOP # {index + 1}: {nums}")  # Show Result of each loop

    return f"\nFINAL OUTPUT: {nums}"  # Final result
            

# num = [4, 3, 2, 10, 12, 1, 5, 6]
# print(insertion_sorting(num)) # [1, 2, 3, 4, 5, 6, 10, 12]


def heap_sorting(nums):
    """Heap Sorting Algorithm"""
    # 🚧 Under construction 
    pass 