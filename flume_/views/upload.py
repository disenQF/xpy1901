from flask import Blueprint
from flask import request
from flask import jsonify

blue = Blueprint('upload_log', __name__)


# 任务1：整理Python中的序列化和反序列的两个模块(json, pickle)

@blue.route('/log/', methods=('POST', ))
def upload_log():
    """
    mmutableMultiDict([('name', 'django.request'),
     ('msg', '出现了192的数据库无法连接'),
     ('args', '()'),
     ('levelname', 'CRITICAL'),
      ('levelno', '50'),
       ('pathname', '/Users/apple/PycharmProjects/xpy1901/log_/__init__.py'),
        ('filename', '__init__.py'),
        ('module', '__init__'),
         ('exc_info', 'None'),
         ('exc_text', 'None'),
         ('stack_info', 'None'),
         ('lineno', '92'),
         ('funcName', '<module>'),
         ('created', '1560390611.566365'),
         ('msecs', '566.3650035858154'),
          ('relativeCreated', '161.0119342803955'),
           ('thread', '140734937761216'),
           ('threadName', 'MainThread'),
            ('processName', 'MainProcess'),
            ('process', '17830'),
            ('message', '出现了192的数据库无法连接'),
             ('asctime', '2019-06-13 09:50:11,566')])
    :return:
    """
    print(request.form)
    print(request.remote_addr)  # 客户端的IP

    # 任务2： 提取上传日志的时间、等级、消息、文件路径、行号和上传日志客户端的IP
    #         并将这些数据写入到数据库中
    return jsonify({'code': 200, 'msg': '上传日志成功!'})
