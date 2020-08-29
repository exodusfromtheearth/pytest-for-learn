# -*- coding: utf-8 -*-
import os
import configparser

cur_path = os.path.dirname(os.path.realpath(__file__))
configpath =os.path.join(cur_path, "cfg.ini")
conf = configparser.RawConfigParser()
# 因为ini的内容中包含了%号这种特殊符号
conf.read(configpath)

# 邮件
smtp_server = conf.get("email", "smtp_server")
sender = conf.get("email", "sender")
psw = conf.get("email", "psw")
receiver = conf.get("email", "receiver")
port = conf.get("email", "port")

# cookie
cookie = conf.get("cookie", "cookie")

# host
host = conf.get("host", "host")

