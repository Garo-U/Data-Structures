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

marks = FDS.values()
freq = {}
for i in marks:
    if  i in freq:
        freq[i] += 1
    else :
        freq[i]=1

high_freq = 0
high_f_marks = None

for m,c in freq.items():
    if c > high_freq:
        high_freq = c
        high_f_marks = m
    

if high_freq == 1:
    print("All marks have the same freq")
else:    
    print(f"marks with max freq are {high_f_marks} : {high_freq}")


Absent_students = list(FDS_absent.values())
print("\nNumber of Absent Students are : ",len(Absent_students))
