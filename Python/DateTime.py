import datetime
import pytz  # for timezone operations

# 1) Date function
# d = datetime.date(2025, 1, 1)  # 01 will lead to syntax error
# print(d)
# tday = datetime.date.today()  # returns the current date
# print(tday)  # prints entire current date
# print(tday.day)  # prints only the current day
# print(tday.month)  # prints only the current month
# print(tday.year)  # prints only the current year
# print(f"{tday.weekday()}, {tday.isoweekday()}")  # for weekday monday is 0 and isoweekday monday is 1

# Timedeltas are the difference between 2 dates or times
# tdelta = datetime.timedelta(days=7)
# print(tday + tdelta)  # will return 7 days after date

# ** date2 = date1 + timedelta **
# ** timedelta = date1 + date2 **
# bday = datetime.date(2025, 3, 1)
# till_bday = bday - tday  # subtraction of 2 dates results into a timedelta
# print(till_bday.days)
# print(till_bday.total_seconds())

# 2) Time function
# t = datetime.time(6, 30, 50, 4000)
# print(t)  # prints the time
# print(t.hour)  # prints only the time
# print(t.minute)  # prints only the minute

# 3) DateTime function  (combination of both date and time)
# dt = datetime.datetime(2025, 1, 1, 6, 30, 50, 4000)
# print(dt)  # prints entire date with its time
# print(dt.date())  # prints only the date
# print(dt.time())  # prints only the time
# dt_today = datetime.datetime.today()  # returns current date and time
# dt_now = datetime.datetime.now()  # returns current date and time but with an option to pass timezone
# dt_utcnow = datetime.datetime.utcnow()  # returns current utc date and time but with an option to pass timezone
# print(dt_today)
# print(dt_now)
# print(dt_utcnow)

# Usage of datetime with pytz
# dt = datetime.datetime(2025, 1, 1, 6, 30, 50, 4000, tzinfo=pytz.UTC)
# print(dt)  # adds utc timezone offset
# dt_now = datetime.datetime.now(tz=pytz.UTC)  # explicitly mentioned timezone here
# print(dt_now)  # returns current date and time with utc timezone
# dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)  # same as above
# print(dt_utcnow)
# ** print(pytz.all_timezones)  ** # gives list of all the timezones
# dt_india = dt_now.astimezone(pytz.timezone('Asia/Kolkata'))  # change timezone explicitly
# print(dt_india)  # returns the indian date and time with respect to utc timezone

# ** Convert naive datetime to specific timezone using localize() **
# dt_now = datetime.datetime.now()
# print(dt_now)  # we don't have timezone here
# india_tz = pytz.timezone('Asia/Kolkata')  # we mention indian timezone
# dt_india = india_tz.localize(dt_now)  # we make naive datetime to indian timezone datetime using localize()
# print(dt_india)
# dt_us_mtn = dt_now.astimezone(pytz.timezone('Us/Mountain'))  # now we can convert timezone
# print(dt_us_mtn)  # prints the datetime with respect to 'Us/Mountain' timezone

# ** strftime and strptime **
# a) strftime - converts date into string
# b) strptime - converts string into a date
# print(dt_india.strftime('%B %d, %Y'))  # prints in specified format using strftime() where f stands for format
# dt_str = 'January 01, 2025'
# dt_strptime = datetime.datetime.strptime(dt_str, '%B %d, %Y')  # p in strptime stands for parse
# print(dt_strptime)
