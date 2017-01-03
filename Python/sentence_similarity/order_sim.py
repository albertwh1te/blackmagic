# -*- coding: utf-8 -*-
import numpy
import pickle
import math
import time
import os
from fuzzywuzzy import fuzz
from simdictloader import SimDictLoader

class ImprovedOrderSim(object):
    '''
    功能: 改进后的语句相似度系统
    '''

    def __init__(self):
        '''
        功能: 不同语句相似度初始化
        '''
        # 词型相似度权重
        self.W1 = 0.4
        # 句长相似度权重
        self.W2 = 0.15
        # 词序相似度权重
        self.W3 = 0.05
        # 单字词型相似度
        self.W4 = 0.4

    def revOrder(self,a_list):
        '''
        功能:对一个纯数字的数组,计算逆序数
        '''
        #获取排列好的数组
        stand_list = sorted(a_list)
        #获取输入数组在正序数组中的下标
        index_list = [stand_list.index(i) for i in a_list]
        index_array = numpy.array(index_list)
        #计算i位置之前比ｉ位置的值大的有多少个
        nums = [numpy.sum(index_array[:i] > sub_index)
                for i,sub_index in enumerate(index_list)]
        return numpy.sum(nums)

    def wordSim(self,a_terms,b_terms):
        '''
        功能:词形相似度
        '''
        # 获取两句话相同的单词
        common_words = set(a_terms) & set(b_terms)
        # 获取单词在第一二句话中的频率
        # 格式为:{term:[first_frq,second_frq]}
        common_freq = {term: [a_terms.count(term), b_terms.count(term)] for term in common_words}
        # 得到两句话共有单词的个数, 如果出现单词出现次数不同
        # 则取最小出现次数
        samews = float(sum(map(min,common_freq.values())))
        # 计算词形相似度
        word_sim = samews/max(len(a_terms),len(b_terms))
        return word_sim

    def lenSim(self,a,b):
        '''
        功能:句长相似度
        '''
        # 转换语句格式成unicode
        if type(a) is str: a = a.decode('utf8')
        if type(b) is str: b = b.decode('utf8')
        # 计算每句话单字的个数
        len_fun = lambda x: float(len(x))
        a_len = len_fun(a)
        b_len = len_fun(b)
        # 计算句长相似度
        len_sim = 1-abs(a_len-b_len)/(a_len+b_len)
        return len_sim

    def orderSim(self,a_terms, b_terms):
        '''
        功能:词序相似度
        参数:
            onews_unsort: 没有排序的单频率单词数组
            onews_sorted: 按照第一句话的单频词下标,
                排序得到的单频词数组
        '''
        # 获取两句话相同的单词
        common_words = set(a_terms) & set(b_terms)
        # 获取单词在第一二句话中的频率
        # 格式为:{term:[first_frq,second_frq]}
        common_freq = {term:
                [a_terms.count(term),b_terms.count(term)]
                for term in common_words}
        # 获取两句话中仅仅出现一次的共同词
        onews_unsort = [term for term in common_words
                if max(common_freq[term]) is 1]
        # 获取单频词在第一句话中的排好序的单词数组
        onews_sorted = [a_terms[i] for i in
                sorted([a_terms.index(w) for w in onews_unsort])]
        # 获取于语句中单频词下表数组以及字典
        first_order = {so:a_terms.index(so) for so in onews_sorted}
        second_order = [first_order[term] for term in b_terms if term in onews_sorted]
        onews_len = len(onews_sorted)
        # 根据第二句话的逆序数,计算词序相似度
        if onews_len > 1:
            order_sim = 1-self.revOrder(second_order)/float(onews_len-1)
        elif onews_len == 1:
            order_sim = 1
        else:
            order_sim = 0
        return order_sim

    def singleWordSim(self,a,b):
        '''
        功能:单字词形相似度
        '''
        # 转换语句格式成unicode
        if type(a) is str: a = a.decode('utf8')
        if type(b) is str: b = b.decode('utf8')
        # 计算每句话单字的个数
        len_fun = lambda x: float(len(x))
        a_len = len_fun(a)
        b_len = len_fun(b)
        # 获取单字在第一二句话中的频率
        # 格式:{char:[first_frq,second_frq]}
        common_char_freq = {singChar:
                [a.count(singChar),b.count(singChar)]
                for singChar in a}
        # 得到两句话共有单字的个数, 如果出现单字出现次数不同
        # 则取最小出现次数
        samews_char = float(sum(map(min,common_char_freq.values())))
        # 计算单字词形相似度
        single_word_sim = samews_char/max(a_len,b_len)
        return single_word_sim

    def calOrderSim(self,a,b,a_terms,b_terms):
        '''
        功能:结合词型,词序,单子相似度,计算两句话语句相似度
        '''
        total_sim = self.W1*self.wordSim(a_terms,b_terms)+self.W2*self.lenSim(a,b)\
            +self.W3*self.orderSim(a_terms,b_terms)+self.W4*self.singleWordSim(a, b)
        return total_sim

