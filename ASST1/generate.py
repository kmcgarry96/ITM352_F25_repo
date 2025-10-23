def generate_numbers(student_id):
    # Example: generate two numbers based on the student_id digits
    digits = [int(ch) for ch in student_id if ch.isdigit()]
    if len(digits) < 2:
        raise ValueError("Student ID must contain at least two digits.")
    return digits[0], digits[1]

try:
    student_id = input("Enter your student id (XXXXXXXX): ")
    num1, num2 = generate_numbers(student_id)
    print(f"Your two numbers are: {num1} and {num2}")
except ValueError as e:
    print(f"Error: {e}")

