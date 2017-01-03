# -*-coding: utf-8 -*-

class LocPattern(object):
    '''处理地点模块'''

    def __init__(self):
        pass

    @staticmethod
    def deal_locations(loc_dict):
        loc_result = {}
        # 无地点代词情况,则跳出
        if len(loc_dict) is 0:
            pass
        else:
            # 对词位置下标进行排序
            loc_index = sorted(loc_dict.keys())
            match_index, time_slot = None, None
            for index in xrange(len(loc_index)):
                try:
                    # 处理两地点代词相邻且间隔为1的情况
                    if 0 < loc_index[index+1] - loc_index[index] < 5:
                        time_slot = loc_index[index+1] - loc_index[index]
                        match_index = loc_index[index]
                        break
                except IndexError:
                    continue
            # 两地点相邻情况
            if match_index is not None:
                loc_result['start'] = loc_dict[match_index]
                loc_result['end'] = loc_dict[match_index+time_slot]
                # print '出发地点:%s\t目的地点:%s'%(loc_dict[match_index],loc_dict[match_index+time_slot])
            # 单地点情况
            else:
                loc_result['start'] = loc_dict[loc_index[0]]
        return loc_result
