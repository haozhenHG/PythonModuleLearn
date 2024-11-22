import logging

# # 配置日志记录器,将日志写入文件
# logging.basicConfig(filename='app.log',level=logging.DEBUG,
#                     format='[%(asctime)s] [%(threadName)s] [line:%(lineno)d] %(levelname)s:%(message)s')
# # 参数filename='app.log' 一旦设置好 则控制台不会输出日志信息  将所有信息会写入到log日志文件
#
#
# logging.debug("这条消息会被记录到文件中")
# logging.info("程序正常运行中...")

#  上述是一种便捷快速的方法  复杂程序使用日志记录器

# 创建一个日志记录器（logger） 将所有消息记录到文件中,同时将错误级别及以上的消息输出到控制台
logger = logging.getLogger('my_app') # 名称
logger.setLevel(logging.ERROR)  # 日志优先级：CRIRICAL>ERROR>WARNING>INFO>DEBUG

# 创建一个文件处理器  文件写入的信息 应该是程序中所有出现的信息  因此级别应该设置为最低
file_handler = logging.FileHandler('appfilerecord.log')
file_handler.setLevel(logging.DEBUG)  # 设置信息处理的级别 DEBUG  将所有DEBUG级别以上的信心写入appfilerecord文件中

# 创建一个控制台处理器  控制台显示的应该是级别较高的信息  因此设置error以上的级别
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.ERROR)

# 创建一个格式器,并将它添加到处理器
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# 将处理器添加到日志记录器
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# 使用日志记录器
# 日志优先级：CRIRICAL>ERROR>WARNING>INFO>DEBUG
logger.debug("这条消息会被记录到文件中")  # 文件处理器
logger.error("这条错误消息会同时出现在文件和控制台中") # 控制台处理器

