# calculator.py - Handles calculations and defaulter detection

from data_manager import attendance_data


def calculate_percentage(roll):
  record = attendance_data.get(roll, [])
  if len(record) == 0:
    return 0.0
  return round((sum(record) / len(record)) * 100, 2)


def get_defaulters(threshold=75.0):
  defaulter_list = []
  for roll in attendance_data:
    pct = calculate_percentage(roll)
    if pct < threshold:
      defaulter_list.append((roll, pct))
  return defaulter_list