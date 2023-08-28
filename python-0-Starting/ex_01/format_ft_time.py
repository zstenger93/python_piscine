import time
import locale
import datetime


# Set locale to use comma as a thousands separator
locale.setlocale(locale.LC_ALL, '')

# Current date and time -> floating-point number
current_time = time.time()
formatted_current_time = \
 locale.format_string("%.4f", current_time, grouping=True)

# Specific date
current_date = datetime.date.today()

print(f"Seconds since January 1, 1970: \
{formatted_current_time} or {current_time:.2e} in scientific notation")
print(f"{current_date}")
print(f"{current_date.strftime('%B')} {current_date.day} {current_date.year}")
print(f"{current_date.strftime('%b %d %Y')}")
