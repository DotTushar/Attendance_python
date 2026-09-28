# Module 1: Data storage and attendance marking operations

attendance_data = {
    "101": [1, 1, 1, 0, 1],
    "102": [1, 0, 0, 1, 0],
    "103": [1, 1, 1, 1, 1],
    "104": [0, 0, 1, 0, 0],
}

all_students = set(attendance_data.keys())


def record_daily_attendance(present_roll_numbers):
  """Updates attendance records and returns absent students using set operations."""
  present_set = set(present_roll_numbers)

  for roll in attendance_data:
    if roll in present_set:
      attendance_data[roll].append(1)
    else:
      attendance_data[roll].append(0)

  absent_today = all_students - present_set
  return absent_today