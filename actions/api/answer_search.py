#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File    : answer_search.py
# @Time    : 3/20/23 21:23
# @Author  : zlhhh
# @Description :
from py2neo import Graph


class AnswerSearcher:
    def __init__(self):
        self.graph = Graph("http://0.0.0.0:7474/", username="neo4j", password="123456", name="Military")

    def search_main(self, sql):
        final_answer = []
        # for sql_ in sqls:
        #     question_type = sql_['question_type']
        #     query = sql_['sql']
        #     # answer = []
        #     answer = self.graph.run(query).data()
        question_type = sql['question_type']
        query = sql['sql']
        # answer = []
        answer = self.graph.run(query).data()
        return answer


def main():
    answer_searcher = AnswerSearcher()
    print(answer_searcher.search_main(
        {'sql': "MATCH (m:Military) where m.name = '歼-16战机' return m", 'question_type': ""}))


if __name__ == '__main__':
    main()
