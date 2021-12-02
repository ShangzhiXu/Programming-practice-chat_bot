# chatbot

基于nltk和parse实现的chatbot脚本语言
针对机器人设计领域的脚本语言设计

**功能**：词干提取，句子分词，同义词提取，词汇匹配，短语匹配, 拼写纠错

nltk：https://github.com/nltk/nltk

parse：https://github.com/r1chardj0n3s/parse

### 脚本样例

```java
Setting
  NAME Michael_chatbot
  VERSION 1.0
  COPY_RIGHT @michael_2021.0.26
  START welcome
  EXIT exit
  FIELD wine
Step welcome
  Speak How are you
  Listen 10
  Branch good|fine,3,default
  Branch angry|bad|not good,0,complaint
  Branch wine|check,3,check
Step complaint
  Speak what would you like to compliant?
  Listen 10
  Branch ?,0,apologize
  Branch fine,0,default
  Branch wine|check,3,check
Step apologize
  Speak sorry
  Listen 10
  Branch ok,0,default
Step check
  Speak the wine is 100¥
  Listen 10
  Branch ok,0,default
Step default
  Speak Is there anything that I can help you？
  Listen 30
  Branch angry|bad|not good,0,complaint
  Branch wine|check,3,check
  Branch ok,0,default
Step exit
  Speak Good bye, have a good day!
  Listen 0


```

运行结果：
```
例1
>>>How are you
I an fine, thank you
>>>Is there anything that I can help you？
yes please tell me the price of the wine
>>>the wine is 100¥
ok
>>>Is there anything that I can help you？
no thanks
>>>Good bye, have a good day!

例2,wine输入错误
>>>How are you
I want to know the price of the wie
>>>the wine is 100¥
ok,thanks alot
>>>Is there anything that I can help you？
no thanks
>>>Good bye, have a good day!

例3,获取词干check
>>>How are you
ChEck the price
>>>the wine is 100¥
ok
>>>Is there anything that I can help you？
no
>>>Good bye, have a good day!
```

### 脚本样例2
```python
Setting
  NAME Michael_chatbot
  VERSION 1.0
  COPY_RIGHT @michael_2021.0.26
  START welcome
  EXIT exit
  FIELD food
Step welcome
  Speak How are you
  Listen 10
  Branch good|fine,3,default
  Branch food|check,3,food
  Branch hotdog,3,hotdog
Step complaint
  Speak what would you like to compliant?
  Listen 10
  Branch ?,0,apologize
  Branch fine,0,default
  Branch food|check,3,food
  Branch hotdog,3,hotdog
Step apologize
  Speak sorry
  Listen 10
  Branch ok,0,default
Step food
  Speak which food?
  Listen 10
  Branch hotdog,3,hotdog
Step hotdog
  Speak the hot dog is 10$,would you like to order?
  Listen 10
  Branch yes,0,buy
Step buy
  Speak done!Enjoy it
  Branch thanks,0,default
Step default
  Speak Is there anything that I can help you？
  Listen 30
  Branch angry|bad|not good,0,complaint
  Branch food|check,3,food
  Branch hotdog,3,hotdog
  Branch ok,0,default
Step exit
  Speak Good bye, have a good day!
  Listen 0

```
运行结果：
```buildoutcfg
纠正hotdog输入错误
>>>How are you
fine
>>>Is there anything that I can help you？
hotdg please
>>>the hot dog is 10$,would you like to order?
yes
>>>done!Enjoy it
thanks
>>>Good bye, have a good day!


Process finished with exit code 0
```
### 脚本语言描述

这里简称本项目脚本语言为RSL(robot Specific langugage)

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

 - Listen 等待用户输入时长，单位：秒（默认不开启，肯不匹配用户输入）

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
              见http://www.nltk.org/book/ch02.html
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

  

