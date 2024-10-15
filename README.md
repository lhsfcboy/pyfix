# pyfix

Simple FIX Engine based on Python3

本项目试图创建一个简单的fix客户端,
可以命令行启动, 亦提供一个客户端.

## 基础的功能

- 可以启动为initiator或acceptor
- 可以从配置文件中读取预定设置
- 支持FIX4.2, FIX4.4, FIX5.0
- 可以多开
- 可以设置任务脚本
  - 形如"sleep 10; new order: price=last_msg.price"

## 参考过的项目

- [simplefix](https://pypi.python.org/pypi/simplefix)
- [PyFIX](https://github.com/wannabegeek/PyFIX)

## FIX协议相关基础知识
- FIX协议相关
  - <https://www.onixs.biz/fix-dictionary.html>
  - <http://fiximate.fixtrading.org/latestEP/>
  - <https://javarevisited.blogspot.com/search/label/FIX%20protocol%20tutorial>
