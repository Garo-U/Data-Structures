no_of_students = int(input("Enter number of students Whose marks are to be filled : "))
FDS = {}
FDS_absent = {}

for i in range (0,no_of_students):
    name = input("Name Of Student : ")
    ask = input("Is student Present or Absent (P/A) : ")
    if (ask == "P"):    
        marks = int(input("Enter Marks (out of 100): "))
        FDS[name]=marks
    elif(ask=="A"):
        FDS_absent[name]="Abesnt"
        
    else:
        pass

# print(FDS_absent)
values = FDS.values()
keys = FDS.keys()

# Average marks
avg = sum(values)/len(values)
print("\nAverage of marks of class : ",avg)

# highest score of class
highest = max(values)
print("\nHighest Score of class : ",highest)


low = min(values)
print("\nLowest Score of class : ",low)

new_list = list(FDS.values())
# print(new_list)

#marks with highest freq
count_max_freq = {}
for i in new_list:
    count_max_freq[i]=count_max_freq.get(i,0)+1


val = count_max_freq.values()
key = count_max_freq.keys()
print(max(count_max_freq, key = count_max_freq.get)," : ",max(val))


Absent_students = list(FDS_absent.values())
print("\nNumber of Absent Students are : ",len(Absent_students))
