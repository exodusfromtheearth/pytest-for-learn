import os.path
import time

class Setting():
    """存放全局基础信息，方便管理"""
    def __init__(self):
        self.BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.SMTP_DICT = {
        "smtp_server": "smtp.163.com",  # 发送邮件服务器
        "send_user": "15611360995@163.com",  # 发送邮件的邮箱账号
        #"send_pwd": "xxxxxx",  # 发送邮件的账号密码
        "send_pwd" : "1230ilovu",
        "sender": "15611360995@163.com",  # 显示在邮件中的发件人,必须与send_user一致
        "receiver": ["xtgao@huaxing.com","863675790@qq.com"],  # 收件邮箱地址
        "subject": "test自动化测试报告",  # 邮件主题
        "from": "test自动化平台"  #邮件发送方
    }
        # 项目名称(自定义)
        self.PROJECT_NAME = 'ca3_test'
        # 存放用例的路径
        self.CASE_PATH = os.path.join(self.BASE_PATH,'case')
        # 存放报告的路径
        self.REPORT_PATH = os.path.join(self.BASE_PATH,'report')
        # 报告的文件名
        times = time.strftime("%Y%m%d%H%M%S")
        self.REPORT_NAME = self.PROJECT_NAME+times+'report.html'
        #邮件中正文内容
        self.CONTENT = 'Hi all,\n    本邮件由系统自动发出，无需回复！为了更好的报告展示，请您使用chrome打开报告。谢谢！'
        #邮件中展示自定义附件名
        self.File_NAME = 'api_report.html'
        # 日志的文件名
        self.LOG_NAME='atp.log'
        # 存放日志的路径
        self.LOG_PATH = os.path.join(self.BASE_PATH, 'logs')
        # 默认日志级别
        self.LEVEL = 'info'
        # 用例参数文件路径
        self.PARAM_PATH = os.path.join(self.BASE_PATH,'params')
        # 用例参数文件名
        self.PARAM_NAME = 'interface.xlsx'
        # 测试结果文件名
        self.RESULT_NAME = 'interface.xls'

bases = Setting()   #实例化Setting
