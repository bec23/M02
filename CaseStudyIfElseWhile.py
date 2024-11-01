#Beck Rieger
#CaseStudyIfElseWhile
# enter student's name and gpa display if made dean's list or honor roll

while True:
    last_name = input("Enter the student's last name (or 'ZZZ' to quit): ")
    if last_name == 'ZZZ':
        break
        
    first_name = input("Enter the student's first name: ")
    gpa = float(input("Enter the student's GPA: "))
        
    if gpa >= 3.5:
        print(f"{first_name} {last_name} has made the Dean's List.")
    elif gpa >= 3.25:
        print(f"{first_name} {last_name} has made the Honor Roll.")
    else:
        print(f"{first_name} {last_name} did not qualify for the Dean's List or Honor Roll.")