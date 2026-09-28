# Main Driver Script
# Integrates custom modules: data_manager, calculator, report

from data_manager import all_students, record_daily_attendance
from report import generate_attendance_report


def main():
  print("Starting Student Attendance & Defaulter Tracker System...")

  # Display current status report
  generate_attendance_report()

  # Simulate taking today's attendance
  print("Enter roll numbers present today (separated by space, e.g., 101 103):")
  raw_input_data = input("> ")

  if raw_input_data.strip():
    present_list = raw_input_data.split()
    absentees = record_daily_attendance(present_list)
    print("\nAttendance logged successfully.")
    print("Students Absent Today:", absentees)

    # Show updated summary
    print("\nUpdated Report Post-Session:")
    generate_attendance_report()


if __name__ == "__main__":
  main()