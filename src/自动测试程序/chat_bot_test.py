
"""
@功能：生成最多step_num数量的脚本，并生成能够遍历每一条链条的用户输入
"""
import random

import nltk


class chat_bot:
    """
    功能：生成指定step数量的脚本，并生成能够遍历每一条链条的用户输入
    用法
    >> t= chat_bot(step_num)
    """
    test_script_file = "./test_script.txt"
    test_input_file = "./test_input.txt"
    start = ""
    exit = ""
    step_set = {}  # A set to store step
    def __init__(self,step_num):
        """
        功能：生成指定链条数量的脚本，并生成能够遍历每一条链条的用户输入
        用法
         >> t= chat_bot_test(step_num)
        :param step_num:指定生成链条的数量
        """
        self.step_num = step_num   #生成链条的数量

    def createSetting(self):
        output_file = open(self.test_script_file,"a+")
        output_file.write("Setting\n")
        rand_word = self.getRandomWord()
        output_file.write(f"  NAME {rand_word}\n")
        output_file.write(f"  VERSION 1.0\n")
        rand_word = self.getRandomWord()
        output_file.write(f"  START {rand_word}\n")
        self.start = rand_word
        rand_word = self.getRandomWord()
        output_file.write(f"  EXIT {rand_word}\n")
        self.exit = rand_word
        rand_word = self.getRandomWord()
        output_file.write(f"  FIELD {rand_word}\n")
        output_file.close()

    def createStep(self,step_name):
        output_file = open(self.test_script_file, "a+")
        output_file.write(f"Step {step_name}\n")
        self.step_set[step_name] = []
        rand_word = self.getRandomWord()
        output_file.write(f"  Speak {rand_word}\n")
        rand_listen_num  = random.randint(0, 30)
        output_file.write(f"  Listen {rand_listen_num}\n")



        if self.step_num != 0 :
            rand_branch_num = random.randint(0, self.step_num)
            for i in range(0,rand_branch_num):
                next_step = self.getRandomWord()
                next_step_list = []
                next_step_list.append(next_step)

                self.step_set[next_step] = []
                output_file.write(f"  Branch ")
                for j in range(0,random.randint(1, 8)):
                    if j != 0:
                        output_file.write("|")
                    rand_matchword = self.getRandomWord()
                    output_file.write(f"{rand_matchword}")
                    next_step_list.append(rand_matchword)
                self.step_set[step_name].append(next_step_list)
                self.step_num -= 1
                output_file.write(f",0,{next_step}\n")
        output_file.close()
        for i in self.step_set[step_name]:
            self.createStep(i[0])


    def createUserInput(self,step_name):
        for next_step in self.step_set[step_name]:#遍历next step
            output_file = open(self.test_input_file, "a+")
            if step_name == self.start:
                output_file.write(f"\n\n")
            for j in range(0, random.randint(3, 10)):#test input 长度
                if j == 0:#放在随机位置
                    match_word = next_step[1]
                    output_file.write(f"{match_word} ")
                rand_word = self.getRandomWord()
                output_file.write(f"{rand_word} ")
            output_file.write(f"\n")
            output_file.close()
            self.createUserInput(next_step[0])





    def getRandomWord(self):
        #rand_word = random.sample('abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()',random.randint(2,10))
        rand_word = random.sample('abcdefghijklmnop qrstuvwxyz1234567890', random.randint(2, 12))
        rand_str = ""
        for i in rand_word:
            rand_str+=i
        return rand_str



t = chat_bot(5)
t.createSetting()
t.createStep(t.start)
t.createStep(t.exit)
t.createUserInput(t.start)