class WordSim(object):
    """
    功能: 单词同义词系统
    """

    def __init__(self, ids,word_ids,id_words):
        '''
        功能：初始化同义词编号数组以及相似度系数
        参数：
            ids: 同义词编号数组
            f: 第一层分支相似度系数
            a: 第二层分支相似度系数
            b: 第三层分支相似度系数
            c: 第四层分支相似度系数
            d: 第五层分支相似度系数
            e: 相关词分支相似度系数
        '''
        self.ids = ids
        self.word_ids = word_ids
        # 获取同义词词库中全部单词
        self.terms = word_ids.keys()
        self.id_words = id_words
        self.f = 0.1
        self.a = 0.65
        self.b = 0.8
        self.c = 0.9
        self.d = 0.96
        self.e = 0.5

    def loadIDWord(self):
        '''
        功能: 获取同义词编号词典
        数据的格式是{id:(word1,word2...)...}
        '''
        pkl_path = '%s/data/id_words.pkl'%self.ROOTDIR
        with open(pkl_path,'rb') as fr:
            id_words = pickle.load(fr)
        return id_words

    def loadWordDict(self):
        '''
        功能: 获取同义词字典
        数据的格式是{word:(id1,id2...)...}
        '''
        pkl_path = '%s/data/word_ids.pkl'%self.ROOTDIR
        with open(pkl_path,'rb') as fr:
            word_dict = pickle.load(fr)
        return word_dict

    def loadIDS(self):
        '''
        功能: 获取同义词编号多维数组
        每一个数组的首字母data都是统一的,分别从A到L
        '''
        ids_path = '%s/data/ids.npy'%self.ROOTDIR
        ids = numpy.load(ids_path)
        return ids

    def countChar(self,fw,sw):
        '''
        功能: 计算两个编号在第一个不同的字符前相同字符的个数
        参数:
            fw: first_word的缩写,第一个单词的同义词词林编号
            sw: second_word的缩写,第二个单词的同义词词林编号
        '''
        same_char_num= 0
        for i in range(8):
            if fw[i] == sw[i]:
                same_char_num += 1
            else:
                break
        return same_char_num

    def getN(self,count,fw):
        '''
        功能: 获取分支层的节点数，既是分支级别上的编号总数
        参数:
            count: 函数countChar得出的相同字符个数
            fw: first_word的缩写,第一个单词的同义词词林编号
        '''
        # 从编号的第一个字符提取编号列表的子数组
        sub_ids = self.ids[ord(fw[0])-ord('A')]
        n = 0
        # 遍历子数组中的编号
        for sub_id in sub_ids:
            # 根据不同的count进行节点数计算
            if count in [1,2,5,8,4,7]:
                if sub_id[:count] == fw[:count]:
                    n += 1
            elif count in [3,6]:
                if sub_id[:count-1] == fw[:count-1]:
                    n += 1
        return n

    def childDiff(self,fw,sw,start,end,now):
        '''
        功能: 服务于getK函数的，用于计算不同级别分支上的ascii差值
        参数:
            fw: first_word的缩写,第一个单词的同义词词林编号
            sw: second_word的缩写,第二个单词的同义词词林编号
            start: 分支在编号中开始的位置
            end: 分支在编号中开始的位置
            now: 判断字符是否为英文的下标,根据count不同而不同
        '''
        # 判断不同级别分支上,首个字符是否为英文字母
        if fw[now].isalpha():
            # 计算分支级别上的字符差值
            return abs(ord(fw[start:end]) - ord(sw[start:end]))
        # 若为数字，则差值计算方法不同
        else:
            return abs(int(fw[start:end]) - int(sw[start:end]))

    def getK(self,count,fw,sw):
        '''
        功能: 根据count的不同,计算不同级别分支上的ascii差值
        参数:
            count: 函数countChar得出的相同字符个数
            fw: first_word的缩写,第一个单词的同义词词林编号
            sw: second_word的缩写,第二个单词的同义词词林编号
        '''
        k = 0
        if count in [1,4]:
            k = self.childDiff(fw,sw,count,count+1,count)
        elif count in [2,5]:
            k = self.childDiff(fw,sw,count,count+2,count)
        elif count in [3,6]:
            k = self.childDiff(fw,sw,count-1,count+1,count)
        else:
            k = 0
        return k

    def getCos(self,n):
        '''
        功能: 根据算出的分支数个数,计算cos值
        '''
        return math.cos(n*(math.pi/180))

    def getM(self,n,k):
        '''
        功能: 根据计算出来的分支层的节点数以及ascii差值,
        计算相似度其中一个系数
        参数:
            n: countChar计算出来的分支层节点数
            k: 不同级别分支上的ascii差值
        '''
        return (float(n)-float(k)+1)/float(n)

    def getSim(self,sim_cos,m,count,fw,sw):
        '''
        功能: 根据不同的分支层节点数进行单词相似度计算
        参数:
            f: 第一层分支相似度系数
            a: 第二层分支相似度系数
            b: 第三层分支相似度系数
            c: 第四层分支相似度系数
            d: 第五层分支相似度系数
            e: 相关词分支相似度系数
        '''
        # 第一层,两个词语的编号(义项)不在同一棵树上
        if count in [0]:
            sim = self.f
        # 第二层分支
        elif count in [1]:
            sim = self.a*sim_cos*m
        # 第三层分支
        elif count in [2,3]:
            sim = self.b*sim_cos*m
        # 第四层分支
        elif count in [4]:
            sim = self.c*sim_cos*m
        # 第五层分支
        elif count in [5,6]:
            sim = self.d*sim_cos*m
        # 两个词语完全一样的情况
        elif count in [7]:
            sim = 1
        # 两个词语语义上不同的情况,对应不同的同义词权重
        # 符号“=”代表同义
        # 符号“#”代表同类,相关
        # 符号“@”代表独立,既没有相关词与同义词
        elif count in [8]:
            if (fw[-1] == sw[-1]) and (fw[-1] == '='):
                sim = 1
            elif (fw[-1] == sw[-1]) and (fw[-1] == '#'):
                sim = self.e
            else:
                sim = 0
        return sim

    def get_word_sim(self,fw,sw):
        '''
        功能: 根据两个词汇的同义词编号计算相似度
        系数:
            n: countChar计算出来的分支层节点数
            k: 不同级别分支上的ascii差值
            fw: first_word的缩写,第一个单词的同义词词林编号
            sw: second_word的缩写,第二个单词的同义词词林编号
            m: 根据n与k计算的相似度其中一个系数
            sim_cos: 根据n计算的相似度的另外一个系数
        '''
        if fw == sw: return 1
        count = self.countChar(fw,sw)
        if count > 0:
            n = self.getN(count,fw)
            k = self.getK(count,fw,sw)
            sim_cos = self.getCos(n)
            m = self.getM(n,k)
            sim = self.getSim(sim_cos,m,count,fw,sw)
        # 如果没有任何一个相似字符,相似度默认为f
        else:
            sim = self.f
        return abs(sim)


    def calWordSim(self,f_word,s_word):
        '''
        功能: 根据单词获得编号列表,并计算两个单词相似度
        参数:
            word_ids: 同义词字典,数据的格式是{word:(id1,id2...)...}
            term: 同义词词库全部单词数组
            word_sims: 单词同义词编号列表
        '''
        if f_word == s_word: return 1
        word_sims = []
        # 判断单词是否在同义词库中
        if f_word in self.terms and s_word in self.terms:
            # 分别获取单词所代表的编号列表
            f_list = self.word_ids[f_word]
            s_list = self.word_ids[s_word]
            # 遍历两个列表并计算相似度
            for first in f_list:
                for second in s_list:
                    word_sims.append(self.get_word_sim(first,second))
            # 返回最大的相似度值
            return max(word_sims)
        # 如果单词不在词库中,返回0.1
        else:
            return self.f


    def get_sim_words(self,word):
        '''
        功能: 从一个单词中衍生出多个同义词
        参数:
            sub_word_ids: 根据单词获得以=结尾的同义词编号
            sim_words: 根据单词得出的同义词列表
        '''
        # 判断该词是否在同义词词库中
        if word in self.word_ids:
            # 根据单词得出同义词的编号
            sub_word_ids = [i for i in self.word_ids[word] if i.endswith('=')]
            if len(sub_word_ids) > 0:
                # 将得到的同义词数组合并
                add_fun = lambda x,y: x+y
                # 同一个编号下,获取同义词,形成数组
                get_words = lambda x: self.id_words[x].strip().split(' ')
                # 根据所给单词得出同义词数组总和
                sim_words = reduce(add_fun,map(get_words,sub_word_ids))
                return list(set(sim_words))
            else:
                return [word]
        else:
            return [word]


    def calListSim(self,fir_terms,sed_terms):
        '''
        功能: 两句话的分词列表,计算不相同词的相似度
        参数:
            same_words: 两句话的相同词
            diff_words: 两句话的不同词
        '''
        word_sims = []
        # 相同词
        same_words = set(fir_terms) & set(sed_terms)
        # 不同词
        fir_diff_words = set(fir_terms) - same_words
        sed_diff_words = set(sed_terms) - same_words
        # 计算不同词之间的相似度
        for fir_word in fir_diff_words:
            for sed_word in sed_diff_words:
                word_sims.append(self.calWordSim(fir_word,sed_word))
        if len(fir_terms) == 0 or len(sed_terms) == 0:
            return self.f
        # 判断是否属于完全同义词
        if len(fir_diff_words) == 0 or len(sed_diff_words) == 0:
            return 1
        elif max(word_sims) == 1:
            return 1
        # 不是完全在一个分支上的情况
        else:
            return max(word_sims)


