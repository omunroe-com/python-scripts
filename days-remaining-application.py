##Number of Days to the event (Days remaining application)
from datetime import *  #Import the datetime library

today = date.today()
future = date(2015,06,30)  #Add the Future date here
days = (str(future - today))
comma = days.find(",")
days = days[:comma]
print(days)
