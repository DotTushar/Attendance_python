# data_manager.py - State and storage

attendance_data = {
    "101": [1, 1, 0, 1],
    "102": [1, 0, 1, 1],
    "103": [1, 1, 1, 1],
    "104": [0, 1, 0, 1],
}

all_students = set(attendance_data.keys())


def record_daily_attendance(present_rolls):
  present = set(present_rolls)
  absentees = all_students - present
  for roll, history in attendance_data.items():
    history.append(1 if roll in present else 0)
  return absentees