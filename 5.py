import urllib.request
import urllib.parse

post_url = 'https://fanyi.baidu.com/'

word = input('输入你想查询的单词:')

form_data = {
    'kw' : word,
}
headers = {
    'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 73.0.3683.86Safari / 537.36'
}


request = urllib.request.Request(url=post_url , headers=headers)
form_date = urllib.parse.urlencode(form_data).encode()
response = urllib.request.urlopen(request,data=form_date)

print(response.read().decode())