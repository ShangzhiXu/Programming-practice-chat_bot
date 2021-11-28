# Chat_bot 生存手册

 **目录**

Chat_bot 生存手册
介绍
模块及调用关系
模块及API介绍
main
getScript
nltk_manager
parse
correct
correct_food
correct_wine
使用方法
脚本样例
脚本语言描述



#### 介绍

​	本文档包含了项目所有的模块和API，包括API的介绍以及使用方法、参数、返回值、样例等，同时介绍了脚本语言的使用方法

#### 模块及调用关系

模块：

- main  

-  getScprit   

- nltk_manager   

- parser 

- correct  

-  correct_food  

-  correct_wine

  调用关系：

> main----getScprit
>
> ​	     ----nltk_manager
>
> getScript-----nltk_manager
>
> ​				-----parser
>
> nltk_manager-----correct
>
> ​						------correct_food
>
> ​						------correct_wine
>
> parser
>
> correct
>
> correct_food
>
> correct_wine



#### 模块及API介绍

##### main

```python
功能：程序入口，根据脚本执行每一个step并跳转到特定分支
def execute(step_name):
    """
    用来执行脚本，获取用户输入并进行匹配，并返回下一step的名称
    用法
    >>>execute(next_step)
    :param step_name: 执行的step名称
    :return: 如果存在下一step，返回下一step的名称，否则返回0
    """
    
```

##### getScript

```python
@功能：将用户脚本进行语法分析，并用set形成树结构进行保存
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
    
```

##### nltk_manager

```python
自然语言处理模块

@ 功能：词干提取，句子分词，同义词提取，词汇匹配，短语匹配, 拼写纠错
@ 工具：nltk === Copyright (C) 2001-2021 NLTK Project
     github开源项目 === Bayes-one
     
class Input_purify:
    """
    此类主要用于净化用户输入，可以对用户输入：词干提取，句子分词，同义词提取，拼写纠错
    用法：
    >>> words = Input_purify("Check My acount")   #对输入字符串进行处理
    >>> words.word_correction()                   #对用户输入进行错误修正
    >>> words.delete_stopwords()                  #设置跳过停止字符
    >>> words.get_stem()                          #设置获取词干
    >>> words.use_synonym()                       #设置获取同义词

    上述函数的具体含义见函数体注释
    """
    words = ""                                  #用户输入的句子
    words_token = ""                            #将用户输入的句子拆分成单词
    words_tag = ""                              #保存用户的输入单词的词性
    words_lemma = []                            #保存用户的输入单词的同义词
    
    def __init__(self,input):
        """
        此函数主要用于初始化类
        :param input:
        用法：
        >>> words = Input_purify("Check My acount")
        """
    def delete_stopwords(self):
        """
        此函数主要用于清除用户输入中的stop words
        :return:;
        用法：
        >>> words.delete_stopwords()
        去除用户输入中的例如'I'，'a'，'an'等常出现的非关键词汇，依托nltk的停止词汇表得出
        删除的词汇，该表由11种语言的2400个停止字组成，见http://nltk.org/book/ch02.html
        """
     
     def use_synonym(self):
        """
        此函数主要用于获取用户输入的同义词
        用法：
        >>> words.use_synonym()
        由于在英语中，可能用户来自不同地区，有不同习惯，依托ntlk的wordnet实现同义词获取
        例如用户输入"check"，调用本函数后将会保存下如"cheque""tick""stop"等穷举出来的
        同义词，脚本用户在编写时可以不需要穷举各种情况

        *** 注意：只适用于处理单个词汇，如"play"，短语如："how much"暂时不支持
        :return:
        """
      
     def word_correction(self,field):
        """
        此函数主要用于修正用户输入中的错误
        用法：
        >>> words.word_correction(field)
        例如用户输入：cheeck，将会修改为check，用户输入：wrod修改为word
        但是对于少写一些字母，例如chck，将无法修改，因为可能的情况太多了
        机器学习依托txt文件进行训练。
        :return:
        """
        
        
        
        
class Words_Match:
    """
    类主要用于匹配用户输入中的内容
    用法：
        >>> b = ('check','account')
        >>> words_match.match(b,1)

    """
    def __init__(self,input_words,match_size):
        """
        用户输入应当是Input_purify类中的words_token

        ***注意：调用本类，如果要匹配多元词组
                words_token不能是获取同义词之后的，也就是不能调用use_synonym
                否则将无法匹配

        :param input_words 用户输入
        :param match_size 穷举为n元组
        用法：
        >>> words_match = Words_Match(words.words_token,1)
        """
    def match(self,match_word):
        """
        用户输入要匹配的单词或短语以及单词或短语的长度（包含几个单词）
        随后本函数将穷举出words_token中所有的n元组并进行匹配
        例如：['check', 'my', 'account']穷举二元组为
        ['check', 'my']['my', 'account']两个

        :param: match_word
        :return:
        """
        
        
        
        
        
def set_match_setting(match_setting,field,Input_purify):
        """

        :param match_setting: 匹配设置

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
        :param Input_purify 用户输入
        :return:
        用法：
        >>> set_match_setting(match_setting,field,purified_user_input)
        """
```

