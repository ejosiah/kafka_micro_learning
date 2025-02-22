import time

from sales_tracker import ProfitTracker
from ui import UI
from sales_consumer import Consumer

pt = ProfitTracker()
ui = UI(pt)
c = Consumer(pt)
pt.start()
ui.start()
c.start()


ui.join()
pt.close()
c.close()

print("sales consumer sucessfully shutdown")