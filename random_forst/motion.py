# -*- coding: utf-8 -*-

import re
from word_annotation import A, B
# from flask import current_app as app
from ltpwebservice import LtpWebService

class Motion(object):
    def __init__(self):
        # self.ltpserver = LtpWebService(app.host,app.port)
        self.ltpserver = LtpWebService("http://192.168.50.46",9527)
        self.pattern = re.compile("(\[1f[0-2]\d\]|\[1f3[0-6]\])")
        self.splitchar = ";"


    def textProcess(self,text):
        '''text processing'''
        # split words
        # words = list(self.segmentor.segment(text))  # 分词
        # # give pos taggers
        # postags = self.postagger.postag(words)  # 词性标注
        # # parser analysis
        # arcs = self.parser.parse(words, postags)  # 句法分析
        # # extract relatioh lable from parsers
        # grammer = [arcs[index].relation for index in range(len(words))]
        # return words, postags, grammer
        raw = self.ltpserver.parser(text)
        words = []
        postags = []
        grammer = []
        for meat in raw:
            words.append(meat['cont'])
            postags.append(meat['pos'])
            grammer.append(meat['relate'])
        return words,postags,grammer

# need 
    def fill(self, pre, current):
        """
            根据上一句补全当前句
        """
        qa = Fill(self, pre, current)
        return qa.fillSentence()


# need 
    def single_word(self, sen, ptg):

        dic_for_pre={
            A.a: '什么',
            A.b: '什么',
            A.g: '什么',
            A.h: '什么',
            A.i: '什么',
            A.k: '什么',
            A.nd: '什么的',
            A.nl: '哪里的',
            A.nt: '嗯,',
            A.o: '',
            A.p: '',
            A.u: '',
            A.x: '什么'
        }
        dic_for_sufx={
            A.q: '什么',
            A.c: '什么',
            A.d: '什么',
            A.e: '什么',
            A.r: '怎么了',
            A.wp: '',
            A.x: '什么',
            A.ns: '哪里'
        }
        res = None
        if ptg in dic_for_pre.keys():
            res = "%s%s?" % (dic_for_pre.get(ptg), sen)
        elif ptg in dic_for_sufx.keys():
            res = "%s%s?" % (sen, dic_for_sufx.get(ptg))
        return res

# need 
    def single_word_query(self, sen, ptg):
        list_for_query=[A.j,A.m,A.n,A.ni,A.nh,A.nz,A.ws]
        list_to_fillin=['是什么','是多少','怎么买','']
        q = []
        if ptg in list_for_query:
            if ptg == A.nh:
                q.append("%s是谁?" % (sen))
            else:
                for s in list_to_fillin:
                    q.append(sen + s)
        return q

