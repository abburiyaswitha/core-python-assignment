def cal_average(marks):
    return sum(marks)/len(marks)
def cal_averages(students):
    averages = {}
    for name, marks in students.items():
        averages[name] = round(cal_average(marks), 2)
    return averages
def top_performer(averages):
    return max(averages,key=averages.get)
def get_student_marks():
    students = {}
    num_students = int(input("Enter the number of students:"))
    for _ in range(num_students):
        name = input("Enter the student's name:")
        marks = input(f"Enter marks for {name} separated by space:").split()
        marks = [int(mark) for mark in marks]  
        students[name] = marks
    return students
students = get_student_marks()
averages = cal_averages(students)
performer = top_performer(averages)
print("\nAverage Marks:", averages)
print("Top Performer:", performer)
