# -*- coding: utf-8 -*-


class BaseModel(dict):

    def __init__(self,**attr):
        super(BaseModel,self).__init__(**attr)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError("Dict object has no attribute %s",key)

    def __setattr__(self, key, value):
        self[key] = value


