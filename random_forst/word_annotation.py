# -*- coding: utf-8 -*-

# plty使用到的词性标注集

# 参考: http://ltp.readthedocs.io/zh_CN/latest/appendix.html#id3

class Participle:
    B = 'B' # 词首
    I = 'I' # 词中
    E = 'E' # 词尾
    S = 'S' # 单字成词

class A:
    a = 'a'
    b = 'b'
    c = 'c'
    d = 'd'
    e = 'e'
    g = 'g'
    h = 'h'
    i = 'i'
    j = 'j'
    k = 'k'
    m = 'm'
    n = 'n'
    nd = 'nd'
    nh = 'nh'
    ni = 'ni'
    nl = 'nl'
    ns = 'ns'
    nt = 'nt'
    nz = 'nz'
    o = 'o'
    p = 'p'
    q = 'q'
    r = 'r'
    u = 'u'
    v = 'v'
    wp = 'wp'
    ws = 'ws'
    x = 'x'


class B:
    SBV = "SBV" # 主谓
    VOB = "VOB" # 动宾
    IOB = "IOB" # 间宾
    FOB = "FOB" # 前置
    DBL = "DBL" # 兼语
    ATT = "ATT" # 定中
    ADV = "ADV" # 状中
    CMP = "CMP" # 动补
    COO = "COO" # 并列
    POB = "POB" # 介宾
    LAD = "LAD" # 左附加
    RAD = "RAD" # 右附加
    IS = "IS" # 独立
    HED = "HED" # 核心
