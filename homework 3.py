import random, time, heapq
import matplotlib.pyplot as plt


#Codes for Quick sort:
def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot
    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


def QuickSort(arr, low, high):

    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        QuickSort(arr, low, pi - 1)
        QuickSort(arr, pi + 1, high)


class MinMaxQuick(object):

    def __init__(self):
        self.content = []

    def add(self, value):
        self.content.append(value)
        low = 0
        high =len(self.content)-1
        QuickSort(self.content,low,high)

    def get_min(self):
        return self.content[0]

    def get_max(self):
        return self.content[-1]



class MinMaxHeap(object):

    def __init__(self):
        self.content_min = []
        self.content_max = []
        # heapq.heapify(self.content_min)
        # heapq.heapify(self.content_max)

    def add(self, value):
        heapq.heappush(self.content_min, value)
        heapq.heappush(self.content_max, -value)

    def get_min(self):
        if len(self.content_min) > 0:
            return self.content_min[0]

    def get_max(self):
        if len(self.content_max) > 0:
            return -self.content_max[0]


class MinMaxBubble(object):

    def __init__(self):
        self.content = []

    def bubble_sort(self):
        for passnum in range(len(self.content) - 1, 0, -1):
            for i in range(passnum):
                if self.content[i] > self.content[i + 1]:
                    temp = self.content[i]
                    self.content[i] = self.content[i + 1]
                    self.content[i + 1] = temp

    def add(self, value):
        self.content.append(value)
        self.bubble_sort()

    def get_min(self):
        return self.content[0]

    def get_max(self):
        return self.content[-1]




#Codes for Binary Tree:
class BinaryTree(object):

    def __init__(self,data=None):
        self.data = data
        self.left = None
        self.right = None

    def add(self, data):
        if self.data == None:
            self.data = data
# Compare the new value with the parent node
        elif self.data:
            if data < self.data:
                if self.left is None:
                    self.left = BinaryTree(data)
                else:
                    self.left.add(data)
            elif data > self.data:
                if self.right is None:
                    self.right = BinaryTree(data)
                else:
                    self.right.add(data)
        else:
            self.data = data

    def get_min(self):
        min = self.data
        if self.left != None:
            min = self.left.get_min()
        return min

    def get_max(self):
        max = self.data
        if self.right != None:
            max = self.right.get_max()
        return max





def measure_time(a, this_list):
    tot_time_add = 0
    tot_time_min = 0
    tot_time_max = 0

    for num in this_list:
        start = time.time()
        a.add(num)
        tot_time_add += (time.time() - start)

        start = time.time()
        min = a.get_min()
        tot_time_min += (time.time() - start)

        start = time.time()
        max = a.get_max()
        tot_time_max += (time.time() - start)

    return tot_time_add, tot_time_min, tot_time_max


