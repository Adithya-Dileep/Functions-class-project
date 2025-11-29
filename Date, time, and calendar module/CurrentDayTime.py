from datetime import date, time, datetime
today = date.today()
now = datetime.now()
print("Today's date:", today)
print("Current time:", now.time())
year = today.year
month = today.month
day = today.day
print("Year:", year)
print("Month:", month)
print("Day:", day)