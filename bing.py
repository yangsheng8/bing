'''
Bing 壁纸爬虫 
'''

'''
{
images: [
{
startdate: "20180524",
fullstartdate: "201805241600",
enddate: "20180525",
url: "/az/hprichbg/rb/WineDay_ZH-CN9852912150_1920x1080.jpg",
urlbase: "/az/hprichbg/rb/WineDay_ZH-CN9852912150",
copyright: "皮利附近的葡萄庄园，瑞士沃州 (© Gallery Stock)",
copyrightlink: "/search?q=%e8%91%a1%e8%90%84%e5%ba%84%e5%9b%ad&form=hpcapt&mkt=zh-cn",
quiz: "/search?q=Bing+homepage+quiz&filters=WQOskey:%22HPQuiz_20180524_WineDay%22&FORM=HPQUIZ",
wp: true,
hsh: "aa330b5ea5dfb2b27cf629dc63e8a55f",
drk: 1,
top: 1,
bot: 1,
hs: [ ]
}
],
tooltips: {
loading: "正在加载...",
previous: "上一个图像",
next: "下一个图像",
walle: "此图片不能下载用作壁纸。",
walls: "下载今日美图。仅限用作桌面壁纸。"
}
}
'''

import urllib
import urllib.request
import ssl
import time
import json
import os.path

class BingBgDownloader(object):
    _bing_interface = 'https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=%d&nc=%d&pid=hp'
    _bing_url = 'https://cn.bing.com'
    _img_filename = '[%s%s][%s].%s'
    def __init__(self):
        super(BingBgDownloader,self).__init__()
        ssl._create_default_https_context = ssl._create_unverified_context
    
    #下载壁纸图片
    def download(self,num=1,local_path="./"):
        if num < 1: 
            num = 1
        url = self._bing_interface %(num, int(time.time()))
        img_info = self._get_img_infos(url)
        for info in img_info:
            print('_get_imgurl:',self._get_imgurl(info))
            print('_get_img_filename:',self._get_img_filename(info))
            self._down_img(self._get_imgurl(info),self._get_img_filename(info))
        
        

    #从接口获取图片资源信息
    def _get_img_infos(self,url):
        request  = urllib.request.urlopen( url )
        bgObjs = json.loads( bytes.decode(request.read()) )
        return bgObjs['images']
        
    #从接口数据提取图片文件名
    def _get_img_filename(self,img_info):
        zh_name =''
        pos = img_info['copyright'].index('(')


        if pos < 0:
                zh_name = img_info['copyright']
        else:
                zh_name = img_info['copyright'][0:pos]

        entmp = img_info['url']
        en_name = entmp[entmp.rindex('/') + 1 :entmp.rindex('_ZH')] #名字
        ex_name = entmp[entmp.rindex('.') + 1 : len(entmp)] #拓展名
        pix = entmp[entmp.rindex('_') + 1 : entmp.rindex('.')] #尺寸
        
        img_name =  self._img_filename%(zh_name,en_name,pix,ex_name)
        return img_name

    #得到图片资源的URL
    def _get_imgurl(self,img_info):
        return img_info['url']

    #下载图片
    def _down_img(self,img_url,img_pathname):
        print("self._bing_url+img_url:----",self._bing_url+img_url)
        img_data =  urllib.request.urlopen(self._bing_url+img_url).read()
        f =  open(img_pathname,'wb')
        f.write(img_data)
        f.close()
        print('success saved image:',img_url)

if __name__ == '__main__':
    dl = BingBgDownloader()
    dl.download(3)
   