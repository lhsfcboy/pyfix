'''
    这里是函数文档
    本函数功能是从仅包含FIX消息的文本中把FIX消息提取出来到字典
    要求的参数类型是String
    分隔符可能为|，（统计|与=数量差异足够小）
    分隔符可能为空格，（统计空格数量与等号数量差异）
    分隔符可能为SOH ^A
    分隔符可能没有.....
    
'''


import re

def parse_fix_log(fix_log):
    fix_dict = {}
    fix_fields = re.findall(r'(\d+)=(.*?)(?=\s+\d+=|$)', fix_log)

    for field in fix_fields:
        fix_dict[int(field[0])] = field[1]

    return fix_dict

if __name__ == "__main__":
    fix_log = "8=FIX.4.2  9=78  35=8  49=Sen 1 derCompID  56=TargetCompID  34=1  52=20240213-10:15:30  6=100.25  11=OrderID123  55=IBM  54=1  38=100  40=1 58=XXX YYY 10=003"

    fix_dict = parse_fix_log(fix_log)
    for key, value in fix_dict.items():
        print(f"{key}={value}")


'''
解释正则表达式： (\d+)=(.*?)(?=\s+\d+=|$)
ChatGPT
这个正则表达式的含义是匹配 FIX 协议中的键值对。下面是它的解释：

(\d+): 这部分匹配一个或多个数字字符（\d+），并使用括号捕获这个数字序列，表示一个键的部分。

=: 匹配一个等号，用于分隔键和值。

(.*?): 这个部分匹配零个或多个任意字符，但尽可能少地匹配，因为 *? 是非贪婪匹配，直到接下来的条件满足为止。这部分捕获了键对应的值。

(?=\s+\d+=|$): 这是一个非捕获的正向预查，用于确定键值对的结束位置。它包含两部分：

\s+\d+=: 匹配一个或多个空白字符（\s+），紧接着一个或多个数字字符（\d+），再紧接着一个等号。这部分表示键值对之间的分隔符。
|: 或操作符，表示前面的部分或者字符串的结尾（$）可以作为键值对的结束。
这个正则表达式可以很好地解析 FIX 协议中的键值对，并且考虑到了键值对之间可能存在的空格分隔和字符串末尾的情况。
'''


import unittest

class TestFixParser(unittest.TestCase):
    def test_parse_fix_log(self):
        # 测试解析简单的 FIX 日志
        fix_log = "35=8  49=SenderCompID 56=TargetCompID 34=4"
        expected_output = {35: '8', 49: 'SenderCompID', 56: 'TargetCompID', 34: '4'}
        self.assertEqual(parse_fix_log(fix_log), expected_output)

        # 测试解析包含特殊字符的 FIX 日志
        fix_log = "35=8  49=SenderCompID 56=TargetCompID 34=4 10=FinalMessage"
        expected_output = {35: '8', 49: 'SenderCompID', 56: 'TargetCompID', 34: '4', 10: 'FinalMessage'}
        self.assertEqual(parse_fix_log(fix_log), expected_output)

        # 测试解析空日志
        fix_log = ""
        expected_output = {}
        self.assertEqual(parse_fix_log(fix_log), expected_output)

        # 添加更多测试用例...

if __name__ == '__main__':
    unittest.main()
