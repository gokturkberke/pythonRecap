#import datetime
from datetime import datetime

now = datetime.now()
print(now) # 2024-11-28 13:42:53.805179

sonuc = now.year
print(sonuc) # 2024
#sonuc = now.month
#sonuc = now.day
#sonuc = now.hour

sonuc = datetime.ctime(now)
print(sonuc) # Thu Nov 28 13:42:53 2024

sonuc = datetime.strftime(now, "%Y") # 2024
#sonuc = datetime.strftime(now, "%X") # 13:42:53
#sonuc = datetime.strftime(now, "%d") # 28
#sonuc = datetime.strftime(now, "%Y %B %A") # 2024 November Thursday

#sonuc = now + timedelta(days=10 , minutes=20) 
# bu kod sonuc'a su an ki gune 10 gun ve 20 dakika ekler
