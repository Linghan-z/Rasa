#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File    : question_parser.py
# @Time    : 3/20/23 21:45
# @Author  : zlhhh
# @Description :

class QuestionPaser:

    def build_entity_dict(self, args):
        '''
        构建实体节点
        :param args:
        :return:
        '''
        entity_dict = {}
        for arg, types in args.items():
            for type in types:
                if type not in entity_dict:
                    entity_dict[type] = [arg]
                else:
                    entity_dict[type].append(arg)

        return entity_dict

    def parser_main(self, res_classify):
        args = res_classify['args']
        entity_dict = self.build_entity_dict(args)
        question_type = res_classify['question_type']
        # question_types = res_classify['question_types']
        # sqls = []
        # for question_type in question_types:
        #     sql_ = {}
        #     sql_['question_type'] = question_type
        #     sql = []
        #     if question_type == 'military_detail':
        #         sql = sql_transfer(question_type, entity_dict.get('Military'))

        sql_ = {}

        sql_['question_type'] = question_type
        sql = []
        if question_type == 'military_detail':
            sql = self.sql_transfer(question_type, entity_dict.get('Military'))

        if sql:
            sql_['sql'] = sql
        return sql_

    def sql_transfer(self, question_type, entity):
        if not entity:
            return []

            # 查询语句
        sql = []

        if question_type == 'military_detail':
            sql = ["MATCH (m:Military) where m.name = '{0}' return m".format(entity)]
        return sql


def main():
    handler = QuestionPaser()


if __name__ == '__main__':
    main()
