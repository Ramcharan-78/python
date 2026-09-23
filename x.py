def grade_manager_demo():
    students = {
        "Ravi": [85, 90, 78],
        "Anita": [60, 55, 40],
        "Kiran": [95, 92, 99],
    }
 
    def calculate_average(marks):
        return sum(marks) / len(marks)
 
    def assign_grade(avg):
        if avg >= 90:
            return "A"
        elif avg >= 75:
            return "B"
        elif avg >= 50:
            return "C"
        else:
            return "F"
 
    for name, marks in students.items():
        avg = calculate_average(marks)
        grade = assign_grade(avg)
        print(f"{name}: Average = {avg:.2f}, Grade = {grade}")

grade_manager_demo()