##### parse

```python
语法分析模块

@ 功能：输入为用户编写的脚本语言文件，格式为.txt，该模块生成语法树
@ 工具：parse === copyright 2012-2021 Richard Jones <richard@python.org>


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
    start = "welcome"   #脚本开始执行位置
    exit = "exit"       #脚本退出位置
    field = "default"   #脚本对应领域
    
    
    
    
    def __init__(self):
        """
        初始化函数，设定Setting类可以识别的语句
        用法：
        >>> set = Setting()
        例如self.parse_list.append(compile('  NAME {:^}'))
        一句表示本类可以识别：以："  NAME "开头的一行文字，其余类似
        """
        
        
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
     def step_name(self,words):
        """
        设定step的名称，例如设定为welcome
        用法：
        >>> temp_step.step_name("Step welcome")
        :param words:
        :return:
        """
        
         def get_para(self,words):
        """
        语法分析语句，输入为一个待匹配句子，如果匹配成功，则将相应的
        属性添加到成员变量中，并返回匹配结果
        能匹配："  Branch ""  Speak ""  Default ""  Listen "开头的句子

        :param words: 带匹配句子
        :return: 如果没有和任何一个匹配成功，返回0
        """
        
  
  
  
class Speak:
    """
    本类处理Speak语句，用于应答用户输入，应答使用用户脚本中定义好的语句
    脚本样例：
    Speak How are you
    表示应答语句为：How are you
    """
    speak_words = ""     #回应语句
    
 


class Listen:
    """
    本类处理Listen语句，处理等待用户输入的时间，超过该时间则停止等待，直接执行下一句
    脚本样例：
    Listen 10
    表示等待时间为10s
    """
    
   
  
  
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
    
    
    
    
    
class Default:
    """
    处理Default语句，跳转到相应的step
    脚本样例：
    Default complaint
    表示跳转到Step compliant执行
    """
    next_step = ""
```



##### correct

```python

@功能：词汇纠正模块，对输入词汇根据训练数据进行纠正


alphabet_set = 'abcdefghijklmnopqrestuvwxyz'  #词汇表


def getLowerWord(text):
    """
    找到输入中的全部字母，转换为小写，搜索使用正则匹配
    用法：
    >>>getLowerWord("text")
    :param text:
    :return:
    """
def known(words):
    """
    判断被查询的字符是否已经被查询过
    :param words:
    :return:
    """
    
def train(new_words):
    """
    训练，输入为带训练的数据集合，根据字典进行查找，
    每发现一个单词，就加入到字典中去，
    如果字典中不存在这个单词，就新创建一个key
    如果存在这个单词，就把key的权重增加

    用法：
    >>>new_words=train(getLowerWord(file.read()))
    :param new_words:
    :return:
    """
```

##### correct_food

##### 

```python
@功能：词汇纠正模块，对输入词汇根据训练数据进行纠正


alphabet_set = 'abcdefghijklmnopqrestuvwxyz'  #词汇表


def getLowerWord(text):
    """
    找到输入中的全部字母，转换为小写，搜索使用正则匹配
    用法：
    >>>getLowerWord("text")
    :param text:
    :return:
    """
def known(words):
    """
    判断被查询的字符是否已经被查询过
    :param words:
    :return:
    """
    
def train(new_words):
    """
    训练，输入为带训练的数据集合，根据字典进行查找，
    每发现一个单词，就加入到字典中去，
    如果字典中不存在这个单词，就新创建一个key
    如果存在这个单词，就把key的权重增加

    用法：
    >>>new_words=train(getLowerWord(file.read()))
    :param new_words:
    :return:
    """
```



##### correct_wine

