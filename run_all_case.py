# coding=utf-8
import os
import unittest
from common import HTMLTestRunner_cn
from common.setting import bases  #引入Setting的实例化对象
from common.myemail import mail_send  #引入MailSend的实例化对象
import sys
import os
from common.logger1 import atp_log


curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(curPath)


def add_case(rule = "ddt_newlogin_case.py"):
    """第一步，获取setting的CASE_PATH,组装case,返回case列表"""
    discover = unittest.defaultTestLoader.discover(bases.CASE_PATH,pattern=rule)
    #print(discover)
    return discover

def run_case():
    """第二步，运行所有case,生成测试报告，返回报告的绝对路径"""
    reportFilePath = os.path.join(bases.REPORT_PATH,bases.REPORT_NAME) #组装完整的报告绝对路径
    with open(reportFilePath,"wb") as file:

        runner = HTMLTestRunner_cn.HTMLTestRunner(stream=file,
                                                  verbosity=2,
                                                  title="API自动化测试报告",
                                                  description="本次测试是test_API接口串联测试，结果如下：",
                                                  retry=2,
                                                  save_last_try=False
                                                  )
        runner.run(add_case())
    return reportFilePath
def get_report_file(report_path):
    """第三步 后去最新的测试报告"""
    lists= os.listdir(report_path)
    lists.sort(key=lambda fn:os.path.getmtime(os.path.join(report_path,fn)))
    print(u"最新测试报告："+lists[-1])
    #找到最新的报告文件
    report_file=os.path.join(report_path,lists-1)
    return report_file

def send_email(sender,psw,receive,stmpserrver,report_file,post):
    """第四步：发送最新的测试报告"""
    with open(report_file,"rb") as f:
        mail_body = f.read()
    #定义邮件内容
    msg=MIMEMultipart()
    body =MIMEText(mail_body)
    msg['subject']=u"自动化测试报告"
    msg["from"]=sender
    msg["to"]=receiver
    msg.attach(body)
    #添加附件
    att= MIMEText(open(report_file,"rb").read(),"base64",'utf-8')
    att["Content-Type"]="application/octet-stream"
    att["Content-Type"]='attachment;filename="report.html'
    msg.attch(att)
    try:
        stmp = smtplib.SMTP_SSL(stmpserrver,port)
    except:
        smtp = smtlib.SMTP()
        stmp.commect(smtpserver,port)
    #用户名密码
    smtp.login(sender,psw)
    stmp.sendmail(sender,receiver,msg.as_string())
    smtp.quit()
    print("test report email  has send out")


if __name__ == '__main__':
    all_case = add_case()
    #生成测试报告路径
    run_case(all_case)
    #获取最新的测试报告文件
    report_path = os.path.join(curPath,"report")
    report_file = get_report_file(report_path)
    #邮件配置
    from config import readConfig
    sender=readConfig.sender
    psw = readConfig.psw
    smtp_server = readConfig.smtp_server
    port= readConfig.port
    receiver= readConfig.receiver
    send_email(sender,psw,receiver,smtp_server,report_file,port)#发送邮件






