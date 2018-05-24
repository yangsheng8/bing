'''
Bing 壁纸爬虫
'''
import urllib
import urllib.request
import ssl
import time
import json
import os.path

class BingBgDownloader(object):
    _bing_interface = 'https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=%d&nc=%d&pid=hp'
    _bing_url = 'https://cn.bing.com/'
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
        en_name = entmp[entmp.rindex('/') +1 :entmp.rindex('_ZH')]
        ex_name = entmp[entmp.rindex('.') +1 : len(entmp)]
        pix = entmp[entmp.rindex('_') + 1 : entmp.rindex('.')]
        
        img_name =  self._img_filename%(zh_name,en_name,ex_name)
        return img_name

    #得到图片资源的URL
    def _get_imgurl(self,img_info):
        return img_info['urlbase']

    #下载图片
    def _down_img(self,img_url,img_pathname):
        img_data =  urllib.request.urlopen(img_url).read()
        f =  open(img_pathname,'wb')
        f.write(img_data)
        f.close()
        print('success saved image:',img_url)

if __name__ == '__main__':
    dl = BingBgDownloader()
    dl.download(1)
   