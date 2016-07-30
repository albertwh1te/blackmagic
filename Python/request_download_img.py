# coding:utf-8
import shutil
import requests


class DownloadImgMixin(object):
    def download_img(self,url):
        r = requests.get(url,stream=True)
        print r.status_code
        print r.raw
        if r.status_code == 200:
            with open('test.png', 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)

url = "http://www.xiangbodao.com/wp-content/uploads/2015/12/%E7%81%AB%E5%BD%B1%E5%BF%8D%E8%80%85-%E4%BD%90%E5%8A%A9%E5%A4%B4%E5%83%8F-%E5%A3%81%E7%BA%B8-%E5%9B%BE%E7%89%87-13.png"
#  url = "http://python.usyiyi.cn/python_278/_static/py.png"
t = DownloadImgMixin()
t.download_img(url)
            

#  if __name__ == "__main_":
    #  t = DownloadImgMixin()
    #  t.download_img(url)
    

