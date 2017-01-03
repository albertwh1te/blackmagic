# coding:utf-8
import requests
import redis
import pymongo
import json

"""
  根据意图做出天气、火车相关信息回答，调用spider_reply(pattern)，参数为用户意图

  输出：{"replay":"",          回复内容
         "success"1,           根据用户输入，是否能实现查询 1 or 0
         "intention":"train"}  意图类别

  具体内容：
  if success = 0:
      replay为str，错误提示
  else：
      if intention = weather:
          replay为dict  {"weather":"今日天气~~~"}
      elif intention = train:
          replay为list  [{},{}],list里面是每趟车次的字典信息。字典具体信息包含
          {'车次','出发时间','到达时间','始发站','到达站','历时','商务座','特等座','一等座','二等座',
            '高级软卧','软卧','硬卧','软座','硬座','无座','总余票'}

"""
class weather_reply(object):
    def __init__(self):
        self.redisClient = redis.Redis(connection_pool = self.createChatbotRedisPool())
        self.mongoClient = pymongo.MongoClient("192.168.10.219",49019)

    def createChatbotRedisPool(self):
        pool = redis.ConnectionPool(host = '192.168.10.219', port = 6379, db = 1, max_connections = 2000)
        return pool

    def weather_select(self,weather_pattern):
        #获取city_id
        city = weather_pattern["loc"]["start"]
        print city
        city_id = self.redisClient.hget("weather_city_id_map",city)
        #查询不到城市id
        if city_id == None:
            return {"reply":'抱歉，此地点不在监控范围之内',"success":0}
        #获取city天气全部信息
        city_weather = self.mongoClient["hhly"]["weather"].find({"city_id":str(city_id)})[0]

        #根据用户意图type，做出应答
        # weather_result = self.weather_pattern_reply(weather_pattern,city_weather)
        return {"reply":{'weather':city_weather["weather_all"].encode("utf8")},"success":1}

    # def weather_pattern_reply(self,weather_pattern,city_weather):
    #     #用户询问温度
    #     if weather_pattern["type"] == "WD":
    #         werther_r = u'当前温度:' + city_weather["temperature"] + ',' + city_weather["cold_index"]
    #     #用户询问湿度
    #     elif weather_pattern["type"] == "SD":
    #         werther_r = u'当前湿度:' + city_weather["humidity"]
    #     #用户询问控制质量
    #     elif weather_pattern["type"] == "KQ":
    #         werther_r = u'控制污染指数:' + city_weather["air_index"]
    #     #用户询问天气
    #     elif weather_pattern["type"] == "TQ":
    #         werther_r = city_weather["weather_all"]
    #     #用户询问风
    #     elif weather_pattern["type"] == "FE":
    #         werther_r = city_weather["wind"]
    #     #用户询问紫外线
    #     elif weather_pattern["type"] == "ZW":
    #         werther_r = city_weather["uv_index"]
    #     #其它
    #     else:
    #         werther_r = city_weather["weather_all"]
    #     return werther_r

