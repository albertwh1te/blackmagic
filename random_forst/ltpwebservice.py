# -*- coding: utf-8 -*-
"""
test response example for ltp server

<?xml version="1.0" encoding="utf-8" ?>
<xml4nlp>
    <note sent="y" word="y" pos="n" ne="n" parser="n" wsd="n" srl="n" />
    <doc>
        <para id="0">
            <sent id="0" cont="对文本进行分词的调用示例如下">
                <word id="0" cont="对" />
                <word id="1" cont="文本" />
                <word id="2" cont="进行" />
                <word id="3" cont="分词" />
                <word id="4" cont="的" />
                <word id="5" cont="调用" />
                <word id="6" cont="示例" />
                <word id="7" cont="如下" />
            </sent>
        </para>
    </doc>
</xml4nlp>

None
200
<?xml version="1.0" encoding="utf-8" ?>
<xml4nlp>
    <note sent="y" word="y" pos="y" ne="n" parser="n" wsd="n" srl="n" />
    <doc>
        <para id="0">
            <sent id="0" cont="ni hao a">
                <word id="0" cont="ni" pos="ws" />
                <word id="1" cont="hao" pos="ws" />
                <word id="2" cont="a" pos="ws" />
            </sent>
        </para>
    </doc>
</xml4nlp>

"""

import requests 
import xml.etree.ElementTree as ET
class LtpWebService():

    def __init__(self,host,port):
        self.host = host
        self.port = port
        self.url  = "%s:%d/ltp" %(host,port)

    def __talkServer(self,data):
        try:
            response = requests.post(self.url, data)
            if response:
                return response
            else:
                return None
        except Exception as e:
            print e
            return None


    def segment(self,text):
        data = {'s':text,
                'x':'n',
                't':'ws'
                }
        ret_list = []
        res = self.__talkServer(data)
        if res:
            tree = ET.fromstring(res.content)
            for word in tree.iter("word"):
                ret_list.append(word.attrib)
        return ret_list


    def postagger(self,text):
        data = {'s':text,
                'x':'n',
                't':'pos'
                }
        ret_list = []
        res = self.__talkServer(data)
        if res:
            tree = ET.fromstring(res.content)
            for word in tree.iter("word"):
                ret_list.append(word.attrib)
        return ret_list


    def parser(self,text):
        data = {'s':text,
                'x':'n',
                't':'dp'
                }
        ret_list = []
        res = self.__talkServer(data)
        if res:
            tree = ET.fromstring(res.content)
            for word in tree.iter("word"):
                ret_list.append(word.attrib)
        return ret_list

    def ner(self,text):
        data = {'s':text,
                'x':'n',
                't':'ner'
                }
        ret_list = []
        res = self.__talkServer(data)
        if res:
            tree = ET.fromstring(res.content)
            for word in tree.iter("word"):
                ret_list.append(word.attrib)
        return ret_list


    def split(self,text):
        data = {'s':text,
                'x':'n',
                't':'ws'
                }
        ret_list = []
        res = self.__talkServer(data)
        if res:
            tree = ET.fromstring(res.content)
            # print ET.tostring(tree)
            for sent in tree.iter('sent'):
                ret_list.append(sent.attrib)
        return map(lambda x:{'sent':x['cont'],'id':x['id']},[i for i in ret_list])

if __name__ == "__main__":
    ltp = LtpWebService("http://192.168.50.46",9527)
    print ltp.ner("七星彩是什么")
