"""
功能：词干提取，句子分词，同义词提取，词汇匹配，短语匹配, 拼写纠错
工具：nltk === Copyright (C) 2001-2021 NLTK Project
     github开源项目 === Bayes-one
"""


from src.parser import *
from src.nltk_manager import *

words = Input_purify("Checck My aacount")
words.word_correction()
print(words.words_token)
words.delete_stopwords()
words.get_stem()
#words.use_synonym()


words_match = Words_Match(words)
b = ('check','account')
words_match.match(b)