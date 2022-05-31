
from loguru import logger
logger.info("hello world")
logger.debug("这是一条debug日志")
logger.error("这是一条error日志")
logger.warning("这是一条warning日志")
logger.info("这是一条info日志")

#输出到文件：add（）
logger.add('a.log',format="{time} {level} {message}",level="DEBUG")
logger.info("hello world")
logger.debug("这是一条debug日志")
logger.error("这是一条error日志")
logger.warning("这是一条warning日志")
logger.info("这是一条info日志")
#进项传入参数的格式化
logger.info("我的名字是{}，今天周{}",'张三','一')
