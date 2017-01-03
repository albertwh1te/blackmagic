# -*- coding: utf-8 -*-

import json
# from rediskeydef import RedisKeyDef

class DBName:
    crazybot = "crazybot"

class TblUser:
    tbl_name = "USERS"
    username = "username"
    passwd = "passwd"
    phone = "phone"
    phone_valid_time = "phone_valid_time"
    authkey = "authkey"
    botkey = "botkey"
    email = "email"
    email_valid_time = "email_valid_time"
    valid = "valid"
    last_login_time = "last_login_time"
    level = "level"
    totalnumber = "totalnum"
    accounttype = "accounttype"
    validid = "validid"
    frontimg = "frontimg"
    backimg = "backimg"

class TblCrazybot:
    tbl_name = "crazybot"

class TblBot:
    tbl_name = "BOT"
    botkey = "botkey"
    name = "name"
    age = "age"
    sex = "sex"
    hobby = "hobby"
    brithday = "birthday"
    region = "region"
    removed = "removed"

class TblKD:
    tbl_name = "KD"
    _id = "_id"
    botkey = "botkey"
    answer = "answer"
    question = "question"
    related = "related"
    removed = "removed"
    create_time = "create_time"
    update_time = "update_time"
    simhash = "simhash"

class TblVagueQuestion:
    tbl_name = "VAGUEQUESTION"
    question = "question"
    rquestion = "rquestion"
    rid = "rid"
    answer = "answer"
    botkey = "botkey"
    dealed = "dealed"
    removed = "removed"
    create_time = "create_time"

class TblUnknowQuestion:
    tbl_name = "UNKNOWQUESTION"
    question = "question"
    botid = "botid"
    removed = "removed"
    create_time = "create_time"

class TblCrazybotConfig:
    tbl_name = "crazybot_config"
    name = "name"
    value = "value"

def get_config_redis(mongoClient, redisClient):
    key = RedisKeyDef.get_crazybot_config_key()
    configs = redisClient.get(key)
    if not configs:
        configs = load_config_mongodb(mongoClient)
        redisClient.setex(key, json.dumps(configs), 24 * 24 * 60 * 60)
        return configs
    elif configs:
        configs = json.loads(configs)
        return configs
    return {}

def load_config_mongodb(mongoClient):
    query = {}
    key_list = {"_id": 0}
    a = mongoClient[DBName.crazybot][TblCrazybotConfig.tbl_name].find(query, key_list)
    ret = {}
    for aa in a:
        ret.update({aa.get(TblCrazybotConfig.name): aa.get(TblCrazybotConfig.value)})
    return ret

def set_config_mongodb(mongoClient, name, value):
    query = {TblCrazybotConfig.name: name}
    udata = {"$set": {TblCrazybotConfig.value: value}}
    mongoClient[DBName.crazybot][TblCrazybotConfig.tbl_name].update(query, udata, upsert = True)