if __name__ == '__main__':
    a = MinMaxQuick()
    a.add(5)
    print(a.content, a.get_min(), a.get_max())
    a.add(7)
    print(a.content, a.get_min(), a.get_max())
    a.add(3)
    print(a.content, a.get_min(), a.get_max())
    a.add(9)
    print(a.content, a.get_min(), a.get_max())

    a = BinaryTree()
    a.add(5)
    print( a.get_min(), a.get_max())
    a.add(7)
    print( a.get_min(), a.get_max())
    a.add(3)
    print( a.get_min(), a.get_max())
    a.add(9)
    print( a.get_min(), a.get_max())

    a = MinMaxHeap()
    a.add(5)
    print(a.content_min, a.content_max, a.get_min(), a.get_max())
    a.add(7)
    print(a.content_min, a.content_max, a.get_min(), a.get_max())
    a.add(3)
    print(a.content_min, a.content_max, a.get_min(), a.get_max())
    a.add(9)
    print(a.content_min, a.content_max, a.get_min(), a.get_max())

    a = MinMaxBubble()
    a.add(5)
    print(a.content, a.get_min(), a.get_max())
    a.add(7)
    print(a.content, a.get_min(), a.get_max())
    a.add(3)
    print(a.content, a.get_min(), a.get_max())
    a.add(9)
    print(a.content, a.get_min(), a.get_max())

    repetitions = 3
    max_operations = 1000
    step = 100

    values_Quick_add, values_Quick_min, values_Quick_max = [], [], []
    values_BinaryTree_add, values_BinaryTree_min, values_BinaryTree_max = [], [], []
    values_heap_add, values_heap_min, values_heap_max = [], [], []
    values_bubble_add, values_bubble_min, values_bubble_max = [], [], []

    for rounds in range(step, max_operations, step):
        this_list = []
        for r in range(rounds):
            this_list.append(random.randint(0, 1000))

        tot_time_add, tot_time_min, tot_time_max = 0, 0, 0
        for repetition in range(repetitions):
            a = MinMaxQuick()
            myadd, mymin, mymax = measure_time(a, this_list)
            tot_time_add += myadd
            tot_time_min += mymin
            tot_time_max += mymax

        tot_time_add /= repetitions
        tot_time_min /= repetitions
        tot_time_max /= repetitions

        values_Quick_add.append(tot_time_add * 1000)
        values_Quick_min.append(tot_time_min * 1000)
        values_Quick_max.append(tot_time_max * 1000)

        tot_time_add, tot_time_min, tot_time_max = 0, 0, 0
        for repetition in range(repetitions):
            a = BinaryTree()
            myadd, mymin, mymax = measure_time(a, this_list)
            tot_time_add += myadd
            tot_time_min += mymin
            tot_time_max += mymax

        tot_time_add /= repetitions
        tot_time_min /= repetitions
        tot_time_max /= repetitions

        values_BinaryTree_add.append(tot_time_add * 1000)
        values_BinaryTree_min.append(tot_time_min * 1000)
        values_BinaryTree_max.append(tot_time_max * 1000)

        tot_time_add, tot_time_min, tot_time_max = 0, 0, 0
        for repetition in range(5):
            a = MinMaxHeap()
            myadd, mymin, mymax = measure_time(a, this_list)
            tot_time_add += myadd
            tot_time_min += mymin
            tot_time_max += mymax

        tot_time_add /= 5
        tot_time_min /= 5
        tot_time_max /= 5

        values_heap_add.append(tot_time_add * 1000)
        values_heap_min.append(tot_time_min * 1000)
        values_heap_max.append(tot_time_max * 1000)

        tot_time_add, tot_time_min, tot_time_max = 0, 0, 0
        for repetition in range(repetitions):
            a = MinMaxBubble()
            myadd, mymin, mymax = measure_time(a, this_list)
            tot_time_add += myadd
            tot_time_min += mymin
            tot_time_max += mymax

        tot_time_add /= repetitions
        tot_time_min /= repetitions
        tot_time_max /= repetitions

        values_bubble_add.append(tot_time_add * 1000)
        values_bubble_min.append(tot_time_min * 1000)
        values_bubble_max.append(tot_time_max * 1000)

    xlabels = range(step, max_operations, step)

    plt.plot(xlabels, values_BinaryTree_add, label='Add')
    plt.plot(xlabels, values_BinaryTree_min, label='Get Min')
    plt.plot(xlabels, values_BinaryTree_max, label='Get Max')
    plt.legend()
    plt.xlabel("Number of Operations")
    plt.ylabel("Execution time (msec)")
    plt.title("Performance of BinaryTree")
    plt.show()

    plt.plot(xlabels, values_Quick_add, label='Add')
    plt.plot(xlabels, values_Quick_min, label='Get Min')
    plt.plot(xlabels, values_Quick_max, label='Get Max')
    plt.legend()
    plt.xlabel("Number of Operations")
    plt.ylabel("Execution time (msec)")
    plt.title("Performance of Quick")
    plt.show()

    plt.plot(xlabels, values_heap_add, label='Add')
    plt.plot(xlabels, values_heap_min, label='Get Min')
    plt.plot(xlabels, values_heap_max, label='Get Max')
    plt.legend()
    plt.xlabel("Number of Operations")
    plt.ylabel("Execution time (msec)")
    plt.title("Performance of Heap Solution")
    plt.show()

    plt.plot(xlabels, values_bubble_add, color='b', linestyle='-', label='Add')
    plt.plot(xlabels, values_bubble_min, color='b', linestyle='--', label='Get Min')
    plt.plot(xlabels, values_bubble_max, color='b', linestyle='-.', label='Get Max')
    plt.legend()
    plt.xlabel("Number of Operations")
    plt.ylabel("Total Execution time (msec)")
    plt.title("Performance of Bubble Sort")
    plt.show()

    plt.plot(xlabels, values_BinaryTree_add, color='g', linestyle='-', label='BinaryTree Add')
    plt.plot(xlabels, values_Quick_add, color='r', linestyle='-', label='Quick Add')
    plt.plot(xlabels, values_heap_add, color='b', linestyle='-', label='Heap Add')
    plt.plot(xlabels, values_bubble_add, color='y', linestyle='-', label='Heap Add')
    plt.legend()
    plt.xlabel("Number of Operations")
    plt.ylabel("Total Execution time (msec)")
    plt.title("Performance of Add")
    plt.show()

    plt.plot(xlabels, values_BinaryTree_min, color='g', linestyle='--', label='BinaryTree Get Min')
    plt.plot(xlabels, values_Quick_min, color='r', linestyle='--', label='Quick Get Min')
    plt.plot(xlabels, values_heap_min, color='b', linestyle='--', label='Heap Get Min')
    plt.plot(xlabels, values_bubble_min, color='y', linestyle='--', label='Heap Get Min')
    plt.legend()
    plt.xlabel("Number of Operations")
    plt.ylabel("Total Execution time (msec)")
    plt.title("Performance of Get Min")
    plt.show()

    plt.plot(xlabels, values_BinaryTree_max, color='g', linestyle='-.', label='BinaryTree Get Max')
    plt.plot(xlabels, values_Quick_max, color='r', linestyle='-.', label='Quick Get Max')
    plt.plot(xlabels, values_heap_max, color='b', linestyle='-.', label='Heap Get Max')
    plt.plot(xlabels, values_bubble_max, color='y', linestyle='-.', label='bubble Get Max')
    plt.legend()
    plt.xlabel("Number of Operations")
    plt.ylabel("Total Execution time (msec)")
    plt.title("Performance of Get Max")
    plt.show()

    plt.plot(xlabels, values_BinaryTree_add, color='g', linestyle='-', label='BinaryTree Add')
    plt.plot(xlabels, values_BinaryTree_min, color='g', linestyle='--', label='BinaryTree Get Min')
    plt.plot(xlabels, values_BinaryTree_max, color='g', linestyle='-.', label='BinaryTree Get Max')
    plt.plot(xlabels, values_bubble_add, color='y', linestyle='-', label='Heap Add')

    plt.plot(xlabels, values_Quick_add, color='r', linestyle='-', label='Quick Add')
    plt.plot(xlabels, values_Quick_min, color='r', linestyle='--', label='Quick Get Min')
    plt.plot(xlabels, values_Quick_max, color='r', linestyle='-.', label='Quick Get Max')
    plt.plot(xlabels, values_bubble_min, color='y', linestyle='--', label='Heap Get Min')

    plt.plot(xlabels, values_heap_add, color='b', linestyle='-', label='Heap Add')
    plt.plot(xlabels, values_heap_min, color='b', linestyle='--', label='Heap Get Min')
    plt.plot(xlabels, values_heap_max, color='b', linestyle='-.', label='Heap Get Max')
    plt.plot(xlabels, values_bubble_max, color='y', linestyle='-.', label='Heap Get Max')
    plt.legend()
    plt.xlabel("Number of Operations")
    plt.ylabel("Total Execution time (msec)")
    plt.title("Performance of BinaryTree, Matteo, Heap solutions")
    plt.show()


