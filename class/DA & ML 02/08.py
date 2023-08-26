# pip install persiantools
# "۱۴۰۲/۰۵/۱۳" == "1402/05/13"

from datetime import datetime, timedelta
from persiantools.jdatetime import JalaliDate


# "2023-04-08 16:01:17"
# d = datetime(2023, 4, 8, 16, 1, 17)
# print(d.year)
# print(d.minute)
# print(d.month)
# print(d.weekday())

# print(d)
# print(d + timedelta(days=27, hours=1400, minutes=2300))


# d = "2023-04-08 20a17:19"
#
# print(datetime.strptime(d, "%Y-%m-%d %H:%M:%S").date())
# print(datetime.strptime(d, "%Y-%m-%d %H:%M:%S").time())

# print(datetime.now())

# n = datetime.now()
# j_date = JalaliDate(n).strftime("%B")
# print(j_date)
# print(j_date.isoweekday())
# JalaliDate.today().to_gregorian()
# print(JalaliDate.days_in_month(12, 1402))
# print(JalaliDate.is_leap(1402))