from threading import Thread
from threading import Lock

class ProfitTracker(Thread):
    def __init__(self):
      Thread.__init__(self)
      self.profits = [0]
      self.new_value = True
      self.running = True
      self.index = 0
      self.lock = Lock()
    
    def update(self, profit):
        try:
            self.lock.acquire()
            self.profits.append(float(profit))
        except:
            print("unable to obtain last profit value")
        finally:
            self.lock.release()


    def total(self):
        return sum(self.profits)

    def run(self):
        while self.running:
            try:
                self.lock.acquire()
                if self.index < len(self.profits):
                    # print(f'last profit: {self.profits[self.index]}, total profit: {self.total()}')
                    self.index = self.index + 1
            except Exception as exp:
                print(f"unable to print latest profit, reason {exp}")
            finally:
                self.lock.release()

        print("Profit track succesfully shutdown")
    
    def close(self):
       self.running = False


