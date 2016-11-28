import os
import requests

for i in range(10):
    # print(os.urandom(10))
    a = requests.post('http://192.168.32.67:5000/api/bchatbot',{'questions':os.urandom(10)})
    print(a.content)