class tranin_reply(object):
    def trian_get(self,from_city,ari_city,date):
        url = 'https://kyfw.12306.cn/otn/lcxxcx/query?purpose_codes=ADULT&queryDate=%s&from_station=%s&to_station=%s'%(date,from_city,ari_city)
        print 'url is:',url
        header = {'Accept': '*/*',
         'Accept-Encoding': 'gzip, deflate, sdch, br',
         'Accept-Language': 'zh-CN,zh;q=0.8',
         'Cache-Control': 'no-cache',
         'Connection': 'keep-alive',
         'Host': 'kyfw.12306.cn',
         'If-Modified-Since': '0',
         'Referer': 'https://kyfw.12306.cn/otn/lcxxcx/init',
         'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
         'X-Requested-With': 'XMLHttpRequest'}
        cookie = {'BIGipServerotn': '972030474.50210.0000',
         'JSESSIONID': '57F1C757C9DEE02F5DA2C88478CC1BA5',
         '_jc_save_fromDate': '2016-12-11',
         '_jc_save_fromStation': '%u6DF1%u5733%u5317%2CIOQ',
         '_jc_save_toStation': '%u5E7F%u5DDE%u5357%2CIZQ',
         '_jc_save_wfdc_flag': 'dc'}

        r = requests.get(url,headers=header,cookies=cookie,verify=False,timeout=2)
        print r.status_code,type(r.status_code)
        if r.status_code == 403:
            return "太累了，休息，休息一会！"
        if json.loads(r.content)["data"].has_key("message"):
            return "好似没有直达的火车，您换个站试试。"
        message_list = json.loads(r.content)["data"]["datas"]
        message_list_new = []
        for d in message_list:
            all_num = self.num_judge(d["swz_num"]) + self.num_judge(d["tz_num"]) + self.num_judge(d["zy_num"]) + self.num_judge(d["ze_num"]) +\
                      self.num_judge(d["gr_num"]) + self.num_judge(d["rw_num"]) + self.num_judge(d["yw_num"]) + self.num_judge(d["rz_num"]) + self.num_judge(d["yz_num"]) + \
                      self.num_judge(d["wz_num"])
            message = {'车次':d["station_train_code"].encode("utf8"),
                    '出发时间':d["start_time"].encode("utf8"),
                    '到达时间':d["arrive_time"].encode("utf8"),
                    '始发站':d["start_station_name"].encode("utf8"),
                    '到达站':d["to_station_name"].encode("utf8"),
                    '历时':d["lishi"].encode("utf8"),
                    '商务座':d["swz_num"].encode("utf8"),
                    '特等座':d["tz_num"].encode("utf8"),
                    '一等座':d["zy_num"].encode("utf8"),
                    '二等座':d["ze_num"].encode("utf8"),
                    '高级软卧':d["gr_num"].encode("utf8"),
                    '软卧':d["rw_num"].encode("utf8"),
                    '硬卧':d["yw_num"].encode("utf8"),
                    '软座':d["rz_num"].encode("utf8"),
                    '硬座':d["yz_num"].encode("utf8"),
                    '无座':d["wz_num"].encode("utf8"),
                    '总余票':str(all_num)}
            message_list_new.append(message)
        return message_list_new
    #判断是否是数字
    def num_judge(self,w):
        try:
            n = int(w)
            return n
        except:
            return 0
    #获取城市id
    # def city_id_get(self,name):
    #     f = open("city_trian_map.txt",'r')
    #     city_d = f.readlines()
    #     f.close()
    #     for i in city_d:
    #         if name == i.split(":")[0]:
    #             return i

    def city_id_get(self, name):
        try:
            return dictf.city_dict[name]
        except:
            pass

    def message_sort(self,train):
        return int(train["总余票"])
    def main(self,from_city,ari_city,date):
        # from_city,ari_city,date = all[0],all[1],all[2]
        # from_city = self.city_id_get(from_city).split(":")[1].strip()
        # ari_city =  self.city_id_get(ari_city).split(":")[1].strip()
        from_city = self.city_id_get(from_city)
        ari_city = self.city_id_get(ari_city)
        data = self.trian_get(from_city,ari_city,date)
        if type(data) == str:
            return data
        else:
            data.sort(key=self.message_sort,reverse=True)
            return data[:5]

def spider_reply(pattern):
    if pattern["intention"] == 'weather':
        if pattern["timediff"] == 0:
            result_all = weather_reply().weather_select(pattern)
            result_all['intention'] = pattern['intention']
            return result_all
        else:
            return {"reply":'抱歉了，过去与未来的天气，小乐一概不晓得。',"success":0,'intention': pattern['intention']}

    if pattern["intention"] == 'train':
        print
        if (pattern["timediff"] <= 30) and (pattern["timediff"]>=0):
            result_all = tranin_reply().main(pattern["loc"]["start"],pattern["loc"]["end"],pattern["time"])
            if type(result_all) == list:
                return {"reply":result_all,"success":1,'intention': 'train'}
            else:
                return {"reply":result_all,"success":0,'intention': 'train'}
        elif weather_pattern["timediff"] <= 0:
            return {"reply":'火车已过站，据我估计，您大意了！',"success":0,'intention': 'train'}
        else:
            return {"reply":'车票满满，可惜未到预售期，查询的任务臣妾做不到呀！',"success":0,'intention': 'train'}


if __name__ == "__main__":
    weather_pattern = {'loc': {'start': 'df'}, 'length': 2, 'quest': [], 'details': {}, 'time': '2016-12-26', 'ask': [], 'timediff': 1, 'intention': 'weather'}
    train_pattern = {'loc': {'start': '武汉', 'end': '北京'}, 'length': 6, 'quest': [], 'details': {}, 'time': '2017-01-21', 'ask': [], 'timediff': 1, 'intention': 'train'}
    d = spider_reply(train_pattern)
    print d["reply"]
    print d["success"]
    print d["intention"]
    # for i in d["reply"]:
    #     print
    #     for k,v in i.items():
    #         print k,v,







