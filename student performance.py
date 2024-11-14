from tabulate import tabulate

class Student:
    def __init__(self, sname, s_scores):
        self.name = sname
        self.scores = s_scores

    def calculate_average(self):
        total = sum(self.scores)
        count = len(self.scores)
        average = total / count
        return average

    def is_passing(self):
        for score in self.scores:
            if score < 40:
                return False
        return True

    def update_scores(self, new_scores):
        self.scores = new_scores

class PerformanceTracker:
    def __init__(self):
        self.students = {}

    def add_student(self, name, scores):
        new_student = Student(name, scores)
        self.students[name] = new_student

    def modify_student(self, name, new_scores):
        if name in self.students:
            student = self.students[name]
            student.update_scores(new_scores)
            print(f"Updated scores for {name}.")
        else:
            print(f"Student '{name}' not found.")

    def display_student_marks(self, name):
        if name in self.students:
            student = self.students[name]
            subjects = ["Math", "Science", "English"]
            data = zip(subjects, student.scores)
            print(f"\nMarks for {name}:")
            print(tabulate(data, headers=["Subject", "Score"], tablefmt="grid"))
            print(f"Average Score: {student.calculate_average():.2f}")
            print(f"Status: {'Passing' if student.is_passing() else 'Needs Improvement'}\n")
            return True
        else:
            print(f"\nStudent '{name}' not found.")
            return False

    def display_class_metrics(self):
        if not self.students:
            print("No students to display.")
            return

        table = []
        for name, student in self.students.items():
            average = student.calculate_average()
            status = "Passing" if student.is_passing() else "Needs Improvement"
            table.append([name, *student.scores, f"{average:.2f}", status])

        headers = ["Name", "Math", "Science", "English", "Average", "Status"]
        print("\nClass Metrics:")
        print(tabulate(table, headers=headers, tablefmt="grid"))
        print(f"\nClass Average: {self.calculate_class_average():.2f}\n")

    def calculate_class_average(self):
        if not self.students:
            return 0
        total_average = 0
        for student in self.students.values():
            total_average += student.calculate_average()
        class_average = total_average / len(self.students)
        return class_average

def get_student_data():
    name = input("Enter student name: ")
    scores = []
    for subject in ["Math", "Science", "English"]:
        while True:
            try:
                score = int(input(f"Enter score for {subject}: "))
                scores.append(score)
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
    return name, scores

def main():
    tracker = PerformanceTracker()

    while True:
        print("\n--- Student Performance Tracker ---")
        print("1. Add New Student")
        print("2. Modify Subject Scores")
        print("3. Show student subject Marks")
        print("4. Show Class performance")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            name, scores = get_student_data()
            tracker.add_student(name, scores)
            print(f"Added student {name}.\n")

        elif choice == '2':
            name = input("Enter the name of the student to modify: ")
            _, new_scores = get_student_data()
            tracker.modify_student(name, new_scores)

        elif choice == '3':
            while True:
                name = input("Enter the name of the student to view marks (or type 'menu' to return to main menu): ")
                if name.lower() == 'menu':
                    break
                if tracker.display_student_marks(name):
                    break
                else:
                    print("Please enter a valid student name or type 'menu' to return to the main menu.")

        elif choice == '4':
            tracker.display_class_metrics()

        elif choice == '5':
            print("Exiting Student Performance Tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please choose a valid option.\n")

if __name__ == "__main__":
    main()
