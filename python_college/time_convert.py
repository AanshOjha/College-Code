time_12hr = input("Enter time in 12-hour format (hh:mm AM/PM): ")

# Split time and period
time_part, period = time_12hr.split()
hours, minutes = map(int, time_part.split(':'))

# Convert hours
if period.upper() == 'PM' and hours != 12:
    hours += 12
elif period.upper() == 'AM' and hours == 12:
    hours = 0

# Format the output
print(f"Time in 24-hour format: {hours:02d}:{minutes:02d}")
