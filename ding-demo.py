'''
钉钉群自定义机器人
https://open-doc.dingtalk.com/docs/doc.htm?spm=0.0.0.0.2g17LT&treeId=257&articleId=105733&docType=1


文本类型
{
     "msgtype": "text",
     "text": {
         "content": "我就是我,  @1825718XXXX 是不一样的烟火"
     },
     "at": {
         "atMobiles": [
             "1825718XXXX"
         ], 
         "isAtAll": false
     }
 }

markdown类型
{
     "msgtype": "markdown",
     "markdown": {"title":"杭州天气",
"text":"#### 杭州天气  \n > 9度，@1825718XXXX 西北风1级，空气良89，相对温度73%\n\n > ![screenshot](http://i01.lw.aliimg.com/media/lALPBbCc1ZhJGIvNAkzNBLA_1200_588.png)\n  > ###### 10点20分发布 [天气](http://www.thinkpage.cn/) "
     },
    "at": {
        "atMobiles": [
            "1825718XXXX"
        ], 
        "isAtAll": false
    }
 }
'''

import urllib
import urllib.request
import json
import ssl

#class
class DtalkRobot(object):
    """docstring for DtalkRobot"""
    webhook =''
    def __init__(self,webhook):
        super(DtalkRobot,self).__init__()
        self.webhook = webhook #执行时，构造函数初始化webhook参数
    
    #发送Text类型
    def sendText(self,msg,isAtAll=False,atMobiles=[]):
        data = {
            "msgtype": "text",
            "text": {
            "content": msg
        },
            "at": {
                "atMobiles": atMobiles, 
                "isAtAll": isAtAll
            }
        }
        return self.post(data)

    #发送Markdown类型
    def sendMarkdown(self,title,text,isAtAll=False,atMobiles=[]):
        data = {
            "msgtype": "markdown",
            "markdown": {"title":title,
            "text":text
            },
            "at": {
                "atMobiles": atMobiles, 
                "isAtAll": isAtAll
            }
        }
        return self.post(data)

    def post(self,data):
        post_data = json.dumps(data)
        #这么设定才能使用https协议
        ssl.create_default_https_context = ssl._create_unverified_context
        #post操作,把json 转成字符串
        req = urllib.request.Request(self.webhook,str.encode(post_data))
        req.add_header('Content-Type','application/json')
        #返回服务器的响应
        content = urllib.request.urlopen(req).read()
        return content

#调用测试
wh = 'https://oapi.dingtalk.com/robot/send?access_token=0d969203c8748c4a7c2b1aae11ee4be681a8cc9e6327c570a1e2355e2f13a064'

#入口函数
if __name__ == '__main__':
    robot = DtalkRobot(wh)
    # robot.sendText("Hello ,小明同学 在吗？ 小明同学 !!",False,['15354306660'])
    robot.sendMarkdown('今天星期几','#### 杭州天气  \n > 9度，@1825718XXXX 西北风1级，空气良89，相对温度73%\n\n > ![screenshot](http://i01.lw.aliimg.com/media/lALPBbCc1ZhJGIvNAkzNBLA_1200_588.png)\n  > ###### 10点20分发布 [天气](http://www.thinkpage.cn/)')
