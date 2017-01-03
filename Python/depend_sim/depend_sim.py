# -*- coding: utf-8 -*-
import math
import numpy
from word_annotation import A as pos
from word_annotation import B as par

class DependSim(object):

    def __init__(self, word_sim):
        self.init_parameters()
        self.word_sim = word_sim

    def init_parameters(self):
        self.o = 0.05
        self.e = 0.05
        self.pos_rules = [pos.r, pos.a, pos.v, pos.n, pos.d]

    def get_words(self, ltp_result):
        major_words, minor_words, other_words = [], [], []
        key_index, index = 0, 0
        while index < len(ltp_result):
            sub_result = ltp_result[index]
            par_role = sub_result['relate']
            word = sub_result['cont']
            if not key_index:
                if par_role == 'HED':
                    key_index = str(index)
                    major_words.append((par_role, word))
                    index = 0
                    continue
            else:
                parent_index = sub_result['parent']
                pos_role = sub_result['pos']
                if parent_index == key_index:
                    if pos_role in self.pos_rules:
                        major_words.append((par_role, word))
                elif index != int(key_index):
                    if pos_role in self.pos_rules:
                        minor_words.append(word)
                    else:
                        other_words.append(word)
            index += 1
        return set(major_words), minor_words, set(other_words)

    def get_all_pars(self, f_major, s_major):
        all_pars = {}
        diff_pars = (f_major | s_major) - (f_major & s_major)
        for sub_par in diff_pars:
            par_role, word = sub_par
            try:
                all_pars[par_role].append(word)
            except KeyError:
                all_pars[par_role] = []
                all_pars[par_role].append(word)
        return all_pars

    def get_major_sim(self, f_major, s_major):
        all_pars = self.get_all_pars(f_major, s_major)
        if all_pars:
            sum_sim = 0
            for sub_par in all_pars:
                words = all_pars[sub_par]
                if len(words) == 2:
                    f_word, s_word = words
                    sum_sim += self.word_sim.calWordSim(f_word, s_word)
                else:
                    sum_sim += self.e
            sim_major = 1 / float(len(all_pars)) * sum_sim
            return sim_major
        else:
            return 1

    def make_sim_matrix(self, f_minor, s_minor):
        sim_matrix = []
        for fm in f_minor:
            row = []
            for sm in s_minor:
                row.append(self.word_sim.calWordSim(fm, sm))
            sim_matrix.append(row)
        sim_matrix = numpy.mat(sim_matrix)
        return sim_matrix

    def make_sim_array(self, f_minor, s_minor, sim_matrix):
        max_sim = sim_matrix.max()
        row_index, col_index =  numpy.where(sim_matrix == max_sim)
        max_list, row_value_list, col_value_list = [], [], []
        for row, col in zip(row_index, col_index):
            max_list.append(max_sim)
            sim_matrix[row, col] = 0
            row_value = f_minor[row]
            col_value = s_minor[col]
            if row_value not in row_value_list:
                row_value_list.append(f_minor[row])
            if col_value not in col_value_list:
                col_value_list.append(s_minor[col])
        return max_list, row_value_list, col_value_list

    def get_minor_sim(self, f_minor, s_minor):
        max_length = max(len(f_minor), len(s_minor))
        if len(f_minor) is not 0 and len(s_minor) is not 0:
            sim_matrix = self.make_sim_matrix(f_minor, s_minor)
            while sim_matrix.max() != 0:
                max_list, row_value_list, col_value_list = \
                        self.make_sim_array(f_minor, s_minor, sim_matrix)
            row_judge, col_judge = False, False
            if len(row_value_list) == len(f_minor):
                row_judge = True
            if len(col_value_list) == len(s_minor):
                col_judge = True
            total_judge = row_judge and col_judge
            if total_judge:
                max_list.append(self.o)
            return sum(max_list) / max_length
        elif len(f_minor) is not 0 or len(s_minor) is not 0:
            return self.o
        else:
            return 0

    def get_other_sim(self, f_other, s_other):
        if len(f_other) is not 0 and len(s_other) is not 0:
            all_others = set(f_other | s_other)
            f_vector, s_vector = [], []
            f_vector = map(lambda x: {False:0,True:1}[x in f_other], all_others)
            s_vector = map(lambda x: {False:0,True:1}[x in s_other], all_others)
            doc_product, fir_length, sed_length = 0, 0, 0
            for i in xrange(len(all_others)):
                doc_product += f_vector[i] * s_vector[i]
                fir_length += f_vector[i]**2
                sed_length += s_vector[i]**2
            cos_sim = doc_product / (math.sqrt(fir_length) * math.sqrt(sed_length))
            return cos_sim
        else:
            return 0

    def modify_value(self, f_minor,s_minor,f_other,s_other):
        a1 = 0.7
        a2 = 0.2
        a3 = 0.1
        if not f_minor and not s_minor:
            a2 = 0
            a1 = a1 / (a1 + a3)
            a3 = a3 / (a1 + a3)
        if not f_other and not s_other:
            a3 = 0
            a1 = a1 / (a1 + a2)
            a2 = a2 / (a1 + a2)
        if (not f_minor and not s_minor) and (not f_other and not s_other):
            a1 = 1
            a2 = 0
            a3 = 0
        return a1, a2, a3

    def get_total_sim(self, f_ltp, s_ltp):
        f_major, f_minor, f_other = self.get_words(f_ltp)
        s_major, s_minor, s_other = self.get_words(s_ltp)
        a1, a2, a3 = self.modify_value(f_minor,s_minor,f_other,s_other)
        total_sim = a1 * self.get_major_sim(f_major, s_major) + \
                    a2 * self.get_minor_sim(f_minor, s_minor) + \
                    a3 * self.get_other_sim(f_other, s_other)
        return round(total_sim)*100

