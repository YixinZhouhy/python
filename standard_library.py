# sys 模块
# 包含version_info 等元组
import sys
print(sys.version_info)


# 日志模块
# os模块 ： 与操作系统交互
# platform : 以获取平台（操作系统）的信息
# logging : 记录信息
import os
import platform
import logging

# platform.platform() 返回字符串
# home drive 主驱动器
# os.path.join() 将三个部分位置信息聚合在一起

if platform.platform().startswith('Windows'):
    logging_file = os.path.join(os.getenv('HOMEDRIVE'),
                                os.getenv('HOMEPATH'),
                                'test.log')
else:
    logging_file = os.path.join(os.getenv('HOME'),
                                'test.log')

print('Logging to', logging_file)

logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s : %(levelname)s : %(message)s',
    filename = logging_file,
    filemode = 'w'
    )

logging.debug('Start of the program')
logging.info('Doing something')
logging.warning('Dying now')
