def calculate_average(marks):
    return sum(marks) / len(marks)

def find_top_performer(students):
    averages = {}
    for student, marks in students.items():
        averages[student] = calculate_average(marks)
    top_performer = ""
    highest_average = 0
    for student, average in averages.items():
        if average > highest_average:
            highest_average = average
            top_performer = student
    return averages, top_performer

students = {
    "John": [85, 78, 92], 
    "Alice": [88, 79, 95], 
    "Bob": [70, 75, 80]
}

averages, top_performer = find_top_performer(students)

print(f"Average Marks: {averages}")
print(f"Top Performer: {top_performer}")
