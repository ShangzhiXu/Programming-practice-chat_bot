"""
功能：词干提取，句子分词，同义词提取，词汇匹配，短语匹配, 拼写纠错
工具：nltk === Copyright (C) 2001-2021 NLTK Project
     github开源项目 === Bayes-one
"""



from chat_bot.src.getScprit import *
from chat_bot.src.nltk_manager import *

def execute(step_name):
    print(step_set[step_name][0].speak_words)  # speak
    user_input = input()  # listen

    purified_user_input = Input_purify(user_input)
    for i in range(2,len(step_set[step_name])):
        for match_word in step_set[step_name][i].match_words:
            l = match_word.split(" ")
            words_match = Words_Match(purified_user_input, len(l))
            match_setting = step_set[step_name][i].match_setting
            field = setting_set.field
            getPara(match_setting,field,purified_user_input)
            if words_match.match(match_word) == 1:
                return step_set[step_name][i].next_step
    return 0
 # match and exec

input_file = open("./script.txt")
script = input_file.readlines()
setting_set = Setting()  # A set to store settings
step_set = {}# A set to store step
getScript(script,setting_set,step_set)
next_step = execute(setting_set.start)
while(next_step!= 0):
    next_step = execute(next_step)
execute(setting_set.exit)
input_file.close()

