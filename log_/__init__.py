"""
python日志模块 logging
重要的四个部分：
一、 记录器 logger
     通过记录器的函数，实现日志信息的记录,如：
     logger.info('----')
     logger.debug('---')
     logger.warning('--')
     logger.error(msg)
     logger.critical(msg)

二、 处理器 Handler
     将记录器的记录日志信息进行特定的处理，
     默认情况使用打印到控制台的StreamHandler处理器

     处理器Handler对象需要添加到记录器logger中的, 如：
        logger.addHandler(xxxHandler)

    常用的处理器：
        流处理器StreamHandler
        文件处理器 FileHandler
        网络请求处理器 HTTPHandler :  上传日志信息到日志服务器(Flask/Flume)
        邮箱处理器  SMTPHandler

三、 日志格式化Formatter
    指定日志信息的格式，如只记录日志信息的时间和消息，则格式为:
    %(asctime)s : %(message)s

    asctime和message都是格式化日志的变量信息。

四、 日志过滤器Filter
     过滤一些无用的日志信息。

"""
import logging
from logging.handlers import TimedRotatingFileHandler, HTTPHandler, SMTPHandler

# 创建日志记录器
# 任务3： 列出django和flask项目中的日志记录器的名称
# django.db.backends
# django.class.AdminEmailHandler

logger = logging.getLogger(name='django.request')
logger.setLevel(logging.WARN)

# 创建日志处理器(StreamHandler, FileHandler)
handler1 = logging.StreamHandler()
handler1.setLevel(logging.INFO)

handler2 = logging.FileHandler('django.log')
handler2.setLevel(logging.ERROR)

handler3 = SMTPHandler('smtp.qq.com',
                       fromaddr='610039018@qq.com',
                       toaddrs='diyuhuan@1000phone.com',
                       subject='日志邮箱通知')

# 配置邮件验证用户和口令（或授权码）
handler3.username = '610039018@qq.com'
handler3.password = 'xrjtaatcuylqbbba'  # QQ邮箱发件时验证的“授权码”
handler3.setLevel(logging.FATAL)

# 创建上传日志请求的处理器HTTPHandler
# 上传日志的接口： http://10.35.162.97:5000/log/
# 接口的方法： post
# 响应的数据是json
handler4 = HTTPHandler(host='10.35.162.97:5000',
                       url='/log/', method='POST')
handler4.setLevel(logging.INFO)


# 创建格式化对象 , 并添加到处理器
formatter = logging.Formatter('[ <%(asctime)s> %(name)s %(levelname)s ] %(message)s')
handler1.setFormatter(formatter)
handler2.setFormatter(formatter)
handler3.setFormatter(formatter)
handler4.setFormatter(formatter)  # 无效的，默认情况下将所有的日志信息上传到服务器

# 将处理器添加到日志记录器
logger.addHandler(handler1)
logger.addHandler(handler2)
# logger.addHandler(handler3)
logger.addHandler(handler4)

# 任务4： 使用SMTPHandler将记录的日志信息发送到邮箱中

if __name__ == '__main__':
    logger.info('hi, disen')
    logger.debug('hi, 190')
    logger.warning('hi, 110')
    logger.error('hi, 120')
    logger.critical('出现了192的数据库无法连接')
