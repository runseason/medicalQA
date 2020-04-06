#!/usr/bin/env python3
# coding: utf-8
# File: answer_search.py
# Author: lhy<lhy_in_blcu@126.com,https://huangyong.github.io>
# Date: 18-10-5

from py2neo import Graph


class AnswerSearcher:
    def __init__(self):
        self.g = Graph(
            # "http://localhost:7474/db/data"  # py2neo 2.0.8写法
            host="127.0.0.1",  # py2neo 3写法
            user="neo4j",
            password="leilu"
        )
        self.num_limit = 30

    '''执行cypher查询，并返回相应结果'''

    def search_main(self, sqls):
        final_answers = []
        for sql_ in sqls:
            question_type = sql_['question_type']
            queries = sql_['sql']
            answers = []
            for query in queries:
                ress = self.g.run(query).data()
                answers += ress
            final_answer = self.answer_prettify(question_type, answers)
            if final_answer:
                final_answers.append(final_answer)
        return final_answers

    '''根据对应的qustion_type，调用相应的回复模板'''

    def answer_prettify(self, question_type, answers):
        final_answer = []
        if not answers:
            return ''
        if question_type == 'disease_symptom':
            desc = [i['n.name'] for i in answers]
            subject = answers[0]['m.name']
            if desc[0]:
                final_answer = '{0}的症状包括：{1}'.format(subject, '；'.join(list(set(desc))[:self.num_limit]))
            else:
                final_answer = '{0}的症状包括：未检索到结果'.format(subject)

        elif question_type == 'symptom_disease':
            desc = [i['m.name'] for i in answers]
            subject = answers[0]['n.name']
            if desc[0]:
                final_answer = '症状{0}可能染上的疾病有：{1}'.format(subject, '；'.join(list(set(desc))[:self.num_limit]))
            else:
                final_answer = '症状{0}可能染上的疾病有：未检索到结果'.format(subject)


        elif question_type == 'disease_cause':
            desc = [i['m.cause'] for i in answers]
            print(answers)
            print(desc)
            subject = answers[0]['m.name']
            if desc[0]:
                final_answer = '{0}可能的成因有：{1}'.format(subject, '；'.join(list(set(desc))[:self.num_limit]))
            else:
                final_answer = '{0}可能的成因有：未检索到结果'.format(subject)

        elif question_type == 'disease_prevent':
            desc = [i['m.prevent'] for i in answers]
            subject = answers[0]['m.name']
            if desc[0]:
                final_answer = '{0}的预防措施包括：{1}'.format(subject, '；'.join(list(set(desc))[:self.num_limit]))
            else:
                final_answer = '{0}的预防措施包括：未检索到结果'.format(subject)

        elif question_type == 'disease_lasttime':
            desc = [i['m.cure_lasttime'] for i in answers]
            subject = answers[0]['m.name']
            if desc[0]:
                final_answer = '{0}治疗可能持续的周期为：{1}'.format(subject, '；'.join(list(set(desc))[:self.num_limit]))
            else:
                final_answer = '{0}治疗可能持续的周期为：未检索到结果'.format(subject)

        elif question_type == 'disease_cureway':
            desc = [';'.join(i['m.cure_way']) for i in answers]
            subject = answers[0]['m.name']
            if desc[0]:
                final_answer = '{0}可以尝试如下治疗：{1}'.format(subject, '；'.join(list(set(desc))[:self.num_limit]))
            else:
                final_answer = '{0}可以尝试如下治疗：未检索到结果'.format(subject)

        elif question_type == 'disease_cureprob':
            desc = [i['m.cured_prob'] for i in answers]
            subject = answers[0]['m.name']
            if desc[0]:
                final_answer = '{0}治愈的概率为（仅供参考）：{1}'.format(subject, '；'.join(list(set(desc))[:self.num_limit]))
            else:
                final_answer = '{0}治愈的概率为（仅供参考）：未检索到结果'.format(subject)

        elif question_type == 'disease_getway':
            desc = [i['m.get_way'] for i in answers]
            subject = answers[0]['m.name']
            if desc[0]:
                final_answer = '{0}的传播方式为：{1}'.format(subject, '；'.join(list(set(desc))[:self.num_limit]))
            else:
                final_answer = '{0}的传播方式为：未检索到结果'.format(subject)

        elif question_type == 'disease_easyget':
            desc = [i['m.easy_get'] for i in answers]
            subject = answers[0]['m.name']
            if desc[0]:
                final_answer = '{0}的易感人群包括：{1}'.format(subject, '；'.join(list(set(desc))[:self.num_limit]))
            else:
                final_answer = '{0}的易感人群包括：未检索到结果'.format(subject)

        elif question_type == 'disease_desc':
            desc = [i['m.desc'] for i in answers]
            subject = answers[0]['m.name']
            if desc[0]:
                final_answer = '{0},熟悉一下：{1}'.format(subject, '；'.join(list(set(desc))[:self.num_limit]))
            else:
                final_answer = '{0},熟悉一下：未检索到结果'.format(subject)

        elif question_type == 'disease_acompany':
            desc1 = [i['n.name'] for i in answers]
            desc2 = [i['m.name'] for i in answers]
            subject = answers[0]['m.name']
            desc = [i for i in desc1 + desc2 if i != subject]
            if desc[0]:
                final_answer = '{0}的并发症包括：{1}'.format(subject, '；'.join(list(set(desc))[:self.num_limit]))
            else:
                final_answer = '{0}的并发症包括：未检索到结果'.format(subject)

        elif question_type == 'disease_can_eat':
            print([answers[0]['m.can_eat']][0])
            desc = [answers[0]['m.can_eat']]
            #desc = [answers[0]['m.can_eat']] if [answers[0]['m.can_eat']][0] is 'None' else '无'

            print(answers)
            print(desc)
            subject = answers[0]['m.name']
            print(subject)
            # 当desc为空时会报错
            if desc[0]:
                final_answer = '{0}可以吃/喝：{1}'.format(subject, '；'.join(list(set(desc))[:self.num_limit]))
            else:
                final_answer = '{0}可以吃/喝：未检索到结果'.format(subject)

        elif question_type == 'disease_not_food':
            desc = [i['n.name'] for i in answers]
            subject = answers[0]['m.name']
            if desc[0]:
                final_answer = '{0}忌食的食物包括有：{1}'.format(subject, '；'.join(list(set(desc))[:self.num_limit]))
            else:
                final_answer = '{0}忌食的食物包括有：未检索到结果'.format(subject)

        elif question_type == 'disease_do_food':
            do_desc = [i['n.name'] for i in answers if i['r.name'] == '宜吃']
            recommand_desc = [i['n.name'] for i in answers if i['r.name'] == '推荐食谱']
            subject = answers[0]['m.name']
            if do_desc[0] and recommand_desc[0]:
                final_answer = '{0}推荐{1}\n推荐食谱包括有：{2}'.format(subject, ';'.join(list(set(do_desc))[:self.num_limit]),
                                                          ';'.join(list(set(recommand_desc))[:self.num_limit]))
            elif do_desc[0]:
                final_answer = '{0}推荐的食谱有：{1}'.format(subject, ';'.join(list(set(do_desc))[:self.num_limit]))
            elif recommand_desc[0]:
                final_answer = '{0}推荐的食谱有：{1}'.format(subject, ';'.join(list(set(recommand_desc))[:self.num_limit]))
            else:
                final_answer = '{0}推荐的食谱有：{1}'.format(subject)


        elif question_type == 'food_not_disease':
            desc = [i['m.name'] for i in answers]
            subject = answers[0]['n.name']
            if desc[0]:
                final_answer = '患有{0}的人最好不要吃{1}'.format('；'.join(list(set(desc))[:self.num_limit]), subject)
            else:
                final_answer = '患有{0}的人最好不要吃 : 未检索到结果'.format(subject)

        elif question_type == 'food_do_disease':
            desc = [i['m.name'] for i in answers]
            subject = answers[0]['n.name']
            if desc[0]:
                final_answer = '患有{0}的人建议多试试{1}'.format('；'.join(list(set(desc))[:self.num_limit]), subject)
            else:
                final_answer = '患有{0}的人建议多试试: 未检索到结果'.format(subject)

        elif question_type == 'disease_drug':
            desc = [i['n.name'] for i in answers]
            subject = answers[0]['m.name']
            if desc[0]:
                final_answer = '{0}通常的使用的药品包括：{1}'.format(subject, '；'.join(list(set(desc))[:self.num_limit]))
            else:
                final_answer = '{0}通常的使用的药品包括：未检索到结果'.format(subject)

        elif question_type == 'drug_disease':
            desc = [i['m.name'] for i in answers]
            subject = answers[0]['n.name']
            if desc[0]:
                final_answer = '{0}主治的疾病有{1},可以试试'.format(subject, '；'.join(list(set(desc))[:self.num_limit]))
            else:
                final_answer = '{0}主治的疾病有: 未检索到结果'.format(subject)

        elif question_type == 'disease_check':
            desc = [i['n.name'] for i in answers]
            subject = answers[0]['m.name']
            if desc[0]:
                final_answer = '{0}通常可以通过以下方式检查出来：{1}'.format(subject, '；'.join(list(set(desc))[:self.num_limit]))
            else:
                final_answer = '{0}通常可以通过以下方式检查出来：未检索到结果'.format(subject)

        elif question_type == 'check_disease':
            desc = [i['m.name'] for i in answers]
            subject = answers[0]['n.name']
            if desc[0]:
                final_answer = '通常可以通过{0}检查出来的疾病有{1}'.format(subject, '；'.join(list(set(desc))[:self.num_limit]))
            else:
                final_answer = '通常可以通过{0}检查出来的疾病有 : 未检索到结果'.format(subject)

        print("final_answer: ", final_answer)
        return final_answer


if __name__ == '__main__':
    searcher = AnswerSearcher()
