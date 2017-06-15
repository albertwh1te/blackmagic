import datetime
from dateutil.relativedelta import relativedelta
import json

print "aa", datetime.datetime.now().date()
print "bb", datetime.datetime.now().date() - relativedelta(months=1)
