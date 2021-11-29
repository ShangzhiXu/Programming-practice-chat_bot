
#为nltk_manager作为测试桩

from chat_bot.src.nltk_manager import *


user_input = "I want to know about the price of the wie"
purified_user_input = Input_purify(user_input)
match_word = "wine"

phrase = match_word.split(" ")  # 处理待匹配词汇为词组的情况
words_match = Words_Match(purified_user_input, len(phrase))  # 匹配初始化


set_match_setting(14,"wine",purified_user_input)#设定匹配模式
print(words_match.match(match_word))