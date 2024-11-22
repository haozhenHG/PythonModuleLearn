import logging


print('logging _nameToLevel:',logging._nameToLevel)

print('logging _levelToName:',logging._levelToName)
# 日志优先级：CRIRICAL>ERROR>WARNING>INFO>DEBUG

# 当日志级别设置为某个级别时，则低于该级别的日志将不输出。如日志级别设置为INFO，则DEBUG级别的日志将不输出。

# 根日志器默认日志级别为WARNING，这里将其重置，以保证debug、info级别的日志也能输出

# logging.basicConfig(level=logging.ERROR)
# 配置基本的日志输出格式和级别
logging.basicConfig(level=logging.INFO, format='[%(asctime)s] [%(threadName)s] [line:%(lineno)d] %(levelname)s:%(message)s')
'''
%(asctime)s：日志记录的时间戳。
%(threadName)s：线程名称，表示产生日志记录的线程的名字
[line:%(lineno)d]：日志记录产生的代码行号。%(lineno)d 会获取当前日志记录的行号。

-：时间戳和日志级别之间的分隔符。
%(levelname)s：日志级别名称（如DEBUG、INFO、WARNING等）。
:：日志级别和日志消息之间的分隔符。
%(message)s：日志消息本身。
'''


# # {'CRITICAL / FATAL': 50,  'ERROR': 40, 'WARN': 30, 'WARNING': 30, 'INFO': 20, 'DEBUG': 10, 'NOTSET': 0}
logging.debug("1 This is a %s message.",logging.getLevelName(logging.DEBUG))
logging.info("2 This is an %s message.",logging.getLevelName(logging.INFO))
logging.warning("3 This is a %s message.",logging.getLevelName(logging.WARNING))
logging.error("4 This is an %s message.",logging.getLevelName(logging.ERROR))
logging.critical("5 This is a %s message.",logging.getLevelName(logging.CRITICAL))
logging.fatal("6 This is a %s message.",logging.getLevelName(logging.FATAL))

logging.log(logging.ERROR,"This ia a message from logging.log().")


# 使用不同级别记录日志
logging.debug("这是一条调试信息")
logging.info("这是一条普通信息")
logging.warning("这是一条警告信息")
logging.error("这是一条错误信息")
logging.critical("这是一条严重错误信息")
'''
D:\ANACONDA\envs\webdev\python.exe E:\pythonProject\PythonProject\learnTest\looger1.py 
[2024-11-20 21:07:34,415] [MainThread] [line:30] INFO:2 This is an INFO message.
[2024-11-20 21:07:34,415] [MainThread] [line:31] WARNING:3 This is a WARNING message.
[2024-11-20 21:07:34,415] [MainThread] [line:32] ERROR:4 This is an ERROR message.
[2024-11-20 21:07:34,415] [MainThread] [line:33] CRITICAL:5 This is a CRITICAL message.
[2024-11-20 21:07:34,415] [MainThread] [line:34] CRITICAL:6 This is a CRITICAL message.
[2024-11-20 21:07:34,415] [MainThread] [line:36] ERROR:This ia a message from logging.log().
[2024-11-20 21:07:34,415] [MainThread] [line:41] INFO:这是一条普通信息
[2024-11-20 21:07:34,415] [MainThread] [line:42] WARNING:这是一条警告信息
[2024-11-20 21:07:34,415] [MainThread] [line:43] ERROR:这是一条错误信息
[2024-11-20 21:07:34,415] [MainThread] [line:44] CRITICAL:这是一条严重错误信息
logging _nameToLevel: {'CRITICAL': 50, 'FATAL': 50, 'ERROR': 40, 'WARN': 30, 'WARNING': 30, 'INFO': 20, 'DEBUG': 10, 'NOTSET': 0}
logging _levelToName: {50: 'CRITICAL', 40: 'ERROR', 30: 'WARNING', 20: 'INFO', 10: 'DEBUG', 0: 'NOTSET'}
'''
