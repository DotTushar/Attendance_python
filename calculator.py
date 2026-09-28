# calculator.py - Pure computation


def calculate_percentage(history):
  if not history:
    return 0.0
  return round(sum(history) / len(history) * 100, 2)


def get_defaulters(records, threshold=75.0):
  # strictly below the threshold: exactly 75.0 remains eligible
  return sorted(
      roll
      for roll, history in records.items()
      if calculate_percentage(history) < threshold
  )