def reverse(fir_split, fir_pos, fir_gra):
    '''
    功能: 判断语句是否为主谓语倒置
    若主谓语的词性一样,则认为倒置不改变其主要意思,反之
    参数:
        split: 带有split的参数代表了语句分词后的结果
        pos:   带有pos的参数代表了对分词进行词性处理
        sbv:   带有sbv的参数代表了主语
        vob:   带有vob的参数代表了宾语
    '''
    # 判断是否有主谓语
    if 'SBV' in fir_gra and 'VOB' in fir_gra:
        # 主谓语词性判断
        sbv_pos = fir_pos[fir_gra.index('SBV')]
        vob_pos = fir_pos[fir_gra.index('VOB')]
        judge_same_pos = not(sbv_pos == vob_pos)
    # 主谓语不全的情况下,视为非主谓倒置
    else:
        judge_same_pos = True
    return judge_same_pos


def sentsim(fir_split, sed_split, fir_pos, sed_pos, wordsim):
    '''
    功能: 在两个语句结构相似的情况下,结合同义词系统,
    计算语句中疑问代词,名词以及动词的相似度
    参数:
        mark: 带有mark的参数代表疑问代词
        verb: 带有verb的参数代表动词
        noun: 带有noun的参数代表名词
    '''
    # 获取人称代词的相关同义词
    person_list = set(reduce(lambda x,y:x+y,[wordsim.get_sim_words(i) for i in ['我','你','他','它']]))
    # 疑问代词,名词,动词的筛选
    mark_filter = lambda split,pos: [split[i] for i,p in enumerate(pos) if p.startswith('r') and split[i] not in person_list]
    noun_filter = lambda split,pos: [split[i] for i,p in enumerate(pos) if p.startswith('n')]
    verb_filter = lambda split,pos: [split[i] for i,p in enumerate(pos) if p.startswith('v')]
    # 获取筛选后的疑问代词,名词,动词
    fir_mark, sed_mark = mark_filter(fir_split, fir_pos), mark_filter(sed_split, sed_pos)
    fir_nouns, sed_nouns = noun_filter(fir_split, fir_pos), noun_filter(sed_split, sed_pos)
    fir_verb, sed_verb = verb_filter(fir_split, fir_pos), verb_filter(sed_split, sed_pos)
    # 计算名词,疑问代词,动词的相似度
    noun_sim = wordsim.calListSim(fir_nouns,sed_nouns)
    mark_sim = wordsim.calListSim(fir_mark,sed_mark)
    verb_sim = wordsim.calListSim(fir_verb,sed_verb)
    # 汇总名词,疑问代词,动词的相似度
    total_sim = noun_sim * mark_sim * verb_sim * 100
    return total_sim


