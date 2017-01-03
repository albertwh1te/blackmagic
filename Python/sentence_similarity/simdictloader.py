#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pickle
import numpy

class SimDictLoader:
    @staticmethod
    def load_ids():
        '''
        功能: 获取同义词编号多维数组
        每一个数组的首字母data都是统一的,分别从A到L
        '''
        ids_path = 'core/sentence_similarity/data/ids.npy'
        ids = numpy.load(ids_path)
        return ids


    @staticmethod
    def load_id_word():
        '''
        功能: 获取同义词编号词典
        数据的格式是{id:(word1,word2...)...}
        '''
        pkl_path = 'core/sentence_similarity/data/id_words.pkl'
        with open(pkl_path,'rb') as fr:
            id_words = pickle.load(fr)
        return id_words

    @staticmethod
    def load_word_dict():
        '''
        功能: 获取同义词字典
        数据的格式是{word:(id1,id2...)...}
        '''
        pkl_path = 'core/sentence_similarity/data/word_ids.pkl'
        with open(pkl_path,'rb') as fr:
            word_dict = pickle.load(fr)
        return word_dict
