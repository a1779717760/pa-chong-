import urllib.request
from selenium import webdriver

#url = 'http://www.baidu.com'
# 完整的url
# http://www.baidu.com:80/index.html?name=goudan&password=123#lala
#response = urllib.request.urlopen(url)

#with open("baidu.html",'wb') as fp:
 #   fp.write((response.re))
image_url='https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1554141857124&di=fa8f46e2cb05e1b687a41940b718dfb6&imgtype=0&src=http%3A%2F%2Fimg17.3lian.com%2Fd%2Ffile%2F201701%2F23%2F957c2d2610210dfa0fe087790530a8dd.jpg'
#response = urllib.request.urlopen(image_url)
#图片只能写入本地二进制格式
#with open('dongmantupian.jpg','wb') as fp:
 #   fp.write(response.read())
urllib.request.urlretrieve(image_url,'dongman.jpg')