import time as t
import datetime as dt

epoch_time = t.time()
today_date = dt.date.today().strftime("%b %d %Y")

print(f"Seconds since January 1, 1970: {'{:,.4f}'.format(epoch_time)} or {'{:e}'.format(epoch_time)} in scientific notation")
print(today_date)
