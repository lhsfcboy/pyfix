
'''
    这里是函数文档
    本函数功能是从一行原始的Log文件中提取出FIX消息的部分
    要求的参数类型是String
    提取方法: 使用正
    异常处理: 如果
    
'''

import re

# 原始文档
text = "xxxx 8=FIX.4.2 | 3= 110=123 210=xyz 10=456| xyz"

# 生成的正则表达式
pattern = r'8=FIX\..*?(?<!\d)10=\d{3}'

# 使用正则表达式进行匹配
matches = re.findall(pattern, text)

# 输出匹配结果
for match in matches:
    print(match)
