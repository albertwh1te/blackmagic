from Queue import Queue
from threading import Thread
import requests
#  import time


hosts = ["https://www.baidu.com/", "https://stackoverflow.com/#", "https://github.com/"]

queue = Queue()

class RequestWithThread(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue
    
    def run(self):
        host = self.queue.get()
        url = requests.get(host)
        print url.title
        self.queue.task_done()


#  start = time.time()
#  def main():
    #  for i in range(5):
        
    
