# -*- coding: UTF-8 -*-
text ="这是一个测试文本, 在关键字中投入了100元."
tager = "关键字"

def findInfo(text,keywords):
    text = text.encode('utf-8')
    keywords = [keyword.encode('utf-8') for keyword in keywords]
    for key in keywords:
        if key in text:
            index = text.find(key)
            return text[index:]


keywords = [tager]
print(text)
print(findInfo(text,keywords))