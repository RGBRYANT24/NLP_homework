# -*- coding: utf-8 -*-
"""
@author: Junhui Yu
@Date:2020/08/30
"""
import yaml
import os

# pku_training_words = 'D:/ADR/PYprojects/NLP _homework/ciku.txt'
pku_training_words = 'D:/ADR/PYprojects/NLP _homework/corpuswordlist.dict.txt'
word_path = 'D:/ADR/PYprojects/NLP _homework/words.txt'
''' words = ["欢迎大家来到文本计算与认知智能实验室"]
words = ["我国发现新物种“白盖鸡油菌” 专家建议不要采食"] '''
words = ["我国发现新物种“白盖鸡油菌” 专家建议不要采食\
我国浙江和海南两地发现了一种名为“白盖鸡油菌”的新物种，这一发现已发表于国际期刊《微生物学前沿》。\
据了解，白盖鸡油菌由海南医学院热带转化医学教育部重点实验室、浙江大学生命科学学院食用菌研究所等研究机构的科研人员于2017年和2020年先后在海南鹦哥岭、浙江天目山发现，经基因测序后确定为新物种。\
据介绍，白盖鸡油菌菌盖表面光滑，边缘呈波浪状，黄白色至浅奶油色，菌肉坚实，气味不明显。\
浙江天目山国家级自然保护区管理局工作人员祁祥斌表示，新物种的发现，对于生态保护和生物进化研究，有十分重要的理论价值和现实意义，也证明自然保护区内的生态系统稳定、物种丰富，保护成效显著。\
这一消息经媒体报道后引发网友热议，不少网友留言询问：“能吃吗？好吃吗？”\
祁祥斌表示，白盖鸡油菌是鸡油菌属的一种，目前业内对这种新物种的了解还比较有限，建议不要采食，以免引起不良反应。"]
result_path = 'D:/ADR/PYprojects/NLP _homework/max_matching_result.txt'


def get_dic(words_list):
    with open(words_list, 'r', encoding='utf-8', ) as f:
        try:
            file_content = f.read().split()
        finally:
            f.close()
    chars = list(set(file_content))
    return chars


def positive_max_matching():
    max_length = 5
    for word in words:  # 分别对每行进行正向最大匹配处理
        max_length = 10
        word_list = []
        len_hang = len(word)
        while len_hang > 0:
            tryWord = word[0:max_length]
            while tryWord not in dic:
                if len(tryWord) == 1:
                    break
                tryWord = tryWord[0:len(tryWord) - 1]
            word_list.append(tryWord)
            word = word[len(tryWord):]
            len_hang = len(word)
    return word_list


if __name__ == '__main__':
    # print(words)
    dic = get_dic(pku_training_words)
    contents = positive_max_matching()
    seg = ""
    for s in contents:
        if seg == "":
            seg += s
        else:
            seg += "/" + s
    print(seg)
    result_file =  open(result_path, 'w+')
    result_file.write(seg)