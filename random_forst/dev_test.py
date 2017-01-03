# -*- coding: utf-8 -*-

import requests
import json
# print map(lambda x:requests.post('http://192.168.33.97:8001/crazybot/api/chat',{'question':'自强不息厚德载物','auth_key':'dedada'}).content,[i for i in range(10)])

# print map(lambda x:requests.post('http://userver:9528/crazybot/api/chat',{'question':'自强不息厚德载物','auth_key':'dedada'}).content,[i for i in range(10)])[0]
# print json.loads(map(lambda x:requests.post('http://ubuntu:9528/crazybot/api/chat',{'question':'拍摄','botkey':'952733'}).content,[i for i in xrange(5000)])[0])['data']['answer']
# print json.loads(map(lambda x:requests.post('http://ubuntu:9528/crazybot/api/chat',{'question':'有何不可','botkey':'9527'}).content,[i for i in range(10)])[0])['data']['answer']

# content
# print json.loads(map(lambda x:requests.post('http://ubuntu:9528/crazybot/api/chat',{'question':'有何不可','botkey':'9524'}).content,[i for i in range(10)])[0])


# get content and code also
def testServer(info,n,last=10):
    print json.dumps(json.loads(map(lambda x:requests.post('http://ubuntu:9528/crazybot/api/chat',info).content,[i for i in range(n)])[0]),ensure_ascii=False,indent=2)

info = {'question':'如果觉得拍出来的原片不好怎么办','botkey':'585898951d41c876a4ec22a6'}
testServer(info,10)
