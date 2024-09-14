from collections import deque

# 用于存储最近的2000行Quote的双端队列
recent_quotes = deque(maxlen=2000)

# 打开包含 FIX 协议日志的文件
with open('fix_log.txt', 'r') as file:
    # 打开用于写入输出的日志文件
    with open('output_log.txt', 'w') as output_file:
        # 逐行读取日志文件
        for line in file:
            # 分割每一行，以逗号和等号为分隔符
            parts = line.strip().split(',')
            message_type = None
            quote_id = None
            
            # 解析每一行的键值对
            for part in parts:
                key, value = part.split('=')
                if key == '35':
                    message_type = value
                elif key == '117':
                    quote_id = value
            
            # 如果是 Quote 消息，则将 Quote ID 添加到 recent_quotes 双端队列中
            if message_type == 'S' and quote_id:
                recent_quotes.append((quote_id, line.strip()))

            # 如果是订单消息，则检查是否引用了 Quote，如果是，则输出对应的 Quote 和订单到输出日志文件中
            elif message_type == 'D' and quote_id:
                for recent_quote_id, recent_quote_line in recent_quotes:
                    if recent_quote_id == quote_id:
                        output_file.write("Order: " + line.strip() + "\n")
                        output_file.write("Quote: " + recent_quote_line + "\n\n")  # 写入空行以分隔不同的订单和相应的 Quote
                        break
