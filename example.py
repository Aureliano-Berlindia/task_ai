from pmnlp.word import build_sentence_word_dict
from pmnlp.sentence import SentenceTplTrie

# 初始化，用于记录用户配置的词槽，以及语句的模版匹配。

user_word_dict = {'num': ["re\d+杯", '一杯', '两杯', '三杯'],
                  'coffee': ['拿铁', '铁咖啡'],
                  'coke': ['百事可乐', '可乐'],
                  'common': [],
                  'phone': ['re\d+'],
                  'taste': ['好喝']
                  }

sentent_intent_tpls = {'coffee#1': '[common:0-6][taste][common:0-10][coffee]',
                       'coffee#2': '[common:0-6][num][coke][phone]'}

# # 建立模型
sentence_word_dict = build_sentence_word_dict(word_dict=user_word_dict, fuzzy=True)

# 语句实例
test_tree = SentenceTplTrie(word_dict=sentence_word_dict)
texts = ['我要1杯好喝的拿铁', '我要300杯可乐133']

for text in texts:
    test_tree.build(sentence_tpl_dict=sentent_intent_tpls, common_key='common', text=text)
    print('One text processed!')
