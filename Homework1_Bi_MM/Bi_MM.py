import time


def get_dic(dic_path):
    with open(dic_path, 'r', encoding='utf-8', ) as f:
        try:
            file_content = f.read().split()
        finally:
            f.close()
    chars = list(set(file_content))
    return chars


class WordSeg(object):
    def __init__(self, dic):
        self.dic = dic
        self.window_size = len(max(dic, key=len, default=''))

    def forward_max_match(self, text):
        fmm_result = []
        index = 0
        text_length = len(text)
        piece = ''
        while index < text_length:
            for size in range(self.window_size + index, index, -1):
                piece = text[index:size]
                if piece in self.dic:
                    index = size - 1
                    break
            index += 1
            fmm_result.append(piece)
        return fmm_result

    def backward_max_match(self, text):
        bmm_result = []
        index = len(text)
        piece = ''
        while index > 0:
            for size in range(index - self.window_size, index):
                piece = text[size:index]
                if piece in self.dic:
                    index = size + 1
                    break
            index -= 1
            bmm_result.append(piece)
        bmm_result.reverse()
        return bmm_result

    def bi_directional_max_match(self, text):
        fmm_list = self.forward_max_match(text)
        bmm_list = self.backward_max_match(text)
        if len(fmm_list) != len(bmm_list):
            return fmm_list if len(fmm_list) < len(bmm_list) else bmm_list
        else:
            is_same = True
            fmm_single = 0
            bmm_single = 0
            for i in range(0, len(fmm_list)):
                if fmm_list[i] != bmm_list[i]:
                    is_same = False
                if len(fmm_list[i]) == 1:
                    fmm_single += 1
                if len(bmm_list[i]) == 1:
                    bmm_single += 1
            if is_same:
                return fmm_list
            else:
                return fmm_list if fmm_single < bmm_single else bmm_list


if __name__ == '__main__':
    # dic = ['研究', '研究生', '生命', '命', '的', '起源']
    # text = '研究生命的起源'
    text = "我国发现新物种“白盖鸡油菌” 专家建议不要采食\
    我国浙江和海南两地发现了一种名为“白盖鸡油菌”的新物种，这一发现已发表于国际期刊《微生物学前沿》。\
    据了解，白盖鸡油菌由海南医学院热带转化医学教育部重点实验室、浙江大学生命科学学院食用菌研究所等研究机构的科研人员于2017年和2020年先后在海南鹦哥岭、浙江天目山发现，经基因测序后确定为新物种。\
    据介绍，白盖鸡油菌菌盖表面光滑，边缘呈波浪状，黄白色至浅奶油色，菌肉坚实，气味不明显。\
    浙江天目山国家级自然保护区管理局工作人员祁祥斌表示，新物种的发现，对于生态保护和生物进化研究，有十分重要的理论价值和现实意义，也证明自然保护区内的生态系统稳定、物种丰富，保护成效显著。\
    这一消息经媒体报道后引发网友热议，不少网友留言询问：“能吃吗？好吃吗？”\
    祁祥斌表示，白盖鸡油菌是鸡油菌属的一种，目前业内对这种新物种的了解还比较有限，建议不要采食，以免引起不良反应。"
    dic_path = 'D:/ADR/PYprojects/NLP_homework/Homework1_Bi_MM/corpuswordlist.dict.txt'
    print('分词前的句子：', text)
    dic = get_dic(dic_path)
    wordSeg = WordSeg(dic)
    time_start = time.clock()
    fmm_result = wordSeg.forward_max_match(text)
    fmm_time = time.clock() - time_start
    print('前向最大匹配：', fmm_result)
    print('前向最大匹配的时间：', fmm_time)
    time_start = time.clock()
    bmm_result = wordSeg.backward_max_match(text)
    bmm_time = time.clock() - time_start
    print('后向最大匹配：', bmm_result)
    print('后向最大匹配的时间：', bmm_time)
    time_start = time.clock()
    bdmm_result = wordSeg.bi_directional_max_match(text)
    bdmm_time = time.clock() - time_start
    print('双向最大匹配：', bdmm_result)
    print('后向最大匹配的时间：', bdmm_time)

    result_path = 'D:/ADR/PYprojects/NLP_homework/Homework1_Bi_MM/Bi_MM_result.txt'
    result_file = open(result_path, 'w+')
    result_file.write('前向最大匹配\n')
    result_file.write('\\'.join(fmm_result) + '\n')
    result_file.write('前向最大匹配的时间: ' + str(fmm_time) + '\n')
    result_file.write('\n')

    result_file.write('后向最大匹配\n')
    result_file.write('\\'.join(bmm_result) + '\n')
    result_file.write('\n')
    result_file.write('后向最大匹配的时间: ' + str(bmm_time) + '\n')
    result_file.write('\n')

    result_file.write('双向最大匹配\n')
    result_file.write('\\'.join(bdmm_result) + '\n')
    result_file.write('双向最大匹配的时间: ' + str(bdmm_time) + '\n')
    result_file.close()