```python
@功能：词汇纠正模块，对输入词汇根据训练数据进行纠正


alphabet_set = 'abcdefghijklmnopqrestuvwxyz'  #词汇表


def getLowerWord(text):
    """
    找到输入中的全部字母，转换为小写，搜索使用正则匹配
    用法：
    >>>getLowerWord("text")
    :param text:
    :return:
    """
def known(words):
    """
    判断被查询的字符是否已经被查询过
    :param words:
    :return:
    """
    
def train(new_words):
    """
    训练，输入为带训练的数据集合，根据字典进行查找，
    每发现一个单词，就加入到字典中去，
    如果字典中不存在这个单词，就新创建一个key
    如果存在这个单词，就把key的权重增加

    用法：
    >>>new_words=train(getLowerWord(file.read()))
    :param new_words:
    :return:
    """
```





#### 使用方法

##### 脚本样例

```java
Setting
  NAME Michael_chatbot
  VERSION 1.0
  COPY_RIGHT @michael_2021.10.26
  START welcome
  EXIT exit
  FIELD wine
Step welcome
  Speak How are you
  Listen 10
  Branch good,3,complaint
  Branch angry|bad|not good,0,complaint
  Branch bye|ok,0,default
  Branch check|account,0,check
Step complaint
  Speak what would you like to compliant?
  Listen 10
  Branch ?,0,apologize
  Branch ok,0,default
  Branch check,0,check
Step apologize
  Speak sorry
  Listen 10
  Branch ok,0,default
Step check
  Speak you have 100¥
  Listen 10
  Branch bye|ok,0,default
Step default
  Speak Is there anything else that I can help you？
  Listen 30
  Branch check|account,0,check
Step exit
  Speak Good bye, have a good day!
  Listen 0
```

##### 脚本语言描述

这里简称本项目脚本语言为RSL(robot setting langugage)

RSL为块结构语言，块分为**Setting**和Step两种**类别**，块内内容称为**元素**，元素中内容称为**属性**。

块的类别单独成行无需缩进，块元素在前面加两个空格，属性与元素中间用一个空格分开

**RSL以Setting块开始，Setting块有如下几种元素**

```java
NAME Michael_chatbot

VERSION 1.0  

COPY_RIGHT @michael_2021.10.26

START welcome

EXIT exit

FIELD wine
```

- NAME 表示编写的脚本的名称

  - 用法：NAME (字符串)

- VERSION 表示编写的脚本的版本

  - 用法：VERSION （字符串）

- COPY_RIGHT 表示编写的脚本的版权

  - 用法：COPY_RIGHT （字符串）

- SRTART 设定脚本应从那个Step块开始执行，例如上例中是从Step welcome开始执行

  - 用法：START （块名称）

- EXIT 设定脚本应从那个Step块退出，例如上例中是从Step exit退出

  - 用法：EXIT （块名称）

- FIELD 设定脚本语言针对哪个领域，例如上例中是针对wine领域现在脚本支持酒：wine和食物：food两种特定领域，不设定本元素，为默认领域。

  - 用法 FIELD （wine|food）

  

  

  **RSL以Step块为主体，Step块有如下几种元素**

  ```java
  Step welcome
    Speak How are you
    Listen 10
    Branch good,3,complaint
    Branch angry|bad|not good,0,complaint
    Branch bye|ok,0,default
    Branch check|account,0,check
  ```

 - Speak 到达本块向用户输出的内容为（字符串）

   - 用法：Speak (字符串)，上例中，到达welcome块，向用户输出“How are you”

 - Listen 等待用户输入时长，单位：秒

   - 用法：Listen（数字）,上例中为监听10s

 - Branch **匹配用户输入词汇**、**匹配模式**、**跳转到下一块名称**，这三个属性之间用","分开

   - 用法：Branch （字符串|字符串|...）,（数字）,（块名称）

     - **匹配用户输入词汇**：待匹配词汇，可以是单个词汇或多个词汇。例如上例中，如果在welcome块中，用户输入包含angry或bad或not good，则跳转到Step complaint块

     - **匹配模式**：

      ```java
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
      ```

    - **跳转到下一块名称**：如果用户输入中存在和**匹配用户输入词汇**相同的词汇，就跳转到名称与**跳转到下一块名称**相同的Step块中继续执行，例如上例中，如果在welcome块中，用户输入包含angry或bad或not good，则跳转到Step complaint块

  

