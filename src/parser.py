"""
语法分析模块

@ 功能：输入为用户编写的脚本语言文件，格式为.txt，该模块生成语法树
@ 工具：parse === copyright 2012-2021 Richard Jones <richard@python.org>
"""
# -*- coding: utf-8 -*-
from .parse import *
from .parse import compile


class Setting:
    """
    此类主要处理用户脚本中的Setting部分，设置脚本的作者、版本、版权信息
    处理脚本例如：
    Setting
        NAME Michael Step
        VERSION 1.0
        COPY_RIGHT @michael_2021.0.26
    用法：
      >>> set = Setting()
      >>> set.get_para("NAME Michael Step")
    返回：<Result ('Michael Step',) {}>

    上述函数的具体含义见函数体注释
    """
    name = ""           #作者名称
    version = ""        #版本号
    copy_right = ""     #版权信息
    parse_list = []     #保存可处理的语句格式
    start = "welcome"
    exit = "exit"
    field = "default"
    def __init__(self):
        """
        初始化函数，设定Setting类可以识别的语句
        用法：
        >>> set = Setting()
        例如self.parse_list.append(compile('  NAME {:^}'))
        一句表示本类可以识别：以："  NAME "开头的一行文字，其余类似
        """
        self.parse_list.append(compile('  NAME {:^}'))
        self.parse_list.append(compile('  VERSION {:^}'))
        self.parse_list.append(compile('  COPY_RIGHT {:^}'))
        self.parse_list.append(compile('  START {:^}'))
        self.parse_list.append(compile('  EXIT {:^}'))
        self.parse_list.append(compile('  FIELD {:^}'))

    def get_para(self, words):
        """
        语法分析语句，输入为一个待匹配句子，如果匹配成功，则将相应的
        属性添加到实例成员变量中，并返回匹配结果
        能匹配："  NAME ""  VERSION ""  COPY_RIGHT "开头的句子

        用法：
        >>> set = Setting()
        >>>set.get_para("  COPY_RIGHT @michael_2021.0.26")
        返回：<Result ('@michael_2021.0.26',) {}>
        :param words:待匹配句子
        :return:如果没有和任何一个匹配成功，返回0
        """
        if words.startswith("  NAME"):
            parse_result = self.parse_list[0].parse(words)
            self.name = parse_result
            return parse_result
        elif words.startswith("  VERSION"):
            parse_result = self.parse_list[1].parse(words)
            self.version = parse_result
            return parse_result
        elif words.startswith("  COPY_RIGHT"):
            parse_result = self.parse_list[2].parse(words)
            self.copy_right = parse_result
            return parse_result
        elif words.startswith("  START"):
            parse_result = self.parse_list[3].parse(words)
            self.start = parse_result[0]
            return parse_result
        elif words.startswith("  EXIT"):
            parse_result = self.parse_list[4].parse(words)
            self.exit = parse_result[0]
            return parse_result
        elif words.startswith("  FIELD"):
            parse_result = self.parse_list[5].parse(words)
            self.field = parse_result[0]
            return parse_result
        else:
            return 0


class Step:
    """
       此类主要处理用户脚本中的Step部分，设置步骤的名称、执行过程
       处理脚本例如：
       Step welcome
            Speak How are you
            Listen 10
            Branch how much|123|check,0,complaint
       用法：
         >>> temp_step = Step()
         >>> temp_step.set_name("Step welcome")
         >>> temp_step.get_para("Speak How are you")
       返回：<Result ('How are you',) {}>

       上述函数的具体含义见函数体注释
       """
    step_name = ""      #step名称
    parse_list = []     #保存可处理的语句格式
    action_list = []    #执行操作以及步骤
    def __init__(self):
        """
        语法分析语句，输入为一个待匹配句子，如果匹配成功，则将相应的
        属性添加到成员变量中，并返回匹配结果
        能匹配："  Branch ""  Speak ""  Default ""  Listen "开头的句子

        用法：
        >>>step = Step()
        :return: Step对象
        """
        self.parse_list.append(compile('  Branch {:^},{:^},{:^}'))
        self.parse_list.append(compile('  Speak {:^}'))
        self.parse_list.append(compile('  Default {:^}'))
        self.parse_list.append(compile('  Listen {:^}'))




    def step_name(self,words):
        """
        设定step的名称，例如设定为welcome
        用法：
        >>> temp_step.step_name("Step welcome")
        :param words:
        :return:
        """
        self.step_name = parse('Step {:^}',words)[0]
    def get_para(self,words):
        """
        语法分析语句，输入为一个待匹配句子，如果匹配成功，则将相应的
        属性添加到成员变量中，并返回匹配结果
        能匹配："  Branch ""  Speak ""  Default ""  Listen "开头的句子

        :param words: 带匹配句子
        :return: 如果没有和任何一个匹配成功，返回0
        """
        if words.startswith("  Branch"):
            parse_result = self.parse_list[0].parse(words)
            self.action_list.append(Branch(parse_result))
            return parse_result
        elif words.startswith("  Speak"):
            parse_result = self.parse_list[1].parse(words)
            self.action_list.append(Speak(parse_result))
            return parse_result
        elif words.startswith("  Default"):
            parse_result = self.parse_list[2].parse(words)
            self.action_list.append(Default(parse_result))
            return parse_result
        elif words.startswith("  Listen"):
            parse_result = self.parse_list[3].parse(words)
            self.action_list.append(Listen(parse_result))
            return parse_result
        else:
            return 0


