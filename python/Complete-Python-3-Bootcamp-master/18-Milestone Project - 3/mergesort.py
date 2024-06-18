import math


def mergesort(arr):

    if len(arr) > 1:
        meio = math.floor((len(arr)) / 2) 
        L = arr[:meio]
        R = arr[meio:]

        mergesort(L)
        mergesort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


    

    
   





print(mergesort([12, 11, 13, 5, 6, 7]))
    