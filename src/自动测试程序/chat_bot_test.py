
"""
@功能：生成最多step_num数量的脚本，并生成能够遍历每一条链条的用户输入

"""
import random

import nltk


class chat_bot:
    """
    功能：生成指定step_num数量的脚本，并生成能够遍历每一条链条的用户输入
    例如step_num = 5，将会至多生成7个step，包含一个start节点和一个exit节点
    用法
    >>> t= chat_bot(step_num)
    >>>t = chat_bot(5)
    >>>t.createSetting()
    >>>t.createStep(t.start)
    >>>t.createStep(t.exit)
    >>>t.createUserInput(t.start)
    """
    test_script_file = "./test_script.txt" #生成test脚本
    test_input_file = "./test_input.txt"   #生成test用户输入
    start = ""  #start step name
    exit = ""   #exit step name
    step_set = {}  # A set to store step
    def __init__(self,step_num):
        """
        功能：生成指定链条数量的脚本，并生成能够遍历每一条链条的用户输入
        例如step_num = 5，将会至多生成7个step，包含一个start节点和一个exit节点
        用法
         >>> t= chat_bot_test(step_num)
        :param step_num:指定生成链条的数量
        """
        self.step_num = step_num   #生成链条的数量

    def createSetting(self):
        """

        在test脚本中生成Setting块，其中NAME、VERSION，START，EXIT，FIELD元素
        全部为随机生成
        用法：
        >>> t.createSetting()
        :return:
        """
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
        """
        在test脚本中生成Step块，Listen元素属性为0-30，Speak元素属性为随机生成的句子
        对于Branch元素的属性，
        1 生成1-8个匹配词汇
        2 匹配设置为0
        3 随机生成下一Step名称

        同时，将每一个Step的信息保存到self.step_set里面。
        self.step_set结构：
        {"step_name":[
            [next_step_name,跳转到下一step的所有匹配词汇],
            [[next_step_name,跳转到下一step的所有匹配词汇],
            ...]}
        用法：
        >>> t.createStep("welcome")
        :param step_name: 创建的step名称
        :return:
        """
        output_file = open(self.test_script_file, "a+")
        output_file.write(f"Step {step_name}\n")#根据入参生成step并存储
        self.step_set[step_name] = []
        rand_word = self.getRandomWord()
        output_file.write(f"  Speak {rand_word}\n")#Speak元素属性为随机生成的句子
        rand_listen_num  = random.randint(0, 30)
        output_file.write(f"  Listen {rand_listen_num}\n")#Listen元素属性为0-30

        if self.step_num != 0 :#如果已经生成的Step没有达到最多Step数
            rand_branch_num = random.randint(0, self.step_num)#本Step的branch数量0-step_num
            for i in range(0,rand_branch_num):#生成branch
                next_step = self.getRandomWord()#生成branch中的下一跳名称
                next_step_list = []  #用于保存下一跳信息
                next_step_list.append(next_step)

                self.step_set[next_step] = []#将下一跳保存在step_set里面
                output_file.write(f"  Branch ")
                for j in range(0,random.randint(1, 8)):#随机生成1-8个match_word
                    if j != 0:
                        output_file.write("|")
                    rand_matchword = self.getRandomWord()
                    output_file.write(f"{rand_matchword}")
                    next_step_list.append(rand_matchword)#保存match_word
                self.step_set[step_name].append(next_step_list)#将下一跳信息保存在本Step下
                self.step_num -= 1#减少一个step的名额
                output_file.write(f",0,{next_step}\n")
        output_file.close()
        for i in self.step_set[step_name]:
            self.createStep(i[0])#对于本Step的每一个next_step，递归的生成块并输出


    def createUserInput(self,step_name):
        """
        根据createStep生成的step_set，生成用户输入语句，遍历step_set里面的每一条链
        用两行空白分开两条不同的链
        用法：
        >>> t.createUserInput(t.start)
        :param step_name:生成本Step跳转到所有next_step的语句
        :return:
        """
        for next_step in self.step_set[step_name]:#遍历next step
            output_file = open(self.test_input_file, "a+")
            if step_name == self.start:
                output_file.write(f"\n\n")#用两行空白分开两条不同的链
            for j in range(0, random.randint(3, 10)):#用户input 长度随机生成
                if j == 0:#把match_word放在随机位置
                    match_word = next_step[1]#随机挑选一个match_word
                    output_file.write(f"{match_word} ")
                rand_word = self.getRandomWord()
                output_file.write(f"{rand_word} ")#用户input 的其余单词随机生成
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
