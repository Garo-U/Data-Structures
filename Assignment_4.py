def selection_sort(array):

    for i in range(len(array)):
        min = i

        for j in range(i+1,len(array)):
            if (array[min]>array[j]):
                min = j
            array[min],array[i] = array[i],array[min]


def bubble_sort(array):
    n = len(array)

    for i in range(n - 1):
        for j in range(n-i-1):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]



nos_students = int(input("Enter Number of Students : "))
Marks = []

for i in range(nos_students):
    ask = float(input(f"Marks of Roll no-{i+1} : "))
    Marks.append(ask)