def text_process(ltps, text):
    ltp_result = ltps.parser(text)
    segment, pos, parser = [], [], []
    for lr in ltp_result:
        segment.append(lr['cont'].encode('utf-8'))
        pos.append(lr['pos'].encode('utf-8'))
        parser.append(lr['relate'].encode('utf-8'))
    return segment, pos, parser


def calc_score(fir_sent, sed_sent, ids, word_ids,ids_words, ltpserver):
    # 编译距离
    simple_sim = fuzz.ratio(fir_sent,sed_sent)
    # 中等编译距离处理
    if simple_sim > 30 and simple_sim < 80:
        fir_seg, fir_pos, fir_gra = text_process(ltpserver, fir_sent)
        sed_seg, sed_pos, sed_gra = text_process(ltpserver, sed_sent)
        # 初始化语句相似度系统
        ordersim = ImprovedOrderSim()
        # 计算语句相似度
        sent_score = ordersim.calOrderSim(fir_sent,sed_sent,fir_seg,sed_seg) * 100
        # 低等匹配词序相似度处理
        if sent_score <= 50:
            #print 'sent_score less than 50'
            return sent_score
        # 中等匹配词序相似度处理
        elif sent_score < 90 and sent_score > 50:
            #print 'sent_score [50,70]'
            wordsim = WordSim(ids, word_ids,ids_words)
            return sentsim(fir_seg, sed_seg, fir_pos, sed_pos, wordsim)
        # 高等匹配词序相似度处理
        # 排除语句倒置情况
        elif sent_score >= 90:
            #print 'sent_score more than 90'
            if reverse(fir_seg, fir_pos, fir_gra):
                return sent_score
            else:
                return 50
    # 低等以及高等编译距离处理
    else:
        #print 'enter simple_sim'
        return simple_sim
