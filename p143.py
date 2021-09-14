#import datetime
from datetime import *
#import dateutil.relativedelta
from dateutil.relativedelta import relativedelta
#today = datetime.date.today()
today = date.today()
# 本日
print(today)
# 50 日 前
#print(today + dateutil.relativedelta.relativedelta(days=-50))
print(today + relativedelta(days=-50))
# 2 ヶ月 後
print(today + relativedelta(months=2))
# 3 ヶ月 と 10 日 後
print(today + relativedelta(days=10, months=3))
