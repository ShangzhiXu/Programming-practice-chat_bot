# Chat_bot_test 生存手册

 **目录**

[TOC]



#### 介绍

​	本文档包含了chat_bot_test模块所有的模块和API，包括API的介绍以及使用方法、参数、返回值、样例等，同时介绍了脚本语言的使用方法



#### 使用方法

```python
   >>> t= chat_bot(step_num)
    >>>t = chat_bot(5)
    >>>t.createSetting()
    >>>t.createStep(t.start)
    >>>t.createStep(t.exit)
    >>>t.createUserInput(t.start)
```



##### 生成脚本样例

```java
Setting
  NAME h572s4yje0
  VERSION 1.0
  START gw pf8dsit
  EXIT 8sgt 
  FIELD locmudstirn
Step gw pf8dsit
  Speak avyku6 s
  Listen 12
  Branch iet,0,bg5y0oj8vh9
  Branch f7|uzw|t2vh|xkp549 jfz|62e,0,b1zk2
  Branch e4|j7z6,0,zp5x
  Branch rg|6sm7 q39n|3nsyp| pe2|k52qxfc|7mw|ca21,0,rku67b3g0t 
Step bg5y0oj8vh9
  Speak vb
  Listen 28
  Branch lxb|djy|n3 ct|hpfmkjza8,0,e451 9mfuk
Step e451 9mfuk
  Speak m19f5nkv648
  Listen 24
Step b1zk2
  Speak i7 h4
  Listen 18
Step zp5x
  Speak 1mupd0
  Listen 24
Step rku67b3g0t 
  Speak c qvbeipx51z
  Listen 3
Step 8sgt 
  Speak uo0w5
  Listen 5

```

##### 生成测试用户输入



```java

iet x6nrk  keh 30d8mohxz4b9 xl47 
lxb 6oxdnc xys14uv 7b0lat x57ntc 


f7 oec4wn vcq38 1u2e4bnciwx 30dx lbniwc1z e3t efts imwy 


e4 hfno961c sd 7r3o rhel4z9v16 rnfx3e sjk1uipl wd9bpx 


rg bm 4i1dq 9s c10hxg47oq 

```

##### 分析

​	生成测试用户输入完全对应上一步的生成脚本样例，例如上例中，从**Step gw pf8dsit**开始，输入**iet x6nrk  keh 30d8mohxz4b9 xl47** 第一个词匹配，跳转到**Step bg5y0oj8vh9**随后输入**lxb 6oxdnc xys14uv 7b0lat x57ntc** 第一个词匹配，跳转到**Step 9mfuk**，随后没有后续Step，一条链分析结束

其余三条也是经过相同步骤，直到一条链结束为止

这里不需要用户手动输入进行测试，可以直接自动化测试



#### API介绍

##### 

```python
@功能：生成最多step_num数量的脚本，并生成能够遍历每一条链条的用户输入
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
      
    def createSetting(self):
        """

        在test脚本中生成Setting块，其中NAME、VERSION，START，EXIT，FIELD元素
        全部为随机生成
        用法：
        >>> t.createSetting()
        :return:
        """
        
        
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
```









  

