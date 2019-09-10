# Necessary Imports
import random

class Sorting:


    # Bubble Sort
    def bubbleSort(self,arr):
        n = len(arr) 
        # Traverse through all array elements 
        for i in range(n): 
        # Last i elements are already in place 
            for j in range(0, n-i-1): 
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
                if arr[j] > arr[j+1] : 
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

    # Selection Sort

    def selectionSort(self,arr):

        for i in range(len(arr)): 
        # Find the minimum element in remaining  
        # unsorted array 
            min_idx = i 
            for j in range(i+1, len(arr)): 
                if arr[min_idx] > arr[j]: 
                    min_idx = j 
            # Swap the found minimum element with  
            # the first element         
            arr[i], arr[min_idx] = arr[min_idx], arr[i] 

        return arr

    # Insertion Sort

    def insertionSort(self,arr):

        # Traverse through 1 to len(arr) 
        for i in range(1, len(arr)): 
            key = arr[i] 
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
            j = i-1
            while j >= 0 and key < arr[j] : 
                    arr[j + 1] = arr[j] 
                    j -= 1
            arr[j + 1] = key
        return arr
    
    # Shell Sort

    def shellSort(self,arr):
            # Start with a big gap, then reduce the gap 
        n = len(arr) 
        gap = n//2
        # Do a gapped insertion sort for this gap size. 
        # The first gap elements a[0..gap-1] are already in gapped  
        # order keep adding one more element until the entire array 
        # is gap sorted 
        while gap > 0: 
  
            for i in range(gap,n): 
    
                # add a[i] to the elements that have been gap sorted 
                # save a[i] in temp and make a hole at position i 
                temp = arr[i] 
    
                # shift earlier gap-sorted elements up until the correct 
                # location for a[i] is found 
                j = i 
                while  j >= gap and arr[j-gap] >temp: 
                    arr[j] = arr[j-gap] 
                    j -= gap 
    
                # put temp (the original a[i]) in its correct location 
                arr[j] = temp 
            gap //= 2

        return arr
    
    # Pegion Hole Sort

    def pigeonHoleSort(self,arr):
            # size of range of values in the list  
            # (ie, number of pigeonholes we need) 
        my_min = min(arr) 
        my_max = max(arr) 
        size = my_max - my_min + 1
  
        # our list of pigeonholes 
        holes = [0] * size 
    
        # Populate the pigeonholes. 
        for x in arr: 
            assert type(x) is int, "integers only please"
            holes[x - my_min] += 1
    
        # Put the elements back into the array in order. 
        i = 0
        for count in range(size): 
            while holes[count] > 0: 
                holes[count] -= 1
                arr[i] = count + my_min 
                i += 1
        return arr
    
    # Heap Sort

    def heapify(self,arr, n, i): 
        largest = i # Initialize largest as root 
        l = 2 * i + 1     # left = 2*i + 1 
        r = 2 * i + 2     # right = 2*i + 2 
    
        # See if left child of root exists and is 
        # greater than root 
        if l < n and arr[i] < arr[l]: 
            largest = l 
    
        # See if right child of root exists and is 
        # greater than root 
        if r < n and arr[largest] < arr[r]: 
            largest = r 
    
        # Change root, if needed 
        if largest != i: 
            arr[i],arr[largest] = arr[largest],arr[i] # swap 
    
            # Heapify the root. 
            self.heapify(arr, n, largest) 
    
    # The main function to sort an array of given size 
    def heapSort(self,arr): 
        n = len(arr) 
    
        # Build a maxheap. 
        for i in range(n, -1, -1): 
            self.heapify(arr, n, i) 
    
        # One by one extract elements 
        for i in range(n-1, 0, -1): 
            arr[i], arr[0] = arr[0], arr[i] # swap 
            self.heapify(arr, i, 0) 
        # Returning the Result
        return arr

    # Gnome Sort

    def gnomeSort(self, arr): 
        index = 0
        n = len(arr)
        while index < n: 
            if index == 0: 
                index = index + 1
            if arr[index] >= arr[index - 1]: 
                index = index + 1
            else: 
                arr[index], arr[index-1] = arr[index-1], arr[index] 
                index = index - 1
  
        return arr

    # Stooage Sort
    def stoogeSort(self,arr,l,h): 
        
        if l >= h: 
            return
    
        # If first element is smaller 
        # than last, swap them 
        if arr[l]>arr[h]: 
            t = arr[l] 
            arr[l] = arr[h] 
            arr[h] = t 
    
        # If there are more than 2 elements in 
        # the array 
        if h-l + 1 > 2: 
            t = (int)((h-l + 1)/3) 
    
            # Recursively sort first 2 / 3 elements 
            self.stoogeSort(arr, l, (h-t)) 
    
            # Recursively sort last 2 / 3 elements 
            self.stoogeSort(arr, l + t, (h)) 
    
            # Recursively sort first 2 / 3 elements 
            # again to confirm 
            self.stoogeSort(arr, l, (h-t))
        return arr

    # Pancake Sorting

    # Reverses arr[0..i]  
    def flip(self,arr, i): 
        start = 0
        while start < i: 
            temp = arr[start] 
            arr[start] = arr[i] 
            arr[i] = temp 
            start += 1
            i -= 1
    
    # Returns index of the maximum 
    # element in arr[0..n-1] */ 
    def findMax(self,arr, n): 
        mi = 0
        for i in range(0,n): 
            if arr[i] > arr[mi]: 
                mi = i 
        return mi 
    
    # The main function that  
    # sorts given array  
    # using flip operations 
    def pancakeSort(self,arr): 
        
        # Start from the complete 
        # array and one by one 
        # reduce current size 
        # by one 
        curr_size = len(arr)
        while curr_size > 1: 
            # Find index of the maximum 
            # element in  
            # arr[0..curr_size-1] 
            mi = self.findMax(arr, curr_size) 
    
            # Move the maximum element 
            # to end of current array 
            # if it's not already at  
            # the end 
            if mi != curr_size-1: 
                # To move at the end,  
                # first move maximum  
                # number to beginning  
                self.flip(arr, mi) 
    
                # Now move the maximum  
                # number to end by 
                # reversing current array 
                self.flip(arr, curr_size-1) 
            curr_size -= 1
        return arr

    # Bogo (OR) Permutation Sort
    # Sorts array a[0..n-1] using Bogo sort 
    def bogoSort(self,arr): 
        n = len(arr) 
        while (self.is_sorted(arr)== False): 
            self.shuffle(arr) 
        return arr

    
    # To check if array is sorted or not 
    def is_sorted(self,arr): 
        n = len(arr) 
        for i in range(0, n-1): 
            if (arr[i] > arr[i+1] ): 
                return False
        return True
    
    # To generate permuatation of the array 
    def shuffle(self,arr): 
        n = len(arr) 
        for i in range (0,n): 
            r = random.randint(0,n-1) 
            arr[i], arr[r] = arr[r], arr[i]
    
    # Merge Sort

    def mergeSort(self,arr): 
        if len(arr) >1: 
            mid = len(arr)//2 #Finding the mid of the array 
            L = arr[:mid] # Dividing the array elements  
            R = arr[mid:] # into 2 halves 
    
            self.mergeSort(L) # Sorting the first half 
            self.mergeSort(R) # Sorting the second half 
    
            i = j = k = 0
            
            # Copy data to temp arrays L[] and R[] 
            while i < len(L) and j < len(R): 
                if L[i] < R[j]: 
                    arr[k] = L[i] 
                    i+=1
                else: 
                    arr[k] = R[j] 
                    j+=1
                k+=1
            
            # Checking if any element was left 
            while i < len(L): 
                arr[k] = L[i] 
                i+=1
                k+=1
            
            while j < len(R): 
                arr[k] = R[j] 
                j+=1
                k+=1
        return arr

    # Quick Sort
    def partition(self,arr, low, high): 
        i = (low - 1)         # index of smaller element 
        pivot = arr[high]     # pivot 
    
        for j in range(low, high): 
    
            # If current element is smaller  
            # than or equal to pivot 
            if arr[j] <= pivot: 
            
                # increment index of 
                # smaller element 
                i += 1
                arr[i], arr[j] = arr[j], arr[i] 
    
        arr[i + 1], arr[high] = arr[high], arr[i + 1] 
        return (i + 1) 
    
    # The main function that implements QuickSort 
    # arr[] --> Array to be sorted, 
    # low --> Starting index, 
    # high --> Ending index 
    
    # Function to do Quick sort 
    def quickSort(self,arr, low, high): 
        if low < high: 
    
            # pi is partitioning index, arr[p] is now 
            # at right place 
            pi = self.partition(arr, low, high) 
    
            # Separately sort elements before 
            # partition and after partition 
            self.quickSort(arr, low, pi-1) 
            self.quickSort(arr, pi + 1, high)
        return arr
    
    # Cocktail Sort

    def cocktailSort(self,arr): 
        n = len(arr) 
        swapped = True
        start = 0
        end = n-1
        while (swapped == True): 
    
            # reset the swapped flag on entering the loop, 
            # because it might be true from a previous 
            # iteration. 
            swapped = False
    
            # loop from left to right same as the bubble 
            # sort 
            for i in range (start, end): 
                if (arr[i] > arr[i + 1]) : 
                    arr[i], arr[i + 1]= arr[i + 1], arr[i] 
                    swapped = True
    
            # if nothing moved, then array is sorted. 
            if (swapped == False): 
                break
    
            # otherwise, reset the swapped flag so that it 
            # can be used in the next stage 
            swapped = False
    
            # move the end point back by one, because 
            # item at the end is in its rightful spot 
            end = end-1
    
            # from right to left, doing the same 
            # comparison as in the previous stage 
            for i in range(end-1, start-1, -1): 
                if (arr[i] > arr[i + 1]): 
                    arr[i], arr[i + 1] = arr[i + 1], arr[i] 
                    swapped = True
    
            # increase the starting point, because 
            # the last stage would have moved the next 
            # smallest number to its rightful spot. 
            start = start + 1

        return arr
    
    # Brick Sort
    def brickSort(self,arr): 
        # Initially array is unsorted 
        isSorted = 0
        n = len(arr)
        while isSorted == 0: 
            isSorted = 1
            temp = 0
            for i in range(1, n-1, 2): 
                if arr[i] > arr[i+1]: 
                    arr[i], arr[i+1] = arr[i+1], arr[i] 
                    isSorted = 0
                    
            for i in range(0, n-1, 2): 
                if arr[i] > arr[i+1]: 
                    arr[i], arr[i+1] = arr[i+1], arr[i] 
                    isSorted = 0
        return arr

    # Radix Sort

    def counting(self, arr, exp1): 
  
        n = len(arr) 
    
        # The output array elements that will have sorted arr 
        output = [0] * (n) 
    
        # initialize count array as 0 
        count = [0] * (10) 
    
        # Store count of occurrences in count[] 
        for i in range(0, n): 
            index = (arr[i]//exp1) 
            count[ int((index)%10) ] += 1
    
        # Change count[i] so that count[i] now contains actual 
        #  position of this digit in output array 
        for i in range(1,10): 
            count[i] += count[i-1] 
    
        # Build the output array 
        i = n-1
        while i>=0: 
            index = (arr[i]/exp1) 
            output[ count[ int((index)%10) ] - 1] = arr[i] 
            count[ int((index)%10) ] -= 1
            i -= 1
    
        # Copying the output array to arr[], 
        # so that arr now contains sorted numbers 
        i = 0
        for i in range(0,len(arr)): 
            arr[i] = output[i] 
    
    # Method to do Radix Sort 
    def radixSort(self,arr): 
    
        # Find the maximum number to know number of digits 
        max1 = max(arr) 
    
        # Do counting sort for every digit. Note that instead 
        # of passing digit number, exp is passed. exp is 10^i 
        # where i is current digit number 
        exp = 1
        while max1/exp > 0: 
            self.counting(arr,exp) 
            exp *= 10
        
        return arr