class Speak:
    """
    本类处理Speak语句，用于应答用户输入，应答使用用户脚本中定义好的语句
    脚本样例：
    Speak How are you
    表示应答语句为：How are you
    """
    speak_words = ""     #回应语句

    def __init__(self, result):
        self.speak_words = result[0]


class Listen:
    """
    本类处理Listen语句，处理等待用户输入的时间，超过该时间则停止等待，直接执行下一句
    脚本样例：
    Listen 10
    表示等待时间为10s
    """
    listen_time = 0   # 输入等待时间，超过该时间则停止等待，直接执行下一句
    def __init__(self, result):
        self.listen_time = result[0]


class Branch:
    """
    处理Branch语句，匹配相应词汇，如果匹配成功，则跳转到相应的step
    脚本样例：
    Branch how much|123|check,0,complaint
    表示如果用户输入中包含："how much"或"123"或"check"，跳转到Step compliant执行，匹配模式为0
    *********************************
    匹配模式：
    0 默认模式，只有用户输入中包含待匹配词组，才会跳转
    1 纠错模式，修正用户输入中的错误，
              例如用户输入：cheeck，将会修改为check
              用户输入：wrod修改为word
              但是对于少写一些字母，例如chck，将无法修改
    2 词干获取，用户输入可能包含不同词性，例如用户输入"playing"，
              会将该单词转化为"play"并保存，默认保存为动词格式，如"I"保存为"be"
    4 去除非关键词， 去除用户输入中的例如'I'，'a'，'an'等常出现的非关键词汇，
                  依托nltk的停止词汇表得出删除的词汇，
                  该表由11种语言的2400个停止字组成，
                  见http://nltk.org/book/ch02.html
    8 使用同义词，由于在英语中，可能用户来自不同地区，有不同习惯，
                依托ntlk的wordnet实现同义词获取
                例如用户输入"check"，
                将会保存下如"cheque""tick""stop"等穷举出来的同义词，
                脚本用户在编写时可以不需要穷举各种情况
                注意：只适用于处理单个词汇，如"play"，短语如："how much"暂时不支持

    这里采用二进制的表示方式，windows部分API中也使用了类似方式
    例如要同时使用：
        词干获取和去除非关键词，就输入6，也就是二者之和
        纠错模式和词干获取，就输入3，也就是二者之和

    *********************************
    """
    match_words = []    #待匹配词汇
    match_setting = 0   #匹配模式
    next_step = ""      #如果匹配成功将要跳转到的step
    def __init__(self,result):
        """
        输入为result，只能够输入Step类处理后的结果，不允许其余外界函数调用，否则将会报错
        :param result:
        """
        self.match_words = result[0].split("|")
        self.match_setting = result[1]
        self.next_step = result[2]


class Default:
    """
    处理Default语句，跳转到相应的step
    脚本样例：
    Default complaint
    表示跳转到Step compliant执行
    """
    next_step = ""
    def __init__(self, result): #将要跳转到的step
        """
        输入为result，只能够输入Step类处理后的结果，不允许其余外界函数调用，否则将会报错
        :param result:
        """
        self.next_step = result[0]




