student_name = input("Insert Student Name: ")
english_marks = int(input("Insert Eng. Marks: "))
urdu_marks = int(input("Insert Urdu Marks: "))
math_marks = int(input("Insert Maths Marks: "))
physics_marks = int(input("Insert Physics Marks: "))
islamiat_marks = int(input("Insert Islamiat Marks: "))
marks_obtained = english_marks + urdu_marks +math_marks + physics_marks + islamiat_marks
total_marks = 500

percentage = marks_obtained/total_marks*100

print("Total Marks: ",total_marks)
print("Obtained Marks: ",marks_obtained)
print("Perentage: ",percentage)

if percentage >= 90:
    print("Greade: A+")
elif percentage < 90 and percentage >= 80:
    print("Greade: A")
elif percentage < 80 and percentage >= 70:
    print("Greade: B")
elif percentage < 70 and percentage >= 60:
    print("Greade: C")
elif percentage < 60 and percentage >= 50:
    print("Greade: D")
else:
    print("Failed")

