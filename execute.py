from src.parser import *
from src.nltk_manager import *

def getScript(script,setting_set,step_set):
    start = 0
    end = 0
    i = 0
    k = 0
    while i + 1 < len(script):
        line = script[i].rstrip('\n')
        if line.startswith("Setting"):
            while i < len(script):
                i += 1
                line = script[i].rstrip('\n')
                if line.startswith(" ") != 0:
                    f = setting_set.get_para(line)
                    if (f == 0):
                        print("Error at" + line)
                else:
                    break
        elif line.startswith("Step"):
            temp_step = Step()
            temp_step.step_name(line)
            while i + 1 < len(script):
                i += 1
                line = script[i].rstrip('\n')
                if line.startswith(" ") != 0:
                    f = temp_step.get_para(line)
                    end += 1
                    if (f == 0):
                        print("Error at" + line)
                else:
                    break
            step_set[temp_step.step_name] = temp_step.action_list[start:end]
            start = end
        else:
            if i + 1 < len(script):
                i += 1
            else:
                break

def a():
    pass
def execute(step_name):
    print(step_set[step_name][0].speak_words)  # speak
    user_input = input()  # listen

    input_words = Input_purify(user_input)
    for i in range(2,len(step_set[step_name])):
        for match_word in step_set[step_name][i].match_words:
            l = match_word.split(" ")
            words_match = Words_Match(input_words, len(l))
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

#todo
# Branch的0248等操作
'''
实现过程：
· 在nltk里面弄一个函数，专门用来识别，把输入的数按位进行计算，计算得到哪一位可以用
'''
#todo
# 想添加一个功能，就是可以设置一个宏，就不用每次都重复编辑重复的单词了
"""
这个其实好实现的
"""

#记录：真的是惊心动魄的github记录