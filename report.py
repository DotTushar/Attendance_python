# report.py - Console reporting
from calculator import calculate_percentage, get_defaulters


def generate_attendance_report(
    records, threshold=75.0, title="ATTENDANCE REPORT"
):
  defaulters = get_defaulters(records, threshold)
  histories = {r: "".join(map(str, h)) for r, h in records.items()}
  # column width grows with the longest history string
  width = max(len("History"), *(len(h) for h in histories.values())) + 4
  line = "-" * (7 + width + 10 + 10 + 9)

  print(f"\n{title}")
  print(line)
  print(f"{'Roll':<7}{'History':<{width}}{'Sessions':<10}{'Percent':<10}Status")
  print(line)
  for roll in sorted(records):
    pct_text = f"{calculate_percentage(records[roll]):.2f}%"
    status = "DEFAULTER" if roll in defaulters else "OK"
    print(
        f"{roll:<7}{histories[roll]:<{width}}{len(records[roll]):<10}{pct_text:<10}{status}"
    )
  print(line)
  if defaulters:
    print(
        f"ALERT: {len(defaulters)} student(s) below {threshold}% ->"
        f" {', '.join(defaulters)}"
    )
    