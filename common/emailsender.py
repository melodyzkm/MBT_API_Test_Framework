from email.mime import text,multipart,image
import smtplib
from get_config import GetConfig
import os,re
BASEDIR=os.path.dirname(os.path.dirname(__file__))
#
# email_info=configparser.ConfigParser()
# email_info.read(os.path.join(BASEDIR,'conf','data'),encoding='utf-8')
c = GetConfig()

class MYEMAIL:
    '''
    params
    :smtp_addr
    '''
    def __init__(self):
        self._smtp_addr = c.get_value('email', 'smtp_addr')
        self._from_addr = c.get_value('email', 'from_addr')
        self._emai_pwd = c.get_value('email', 'emai_pwd')
        self._to_addr = c.get_value('email', 'to_addr').split(',')
        self._s = smtplib.SMTP(self._smtp_addr)
        self._s.login(self._from_addr, self._emai_pwd)

    def email_text(self,text_info,subject=None,sendername=None):
        #定义邮件内容msg
        self.text_obj=text.MIMEText(_text=text_info)
        self._email_conf(subject,sendername)
        self._send_eamil()

    def email_html(self,url_info,subject=None,sendername=None):
        self.text_obj=text.MIMEText(url_info,_subtype='html')
        self._email_conf(subject,sendername)
        self._send_eamil()

    def email_file(self,filename=None,showname=None,img=None,body=None,subject=None,sendername=None):  #此处直接定义一个发送图片+文件的方法
        self.text_obj = multipart.MIMEMultipart()  # 附件形式
        # 添加一个文件
        if  filename:
            with open(filename, 'rb') as fo:
                fo_str = fo.read()
            attr = text.MIMEText(fo_str, _charset='utf-8')
            attr["Content-Type"] = 'application/octet-stream'
            if not showname:
                showname=os.path.basename(filename)
            # attr['Content-Disposition'] = 'attachment; filename=%s'%showname # 没有这个不显示附件位置··WWWW是名称，可以参数格式化
            attr.add_header('Content-Disposition', 'attachment', filename=('gbk', '', showname))
            self.text_obj.attach(attr)
            if not subject:
                subject='附件--%s'%showname

        if  img and body:
            self.text_obj.attach(text.MIMEText(body, 'html', 'utf-8'))
            # 显示一个图片
            with open(img, 'rb') as fo:
                im_str = fo.read()
            attr = image.MIMEImage(im_str)
            # attr.add_header('Content-ID', '<image1>') #指定图片
            img_id = re.findall(r'cid:(\w+).*', body)[0]
            attr['Content-ID'] = '<%s>'%img_id  # 这个是和body中的image1一致
            self.text_obj.attach(attr)
            if not subject:
                subject='图片--%s'%(os.path.basename(img))
        self._email_conf(subject,sendername)
        self._send_eamil()

    def _email_conf(self,subject,sendername):
        if not sendername:
            sendername=self._from_addr
        self.text_obj['Subject']=subject
        self.text_obj['from']=sendername

    def _send_eamil(self):
        self._s.sendmail(self._from_addr, self._to_addr, self.text_obj.as_string())

    def smtp_close(self):
        self._s.close()


if __name__=='__main__':
    email=MYEMAIL()
    body = """
    <h3>测试结果截图如下，详细请下载report.html查看！</h3>
    <img src="cid:image2"/>
    """
    # email.email_file(filename=os.path.join(BASEDIR,'resultfile','emai哈哈l.py'),img=os.path.join(BASEDIR,'resultIMG','123.png'),body=body,subject='haha',sendername='LM')
    # email.smtp_close()
    email.email_text('223344',sendername="哈哈",subject='测试')
