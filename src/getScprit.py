
"""
@功能：将用户脚本进行语法分析，并用set形成树结构进行保存
"""

from chat_bot.src.parser import *
from chat_bot.src.nltk_manager import *

def getScript(script,setting_set,step_set):
    """
    将用户脚本进行语法分析，并用set形成树结构进行保存
    用法：
    >>> getScript(script,setting_set,step_set)
    :param script: 用户输入脚本
    :param setting_set: 用于保存setting
    :param step_set: 用于保存step
    :return:
    """
    start = 0#用于记录每一个step在step_set里的存储的起始位置
    end = 0#用于记录每一个step在step_set里的存储的结束位置
    i = 0
    k = 0
    while i + 1 < len(script):
        line = script[i].rstrip('\n')
        if line.startswith("Setting"):#处理setting
            while i < len(script):
                i += 1
                line = script[i].rstrip('\n')
                if line.startswith(" ") != 0:#要求两个空格开头
                    f = setting_set.get_para(line)
                    if (f == 0):
                        print("Error at" + line)#如果不符合愈发要求，报错并输出错误位置
                else:
                    break
        elif line.startswith("Step"):#处理step
            temp_step = Step()#临时保存step数据
            temp_step.step_name(line)#设定step名称
            while i + 1 < len(script):
                i += 1
                line = script[i].rstrip('\n')
                if line.startswith(" ") != 0:#两个空格开头
                    f = temp_step.get_para(line)
                    end += 1
                    if (f == 0):
                        print("Error at" + line)#如果不符合愈发要求，报错并输出错误位置
                else:
                    break
            step_set[temp_step.step_name] = temp_step.action_list[start:end]
            #结束后复制到step_set里面
            start = end
        else:
            if i + 1 < len(script):
                i += 1
            else:
                break






