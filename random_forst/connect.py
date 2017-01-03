# -*- coding: utf-8 -*-

import redis
# from mongo_config import MongoConfig
# from redis_config import RedisConfig
import pymongo

# mongodb,redis连接池初始化

def createChatbotRedisPool():
    pool = redis.ConnectionPool(host = RedisConfig.ChatbotConfig.HOST, port = RedisConfig.ChatbotConfig.PORT, db = RedisConfig.ChatbotConfig.DB, max_connections = 2000)
    return pool

def createChatbotMongoPool():
    pool = pymongo.MongoClient(
        host = 'ubuntu',
        port = 27017,
        minPoolSize = 10
    )
    c = pool[MongoConfig.ChatbotConfig.DB]
    c.authenticate(MongoConfig.ChatbotConfig.USER, MongoConfig.ChatbotConfig.PASSWORD)
    return pool
