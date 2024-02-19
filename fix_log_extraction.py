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
