from pmnlp.word import build_sentence_word_dict
from pmnlp.sentence import SentenceTplTrie

# 初始化，用于记录用户配置的词槽，以及语句的模版匹配。

user_word_dict = {'num': ["re\d+杯", '一杯', '两杯', '三杯'],
                  'coffee': ['拿铁', '咖啡'],
                  'coke': ['百事可乐', '可乐'],
                  'common': [],
                  'phone': ['re\d+'],
                  'taste': ['好喝的']
                  }

sentent_intent_tpls = {'coffee#1': '[common:0-6][taste][common:0-10][coffee]',
                       'coke#2': '[common:0-6][num][taste][coke][phone]'}

multi_sen = {
    'coffee': {'coffee#1': '[common:0-6][taste][common:0-10][coffee]',
               'coffee#2': '[common:0-6][coffee][phone]'},
    'coke': {'coke#1': '[common:0-6][taste][common:0-10][coke]',
             'coke#2': '[common:0-6][num][taste][coke][phone]'}
}

## 建立模型
sentence_word_dict = build_sentence_word_dict(word_dict=user_word_dict, fuzzy=True)

# 语句实例
test_tree = SentenceTplTrie(word_dict=sentence_word_dict)
texts = ['我要1杯拿铁', '我要300杯好喝的可乐123']

for text in texts:
    test_tree.build(sentence_tpl_dict=sentent_intent_tpls, common_key='common', text=text)
    print('One text processed!')


###################################################################
print('=======================================')
node = {'common:0-6': {'num': {'taste': {'coke': {'phone': 'coke#2'}}}}}
string = '我要300杯好喝的可乐123'

_, intent, result = test_tree.sep(string, common_key='common', init_node=node)
if isinstance(intent, str):
    # 匹配到
    print('[Match!]: ', intent, result)
else:
    # 无匹配
    print('[None Match]')

