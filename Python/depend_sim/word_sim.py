# -*- coding: utf-8 -*-
import pickle
import numpy
import math

class WordSim(object):
    """
    功能: 单词同义词系统
    """


    def __init__(self,ids,word_ids,id_words):
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
        self.terms = self.word_ids.keys()
        self.id_words = id_words
        self.f = 0.1
        self.a = 0.65
        self.b = 0.8
        self.c = 0.9
        self.d = 0.96
        self.e = 0.5


#     def loadIDWord(self):
#         '''
#         功能: 获取同义词编号词典
#         数据的格式是{id:(word1,word2...)...}
#         '''
#         pkl_path = '%s/data/id_words.pkl'%self.ROOTDIR
#         with open(pkl_path,'rb') as fr:
#             id_words = pickle.load(fr)
#         return id_words
# 
# 
#     def loadWordDict(self):
#         '''
#         功能: 获取同义词字典
#         数据的格式是{word:(id1,id2...)...}
#         '''
#         pkl_path = '%s/data/word_ids.pkl'%self.ROOTDIR
#         with open(pkl_path,'rb') as fr:
#             word_dict = pickle.load(fr)
#         return word_dict
# 
# 
#     def loadIDS(self):
#         '''
#         功能: 获取同义词编号多维数组
#         每一个数组的首字母data都是统一的,分别从A到L
#         '''
#         ids_path = '%s/data/ids.npy'%self.ROOTDIR
#         ids = numpy.load(ids_path)
#         return ids


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
        if type(f_word) is unicode: f_word = f_word.encode('utf8')
        if type(s_word) is unicode: s_word = s_word.encode('utf8')
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
                print fir_word, sed_word, self.calWordSim(fir_word,sed_word)
        # 处理两数组任何一个为空的情况
        if (len(fir_terms) == 0) ^ (len(sed_terms) == 0):
            return self.f
        # 处理两数组都不为空的情况
        elif len(fir_terms) != 0:
            pass
        # 处理两数组都为空的情况
        else:
            return 1
        # 判断是否属于完全同义词
        if len(fir_diff_words) == 0 or len(sed_diff_words) == 0:
            return 1
        elif max(word_sims) == 1:
            return 1
        # 不是完全在一个分支上的情况
        else:
            return max(word_sims)


