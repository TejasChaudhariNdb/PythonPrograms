# Program for LIST In Python

print("Enter Your Name")
subject = []   #Empty List
marks = []  #Empty Marks List


name = input()

print("Wellcome "+name)

print("How Many subject do You Have....")
TotalSub = int(input())

for x in range(TotalSub):
   
   sub = input("Subject Name ")
   subject.append(sub)
   

print("Now enter Subject Marks As Follow")

for y in subject:
      print(y)
      marks.append(int(input))
      
total = sum(marks)
per = total/TotalSub

print(name + "Your Total is "+ str(total))
print("Percentage is " str(per))
print("--------------------------------------")

for sub in range(len(subject)):
     print(str(subject[sub]) + "Marks Are " + str(marks[sub]))
     
     
     
     # Thanx For Watching Video See OutPut Now More Video 
     # Code IS On github see link bellow
     # Subscribe And Like video 
     # 100k likes
     # Have Nice Day
     
     
     
     
     
     
