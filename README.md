# Homework
#QuickSort
QuickSort is a fast sorting algorithm that takes a divide and conquer approach to sorting lists. Divide and conquer is a technique used for breaking algorithms down into subproblems, solving the subproblems, and then combining the results back together to solve the original problem. The divide and conquer part include choosing an element as a pivot. Pivot is one of the items in the array that meets the following conditions afterwe have sorted it: first, the pivot is in it's correct position in the final sorted array. This means that all the items to the left are smaller and all items to the right are larger. The actual position where the pivot element belongs in the final sorted list is called the 'Split point'.
for example, we take an array and choose the pivot element, which we then move to the end of the array. Then, we look for two items, the item from the left which is larger than the pivot and the item from the right that is smaller than the pivot. we then swap the two items. We repeat the process until the item from the left has a greater index than the item from the right. We then swap the item from left with our pivot, which returns to it's correct spot.
 The list can now be divided at the split point and the quick sort can be invoked recursively on the two halves.
To analyze the quicksort function, (for a list of length n), if the partition always occurs in the middle of the list, there will again be logn divisions. In order to find the split point, each of the n items needs to be checked against the pivot value.

The pivot makes a difference in the performance of the algorithm because the role of the pivot value is to assist with splitting the list.
If a pivot is chosen properly, it can be shown to have an average case of O(nlogn) 
But in the worst case(which occurs when the partition sizes are unbalanced), it is shown to have a O(n2)

QuickSort is a recursive process.



#MergeSort

