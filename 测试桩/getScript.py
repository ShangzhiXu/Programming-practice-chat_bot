
# -*- coding: utf-8 -*-

#为parser进行测试，作为测试桩
#为main进行测试，作为测试桩
#由于先写的parser，所以getScript不需要测试集
from chat_bot.src.parser import *


def getScript(script,setting_set,step_set):

    #line = "NAME Michael_chatbot"
    #line = "VERSION 1.0"
    #line = "START welcome"
    line = "FIELD wine"
    setting_set.get_para(line)
    temp_step = Step()#临时保存step数据
    line = "Step default"
    temp_step.step_name(line)#设定step名称
    line = "Speak Is there anything that I can help you？"
    f = temp_step.get_para(line)
    step_set[temp_step.step_name] = temp_step.action_list



