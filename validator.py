# validator.py - Input sanitising


def check_valid_rolls(raw_input, all_students):
  valid, invalid, seen = [], [], set()
  for token in raw_input.split():
    if token in seen:
      continue
    seen.add(token)
    if token in all_students:
      valid.append(token)
    else:
      invalid.append(token)
  return valid, invalid