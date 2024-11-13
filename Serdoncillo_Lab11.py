list_num = []
student_number = 5 
Pass_grade = 75 
 

for num in range (5):
    num=int(input("Enter Grade: "))
    if num <= 100 and num >= 40:
        list_num.append(num)
        if num >= 75 and num <= 100:
            passed =+1
        else:
            failed =+1
    else:
        print("Invalid Grade")
    
fAverage = sum(list_num) / student_number

Passing_Grade = sum(1 for grade in list_num if grade >= Pass_grade )

Passing_Percentage = ( Passing_Grade/student_number)*100

print("Input Grade:", list_num)
print("Passing grade:", Passing_Grade)
print ("Average grade:" , fAverage )  
print("Passing Percentage:", (round),Passing_Percentage, "%" )