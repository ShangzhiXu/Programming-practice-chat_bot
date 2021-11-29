"""
功能：程序入口，根据脚本执行每一个step并跳转到特定分支

"""
# -*- coding: utf-8 -*-
from chat_bot.src.getScprit import *
from chat_bot.src.nltk_manager import *

def execute(step_name):
    """
    用来执行脚本，获取用户输入并进行匹配，并返回下一step的名称
    用法
    >>>execute(next_step)
    :param step_name: 执行的step名称
    :return: 如果存在下一step，返回下一step的名称，否则返回0
    """
    print(step_set[step_name][0].speak_words)  # speak
    user_input = input()  # 获取用户输入

    purified_user_input = Input_purify(user_input)#根据用户输入创建自然语言处理类
    for i in range(2,len(step_set[step_name])):
        branch = step_set[step_name][i]
        for match_word in branch.match_words:
            #对于step里每一个branch的match_words进行处理
            phrase = match_word.split(" ")#处理待匹配词汇为词组的情况
            words_match = Words_Match(purified_user_input, len(phrase))#匹配初始化
            match_setting = branch.match_setting#获取对于匹配的设定
            field = setting_set.field#获取用户设定的脚本领域
            set_match_setting(match_setting,field,purified_user_input)#设定匹配模式
            if words_match.match(match_word) == 1:#对match_word进行匹配
                return step_set[step_name][i].next_step
    return 0
 # match and exec

input_file = open("./script.txt")
script = input_file.readlines()
setting_set = Setting()  # A set to store settings
step_set = {}# A set to store step
getScript(script,setting_set,step_set)#读取脚本内容并存储
next_step = execute(setting_set.start)#设定初始step，从用户设定第一个step开始
while(next_step!= 0):
    next_step = execute(next_step)
execute(setting_set.exit)#执行结束step
input_file.close()

