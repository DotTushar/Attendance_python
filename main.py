# main.py - Driver script
import data_manager
from report import generate_attendance_report
from validator import check_valid_rolls


def main():
  generate_attendance_report(
      data_manager.attendance_data, title="PRE-SESSION SUMMARY"
  )
  raw = input("Enter roll numbers present today (space-separated): ")
  present, invalid = check_valid_rolls(raw, data_manager.all_students)

  if invalid:
    print(f"Ignored unrecognised roll numbers: {invalid}")
  if not present:
    print("Warning: no valid rolls entered; everyone is marked absent.")

  absentees = data_manager.record_daily_attendance(present)
  print(f"Absentees identified: {absentees}")

  generate_attendance_report(
      data_manager.attendance_data, title="POST-SESSION SUMMARY"
  )


if __name__ == "__main__":
  main()
  