# -*- coding: utf-8 -*-
from time_respond import calc_get,calc_post
data ={
    "question":"發大發發大發43",
    "botkey":"586218e51d41c8772ca1c1d4"
}
print map(lambda x:calc_post("192.168.33.90:9528/crazybot/",data),[i for i in xrange(10)])[0]

