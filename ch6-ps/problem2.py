# # Initialize variables
# total_marks = 0
# subject_count = 3
# pass_criteria_each_subject = 33
# pass_criteria_total = 40
# passed_all_subjects = True

# # Loop to input marks for each subject
# for i in range(1, subject_count + 1):
#     marks = float(input(f"Enter marks for Subject {i}: "))
#     total_marks += marks
#     if marks < pass_criteria_each_subject:
#         passed_all_subjects = False

# # Calculate average marks
# average_marks = total_marks / subject_count

# # Check pass/fail criteria
# if passed_all_subjects and average_marks >= pass_criteria_total:
#     print("Congratulations! The student has passed.")
# else:
#     print("Sorry, the student has failed.")


marks1 = int(input("enter marks1: "))
marks2 = int(input("enter marks 2:"))
marks3 = int(input("enter marks 3:"))

total_marks = marks1 + marks2 + marks3
percentage = total_marks/3

if(percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("yes you pass")
else:
    print("you failed!")
