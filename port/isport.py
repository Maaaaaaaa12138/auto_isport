import requests
import random
import json
import time
from threading import Thread

import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart


from .models import *
from django.utils import timezone

class CodeSender(object):
    def __init__(self):
        # 邮件发送者和SMTP密码
        self.sender = "example@qq.com"
        self.passWord = 'password'
        #邮件正文是MIMEText:
        
    
    def send(self, email):
        self.s = smtplib.SMTP_SSL("smtp.qq.com", 465)
        self.s.set_debuglevel(0)
        self.s.login(self.sender,self.passWord)
        try:
            msg = MIMEMultipart()
            #邮件主题
            msg['Subject'] = "重大通知"
            #发送方信息
            msg['From'] = self.sender
            #QQsmtp服务器的端口号为465或587
            msg_content = f"session已失效，请重新获取"
            msg.attach(MIMEText(msg_content, 'plain', 'utf-8'))
            msg['To'] = to = email
            self.s.sendmail(self.sender,to,msg.as_string())
            return "发送成功"
        except smtplib.SMTPException:
            return "发送失败"


class Isport(object):

    def __init__(self):
        self.codesender = CodeSender()
        self.postHeaders = {
            "Host": "isport.ustb.edu.cn",
            "Connection": "keep-alive",
            "X-Requested-With": "XMLHttpRequest",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,en-US;q=0.9",
            "Origin": "https://isport.ustb.edu.cn",
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; MI 9 Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 XWEB/1171 MMWEBSDK/200201 Mobile Safari/537.36 MMWEBID/207 MicroMessenger/7.0.12.1620(0x27000C37) Process/tools NetType/WIFI Language/zh_CN ABI/arm64",
            "Referer": "https://isport.ustb.edu.cn/app.RSPWxClient/index.jsp?m=yqinfo&c=index&a=init",
            "Cookie": "JSESSIONID=0B6E18B5C57F62A8DABA1E17BB5ED4FA"
        }
        self.drtw = ['36.2', '36.3', '36.4', '36.5', '36.6', '36.7']
        self.postData = {
            "m": "yqinfo",
            "c": "index",
            "a": "submit",
            "phone": "18888888888",
            "dwszd": "北京市海淀区",
            "mqszd": "北京 北京市 海淀区",
            "mqszdxx": "学院路30号北京科技大学",
            "age": "19",
            "mqszdjnw": "境内",
            "drtw": "36.3",
            "jzdiszg": "否",
            "dqsfczfkq": "否",
            "dqsfjjgl": "否",
            "brgtshrysfcj": "否",
            "brgtshrysfdgjwbtgrzszxq": "undefined",
            "brsfzl": "undefined",
            "sfjcbr": "否",
            "brjcsj": "",
            "brjcdd": "",
            "brjcry": "",
            "sfzxfyyq": "无居家要求",
            "wcyy": "",
            "gjcs": "",
            "JiGuan": "北京市 北京市",
            "SuShe": "本部校区-1斋-101-1",
            "Szxq": "本部",
            "JszdJnw": "境内",
            "Jszdjn": "北京市 北京市",
            "Jszdjw": "",
            "sfqgxfd": "否",
            "fjsj": "undefined",
            "fjsj_time": "undefined",
            "fjjtgj": "undefined",
            "qtqk": "",
            "sfcxbz": "否",
            "mqczcs": "undefined",
            "whjqjzdzsxx": "undefined",
            "whjqjzdzjnw": "undefined",
            "whjqjzdzgc": "undefined",
            "whjqjzdzsss": "undefined",
            "bjczsq": "undefined",
            "fjhbjczsq": "undefined",
            "jhfjhczsq": "undefined",
            "xzz": "undefined",
            "jhfjjtzz": "undefined",
            "fjcc": "undefined",
            "sfzxnjsq": "undefined",
            "jtzz": "undefined",
            "sfzjtss": "undefined",
            "fjhsfzjtss": "undefined",
            "fjhsfzx": "undefined",
            "fjhjtzz": "undefined",
            "sfzj": "是",
            "xssffj": "已返京",
            "xsfjrq": "2022-02-06 15:10",
            "mqzt": "正常生活",
            "cqcs": "其他",
            "sfdtfj": "是",
            "xjzjd": "北京科技大学",
            "xjzsq": "北京科技大学",
            "xsfxlyjnw": "境内",
            "fxlyjw": "",
            "fxlyjn": "北京市 北京市",
            "czjtgj": "飞机",
            "hbhcc": "MU5555",
            "sfzx": "校本部",
            "jtwzss": "",
            "jtwzxx": "",
            "sfzjwgfxdqszx": "否",
            "sfzjwgfxdqqtx": "否",
        }
        super().__init__()
        self.s = requests.Session()

    def refreshSession(self):
        "刷新session信息"
        session = JSESSIONID.objects.get(name="isport")
        self.postHeaders['Cookie'] = session.content

    def getOut(self):
        "申请出校（当天）"
        data = {
            "m": "yqinfo",
            "c":"cx",
            "a":"add",
            "isDt":"0",
            "GoWhere":"去哪儿",
            "CxReason":"干什么"
        }

        response = requests.post("https://isport.ustb.edu.cn/app.RSPWxClient/index.jsp", data=data, headers=self.postHeaders)
        d = json.loads(response.text)
        if int(d['statusCode']) == 200:
            return True
        return False
        
    def port(self):
        # 不再修改体温
        # self.postData['drtw'] = random.choice(self.drtw)
        self.refreshSession()
        response =  self.s.post(url="https://isport.ustb.edu.cn/app.RSPWxClient/index.jsp", data=self.postData, headers=self.postHeaders, allow_redirects=True)
        data = json.loads(response.text)
        if int(data['statusCode']) == 200:
            #if self.getOut():
                #return "上报+申请成功"
            return "上报成功"
        elif int(data['statusCode']) == 300:
            return "当日已上报"
        else:
            print(response.text)

def main():
    a = Isport()
    while (1):
        try:
            res = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "：" +a.port()
        except:
            a.codesender.send("1304565847@qq.com")
            res = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "：session已失效，请重新获取"
        finally:
            print(res)
            Status(content=res, time=timezone.now()).save()
            time.sleep(20*60)

t = Thread(target=main)
t.setDaemon(True)
t.start()
