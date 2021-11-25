from chat_bot.src.parser import *
from chat_bot.src.nltk_manager import *
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






