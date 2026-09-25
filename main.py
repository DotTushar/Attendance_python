# Student Attendance and Defaulter Tracker
# Course: CSE1021 Problem Solving and Python Programming

# Dictionary to store attendance records: roll_no -> list of 1s (present) and 0s (absent)
attendance_data = {
    "101": [1, 1, 1, 0, 1],
    "102": [1, 0, 0, 1, 0],
    "103": [1, 1, 1, 1, 1],
    "104": [0, 0, 1, 0, 0],
}

# Set containing all registered roll numbers
all_students = set(attendance_data.keys())


# Module 1: Mark attendance for a single day using Lists and Sets
def mark_attendance():
  print("\n--- Mark Today's Attendance ---")
  present_input = input(
      "Enter roll numbers present today (separated by space): "
  )
  present_list = present_input.split()

  # Set of students present today
  present_set = set(present_list)

  for roll in attendance_data:
    if roll in present_set:
      attendance_data[roll].append(1)
    else:
      attendance_data[roll].append(0)

  # Using set difference to find who was absent today
  absent_today = all_students - present_set
  print("Attendance recorded.")
  print("Absent today:", absent_today)


# Module 2: Calculate attendance percentage using List sum and len
def calculate_percentage(roll):
  record = attendance_data[roll]
  if len(record) == 0:
    return 0.0

  total_classes = len(record)
  attended_classes = sum(record)
  percentage = (attended_classes / total_classes) * 100
  return round(percentage, 2)


# Module 3: Identify defaulters (< 75% attendance) using conditions
def find_defaulters():
  defaulter_list = []
  for roll in attendance_data:
    pct = calculate_percentage(roll)
    if pct < 75.0:
      defaulter_list.append((roll, pct))
  return defaulter_list


# Module 4: Display complete summary report
def display_summary():
  print("\n================ ATTENDANCE SUMMARY ================")
  print("Roll No\t\tRecords\t\tPercentage\tStatus")
  print("----------------------------------------------------")

  for roll in attendance_data:
    pct = calculate_percentage(roll)
    status = "Defaulter" if pct < 75.0 else "Eligible"
    print(f"{roll}\t\t{attendance_data[roll]}\t{pct}%\t\t{status}")

  defaulters = find_defaulters()
  print("\nTotal Defaulters (< 75%):", len(defaulters))
  for roll, pct in defaulters:
    print(f"Warning: Roll No {roll} has only {pct}% attendance!")
  print("====================================================\n")


# Main driver loop
while True:
  print("=== Attendance Management System ===")
  print("1. View Attendance Summary")
  print("2. Mark Attendance for Today")
  print("3. Check Only Defaulters (< 75%)")
  print("4. Exit")

  choice = input("Enter choice (1-4): ")

  if choice == "1":
    display_summary()
  elif choice == "2":
    mark_attendance()
  elif choice == "3":
    defaulters = find_defaulters()
    print("\n--- Defaulters List ---")
    if len(defaulters) == 0:
      print("No defaulters! Everyone is above 75%.")
    else:
      for roll, pct in defaulters:
        print(f"Roll: {roll} | Attendance: {pct}%")
    print()
  elif choice == "4":
    print("Exiting program. Thank you!")
    break
  else:
    print("Invalid choice, please enter 1, 2, 3, or 4.\n")