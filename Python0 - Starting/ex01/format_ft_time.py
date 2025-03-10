import time
import datetime

# Get current time in seconds since January 1, 1970
current_time = time.time()

# Format the seconds in both standard and scientific notation
formatted_time = f"Seconds since January 1, 1970: {current_time:,.4f} or {current_time:.2e} in scientific notation"

# Get the current date and format it
current_date = datetime.datetime.now().strftime("%b %d %Y")

# Print results
print(formatted_time)
print(current_date)
