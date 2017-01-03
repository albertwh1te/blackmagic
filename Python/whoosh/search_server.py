# coding:utf-8

from flask import current_app as app

from whoosh.qparser import QueryParser
from whoosh.query import Term
from whoosh.index import create_in,open_dir
from whoosh.fields import *
from whoosh.analysis import RegexAnalyzer

analyzer = RegexAnalyzer(ur'[\u4e00-\u9fa5]|\w')
whoosh_schema = Schema(whooshid = ID(stored=True,unique=True), question=TEXT(stored=True,analyzer=analyzer), answer=TEXT(stored=True),botkey=TEXT(stored=True))

class WhooshServer(object):

    def __init__(self,**options):
        self.__datapath = options.get('datapath')
        # self.__schema = options.get('schema')
        self.__mclient = options.get('mclient')
        self.__reload = options.get('RELOAD')
        self.__schema = whoosh_schema
        if self.__reload:
            self.__index = create_in(self.__datapath,self.__schema)
            self.__writer = self.__index.writer()
            self.load_from_mongo(self.__mclient)
        else:
            self.__index = open_dir(self.__datapath)
            self.__writer = self.__index.writer()

    # basic method
    def init_whoosh(self, dataset):
        # types is important
        for data in dataset:
            # to do check types
            data.get('_id') and data.update({'id':unicode(data.get('_id'))})
            # data.update({'question':data.get('question')})
            # print data.get('question')
            self.__writer.add_document(
                whooshid = data.get('id'),
                question = data.get('question'),
                answer = data.get('answer'),
                botkey = data.get('botkey')
                )
        self.commit()


    def add_one_document(self, data):
        self.__writer.add_document(**data)

    def commit(self):
        self.__writer.commit()
        self.__writer = self.__index.writer()

    def search_document(self, field, data):
        query = QueryParser(field, self.__index.schema).parse(data)
        return self.__index.searcher().search(query)


    # business method
    def load_from_mongo(self,mclient):
        # mclient = app.cbMongoPool[tabledef.DBName.chatbot]
        all_data = mclient['KD'].find({u'removed':0},
                                              {u'_id':1,u'answer':1,u'question':1,u'botkey':1})
        self.init_whoosh(all_data)

    def search_question(self,keywords):
        return self.search_document('question',keywords)

    def update_one_document(self,whooshid,question,botkey,answer):
        self.__writer.update_document(
            whooshid=whooshid,
            question=question,
            botkey=botkey,
            answer=answer
            )
        self.commit()

    def search_question_with_bot(self,keywords,botkey):
        query_obj = QueryParser('question', self.__index.schema)
        search_data = query_obj.parse(keywords)
        filter_data = Term('botkey',botkey)
        return self.__index.searcher().search(search_data,filter=filter_data)

    def delete_question(self,whooshid):
        # TO DO figure out index lock problem
        # self.__index.delete_by_term('whooshid',whooshid)
        self.__writer.update_document(whooshid=whooshid)
        self.commit()


