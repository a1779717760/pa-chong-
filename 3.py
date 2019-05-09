import urllib.parse
import urllib.request

word = input('请输入你想要搜索的内容：')
url = 'http://www.baidu.com/s?'

#参数单独写出，字典
data = {
    'ie' : 'utf-8',
    'wd' : word,
}

query_string = urllib.parse.urlencode(data)
url += query_string

response = urllib.request.urlopen(url)

filenmane = word + '.html'
with open(filenmane,'wb') as fp:
    fp.write(response.read())