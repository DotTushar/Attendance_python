# report.py - Handles console reporting and summaries

from calculator import calculate_percentage, get_defaulters
from data_manager import attendance_data


def generate_attendance_report():
  print("\n================ ATTENDANCE SUMMARY ================")
  print("Roll No\t\tRecords\t\t\tPercentage\tStatus")
  print("----------------------------------------------------")
  for roll, records in attendance_data.items():
    pct = calculate_percentage(roll)
    status = "Defaulter" if pct < 75.0 else "Eligible"
    print(f"{roll}\t\t{records}\t{pct}%\t\t{status}")

  defaulters = get_defaulters(75.0)
  print("\nTotal Defaulters (< 75%):", len(defaulters))
  for roll, pct in defaulters:
    print(f"Warning: Roll No {roll} has only {pct}% attendance!")
  print("====================================================\n")