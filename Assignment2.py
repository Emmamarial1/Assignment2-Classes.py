class StudentRegistration:
    def __init__(self, course_name, max_students):
        self.course_name = course_name
        self.max_students = max_students
        self.registration_numbers = []

    def add_registration_number(self, reg_number):
        if len(self.registration_numbers) < self.max_students:
            self.registration_numbers.append(reg_number)
            print(f"Registration number {reg_number} added successfully.")
        else:
            print("Maximum number of students registered. Cannot add more.")

    def display_registration_numbers(self):
        print(f"Registration numbers for {self.course_name}:")
        for reg_number in self.registration_numbers:
            print(reg_number)


# Example usage
if __name__ == "__main__":
    # Create an instance of StudentRegistration
    course = StudentRegistration("Computer Science", 3)

    # Add registration numbers
    course.add_registration_number("CS2024001")
    course.add_registration_number("CS2024002")
    course.add_registration_number("CS2024003")
    course.add_registration_number("CS2024004")  # This should display an error

    # Display all registered numbers
    course.display_registration_numbers()