class Fill(object):
    """docstring for Fill
    Used for complete the unfinished sentence
    including
    1) extract the essential terms from previous sentence based on rules
    2) judge position of current sentence whether to insert the terms"""

    def __init__(self, Process, previous_sentence, current_sentence):
        '''initialization'''
        self.Process = Process
        self.previous_sentence = previous_sentence
        self.current_sentence = current_sentence
        # different matched patterns for previous sentence
        self.matchList = [
            [B.SBV],
            [B.VOB],
            [B.POB],
            [B.RAD,B.ATT,B.SBV],
            [B.ATT,B.SBV],
            [B.ATT,B.RAD,B.ATT,B.ATT,B.SBV],
            [B.SBV,B.SBV],
            [B.ATT,B.VOB],
            [B.ATT,B.RAD,B.ATT,B.VOB],
            [B.ATT,B.ATT,B.RAD,B.SBV],
            [B.ATT,B.RAD,B.SBV],
            [B.ATT,B.ATT,B.SBV]
        ]
        self.splitchar = ';'

    def findMatchPatter(self):
        '''Used for extract essential terms from previous sentence based on patterns'''
        fill_words = None
        # textProcess for previous sentence
        # words_pre: 为分词数组
        # postags_pre: 为词性数组(动词,名词等)
        # grammer_pre: 主谓宾的数组
        words_pre, postags_pre, grammer_pre = self.Process.textProcess(self.previous_sentence)
        #grammer_pre = 是一个数组[SBV,VOB,RAD]类似
        # get matched pattern based on rules
        gp = self.splitchar.join(grammer_pre)
        matched_pre = sorted([match for match in self.matchList
            if self.splitchar.join(match) in gp], cmp = lambda x,y: len(y) - len(x))
        # dealing with sentence that no need to process
        if ((len(grammer_pre) == 1) or (len(matched_pre) == 0)):
            pass
        else:
            for match in matched_pre:
                # get the index of match in matchList
                pattern_index = gp.index(self.splitchar.join(match))
                # get the index of match in the stru_tag
                matched_index = len(gp[:pattern_index].split(self.splitchar)) - 1
                start_index = matched_index
                end_index = matched_index + len(match)
                # get the corresponding pos substring
                pos_sub = list(postags_pre[start_index:end_index])
                # make sure no human, direction and time words in matched sub sentence
                mask = set([A.r, A.nt, A.nd]) # 屏蔽字,这其任何一个存在直接continue
                if mask & set(pos_sub): # mask和pos_sub的交集
                    continue
                else:
                    fill_words = ''.join(words_pre[start_index:end_index])
                    break
        return fill_words

    def judgeComplete(self,postags,grammer):
        '''judge whether sentence is completed'''
        judge = True
        if len(grammer) == 1:
            judge = False
        else:
            if (B.SBV in grammer) and (B.VOB in grammer):
                SBV_index = grammer.index(B.SBV)
                VOB_index = grammer.index(B.VOB)
                mask = set([A.r, A.v])
                if set([postags[SBV_index], postags[VOB_index]]) & mask:
                    judge = False
        return judge


    def fillSentence(self):
        fill_words = self.findMatchPatter()
        if not fill_words:
            return None
        # textProcess for current sentence
        words_cur, postags_cur, grammer_cur = self.Process.textProcess(self.current_sentence)
        # choose complete sentence
        judge = self.judgeComplete(postags_cur,grammer_cur)

        hasWP = False
        WP_value = None
        if A.wp == postags_cur[-1]:
            hasWP = True
            WP_value = words_cur[-1]
            del words_cur[-1]

        if judge:
            if (B.SBV in grammer_cur) and (B.VOB in grammer_cur):
                # 有主语有宾语,且主语是人称代词,把人称代词替换成上一句的关键词
                SBV_index = grammer_cur.index(B.SBV)
                VOB_index = grammer_cur.index(B.VOB)

                if ((postags_cur[SBV_index] == A.r) and (postags_cur[VOB_index] == A.r)):
                    words_cur[VOB_index] = fill_words
                elif ((postags_cur[SBV_index] == A.r) and ((postags_cur[VOB_index] != A.r))):
                    words_cur[SBV_index] = fill_words
                else:
                    # 找到第一个动词,把这个fill_words放到这个动词前面
                    try:
                        v_index = postags_cur.index(A.v)
                        words_cur.insert(v_index - 1,fill_words)
                    except:
                        words_cur.insert(0,fill_words)
            elif (B.SBV in grammer_cur) and (B.VOB not in grammer_cur):
                # 有主语,没有宾语
                SBV_index = grammer_cur.index(B.SBV)
                if postags_cur[SBV_index] == A.r:
                    try:
                        v_index = postags_cur.index(A.v)
                        words_cur.insert(v_index + 1,fill_words)
                    except:
                        words_cur.append(fill_words)
            elif B.VOB in grammer_cur:
                VOB_index = grammer_cur.index(B.VOB)
                if postags_cur[VOB_index] == A.r:
                    words_cur[VOB_index]= fill_words
                elif postags_cur[VOB_index] == A.v:
                    try:
                        v_index = postags_cur.index(A.v)
                        words_cur.insert(v_index + 1,fill_words)
                    except:
                        words_cur.insert(0, fill_words)
                else:
                    words_cur.insert(0, '关于' + fill_words)
            else:
                words_cur.insert(0, fill_words)

        if hasWP:
            words_cur.append(WP_value)
        return ' '.join(words_cur)

if __name__ == "__main__":
    a = Motion()
    result = a.textProcess('你好我是好孩子')
    for i in result[0]:
        print i
    print result
